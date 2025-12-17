---
title: apple-instruments-profiling
tags: [apple, instruments, profiling, performance]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Instruments Profiling apple instruments profiling performance

Instruments 를 사용한 성능 분석. 기본은 [[apple-performance-and-debug]] 참고.

### Time Profiler

CPU 사용량 분석.

```bash
# Xcode → Product → Profile → Time Profiler
```

**분석 포인트:**
- Call Tree 에서 시간 많이 소요되는 함수 찾기
- Self Weight 높은 함수 최적화
- 불필요한 반복 작업 제거

### Allocations

메모리 할당 추적.

**확인 사항:**
- Persistent Bytes: 계속 증가하면 메모리 누수
- Transient Bytes: 일시적 할당
- Generations: 메모리 스냅샷 비교

### Leaks

메모리 누수 감지.

**해결 방법:**
1. Leaks 발견 시 Call Stack 확인
2. 순환 참조 찾기
3. weak/unowned 로 수정

### Energy Log

배터리 사용량 분석.

**최적화:**
- 네트워크 요청 배치 처리
- 위치 업데이트 빈도 줄이기
- 백그라운드 작업 최소화

### 더 보기

[[apple-performance-and-debug]], [[apple-memory-management]], [[apple-xctest-deep-dive]]
