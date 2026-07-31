# Google Play Console 연동 및 실서비스 모니터링 (App Size & Vitals)

R8 최적화 결과는 수동 검증뿐만 아니라 **Google Play Console**과의 연동을 통해 지속 모니터링됩니다.

### 8-1. Android App Bundle (AAB) 및 Dynamic Delivery와의 시너지
* R8은 AAB 빌드 시 디바이스 아키텍처(arm64-v8a 등) 및 화면 밀도(density)에 따라 Split APK 단위로 미사용 코드를 정밀 수축시킵니다.
* Google Play Console의 **App Size 리포트**를 통해 실제 사용자가 Play 스토어에서 다운로드하는 용량(Download Size)과 기기 설치 용량(On-device Size)을 트래킹합니다.

### 8-2. Play Console Android Vitals 모니터링
* R8 최적화 및 Obfuscation(난독화) 적용 시 Play Console에 `mapping.txt`를 업로드하면, Crash 및 ANR 발생 시 난독화된 StackTrace가 **실제 소스 코드의 라인 번호와 클래스명으로 자동 De-obfuscation되어 수집**됩니다.
* 이를 통해 프로덕션 환경의 Crash rate 및 시작 시간 지표를 정밀 모니터링할 수 있습니다.
