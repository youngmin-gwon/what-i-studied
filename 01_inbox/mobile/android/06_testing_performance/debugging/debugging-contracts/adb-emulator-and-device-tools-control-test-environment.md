---
title: "ADB, emulator, device tool은 테스트 환경을 제어한다"
tags: ["android", "android/testing-performance"]
---

# ADB, emulator, device tool은 테스트 환경을 제어한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [디버깅 도구 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
관련 노트: [테스트 레이어는 피드백 비용으로 선택한다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/test-layer-is-chosen-by-feedback-cost-and-risk.md)

테스트 환경은 같은 앱을 실행해도 서로 다른 사실을 보여준다.
JVM 테스트는 빠르지만 실제 Android 시스템과 입력 장치를 재현하지 않는다.
에뮬레이터는 반복 가능하고 자동화하기 쉽다.
실제 기기는 하드웨어, 제조사 설정, 성능, 센서, 배터리 차이를 드러낸다.

## 환경 선택

순수 도메인 규칙은 기기 없이 실행한다.
Android resource와 lifecycle 계약은 계측 테스트에서 확인한다.
화면, 회전, 키보드, 권한, window 동작은 에뮬레이터로 반복한다.
카메라, Bluetooth, 생체 인증, 성능, 제조사 변형은 실제 기기로 보완한다.
한 환경의 통과를 모든 환경의 품질 증거로 해석하지 않는다.

## 매트릭스

최소 매트릭스에는 API 수준, 화면 크기, locale, 글꼴 배율을 포함한다.
다크 모드와 회전은 상태 보존과 layout 회귀를 찾는 데 유용하다.
모든 조합을 매 commit에 실행하면 피드백 비용이 커진다.
대표 조합은 pull request에, 넓은 조합은 nightly 또는 release에 배치한다.
Gradle Managed Devices와 에뮬레이터 snapshot은 반복 실행을 안정화한다.

## ADB의 역할

ADB는 앱 내부가 아닌 디바이스 경계에서 상태를 관찰하고 조작한다.
```bash
adb devices
adb shell am force-stop com.example.app
adb shell am start -n com.example.app/.MainActivity
adb shell dumpsys activity activities
adb logcat --pid=$(adb shell pidof -s com.example.app)
```
패키지, 프로세스, 권한, 로그, 파일, 포트 forwarding을 확인할 수 있다.
명령은 대상 device를 명시해 여러 기기 연결에서 오작동을 줄인다.
테스트 코드가 ADB에 직접 의존하면 낮은 레이어 테스트가 느려진다.
ADB 작업은 기기 준비, 진단, E2E 보조 단계에 한정한다.

## 재현 기록

API level, device model, locale, orientation, build variant를 기록한다.
실행한 ADB 명령과 앱 로그의 시각을 함께 보존한다.
에뮬레이터 snapshot을 상태 초기화 수단으로 사용하되 테스트 간 공유 상태를 제거한다.

공식 참고: [ADB 문서](https://developer.android.com/tools/adb)
공식 참고: [Gradle Managed Devices](https://developer.android.com/studio/test/gradle-managed-devices)
