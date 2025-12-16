---
title: apple-distribution-and-policies
tags: [apple, appstore, policy]
aliases: []
date modified: 2025-12-16 16:15:25 +09:00
date created: 2025-12-16 16:14:32 +09:00
---

## Distribution & Policies apple appstore policy

앱을 세상에 내놓을 때 필요한 정책/검토/운영 정보를 쉽게 정리했다. 용어는 [[apple-glossary]].

### 제출 전 체크
- 개인정보 라벨, ATT 설명, 권한 문구 (카메라/마이크/사진/위치/블루투스 등) 작성.
- 콘텐츠 등급, 지역 제한, 인앱 구매 설정 (IAP/구독/원타임).
- 스크린샷/미리보기/설명/키워드 준비.

### 리뷰 가이드
- 비공개 API 사용 금지, [[apple-glossary#hidden-api|사설 API]] 접근 금지.
- 사기/스팸/중복 앱 거절. 사용자 기만/데이터 과도 수집 금지.
- 결제는 IAP 를 사용 (일부 리더 앱/외부 링크 정책은 국가별 예외).
- 충분한 기능/콘텐츠 없이 웹뷰만 감싼 앱은 거절될 수 있다.

### 베타/테스트
- [[apple-glossary#Sideloading/TestFlight|TestFlight]]: 최대 1 만 테스터, 90 일 만료. 베타 리뷰가 필요할 수 있다.
- 내부 배포: Ad Hoc/Enterprise/MDM. 인증서 남용은 취소될 수 있다.

### 업데이트/릴리스 관리
- 단계적 출시 (지역/비율), 리셋/롤백은 버전 제출로 해결.
- App Store Connect 에서 크래시/메트릭/평점 모니터링.
- 가격/인앱 구매/프로모션 코드 관리.

### 법/규제
- GDPR/CCPA 등 개인정보 법규 준수. 데이터 수집/보관/삭제 흐름 문서화.
- 암호화 수출 규정: 강한 암호화를 쓰면 수출 신고/면제를 체크.
- 어린이용 앱: 광고/트래킹/콘텐츠 제한.

### B2B/엔터프라이즈
- 커스텀 앱 (Apple Business Manager/School Manager) 으로 특정 조직 대상 배포.
- MDM 으로 기기/앱 관리, 푸시 명령, 설정 강제.

### macOS 특수
- 노타리제이션 필수, 서명 후 `altool`/`notarytool` 로 업로드/스테이플.
- 시스템 확장/드라이버는 별도 승인/커널 정책 확인.

### 링크

[[apple-build-and-distribution]], [[apple-sandbox-and-security]], [[apple-performance-and-debug]], [[apple-testing-and-quality]].
