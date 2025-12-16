# Secure Coding Checklist (공통) #apple #security #checklist

보안 사고를 막기 위한 간단하지만 꼼꼼한 체크리스트. 모르는 말은 [[apple-glossary]].

## 입력/출력
- 모든 외부 입력(네트워크/파일/사용자 입력/URL 스킴)을 검증한다.
- 직렬화/파싱(JSON/Plist/Proto)은 에러 처리와 사이즈 제한을 둔다.
- 파일 경로 주입 방지: 사용자 입력을 경로에 직접 붙이지 않는다.

## 인증/세션
- 토큰/쿠키/세션ID는 [[apple-glossary#Keychain|Keychain]]에 저장. 메모리에는 최소 시간만.
- 세션 만료/로그아웃/토큰 재발급 흐름을 명확히.
- 멀티 디바이스 로그인 정책을 정의한다.

## 네트워크
- [[apple-glossary#ATS|ATS]] 기본, 예외 최소화. TLS 1.2+.
- 인증서 핀닝은 교체/만료 대비 로테이션 계획 포함.
- 민감 데이터는 GET 쿼리 대신 POST 바디로, 로깅 금지.

## 권한/프라이버시
- 필요한 권한만 요청, 이유 문구 명확히. 거부 시 대체 흐름 제공.
- App Tracking Transparency/Privacy 라벨 업데이트.
- 위치/사진/연락처 등은 “선택 항목만” 접근 옵션을 우선 고려.

## 스토리지
- 민감 파일/DB에 Data Protection Class 설정. 백업 제외 여부 검토.
- 캐시/로그에 민감 정보 남기지 않기. 만료/삭제 정책 적용.
- 앱 종료/백그라운드 전환 시 화면 가리기(스냅샷 보호) 고려.

## 코드 서명/엔타이틀먼트
- 필요 없는 [[apple-glossary#Entitlement|Entitlement]] 제거. 최소 권한 원칙.
- 번들 ID/프로비저닝/서명 상태를 CI에서 자동 검증.

## 안전한 API 사용
- 사설 API 호출/리플렉션/메서드 스위즐을 피한다(심사 거절/보안 위험).
- `eval`/동적 코드 로딩 금지. 플러그인은 서명/검증된 것만.

## 로깅/모니터링
- OSLog/Logger로 PII 제거한 구조화 로그 사용.
- 크래시/ANR/보안 관련 이벤트(권한 거부/서명 실패)를 모니터링.

## 빌드/배포
- 디버그 심볼/Bitcode/Strip 설정을 환경에 맞게. dSYM 업로드 자동화.
- macOS: 노타리제이션, Hardened Runtime 옵션 확인.
- 서드파티 SDK 라이선스/권한/데이터 수집을 검토.

## 테스트
- 단위/통합 테스트에 에러/권한 거부/오프라인/대용량/경계값 포함.
- 정적 분석/취약점 스캔/펜테스트 결과를 리뷰하고 조치.
- 시뮬레이터+실기기, 다양한 OS 버전/설정에서 반복.

## 사고 대응
- 키/토큰 유출 시 폐기/재발급, 서버 블록/로그아웃.
- 사용자 공지/법적 요구사항 준비.
- 원인 분석/재발 방지 문서화.

## 링크
[[apple-security-models]], [[apple-privacy-and-tcc-details]], [[apple-cryptography-and-keychain]], [[apple-distribution-and-policies]].
