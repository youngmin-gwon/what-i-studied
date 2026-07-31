# Android Studio Profiler

상위 노트: [android-profiling-tools](01_inbox/mobile/android/06_testing_performance/performance/android-profiling-tools.md)

실시간 CPU, 메모리, 네트워크, 에너지 모니터링.

##### CPU Profiler

**사용법:**

1. Android Studio → View → Tool Windows → Profiler
2. 앱 선택 후 CPU 타임라인 클릭
3. Record 버튼 → 작업 수행 → Stop

**Trace 종류:**

- **Sample Java Methods**: 낮은 오버헤드, 대략적 분석
- **Trace Java Methods**: 정확하지만 느림
- **Sample C/C++ Functions**: 네이티브 코드 분석
- **Trace System Calls**: 시스템 레벨 추적

**분석:**

```
Call Chart: 시간 순서대로 호출 표시
Flame Chart: 소요 시간 기준 정렬
Top Down: 호출자 → 피호출자
Bottom Up: 피호출자 → 호출자 (병목 찾기 좋음)
```

##### Memory Profiler

**Heap Dump:**

1. Memory 타임라인에서 Dump Java heap 클릭
2. Class List 에서 메모리 많이 차지하는 클래스 확인
3. Instance View 에서 개별 객체 검사
4. References 에서 누가 참조하는지 확인

**Allocation Tracking:**

```kotlin
// 특정 구간 추적
fun loadData() {
    // 여기서 Record allocation 시작
    val list = mutableListOf<String>()
    repeat(10000) {
        list.add("Item $it")
    }
    // Stop → 어디서 할당되었는지 확인
}
```

**메모리 누수 감지:**

1. 의심되는 화면 열기
2. Heap dump 생성
3. 화면 닫기
4. GC 강제 실행 (Profiler 에서 Initiate GC)
5. 다시 Heap dump
6. Activity/Fragment 인스턴스가 남아있는지 확인

##### Network Profiler

**분석 항목:**

- 요청/응답 크기
- 타임라인
- 요청 헤더/바디
- 응답 헤더/바디
- Call Stack (어디서 호출했는지)

```kotlin
// OkHttp Interceptor 로 상세 로깅
val loggingInterceptor = HttpLoggingInterceptor().apply {
    level = HttpLoggingInterceptor.Level.BODY
}

val client = OkHttpClient.Builder()
    .addInterceptor(loggingInterceptor)
    .build()
```

##### Energy Profiler

배터리 소모 분석.

**주요 지표:**

- CPU 사용량
- 네트워크 활동
- GPS 사용
- Wakelock 획득
