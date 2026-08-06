---
title: archive-compression-commands
tags: [archive, commands, compression, gzip, linux, tar]
aliases: [Archive, gzip, tar, 압축 명령어]
date modified: 2025-12-28 21:22:29 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

파일 아카이브와 압축 관련 명령어들입니다.

## 📋 Quick Reference

| 명령어 | 용도 | 확장자 |
|--------|------|--------|
| `tar` | 아카이브 | `.tar` |
| `gzip` | 압축 | `.gz` |
| `bzip2` | 압축 (더 강함) | `.bz2` |
| `xz` | 압축 (가장 강함) | `.xz` |
| `zip`/`unzip` | ZIP | `.zip` |

## 📦 tar - Tape Archive

### 옵션 설명

| 옵션 | 의미 |
|------|------|
| `-c` | Create (생성) |
| `-x` | Extract (추출) |
| `-t` | List (목록) |
| `-v` | Verbose (상세) |
| `-f` | File (파일 지정) |
| `-z` | gzip |
| `-j` | bzip2 |
| `-J` | xz |
| `-C` | 디렉토리 변경 |

### 아카이브 생성

```bash
tar -cvf archive.tar dir/              # 생성
tar -czvf archive.tar.gz dir/          # gzip
tar -cjvf archive.tar.bz2 dir/         # bzip2
tar -cJvf archive.tar.xz dir/          # xz

# 여러 파일/디렉토리
tar -czf backup.tar.gz file1.txt dir1/ file2.txt
```

### 아카이브 추출

```bash
tar -xvf archive.tar                   # 현재 디렉토리에
tar -xzvf archive.tar.gz
tar -xjvf archive.tar.bz2
tar -xJvf archive.tar.xz

# 특정 디렉토리에
tar -xzvf archive.tar.gz -C /path/to/dest/

# 특정 파일만
tar -xzvf archive.tar.gz file.txt
tar -xzvf archive.tar.gz dir/
```

### 목록 확인

```bash
tar -tvf archive.tar                   # 목록
tar -tzvf archive.tar.gz
tar -tzvf archive.tar.gz | grep file.txt  # 파일 검색
```

### 실용 예제

```bash
# 백업
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/data/

# 진행상황 표시
tar -czf - dir/ | pv > archive.tar.gz

# 특정 파일 제외
tar -czf archive.tar.gz --exclude='*.log' dir/

# 증분 백업
tar -czf full.tar.gz -g snapshot.file /data
tar -czf incr.tar.gz -g snapshot.file /data
```

## 🗜️ Compression Tools

### gzip - GNU Zip

```bash
gzip file.txt                          # file.txt.gz 생성 (원본 삭제)
gzip -k file.txt                       # 원본 보존
gzip -d file.txt.gz                    # 압축 해제
gunzip file.txt.gz                     # 동일

# 압축률
gzip -1 file.txt                       # 빠름 (1-9)
gzip -9 file.txt                       # 최대 압축
```

### bzip2 - Better Compression

```bash
bzip2 file.txt                         # file.txt.bz2
bzip2 -k file.txt                      # 원본 보존
bzip2 -d file.txt.bz2                  # 압축 해제
bunzip2 file.txt.bz2                   # 동일
```

### xz - Best Compression

```bash
xz file.txt                            # file.txt.xz
xz -k file.txt                         # 원본 보존
xz -d file.txt.xz                      # 압축 해제
unxz file.txt.xz                       # 동일
```

### 압축률 비교

```
속도: gzip > bzip2 > xz
압축률: xz > bzip2 > gzip

일반적: tar.gz (속도와 압축률 균형)
백업: tar.xz (최대 압축)
빠른 작업: tar.gz
```

## 📁 zip/unzip

### zip

```bash
zip archive.zip file.txt
zip -r archive.zip directory/          # 재귀
zip -e archive.zip file.txt            # 암호화
zip -u archive.zip newfile.txt         # 업데이트
zip -d archive.zip file.txt            # 삭제
```

### unzip

```bash
unzip archive.zip
unzip archive.zip -d /path/to/dest/
unzip -l archive.zip                   # 목록만
unzip -t archive.zip                   # 테스트
unzip archive.zip file.txt             # 특정 파일만
```

## 💡 Scenarios

### 백업 스크립트

```bash
#!/bin/bash
BACKUP_DIR=~/backups
DATE=$(date +%Y%m%d)

tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" \
    --exclude='*.log' \
    --exclude='*.tmp' \
    /path/to/data/

# 30일 이상 된 백업 삭제
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +30 -delete
```

### 압축률 비교

```bash
time gzip -c file > file.gz
time bzip2 -c file > file.bz2
time xz -c file > file.xz
ls -lh file.*
```

## 🔗 연결 문서 (Related Documents)

- [file-operations-commands](file-operations-commands.md) - 파일 작업
- [process-job-control-commands](process-job-control-commands.md) - 백그라운드 실행
