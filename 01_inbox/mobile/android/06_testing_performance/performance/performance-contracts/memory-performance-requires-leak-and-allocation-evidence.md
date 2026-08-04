---
title: memory-performance-requires-leak-and-allocation-evidence
tags: ["android", "android/testing-performance"]
aliases: ["Android 메모리는 사용량보다 회수되지 않는 객체를 본다"]
date created: 2026-07-31 17:32:53 +09:00
date modified: 2026-08-04 22:00:00 +09:00
---

## Android 메모리는 사용량보다 회수되지 않는 객체를 본다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](./performance-contracts.md)

단순히 전체 메모리 힙 점유량이 크다고 해서 누수(Leak)는 아니며, Activity/Fragment 수명주기 파괴(Destroy) 이후에도 GC Root로부터 접근 가능하여 힙에서 회수되지 못하는 '잔존 참조 객체' 및 프레임 잔크를 유발하는 '단기 객체 대량 할당(Allocation Churn)'을 포착하는 것이 본질이다.

### 1. ART GC 및 메모리 측정 메커니즘

- **ART GC 메커니즘**: Generational Concurrent Copying (CC) GC 기반. Young Generation(Eden/Survivor)에서 생성된 단기 객체가 잦은 GC 소탕 대상이 되며, 대량 할당 발생 시 CPU 주기를 점유하여 프레임 Drop을 유발한다.
- **메모리 분류 지표**:
  - **Java Heap**: Android Dalvik/ART 힙 객체 (Bitmap 버퍼 제외한 표준 객체).
  - **Native Heap**: C/C++ `malloc` allocation, Native Bitmaps (Android 8.0+), Webview/RenderThread 버퍼.
  - **Graphics**: EGL, GL Malloc, SurfaceFlinger 렌더 버퍼.
  - **PSS (Proportional Set Size)**: 프로세스 고유 메모리 + 공유 라이브러리(Shared Page)를 공유 프로세스 수로 나눈 합산 지표.
- **LeakCanary 누수 탐지 원리**:
  - `Activity.onDestroy()` 시 해당 객체에 대한 `WeakReference`를 생성하고 `ReferenceQueue`에 등록.
  - 5초 후 명시적 `Runtime.getRuntime().gc()` 후에도 `ReferenceQueue`로 이탈하지 않은 객체를 GC Root 탐색 알고리즘(Shark Hprof Parser)으로 힙 덤프 추적.

### 2. 메모리 누수 GC Root 참조 사슬 흐름

```mermaid
classDiagram
    direction LR
    class SingletonManager {
        +static instance
        +listeners: List
    }
    class CustomEventListener {
        +onEvent()
    }
    class MainActivity {
        +Context context
        +View rootLayout
    }

    SingletonManager "1" --> "*" CustomEventListener : Holding Strong Ref
    CustomEventListener --> MainActivity : Inner Class / Lambda Holds Outer Activity
    MainActivity --> ViewTree : Holds View Graph & Bitmaps

    note for MainActivity "Activity Destroyed by User Back Press,\nbut Singleton still holds Reference!\nResult: Memory Leak"
```

### 3. Lifecycle 릴리스 및 WeakReference 추적 Kotlin 코드 구체 예시

```kotlin
import androidx.lifecycle.DefaultLifecycleObserver
import androidx.lifecycle.LifecycleOwner
import java.lang.ref.WeakReference

class SafeListenerRegistrar : DefaultLifecycleObserver {
    private var activityRef: WeakReference<LifecycleOwner>? = null

    fun register(owner: LifecycleOwner) {
        activityRef = WeakReference(owner)
        owner.lifecycle.addObserver(this)
    }

    override fun onDestroy(owner: LifecycleOwner) {
        // Destroy 시점에 관찰자 해제 및 약한 참조 정리
        owner.lifecycle.removeObserver(this)
        activityRef?.clear()
        activityRef = null
    }
}
```

### 4. 관측 가능한 실행 증거 (Observable Evidence)

#### ADB dumpsys meminfo 힙 덤프 분석
`adb shell dumpsys meminfo <package>` 명령으로 Java, Native, Graphics 메모리 분포 덤프 관측:

```bash
adb shell dumpsys meminfo com.example.app
```

```text
** MEMINFO in pid 24102 [com.example.app] **
                   Pss  Private  Private  SwapPss     Heap     Heap     Heap
                 Total    Dirty    Clean    Dirty     Size    Alloc     Free
                ------   ------   ------   ------   ------   ------   ------
  Native Heap    42104    41980        0     1204    78200    62100    16100
  Dalvik Heap    28410    28240        0       88    42100    26400    15700
 Dalvik Other     4120     4100        0        0
        Other     8120     7900      100        0
       Ashmem      120        0        0        0
    Gfx dev     18400    18400        0        0
  Other dev        44        0       40        0
   .so mmap     12400     1200     8900        0
  .apk mmap      4100        0     1200        0
  .dex mmap     28900       12    21000        0
   TOTAL PSS   158100   114800    31240     1292   120300    88500    31800

 Objects
               Views:       240         ViewRootImpl:        2
          AppContexts:         4         Activities:        3  <-- Multi-activity Leak Alert!
               Assets:         8      AssetManagers:        0
        Local Binders:        18      Proxy Binders:       32
```

### 5. 메모리 최적화 가이던스

- **Activities 카운트 관측**: 화면을 모두 백버튼으로 이탈한 후에도 `Activities` 수치가 1 이상으로 지속 유지되면 힙 덤프(.hprof)를 즉시 수집한다.
- **Bitmap Config**: Compose/View 이미지 표현 시 필요 이상의 Resolution 디코딩을 방지하고 `Bitmap.Config.HARDWARE` 설정을 적용한다.

