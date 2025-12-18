# Privacy & TCC Details #apple #privacy #tcc #common

민감 권한(TCC)과 프라이버시 정책을 쉽게 풀어쓴다. 용어는 [apple-glossary](../00_foundations/apple-glossary.md).

## TCC가 하는 일
- 카메라/마이크/사진/연락처/캘린더/리마인더/블루투스/위치/알림 등 민감 자원에 접근할 때 사용자에게 묻는다.
- 사용자가 허락/거부/한 번만 허락을 선택하면, 그 설정을 저장하고 앱 호출 때마다 검사한다.
- Info.plist의 이유 문구가 없으면 바로 거절되거나 크래시한다.

## 권한 종류별 요약
- 카메라/마이크: 실시간 영상/음성. 백그라운드 사용은 제한적.
- 사진: 전체 라이브러리 vs 선택한 항목만. Photos picker로 최소 권한 권장.
- 위치: 항상/앱 사용 시/정확도 낮춤. 백그라운드 위치는 별도 플래그 필요.
- 블루투스: 주변 기기 검색/연결. 광고/스캔은 배터리/프라이버시 고려.
- 알림: 배너/사운드/배지. iOS 15+는 시간 민감/크리티컬 알림 옵션.
- 연락처/캘린더/리마인더: 개인 정보. 최소 권한/선택 UI 제공.
- 헬스/피트니스/모션: HealthKit/WorkoutKit/모션 센서. 데이터 종류별로 더 엄격.

## 사용자 경험 가이드
- 권한을 “필요할 때” 요청. 앱 실행 직후 남용 금지.
- 왜 필요한지 짧고 친절하게 설명. 실제 사용 시점과 문구가 일치해야 한다.
- 거부 시 대체 흐름 제공(읽기 전용/기능 축소), 설정으로 이동 버튼 제공.

## 데이터 최소화
- 필요한 필드만 요청/저장. 예: 연락처 전체 대신 이메일만.
- 서버로 보내기 전에 익명화/집계/토큰화.
- 진단/로그에 개인 정보 넣지 않기.

## 지역/정책
- GDPR/CCPA 등 법에 따라 데이터 접근/삭제/이동 요청을 처리할 수 있어야 한다.
- 아동/학생 대상 앱은 부모 동의/추적 제한을 철저히.
- 중국 등 일부 지역은 인증서/네트워크/지도 데이터 정책이 다를 수 있다.

## 테스트/디버깅
- 시뮬레이터 `xcrun simctl privacy`로 권한 허용/거부 테스트.
- 실제 기기에서 한 번만 허용/정확도 낮춤/백그라운드 조합 모두 확인.
- `log stream --predicate 'subsystem == "com.apple.TCC"'`로 TCC 로그 보기.

## 심사 대비 체크리스트
- 권한 설명 문구가 명확한가? (무엇을, 왜 쓰는지)
- 실제 기능과 권한 사용 타이밍이 맞는가?
- 대체 경로가 있는가? 거부 시 앱이 멈추지 않는가?
- 데이터 사용/공유/추적을 개인정보 라벨/ATT에 반영했는가?

## 링크
[apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md), [apple-security-models](../../../../apple-security-models.md), [apple-distribution-and-policies](../05_security_privacy/apple-distribution-and-policies.md), [apple-accessibility-and-internationalization](../02_ui_frameworks/apple-accessibility-and-internationalization.md).
