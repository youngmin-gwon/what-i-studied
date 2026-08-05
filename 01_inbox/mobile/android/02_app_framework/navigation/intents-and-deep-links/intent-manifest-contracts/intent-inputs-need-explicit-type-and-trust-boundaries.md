---
title: intent-inputs-need-explicit-type-and-trust-boundaries
tags: [android, android/intents, android/navigation]
aliases: ["Intent extras와 URI 인자는 명시적인 타입과 신뢰 경계가 필요하다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent extras 와 URI 인자는 명시적인 타입과 신뢰 경계가 필요하다

배경 지식: [접근 제어 모델](../../../../../../security/fundamentals/access-control-models.md)

외부 앱이나 system 에서 들어온 Intent 는 내부 함수 호출과 같은 신뢰 수준이 아니다. `extras`, `data` URI, MIME type, `ClipData`, URI permission grant flag 는 서로 다른 입력 경계이며 각각 타입과 출처를 확인해야 한다.

컴포넌트를 `exported=true` 로 열거나 implicit intent 를 받는다면 입력 검증은 선택 사항이 아니다. Parcelable/classloader 문제, oversized extras, 예상하지 않은 URI authority, 권한 없는 content URI 접근을 별도로 방어한다.

### 판단 기준

- extra key 와 type 은 명시적으로 파싱하고 실패 경로를 둔다.
- URI authority 와 MIME type 은 allowlist 로 확인한다.
- `ClipData` 와 URI grant flag 는 접근 권한의 범위를 별도로 검증한다.
- 외부 입력에서 만든 route key 는 인증/권한 확인 뒤에만 적용한다.

예를 들어 다른 앱이 보낸 `extras` 에서 앱 전용 커스텀 `Parcelable` 클래스를 기대하면, 발신 프로세스가 그 클래스를 모를 때 `android.os.BadParcelableException` 이 발생할 수 있다. `getStringExtra`/`getIntExtra` 처럼 primitive 로 좁히거나 값을 읽는 시점에 try/catch 로 방어해야 한다.

관련 노트: [exported boundary](exported-attribute-defines-external-component-boundary.md), [PendingIntent](pendingintent-is-delegated-future-intent-token.md), [URI validation](../deep-link-contracts/external-uri-must-be-validated-before-navigation.md)
