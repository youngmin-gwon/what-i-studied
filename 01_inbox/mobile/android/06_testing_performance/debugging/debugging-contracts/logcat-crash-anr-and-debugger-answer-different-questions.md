# Logcat, crash, ANR, debugger는 서로 다른 질문에 답한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [디버깅 도구 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
관련 정본: [테스트 레이어는 피드백 비용으로 선택한다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/test-layer-is-chosen-by-feedback-cost-and-risk.md)

테스트는 문제가 다시 발생하는지 확인하고, 진단 도구는 왜 발생했는지 좁힌다.
둘을 같은 목적으로 사용하면 로그를 과도하게 남기거나 재현 절차를 놓치게 된다.

## Logcat

Logcat은 시간 순서로 사건을 수집하는 1차 관찰 도구다.
feature와 사건 유형을 구분할 수 있는 tag 또는 구조화된 필드를 사용한다.
민감 정보, 토큰, 비밀번호, 전체 응답 본문은 기록하지 않는다.
재현 전에 관련 tag의 로그를 필터링하고 필요하면 버퍼를 정리한다.
```bash
adb logcat -c
adb logcat --pid=$(adb shell pidof -s com.example.app)
```
로그만 보고 원인을 단정하지 말고 사용자 행동과 시각을 함께 기록한다.

## 크래시

먼저 예외 타입과 메시지를 읽는다.
그 다음 앱 코드의 첫 stack frame과 호출 경로를 찾는다.
릴리즈 난독화가 적용됐다면 동일 버전의 mapping으로 stack trace를 복원한다.
재현 입력, OS 버전, 앱 버전, 직전 로그를 하나의 사건으로 묶는다.

## ANR

ANR은 메인 스레드가 사용자 입력과 생명주기를 처리하지 못한 상태다.
main thread trace에서 block, lock, disk, network, 긴 계산을 찾는다.
메인 스레드에서 동기 네트워크와 큰 파일 입출력을 제거한다.
코루틴을 쓰더라도 실제 dispatcher 전환이 되었는지 확인한다.
ANR은 단순히 timeout을 늘리는 방식으로 해결하지 않는다.

## Debugger

브레이크포인트는 특정 입력에서 변수와 호출 순서를 볼 때 사용한다.
조건부 breakpoint는 반복문과 고빈도 경로의 관찰 비용을 줄인다.
로그 breakpoint는 실행을 멈추지 않고 값을 기록할 때 적합하다.
디버거가 연결되면 timing이 바뀌어 race나 ANR이 사라질 수 있다.
따라서 디버거 결과를 단독 증거로 보지 않고 로그와 trace로 교차 확인한다.

진단의 결과는 수정 가능한 가설이어야 한다.
가설마다 재현 단계와 성공 기준을 기록하면 디버깅이 테스트로 전환된다.

공식 참고: [Logcat으로 로그 보기](https://developer.android.com/tools/logcat)
공식 참고: [앱이 응답하지 않는 문제 진단](https://developer.android.com/topic/performance/vitals/anr)
