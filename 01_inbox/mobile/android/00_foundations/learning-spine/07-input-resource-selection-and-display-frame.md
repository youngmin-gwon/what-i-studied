---
title: 07-input-resource-selection-and-display-frame
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Input, resource selection, and display frame"]
date modified: 2026-08-04 10:10:43 +09:00
date created: 2026-08-03 21:55:00 +09:00
---

## 입력, 리소스 선택과 화면 프레임

6 장은 코드가 어느 스레드에서, 어떤 프로세스 경계를 넘어, 누가 소유한 lifetime 안에서 실행되는지를 다뤘다. 그러나 사용자의 터치가 실제로 그 main thread 의 이벤트 큐에 도달하기까지 어떤 경로를 거치는지, 그리고 코드가 계산한 UI 상태가 실제로 화면의 픽셀이 되기까지 무엇을 거치는지는 아직 다루지 않았다. 이 장은 입력에서 시작해 화면 프레임으로 끝나는 그 왕복을 다룬다.

이 장의 핵심 질문은 다음과 같다.

>사용자 입력과 configuration 은 어떤 경로를 거쳐 UI 상태가 되고, 그 상태는 어떻게 실제 화면에 표시되는 프레임이 되는가?

이 장은 View 나 Compose 의 개별 API 사용법을 처음부터 가르치지 않는다. 각 단계의 상세 계약은 원자 노트가 다루는 수준으로 남겨두고, 여기서는 입력이 도착하는 지점부터 프레임이 표시되는 지점까지의 인과 순서를 하나로 연결한다.

### 1. 물리 입력은 커널에서 시작해 특정 윈도우로 전달된다

터치나 키 입력은 앱 코드가 처음 보는 것이 아니다. AOSP 문서는 이 경로를 다음과 같이 설명한다.

>"The InputReader sends input events to the InputDispatcher which forwards them to the appropriate window."

커널의 입력 서브시스템(evdev)에서 시작한 신호는 `EventHub` 가 읽고, `InputReader` 가 디코딩해 `InputDispatcher` 로 넘긴다. `InputDispatcher` 는 현재 어떤 윈도우가 포커스를 갖고 있는지, 어떤 좌표가 어떤 윈도우 영역에 속하는지를 판단해 "적절한 윈도우"로 이벤트를 전달한다. 이 판단은 앱 코드가 아니라 system_server 쪽의 입력 파이프라인이 담당한다.

즉 앱이 받는 `MotionEvent`/`KeyEvent` 는 이미 "이 윈도우가 받아야 할 이벤트"라는 라우팅 판단을 거친 결과다. 여러 입력 장치가 동시에 연결돼 있어도 각 이벤트는 소스 타입과 대상 윈도우가 이미 정해진 채로 도착한다.

### 2. ViewRootImpl 은 윈도우와 View 트리를 잇는 다리다

`InputDispatcher` 가 "이 윈도우로 보낸다"고 판단했을 때, 그 윈도우 쪽에서 이벤트를 받아 View 트리로 밀어 넣는 역할은 `ViewRootImpl` 이 담당한다. `ViewRootImpl` 은 한 윈도우의 최상단에서 앱의 View 트리와 시스템의 WindowManagerService 를 연결하는 다리다.

Activity 가 화면에 윈도우를 붙일 때, `ViewRootImpl` 은 window session 을 통해 윈도우 속성을 WindowManagerService 쪽에 전달한다. WindowManagerService 는 이 정보로 해당 윈도우의 상태를 관리하고, 이 윈도우가 실제로 화면에 그려질 표면을 확보하도록 조율한다.

이 절이 채우는 공백은 다음과 같다. 4 장은 컴포넌트가 프로세스 안에서 활성화되는 과정을, 6 장은 코드가 어느 스레드에서 실행되는지를 다뤘지만, "화면에 보이는 이 View 트리가 시스템의 윈도우 관리와 어떻게 연결되는가"는 아직 답하지 않았다. `ViewRootImpl` 이 그 연결점이다.

### 3. 입력 이벤트는 결국 6 장의 main thread 큐를 통과한다

`ViewRootImpl` 이 입력 이벤트를 받았다고 곧바로 앱 코드가 그 이벤트를 처리하는 것은 아니다. 이 이벤트는 6 장에서 다룬 main thread 의 이벤트 큐에 들어가야 View 의 리스너나 Compose 의 입력 처리 코드에 도달한다.

그래서 6 장의 규칙은 여기서도 그대로 적용된다. main thread 가 다른 작업으로 막혀 있으면, 입력이 도착했다는 사실과 그 입력이 실제로 처리된다는 사실은 별개다. 입력 지연(input latency)의 상당 부분은 입력이 늦게 도착해서가 아니라 이미 도착한 입력이 큐에서 오래 기다렸기 때문에 생긴다.

### 4. Configuration 변경은 리소스 재선택을 동반한다

회전, 언어, 다크 모드, 창 크기 변경 같은 configuration 값이 바뀌면, 시스템은 단순히 값 하나를 갱신하는 것이 아니라 그 새 configuration 에 맞는 대체 리소스를 다시 골라야 한다. 공식 문서는 이 목적을 이렇게 설명한다.

>"These parameters usually require large enough changes to your application's UI that the Android platform has a purpose-built mechanism for when they change. This mechanism is Activity recreation."
>
>"The recreation behavior helps your application adapt to new configurations by automatically reloading your application with alternative resources that match the new device configuration."

5 장은 이 사건이 Activity 를 destroy 하고 재생성한다는 것, 그리고 그 과정에서 어떤 lifetime 이 유지되고 어떤 lifetime 이 끊기는지를 다뤘다. 이 장이 더하는 것은 그 재생성이 왜 필요한가다. 언어가 바뀌면 문자열 리소스 테이블에서 다시 선택해야 할 값이 바뀌고, 화면 크기나 방향이 바뀌면 레이아웃 리소스 qualifier 가 다시 평가돼야 한다. Activity 재생성은 이 재선택 결과를 반영해 처음부터 다시 구성하는 가장 확실한 방법이다.

Compose 에서도 이 원리는 같다. `stringResource()` 같은 API 는 현재 configuration 을 읽어 적절한 리소스를 찾으므로, configuration 이 바뀌어 Activity 가 재생성되면 Compose UI 도 다시 계산되면서 새 리소스 값을 반영한다.

### 5. 계산된 UI 상태는 View 또는 Compose 를 거쳐 그리기 명령이 된다

입력과 configuration 이 반영된 UI 상태는 그 자체로 픽셀이 아니다. View 시스템에서는 이미 존재하는 View 객체의 속성을 바꾸는 방식으로 화면을 갱신하고, Compose 에서는 state 를 다시 읽어 UI 트리 전체를 재계산한다. Compose 의 계산은 composition(무엇을 보여줄지 결정) → layout(측정과 배치) → drawing(그리기 명령 생성)이라는 단계로 나뉜다.

어느 쪽이든 이 단계의 산출물은 "그릴 내용"이지 화면에 표시된 결과가 아니다. Custom View 의 `onDraw(canvas)` 나 Compose 의 drawing 단계는 현재 윈도우가 제출할 그래픽 내용을 만들 뿐, 여러 레이어를 어떤 순서로 합칠지는 이 단계의 책임이 아니다.

### 6. 그리기 명령은 Surface 를 거쳐 SurfaceFlinger 의 합성으로 이어진다

그려진 내용은 그 윈도우의 `Surface` 에 버퍼로 제출된다. AOSP 문서는 이 뒤의 협업을 다음과 같이 설명한다.

>"When an app comes to the foreground, it requests buffers from WindowManager. WindowManager then requests a layer from SurfaceFlinger… SurfaceFlinger creates the layer and sends it to WindowManager. WindowManager then sends the surface to the app, but keeps the SurfaceControl instance to manipulate the appearance of the app on the screen."
>
>"A layer is a combination of a surface, which contains the BufferQueue, and a SurfaceControl instance, which contains the layer metadata like the display frame."

즉 앱은 그림을 그릴 수 있는 `Surface`(버퍼를 채우는 쪽)만 받고, 그 레이어를 화면 어디에 어떤 크기·투명도로 배치할지 결정하는 `SurfaceControl` 은 WindowManager 가 계속 쥐고 있다. 앱이 열심히 그려도 그 결과가 화면의 어디에 어떻게 나타날지는 앱이 아니라 WindowManagerService 와 SurfaceFlinger 의 몫이라는 뜻이다.

RenderThread 는 UI thread 가 만든 그리기 명령을 실제로 GPU 에 제출하는 역할을 나누어 맡지만, UI thread 의 measure/layout 작업 자체를 대신하지는 않는다. 채워진 버퍼는 `BufferQueue` 를 통해 SurfaceFlinger 로 전달되고, SurfaceFlinger 는 Hardware Composer 와 협력해 여러 레이어(앱 윈도우, 상태바, 내비게이션 바 등)를 하나의 display frame 으로 합성한다. 이 전체 과정은 VSync 신호에 맞춰 Choreographer 가 스케줄링하는 프레임 예산 안에서 끝나야 한다.

### 하나의 루프로 정리한다

| 단계 | 담당 | 5~6 장과의 연결 |
| --- | --- | --- |
| 물리 입력 → EventHub → InputReader → InputDispatcher | system_server 입력 파이프라인 | 4 장의 프로세스와는 별개로, system_server 가 어느 윈도우로 보낼지 먼저 판단한다 |
| InputDispatcher → 대상 윈도우의 ViewRootImpl | WindowManagerService 가 관리하는 윈도우 상태 | 5 장의 task/윈도우와 연결되는 지점 |
| ViewRootImpl → main thread 이벤트 큐 | Looper/Handler(6 장) | 6 장의 "유일한 큐" 제약이 그대로 적용된다 |
| 입력 처리 → UI 상태 갱신(View 또는 Compose) | 앱 코드, Compose composition/layout/draw | 여기서 만들어진 상태가 5 장의 [viewmodel](../../02_app_framework/viewmodel.md)/transient state 와 연결된다 |
| 그리기 명령 → RenderThread → Surface 버퍼 제출 | RenderThread, GPU | 6 장에서 본 "UI thread 와 분리되지만 비용이 사라지지 않는" 계층 |
| Surface 버퍼 → BufferQueue → SurfaceFlinger/HWC 합성 → display | SurfaceFlinger, WindowManagerService(SurfaceControl) | 앱은 surface 만 갖고 최종 배치는 WindowManager 가 갖는다 |

configuration change 는 이 루프 전체를 다시 타게 만드는 별도의 시작점이다. configuration 값 갱신 → 리소스 재선택 → (5 장의) Activity destroy/recreate → 새 크기의 윈도우로 다시 measure/layout → 다시 이 루프를 거쳐 새 프레임이 합성된다.

### Worked example: 화면을 회전한다

사용자가 기기를 회전시키는 사건 하나가 이 장과 5 장, 6 장의 내용을 모두 지나간다.

1. 센서 이벤트로 configuration 이 갱신된다.
2. 시스템은 새 configuration 에 맞는 레이아웃·문자열·drawable 리소스를 다시 선택해야 한다고 판단한다.
3. 5 장에서 본 것처럼 Activity 가 destroy 된 뒤 재생성된다. 이 경로에서 프로세스와 `ViewModel` 은 유지된다.
4. 재생성된 Activity 는 새 방향의 화면 크기로 `ViewRootImpl` 을 통해 다시 windowManagerService 에 윈도우 정보를 알리고, View 트리는 새 크기로 measure/layout 을 다시 수행한다.
5. 새로 계산된 UI 는 다시 그려져 Surface 에 제출되고, SurfaceFlinger 가 새 프레임을 합성해 화면에 표시한다.

같은 회전 사건이라도 3 번은 5 장의 lifetime 모델로, 4~5 번은 이 장의 입력 - 리소스 - 프레임 모델로 설명해야 한다. 어느 한 장의 모델만으로는 "회전하면 무슨 일이 일어나는가"에 완전히 답할 수 없다.

### 실패 사례: jank 를 구간별로 분류한다

사용자가 스크롤할 때 화면이 끊긴다는 증상은 이 루프의 여러 지점 중 하나가 프레임 예산을 넘겼다는 뜻이다. UI thread 의 과도한 measure/layout, RenderThread 의 지연, GPU 작업, `BufferQueue` 의 backpressure, SurfaceFlinger/HWC 합성 지연 중 어디가 원인인지에 따라 처방이 다르다. "[recomposition](../../02_app_framework/jetpack-compose/runtime/recomposition.md) 이 많다"와 "합성이 느리다"는 같은 "jank"라는 이름 아래 있어도 관찰 지점과 해결 방법이 다르다.

### 조사 방법: 입력에서 프레임까지 어디서 지연이 생겼는지 분류한다

1. **입력이 언제 도착했고 언제 처리됐는가?** `adb shell dumpsys input` 으로 입력 라우팅 대상을, 프레임 trace 로 처리 시점을 확인한다.
2. **configuration 변경으로 인한 재구성인가, 단순 프레임 지연인가?** Activity 재생성 로그가 있는지 먼저 구분한다(5 장 참고).
3. **UI 상태 계산과 그리기 명령 생성 중 어디가 오래 걸렸는가?** Compose recomposition 범위나 View measure/layout 비용을 본다.
4. **RenderThread, BufferQueue, SurfaceFlinger/HWC 중 어디서 막혔는가?** Perfetto 나 `dumpsys gfxinfo` 로 각 구간의 시간을 분리해서 본다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| 앱이 화면에 그리면 그 결과가 곧바로 화면에 나타난다. | 앱은 Surface 에 버퍼를 채울 뿐이며, 화면상의 배치는 WindowManager 가 쥔 SurfaceControl 과 SurfaceFlinger 의 합성을 거쳐야 한다. |
| 입력 이벤트는 앱 코드가 등록한 리스너로 바로 전달된다. | 입력은 InputDispatcher 가 대상 윈도우를 결정하고, ViewRootImpl 을 거쳐 main thread 큐에 들어간 뒤에야 리스너에 도달한다. |
| configuration change 는 리소스 값 하나만 바뀌는 가벼운 이벤트다. | 언어·화면 크기 변경은 리소스 테이블 재선택을 요구하며, 이것이 Activity 재생성이라는 무거운 메커니즘의 이유다. |
| RenderThread 가 있으니 그리기는 항상 UI thread 와 무관하게 빠르다. | UI thread 가 늦게 display list 를 만들면 RenderThread 가 빨라도 프레임 deadline 을 놓친다. |
| jank 는 항상 GPU 나 SurfaceFlinger 의 문제다. | jank 의 원인은 UI thread 작업, RenderThread, BufferQueue backpressure, SurfaceFlinger/HWC 합성 중 어디에나 있을 수 있다. |
| 화면 회전은 이 장 또는 5 장 중 한쪽 모델로만 설명하면 충분하다. | 회전은 5 장의 lifetime 재구성과 이 장의 리소스 재선택·재측정·재합성이 함께 일어나는 사건이다. |

### 확인 질문

1. 물리 입력이 특정 윈도우로 전달되기까지 어떤 구성요소를 거치는가?
2. ViewRootImpl 은 View 트리와 어떤 시스템 구성요소를 연결하는가?
3. 입력 이벤트가 6 장의 main thread 이벤트 큐를 거쳐야 하는 이유는 무엇인가?
4. configuration change 가 리소스 재선택을 요구하는 이유는 무엇이며, 이것이 왜 Activity 재생성으로 이어지는가?
5. View 시스템과 Compose 는 UI 상태를 그리기 명령으로 바꾸는 방식이 어떻게 다른가?
6. 앱이 받는 Surface 와 WindowManager 가 쥐고 있는 SurfaceControl 은 각각 무엇을 담당하는가?
7. 화면 회전 사건에서 5 장의 모델과 이 장의 모델은 각각 어떤 부분을 설명하는가?
8. jank 를 진단할 때 왜 하나의 구간만 보고 원인을 단정하면 안 되는가?

### 다음 장으로 이어지는 질문

이 장은 입력과 configuration 이 UI 상태를 거쳐 화면 프레임으로 이어지는 경로를 다뤘다. 그러나 그 화면이 보여주는 데이터 자체가 어디서 오고, 네트워크가 끊겼을 때 어떻게 복구되는지는 아직 다루지 않았다.

다음 장에서는 데이터가 어느 owner 에 의해 보존되고, 실패 이후 어떻게 복구되는지를 다룬다.

- 화면이 관찰하는 데이터의 source of truth 는 어디에 있는가?
- 네트워크 요청이 실패하거나 프로세스가 죽어도 데이터가 유실되지 않으려면 무엇이 필요한가?
- 로컬 상태와 서버 상태가 다를 때 이를 어떻게 조정하는가?

### 관련 정본

- [InputManager/InputDevice는 물리 입력 장치를 이벤트 소스로 추상화한다](../../04_system_services/device-capabilities/input-accessibility-contracts/inputmanager-abstracts-physical-input-devices-as-event-sources.md)
- [설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다](../../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md)
- [View System은 object tree를 변경하고 Compose는 state에서 UI를 재계산한다](../../02_app_framework/ui/system/ui-system-contracts/view-system-mutates-object-tree-while-compose-recomputes-ui-from-state.md)
- [Compose 프레임 파이프라인은 Composition, Layout, Drawing 단계로 분리된다](../../02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)
- [Canvas, Skia, Compose는 합성기가 아니라 그리기 명령의 생산자다](../../01_system_internals/graphics-and-media/graphics-media-contracts/canvas-skia-and-compose-produce-drawing-commands-not-display-composition.md)
- [RenderThread는 렌더 작업을 나누지만 UI 스레드 비용을 없애지 않는다](../../01_system_internals/graphics-and-media/graphics-media-contracts/renderthread-submits-render-work-without-making-ui-thread-free.md)
- [Surface는 그래픽 버퍼 producer 측 계약이다](../../01_system_internals/graphics-and-media/graphics-media-contracts/surface-is-producer-side-contract-for-graphic-buffers.md)
- [BufferQueue는 producer와 consumer를 버퍼 소유권으로 분리한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md)
- [SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md)
- [VSync와 Choreographer는 frame deadline을 정의한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](../../01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
- [Android 렌더링 파이프라인은 Surface 버퍼를 합성기로 넘기는 계약이다](../../01_system_internals/graphics-and-media/graphics-media-contracts/android-rendering-pipeline-is-surface-to-bufferqueue-to-compositor.md)

### 공식 근거

- [Input pipeline overview](https://source.android.com/docs/core/interaction/input)
- [SurfaceFlinger and WindowManager](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager)
- [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes)
- [Compose phases](https://developer.android.com/develop/ui/compose/phases)
- [Choreographer API reference](https://developer.android.com/reference/android/view/Choreographer)
- [Slow rendering](https://developer.android.com/topic/performance/vitals/render)

검증일: 2026-08-03. ViewRootImpl/WindowManagerService/SurfaceControl 의 내부 통신(window session, IWindowSession)은 AOSP 소스 구조에 속하며 프레임워크 버전에 따라 세부 구현이 달라질 수 있다. 이 장은 공식 문서로 확인 가능한 수준의 책임 분리까지만 다뤘다.
