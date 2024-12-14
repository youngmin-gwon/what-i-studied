---
title: githooks concept
created at: 2024-12-12
tags:
  - concept
  - githooks
  - git
aliases:
---

## pre-commit

커밋할 때 가장 먼저 호출되는 Hook 으로 커밋 메시지를 작성하기 전에 호출된다. pre-commit hook 에서는 린트를 실행하여 코드 스타일을 검사하거나, 라인 끝의 공백 문자를 검사하거나 테스트를 한다.

아래 명령어를 실행하면 commit 시 pre-commit hook 을 `생략` 할 수 있다.

```bash
git commit --no-verify
```

## prepare-commit-msg

커밋 메시지를 수정하기 전에 먼저 prefix 또는 suffix 를 붙이는 것과 같이 hook 을 통해 커밋 메시지를 손보고 싶을 때 사용한다.

## commit-msg

이 hook 은 커밋 메시지가 들어 있는 임시 파일의 경로를 argument 로 받고 스크립트가 0 이 아닌 값을 반환하면 커밋이 되지 않는다. 이 hook 에서는 최종적으로 커밋이 완료되기 전에 프로젝트 상태나 커밋 메시지를 검증한다.

## post-commit

커밋이 완료되면 post-commit hook 이 실행되므로 post-commit 은 커밋한 것을 동료나 다른 프로그램에 노티를 줄 때 사용할 수 있다.

## pre-rebase

rebase 하기 전에 실행되는 훅으로 이미 push 한 커밋을 rebase 하지 못하게 할 수 있는 hook 으로 사용한다. Git 이 기본적으로 제공해주는 pre-rebase.sample 코드에 예제 또한 있다.

## post-rewrite

커밋을 변경하는 명령을 실행했을 때 실행되는 훅으로 용량이 크거나 Git 이 관리하지 않는 파일을 옮길 때, 문서를 자동으로 생성할 때 사용한다.

## post-merge

Merge 가 끝나고 나서 실행되는 hook 이다.
