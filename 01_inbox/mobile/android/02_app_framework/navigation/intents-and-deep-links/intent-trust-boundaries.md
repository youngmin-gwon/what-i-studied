---
title: intent-trust-boundaries
tags: [android, android/navigation, android/intent, security]
aliases: ["Intent 입력은 명시적 타입과 신뢰 경계가 필요하다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent 입력은 명시적 타입과 신뢰 경계가 필요하다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 보안 입력 검증 가이드 (What & Why)

1. **외부 Intent Extra의 검증**:
   `intent.getExtras()`로 전달되는 데이터는 검증되지 않은 데이터이므로, `ClassCastException` 예외 처리 및 널 타입 검증을 거친 후 안전하게 사용해야 한다.
2. **Parcelable / Serializable 역직렬화 위험**:
   검증되지 않은 외부 클래스를 Parcelable로 수신할 경우 ClassNotFoundException이나 원격 코드 실행 취약점이 유발될 수 있으므로 기본 타입(Primitive Types) 위주로 인자를 수신한다.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
