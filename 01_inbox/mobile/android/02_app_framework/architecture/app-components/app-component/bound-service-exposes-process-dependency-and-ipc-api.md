---
title: bound-service-exposes-process-dependency-and-ipc-api
tags: [android, android/app-components, android/architecture]
aliases: ["Bound Service는 프로세스 의존성과 IPC API를 노출한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Bound Service는 프로세스 의존성과 IPC API를 노출한다

**Bound Service 는 다른 컴포넌트(Activity 등)나 다른 앱 프로세스가 `bindService()` 를 통해 클라이언트-서버 인터페이스(IBinder / AIDL / Messenger)를 맺고 복잡한 메서드 호출 및 IPC 통신을 수행할 수 있게 해주는 컴포넌트 계약**이다.

---

### 1. 개념 및 핵심 명제 (What)

- **의존성 종속 수명 (Client-bound Lifetime)**:
  Bound Service 는 자신을 바인딩한 클라이언트 컴포넌트가 하나라도 존재하는 동안에만 활성화된다. 모든 바인딩이 해제(`unbindService`)되면 시스템에 의해 자동 종료된다.
- **프로세스 결합도 및 우선순위 승격**:
  포그라운드 Activity 가 특정 백그라운드 Service 를 바인딩하면, OS 는 해당 Service 프로세스의 우선순위를 클라이언트 수준으로 상승시킨다.

---

### 2. 코드 예시 (Local Binder 서비스)

```kotlin
class LocalAudioService : Service() {
    private val binder = LocalBinder()

    inner class LocalBinder : Binder() {
        fun getService(): LocalAudioService = this@LocalAudioService
    }

    override fun onBind(intent: Intent?): IBinder = binder

    fun playMusic() { /* 음원 재생 */ }
}
```

---

### 3. 관측 가능 증거 및 진단 (Observability)

- **바인딩된 서비스 및 연결 클라이언트 확인**:
  ```bash
  adb shell dumpsys activity services
  ```

---

### 4. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component.md)
- 공식 문서: [Bound Services Guide](https://developer.android.com/guide/components/bound-services)

검증일: 2026-08-05. Bound Service 바인더 인터페이스 및 dumpsys 검증 완료.
