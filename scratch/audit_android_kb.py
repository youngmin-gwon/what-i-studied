#!/usr/bin/env python3
"""Read-only structural audit for the Android Markdown knowledge base."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote


FRONTMATTER_KEYS = ("title", "tags", "aliases", "date modified", "date created")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^)\s]+(?:\s+[^)]+)?)\)")
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")
H1_RE = re.compile(r"^#(?!#)\s+", re.MULTILINE)
MERMAID_TYPE_RE = re.compile(
    r"^(?:flowchart|graph|sequenceDiagram|stateDiagram(?:-v2)?|classDiagram|"
    r"erDiagram|journey|gantt|pie|mindmap|timeline|gitGraph|quadrantChart|"
    r"requirementDiagram|C4Context|C4Container|C4Component|C4Dynamic|sankey-beta)\b"
)


def split_fences(text: str):
    """Yield (inside_fence, language, start_line, block_text)."""
    lines = text.splitlines()
    in_fence = False
    language = ""
    start = 1
    block: list[str] = []
    for number, line in enumerate(lines, 1):
        match = re.match(r"^\s*(```+|~~~+)\s*([^\s`]*)", line)
        if match:
            marker = match.group(1)[0]
            if not in_fence:
                if block:
                    yield False, "", start, "\n".join(block)
                in_fence = True
                language = match.group(2).lower()
                start = number + 1
                block = []
            elif line.lstrip().startswith(marker * 3):
                yield True, language, start, "\n".join(block)
                in_fence = False
                language = ""
                start = number + 1
                block = []
            else:
                block.append(line)
        else:
            block.append(line)
    if block:
        yield in_fence, language, start, "\n".join(block)


def prose_only(text: str) -> str:
    chunks = [block for inside, _, _, block in split_fences(text) if not inside]
    value = "\n".join(chunks)
    return re.sub(r"`[^`\n]*`", "", value)


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0, "missing"
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            raw = lines[1:index]
            keys = {}
            for line in raw:
                match = re.match(r"^([^:#][^:]*):(?:\s*(.*))?$", line)
                if match:
                    keys[match.group(1).strip()] = (match.group(2) or "").strip()
            return keys, index + 1, "ok"
    return None, 0, "unclosed"


def markdown_targets(text: str):
    for match in LINK_RE.finditer(prose_only(text)):
        raw = match.group(1).strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1]
        if " \"" in raw or " '" in raw:
            raw = re.split(r"\s+[\"']", raw, maxsplit=1)[0]
        yield unquote(raw)


def resolve_target(source: Path, target: str, vault: Path):
    clean = target.split("#", 1)[0].split("?", 1)[0]
    if not clean or re.match(r"^(?:https?|mailto|tel|obsidian):", clean, re.I):
        return None
    if clean.startswith("file:") or clean.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", clean):
        return "absolute"
    candidates = [(source.parent / clean).resolve(), (vault / clean).resolve()]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
        if not candidate.suffix and candidate.with_suffix(".md").is_file():
            return candidate.with_suffix(".md")
    return candidates[0]


def audit(vault: Path, android: Path):
    files = sorted(android.rglob("*.md"))
    knowledge = [path for path in files if "_meta" not in path.parts]
    issues: dict[str, list[dict]] = collections.defaultdict(list)
    edges: dict[Path, set[Path]] = collections.defaultdict(set)
    stems: dict[str, list[Path]] = collections.defaultdict(list)
    bodies: dict[str, list[Path]] = collections.defaultdict(list)
    paragraphs: dict[str, list[tuple[Path, str]]] = collections.defaultdict(list)
    metrics = collections.Counter()

    for path in files:
        rel = path.relative_to(vault).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        stems[path.stem].append(path)
        keys, fm_end, fm_status = parse_frontmatter(text)
        if fm_status != "ok":
            issues["frontmatter"].append({"file": rel, "detail": fm_status})
        elif keys is not None:
            missing = [key for key in FRONTMATTER_KEYS if key not in keys]
            if missing:
                issues["frontmatter_keys"].append({"file": rel, "detail": missing})
            first = next((line for line in lines[fm_end:] if line.strip()), "")
            if not first.startswith("## "):
                issues["first_heading"].append({"file": rel, "detail": first[:120]})

        prose = prose_only(text)
        for match in H1_RE.finditer(prose):
            line = prose[: match.start()].count("\n") + 1
            issues["h1"].append({"file": rel, "line": line})
        for match in WIKILINK_RE.finditer(prose):
            line = prose[: match.start()].count("\n") + 1
            issues["wikilink"].append({"file": rel, "line": line, "detail": match.group(0)})

        targets = list(markdown_targets(text))
        metrics["markdown_links"] += len(targets)
        for target in targets:
            resolved = resolve_target(path, target, vault)
            if resolved is None:
                continue
            if resolved == "absolute":
                issues["absolute_or_file_uri"].append({"file": rel, "detail": target})
            elif isinstance(resolved, Path) and not resolved.exists():
                issues["broken_link"].append({"file": rel, "detail": target})
            elif isinstance(resolved, Path) and android in resolved.parents and resolved.suffix == ".md":
                edges[path].add(resolved)

        body = re.sub(r"\s+", " ", "\n".join(lines[fm_end:])).strip()
        if body:
            bodies[hashlib.sha256(body.encode()).hexdigest()].append(path)
        for paragraph in re.split(r"\n\s*\n", prose_only("\n".join(lines[fm_end:]))):
            normalized = re.sub(r"\s+", " ", paragraph).strip()
            if len(normalized) >= 120 and not normalized.startswith(("#", "|", "- [", "검증일:")):
                digest = hashlib.sha256(normalized.encode()).hexdigest()
                paragraphs[digest].append((path, normalized))
        if len(lines) <= 14:
            issues["very_short_14"].append({"file": rel, "detail": len(lines)})
        if len(lines) > 120 and not re.search(r"(?:map|contracts|glossary|topics|learning-spine|worked-examples|diagnostic-runbooks)", rel):
            issues["long_nonhub_120"].append({"file": rel, "detail": len(lines)})

        is_atomic = (
            "_meta" not in path.parts
            and "glossary" not in path.parts
            and "topics" not in path.parts
            and "learning-spine" not in path.parts
            and "worked-examples" not in path.parts
            and "diagnostic-runbooks" not in path.parts
            and not path.stem.endswith("contracts")
            and not path.stem.endswith("map")
            and not path.stem.startswith("android-")
        )
        if is_atomic:
            code_languages = [
                language
                for inside, language, _, _ in split_fences(text)
                if inside and language not in ("", "text", "plaintext", "mermaid")
            ]
            has_diagram = "```mermaid" in text or bool(
                re.search(r"[┌┐└┘├┤┬┴┼│─]|(?:-->|=>|→).*(?:-->|=>|→)", text)
            )
            has_evidence = bool(
                re.search(
                    r"\b(?:adb|dumpsys|logcat|perfetto|bugreport|apkanalyzer|apksigner|"
                    r"Exception|Error|trace|profiler)\b|관찰|출력 예시|정상 신호|실패 신호",
                    text,
                    re.I,
                )
            )
            has_mechanism = bool(
                re.search(r"메커니즘|동작 흐름|상태 전이|호출 경로|실행 흐름|내부 동작|작동 원리", text)
            )
            score = sum((bool(code_languages), has_diagram, has_evidence, has_mechanism))
            if score < 3:
                issues["atomic_substance_signal_lt3"].append(
                    {
                        "file": rel,
                        "detail": {
                            "score": score,
                            "code": bool(code_languages),
                            "diagram": has_diagram,
                            "evidence": has_evidence,
                            "mechanism_phrase": has_mechanism,
                            "lines": len(lines),
                        },
                    }
                )

        for inside, language, start, block in split_fences(text):
            if not inside:
                continue
            if language == "mermaid":
                nonblank = [line.strip() for line in block.splitlines() if line.strip() and not line.strip().startswith("%%")]
                if not nonblank or not MERMAID_TYPE_RE.match(nonblank[0]):
                    issues["mermaid_type"].append({"file": rel, "line": start, "detail": nonblank[0] if nonblank else "empty"})
                subgraphs = sum(1 for line in nonblank if re.match(r"^subgraph\b", line))
                ends = sum(1 for line in nonblank if line == "end")
                if subgraphs != ends:
                    issues["mermaid_subgraph_balance"].append({"file": rel, "line": start, "detail": [subgraphs, ends]})
                for offset, line in enumerate(block.splitlines()):
                    # Flag unquoted flowchart labels containing parser-sensitive punctuation.
                    if re.search(r"(?:\[[^\]\"]*[()|][^\]]*\]|\{[^}\"]*[()|][^}]*\})", line):
                        issues["mermaid_unquoted_special"] .append({"file": rel, "line": start + offset, "detail": line.strip()})
            elif language in ("", "text", "plaintext"):
                if re.search(r"[┌┐└┘├┤┬┴┼│─]|(?:-->|=>|→).*(?:-->|=>|→)", block):
                    issues["ascii_diagram_candidate"].append({"file": rel, "line": start, "detail": block.splitlines()[0][:120] if block else ""})

    for stem, paths in stems.items():
        if len(paths) > 1:
            issues["duplicate_stem"].append({"stem": stem, "files": [p.relative_to(vault).as_posix() for p in paths]})
    for digest, paths in bodies.items():
        if len(paths) > 1:
            issues["duplicate_body"].append({"hash": digest[:12], "files": [p.relative_to(vault).as_posix() for p in paths]})
    for digest, occurrences in paragraphs.items():
        distinct = sorted({path for path, _ in occurrences})
        if len(distinct) >= 3:
            issues["repeated_paragraph_3plus"].append(
                {
                    "hash": digest[:12],
                    "count": len(distinct),
                    "sample": occurrences[0][1][:240],
                    "files": [path.relative_to(vault).as_posix() for path in distinct],
                }
            )

    root = android / "00_foundations" / "android-foundation-map.md"
    seen = {root}
    queue = collections.deque([root])
    while queue:
        current = queue.popleft()
        for target in edges.get(current, set()):
            if target in knowledge and target not in seen:
                seen.add(target)
                queue.append(target)
    unreachable = sorted(set(knowledge) - seen)
    for path in unreachable:
        issues["foundation_unreachable"].append({"file": path.relative_to(vault).as_posix()})

    return {
        "metrics": {
            "android_md": len(files),
            "knowledge_md_excluding_meta": len(knowledge),
            "markdown_links": metrics["markdown_links"],
            "foundation_reachable": len(seen & set(knowledge)),
            "foundation_unreachable": len(unreachable),
        },
        "issue_counts": {key: len(value) for key, value in sorted(issues.items())},
        "issues": dict(sorted(issues.items())),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--android", type=Path, default=Path("01_inbox/mobile/android"))
    parser.add_argument("--details", action="store_true")
    args = parser.parse_args()
    vault = args.vault.resolve()
    android = (vault / args.android).resolve()
    report = audit(vault, android)
    if not args.details:
        report = {"metrics": report["metrics"], "issue_counts": report["issue_counts"]}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
