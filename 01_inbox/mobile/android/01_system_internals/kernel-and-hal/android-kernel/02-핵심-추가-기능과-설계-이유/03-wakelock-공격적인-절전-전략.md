# Wakelock: 공격적인 절전 전략

상위 노트: [02-핵심-추가-기능과-설계-이유](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel/02-%ED%95%B5%EC%8B%AC-%EC%B6%94%EA%B0%80-%EA%B8%B0%EB%8A%A5%EA%B3%BC-%EC%84%A4%EA%B3%84-%EC%9D%B4%EC%9C%A0.md)

#### 배경: 서버 vs 모바일

일반 리눅스의 suspend(S3 sleep) 는 **시스템 전체를 정지** 시킨다. 메모리만 유지하고 CPU, 디스크, 네트워크를 끈다. 하지만 이는 서버에 적합하지 않다 (네트워크 요청에 응답 불가).

모바일은 정반대다:

- **화면 꺼짐 ≠ 시스템 정지**: 음악 재생, 파일 다운로드, 알림 수신이 계속되어야 한다.
- **기본 상태는 절전**: 화면이 꺼지면 가능한 한 빨리 suspend 로 진입해 배터리를 아낀다.

#### Wakelock 의 메커니즘

**Wakelock**(2009~2012, 초기 구현) 은 "지금은 sleep 하지 마"를 커널에 알리는 메커니즘이었다. 앱이나 서비스가 wakelock 을 잡으면 (acquire), 커널은 suspend 를 연기한다.

```bash
echo "my_wakelock" > /sys/power/wake_lock  # 잡기
echo "my_wakelock" > /sys/power/wake_unlock  # 풀기
```

**문제**: 앱이 wakelock 을 풀지 않으면 배터리가 급격히 소모된다. 초기 안드로이드의 악명 높은 "배터리 킬러" 문제의 주범이었다.

#### Wakeup Sources 로의 통합

리눅스 커뮤니티는 wakelock 패치를 거부했다 (메인라인에 맞지 않는 설계). 결국 양측이 타협해 **Wakeup Sources**(2012, Linux 3.5) 가 메인라인에 통합되었다. 안드로이드는 이를 사용하도록 마이그레이션했다.

```c
// 커널 코드
struct wakeup_source *ws = wakeup_source_register("my_wakelock");
__pm_stay_awake(ws);  // 잡기
__pm_relax(ws);       // 풀기
```

유저 공간에서는 `PowerManager` API 를 통해 간접적으로 사용한다:

```java
PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
PowerManager.WakeLock wl = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MyWakeLock");
wl.acquire();  // CPU 깨어있음, 화면/센서는 끄기 가능
// 작업 수행
wl.release();
```

#### 배터리 최적화

Android 6.0(Marshmallow) 부터 **Doze 모드**가 도입되었다. 기기가 오랫동안 움직이지 않으면, 백그라운드 작업과 wakelock 을 제한한다. "유지 관리 기간 (maintenance window)"에만 작업을 허용한다.

---
