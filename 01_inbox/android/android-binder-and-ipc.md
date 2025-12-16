---
title: android-binder-and-ipc
tags: [android, android/binder, android/ipc, systems]
aliases: []
date modified: 2025-12-16 16:02:43 +09:00
date created: 2025-12-16 15:23:24 +09:00
---

## Binder & IPC android android/binder android/ipc systems

앱과 시스템이 서로 이야기를 나누는 통로가 Binder 다. 낯선 단어는 [[android-glossary]] 에서 본다.

### Binder 가 뭐길래?
- 프로세스 사이에 메시지를 전달하는 커널 기반 우체부다.
- 보낸 사람 UID/PID 가 함께 실려서, 수신자가 권한을 검사할 수 있다.
- 파일 설명자나 [[android-glossary#binder#parcelable|Parcelable]] 데이터를 함께 실을 수 있다.

### 어떻게 오갈까
1. 클라이언트가 Stub/Proxy 를 통해 호출을 만든다.
2. [[android-glossary#binder|Binder]] 드라이버가 서버 쪽 스레드 풀에 일을 건넨다.
3. 서버가 onTransact 에서 처리하고 결과를 돌려준다.
4. 비동기 (oneway) 호출은 큐에 쌓이므로 너무 많이 보내면 막힌다.

### 스레드와 안전
- 서비스마다 Binder 스레드 풀 크기가 있다. 긴 일은 다른 스레드나 [[android-glossary#workmanager|WorkManager]] 로 넘긴다.
- [[android-glossary#anr|ANR]] 을 피하려면 호출을 짧게 유지하고, 큰 데이터는 공유 메모리로 보낸다.

### 안정성 도구
- AIDL 에서 @Nullable/@FixedSize/@VintfStability 같은 표시로 호환성을 지킨다.
- DeathRecipient 로 상대가 죽었는지 감지한다.
- [[android-glossary#binder#death|Death]] 알림을 받으면 자원을 정리한다.

### 서비스 찾기
- system_server 쪽: ServiceManager 에 이름으로 등록/조회한다.
- 앱 사이: bindService 로 바인드하고 AIDL 인터페이스로 대화한다.
- [[android-glossary#binder#parcelable|ContentProvider]] 도 내부적으로 Binder 를 쓴다.

### 보안
- 호출이 들어오면 서비스가 UID/권한 ([[android-glossary#permission|Permission]], [[android-glossary#appops|AppOps]]) 을 검사한다.
- [[android-glossary#selinux|SELinux]] 가 도메인 간 Binder 호출도 제어한다.
- shell UID 로 실행되는 adb 명령은 일반 앱과 권한이 다르다.

### 디버깅
- `adb shell dumpsys binder` 로 트랜잭션 수와 서비스 목록을 본다.
- `service call` 로 원시 호출을 테스트할 수 있다 (개발 빌드).
- Perfetto/atrace 에서 binder 항목을 켜고, blocker 가 어디 있는지 확인한다.

### 더 읽기

[[android-zygote-and-runtime]], [[android-activity-manager-and-system-services]], [[android-security-and-sandboxing]], [[android-adb-and-images]].
