# APEX 설치 흐름

상위 노트: [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

1. **다운로드**: Play Store 에서 APEX 다운로드
2. **검증**: 서명 확인
3. **스테이징**: `/data/apex/active` 에 복사
4. **재부팅**: 다음 부팅 시 활성화
5. **마운트**: `/apex/<module_name>` 에 마운트
6. **롤백 준비**: 이전 버전 유지
