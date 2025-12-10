---
title: flutter under the hood
tags: [concept, flutter]
aliases: []
date modified: 2024-12-16 15:31:54 +09:00
date created: 2024-12-14 11:17:03 +09:00
---

## flutter framework

- 모두 이해하는데 많은 시간이 걸림
- 우선 최고의 performance 를 위해 무엇을 optimization 해야하는지 이해하자
![Flutter Pipeline](flutter_pipeline.jpeg)
- Flutter Framework 와 그 layers 를 이해하는데 도움이 되는 그림
    - 각각의 **상위에 있는 layer 들은 모두 abstraction** 으로 이루어져 있음

### dart:ui

- path: FLUTTER_PATH/bin/cache/pkg/sky_engine/lib/ui
- 패키지는 Flutter framework 가 어플리케이션을 만들기 위한 가장 낮은 수준의 서비스를 노출한다
    - input, layout, graphics, rendering system 같은 것들
    - 심지어 dart:ui 라이브러리만 이용해서 어플리케이션을 만드는 것도 " 가능은 " 하다

### Rendering

- path: FLUTTER_PATH/packages/flutter/lib/rendering.dart
- Flutter 의 rendering tree
- dart:ui 라이브러리의 상위 레이어에 존재함
- widgets 의 layout 과 painting 을 어떻게 구성할지를 책임짐
- Renderbox 와 RenderObject 를 사용함
    - 이 클래스들은 layout, painting, hit testing 를 위한 method 를 제공함

### Widgets

- path: FLUTTER_PATH/packages/flutter/lib/widgets.dart
- layout, painting, hit testing 을 쉽게 만들어주는 요소
- 개발자에게 가장 익숙한 layer
- Flutter Framework 는 UI 구성요소의 설정을 담당하는 widgets 을 제공하여 RenderObject 를 추상화함

### Material and Cupertino

- path: FLUTTER_PATH/packages/flutter/lib
- 가장 상위에 있는 layer
- Material 혹은 iOS 스타일을 따를 수 있는 UI 요소 제공하기 위해 추상화

### Framework

- 모든 layer 를 포함하고 있는 곳
- 이러한 layering 으로 인해 빠른 성능이 가능함
    - performance, development 두 가지 관점에서 모두
- 개발자는 간단하게 material, cupertino, widgets 를 사용하지만 rendering layer 는 아래에서 많은 일을 처리한다
    - 하지만, 최고의 성능을 내기 위해 때로는 Framework 에게 가이드를 내려줘야하는 경우도 있다

**개발자는 Widgets 을 직접 사용하지만, 실제로 Widgets 은 rendering 을 전혀 관리하지 않는다!**

참고자료

[Flutter Under the Hood](https://medium.com/surfstudio/flutter-under-the-hood-401503d2979e)

## Widget, Element, RenderObject

- Flutter 은 Widgets, Elements, RenderObjects 로 나누어짐

| Widgets   | Elements | Render Object |
| --------- | -------- | ------------- |
| immutable | mutable  | mutable       |

![Flutter Tree](flutter_tree.png)

1. Widget
	- 오직 Configuration 에 관련됨
	- build 메소드가 불릴 때 마다 빠르게 화면을 그리는 것이 가능한 이유
	- 설정값을 가지고 있음 (holds config)
		- Blueprint 역할을 함
	- UI 에 대해 설명함
	- 화면에 그리는 것을 담당하지 않음 ⇒ RenderObjects 가 담당함
	- Widget 이 tree 에 위치하게 되면, Element 에 inflate 되고, tree 에 여러번 추가된 widget 은 여러번 inflate 된다
		- inflate: 부풀리다 ⇒ layout 에 그때 그때 다른 layout 을 집어 넣을 수 있다는 의미
		- 안드로이드에서의 의미: 레이아웃들을 메모리에 객체화시킴
	- widget 을 만들고 widget tree 를 업데이트 하는 performance cost 에 대한 걱정을 덜어주게 함
		- widget 을 다시 만드는 것이 반드시 아래에 있는 render object 를 다시 생성하는 것이 아니므로
		- 새로운 widget configuration 을 갖기 위해 오직 연결된 RenderObject 만 업데이트 한다
2. Element
	- Mutable 객체
	- 생명주기를 책임지고, widget 을 위계로 정렬 및 RenderObject 와 연결하는 역할을 함
	- widget layer 와 render layer 를 붙이는 glue 역할
	- widget 은 immutable 하기 때문에 부모 자식 관계를 기억할 수 없지만, Element 는 이를 기억하고 UI 의 논리적 구조를 유지한다
	- widget 설정 변화가 있을 때, 변화를 연관있는 RenderObject 에 전달함
	- StatefulWidget 에서는 State 정보 역시 포함 한다
	- 성능에 대해 걱정하지 않고 widget tree 를 자유자재로 없애고 만들게 해주는 역할을 함
	- Widget 과 RederObject 의 레퍼런스를 가지고 있음 (holds reference)
		- Life Cycle 역할을 함
	- Element 는 생성이 비싸기 때문에 재사용할 수 있으면 재사용 된다
		- Keys(ValueKey 나 GlobalKey) 를 이용하여 재사용 한다
		- widget 이 GlabalKey 를 가지고 있고, 이미 같은 GlobalKey 인 widget 을 element 가 가지고 있다면, element 는 재사용 된다
	- render tree 를 관리함
		- render tree: 화면에 그려질 render objects 들의 tree.
		- UI hierarchy 의 위치 정보를 가지고 있고, parent/child 관계를 관리함
	- widget tree 가 바뀌면, element tree 는 tree 를 그리기 위해 필요한 작업을 처리함
	- build 메소드의 BuildContext 는 사실 해당 widget 에 상응하는 element 이다
		- Element 정의로 가서 확인해보면 BuildContext 를 implements 한 것 확인할 수 있음
	- element life cycle
		- Widget.createElement() 로 element 가 생성됨
		- **mount** 메소드가 새롭게 추가된 element 를 주어진 parent 에 맞는 주어진 slot 에 element 를 추가함
		- element 가 추가 되면서, element 는 **active** 한 상태로 변경되고 화면에 나타남
		- element 와 연관된 widget 이 바뀌었을 때
			1. newWidget 이 oldWidget 의 runtimeType 과 key 가 같다면 element 는 newWidget 과 새로 연결되고 계속 사용됨
			2. 그렇지 않은 경우, element 는 tree 로 부터 제거되고 새 element 가 만들어짐
		- widget 이 삭제될 때, 삭제되는 element 는 **inactive** 상태로 바뀌게 되고 화면에서 사라짐
			- element 랑 연결된 render object 는 render tree 에서 삭제됨
			- 같은 frame 단위 안에서만 inactive 상태로 element tree 에 남아있을 수 있음
			- 같은 frame 안에 inactive 상태에서 변경되지 않았다면 deactivateChild 메소드를 불러 element 를 **deactivate** 상태로 만듬
			- element 가 다시 element tree 로 들어가는 경우 (ex. key 재사용) inactive element 리스트에서 제거되고, activate 메소드를 불러 해당 element 를 element tree 로 다시 포함 되게 됨
3. RenderObject
	- Mutable 객체
	- widget 의 configuration 을 화면의 pixel 로 바꾸는 역할
	- 직접적으로 화면에 그리는 담당
	- 기본적인 layout 과 paint protocol 을 책임진다
	- 성능 이슈 없이 만들고 없애는 것이 불가능함 ⇒ 재활용 (그래서 mutable)
	- render tree 안의 객체
		- render tree: UI 의 geometry 정보를 포함하는 data structure
		- layout 동안 계산되고, painting, hit testing 동안 사용된다
		- 대부분의 개발자는 RenderObject 를 직접 생산하진 않지만 widget 을 이용하여 조작하게 된다
	- size, layout, painting, compositing 처리함
		- Painting 역할을 함
	- 대부분의 경우 직접 만들 필요는 전혀 없다

![Flutter 3 Structure](flutter_3_structure.png)

**왜 3 개의 tree 로 나눠지는가?**

- 1) Complexity 와 Reactive Paradigm, 2) Performance 의 이유
    1. Complexity and Reactive Paradigm
        - 개발자는 Widget 만 신경쓰면 RenderObject 와 LifeCycle 을 직접 관리하는 일은 없다
	- Reactive Paradigm
		- 부드러운 UI 전환과 real-time 업데이트를 보증하기 위해 "events" 를 제대로 처리하는 것이 이 패러다임의 목적
		- 목표
			- 추상화 수준을 제공하여 많은 구현 세부 사항을 처리하도록 강요하기보다는 애플리케이션에서 생성될 이벤트에 집중할 수 있도록 하는 것
			   - Instagram 의 "Like" 버튼을 눌렀을 때 Like Event 로 발생하는 비즈니스 로직에 집중하고 나머지 구현 세부사항은 강요하지 않음
			   ![[reactive_paradigm.png]]
    1. Performance
        - widget 이 rebuilding 되어야 하는 상황에 (ex.setState), framework 는 필요한 부분만 업데이트 하기 위해서 old tree 와 new tree 사이에 변화된 것을 찾는다
        - widget, element, render tree 를 각각 비교 ⇒ 무엇이 업데이트 되어야하는지 framework 에게 알려주는 역할을 함
        - 각각으로 나누어서 필요한 부분만 바꾸기 때문에 flutter 가 빠름

## Flutter's Rendering Pipeline

![Flutter Rendering Pipeline](flutter_rendering_pipeline.png)

vsync : 화면의 트랙을 유지하는 역할

- 화면이 없는 부분에서는 아무것도 그리지 않게 도와줌

Rendering 에 관련된 타임라인을 Build - Layout - Paint 페이즈로 나눌 수 있음

![Rendering Phase](flutter_rendering_phase.png)

- 이 페이즈들을 거쳐 Display list 생성 → GPU 에 의해 rasterize 됨
	- rasterize: 벡터 그래픽 형식으로 설명된 이미지를 픽셀로 생성하는 작업
- Build Phase
	- 개발자가 책임이 있는 곳
	- 대부분의 control 을 가지고 있는 곳
	- Layout 과 Painting Phase 는 Framework 가 처리하기 때문에 신경쓸 필요 없음
		- 특정 부분은 개발자가 control 할 수 있음
![Rendering Process 1](flutter_rendering_process1.png)
- Widget Tree 와 Element Tree 는 같은 Node 수를 가지고 있지만, RenderObject 는 작은 Node 수를 가지고 있다
	- 몇몇의 Widget 은 component 여서 RenderObject 를 만들지 않기 때문
- Display list 는 Rendered Image
![Rendering Process 2](flutter_rendering_process2.png)
- 개발자가 정의한 Widget 외에도 Node 가 생겼음
	- Flutter Framework 가 자체적으로 생성함
![Process 3](flutter_rendering_process3.png)
- ComponentElement
	- 다른 Elements 를 생성하는 Element (ex. StatelessElement, StatefulElement)
	- 다른 Element 를 생성하므로서 간접적으로 RenderObject 를 생성
	- RenderObjectElement 와 반대
- RenderObjectElement
	- RenderObjectWidget 을 설정값으로 사용하는 Element
	- render tree 에 RenderObject 와 관련 있음
- Element 는 Widget tree 를 추적함
	- RenderObject 와 widget 을 연결하는 역할을 함
- 관련 코드
```dart
// Element의 mount 하는 코드
void mount(Element parent, dynamic newSlot) {
    assert(_debugLifecycleState == _ElementLifecycle.initial);
    assert(widget != null);
    assert(_parent == null);
    assert(parent == null || parent._debugLifecycleState == _ElementLifecycle.active);
    assert(slot == null);
    assert(depth == null);
    assert(!_active);
    _parent = parent;
    _slot = newSlot;
    _depth = _parent != null ? _parent.depth + 1 : 1;
    _active = true;
    if (parent != null)
        _owner = parent.owner;
    if (widget.key is GlobalKey) {
        final GlobalKey key = widget.key;
        key._register(this);
    }
    _updateInheritance();
    assert(() {
        _debugLifecycleState = _ElementLifecycle.active;
        return true;
    }());
}
```

- 별다른 사항이 없어서 Element 의 추상인 BuildContext 를 가서 확인

```dart
RenderObject? get renderObject {
    RenderObject? result;
    void visit(Element element) {
      assert(result == null); // this verifies that there's only one child
      if (element._lifecycleState == _ElementLifecycle.defunct) {
        return;
      } else if (element is RenderObjectElement) {
        result = element.renderObject;
      } else {
        element.visitChildren(visit);
      }
    }
    visit(this);
    return result;
  }
```
- 여기서 확인할 수 있듯이 RenderObjectElement 일때 만 이에 상응하는 RenderObject 를 만든다
![Rendering Process 3](flutter_rendering_process3.png)
- StatefulWidget 을 생성하는 경우에는 State 는 Element 에 의해 관리됨
![Rendering Process 4](flutter_rendering_process4.png)
![Rendering Process 5](flutter_rendering_process5.png)
- build, layout, paint, compositing 이후, Flutter framework 가 render tree 를 마무리하고, 모든 정보를 raster thread 로 보낸다
	- 모든 painting construction 을 display list 라고 함
	- display list: 그래픽 명령어 묶음
- Skia 엔진에 의해 명령이 처리되어 그려짐

**Widget Tree 가 업데이트 될 때 (ex. setState) 는 어떻게 되는가?**

- Widget 은 immutable 하기 때문에 이전 Widget Tree 를 모두 버림
![Rendering Process 6](flutter_rendering_process6.png)
- 새 Widget Tree 를 만듬
![Rendering Process 7](flutter_rendering_process7.png)
- Element 와 RenderObject 에게는 다르기 때문에 구성을 바꿈
	- 언제, 어떻게 바꾸나? ⇒ Element, Element Tree 에 의해 관리됨
- Element.updateChild() method 가 Widget 으로부터 온 새 configuration 을 이용해서 자식을 바꿈
- update 하기전에 update 가능한지 먼저 확인
	- 업데이트 불가능하면 Element, RenderObject 를 다시 만들어야 하기 때문
	- 코드
```dart
static bool canUpdate(Widget oldWidget, Widget newWidget) {
    return oldWidget.runtimeType == newWidget.runtimeType && oldWidget.key == newWidget.key;
}
```

![Rendering Process 8](flutter_rendering_process8.png)

- ComponentElement 는 update() method 를 사용
![Rendering Process 9](flutter_rendering_process9.png)
- 중요한 점: 바뀌는 새 Widget 은 반드시 같은 runType 을 가지는 Widget 이어야 함
	- performance 에 중요한 영향을 미치는 부분
	- 만약 다르게 되면, 전체 render tree 를 다시 그려야하기 때문에 비용이 비싸게 됨
	- 위의 코드 참고
- configuration 값을 업데이트 한 이후에 updateChild() method 호출
![Rendering Process 10](flutter_rendering_process10.png)
- RenderObjectElement 역시 update() method 를 사용하여 configuration 을 바꾼 이후 ComponentElement 와 다르게 수행됨
- updateRenderObject() method 를 수행하게 됨
	- RenderObjectWidget 의 configuration 을 RenderObject 로 복사함
- 이전 configuration 과 변한 것이 없으면 update 하지 않음
![Rendering Process 11](flutter_rendering_process11.png)

![Rendering Process 12](flutter_rendering_process12.png)

![Rendering Process 13](flutter_rendering_process13.png)

- 앞선 과정을 같은 프로세스로 반복
- 업데이트가 필요한 Text Widget 의 경우, updateRenderObject 가 업데이트 됨
![Rendering Process 14](flutter_rendering_process14.png)
- Flutter Framework 는 RenderObject 를 최대한 재사용하려고 한다는 것을 이해해야함
	- framework 가 똑똑한 선택을 하게 하기 위해 guide 를 제공해줄 수 있음
	1. Widget: 필요한 부분만 update
	2. Element: Keys, Same Type 제공
	3. Layout, Paint: RepaintBoundary 을 small part 에만 적용

여기서 질문이 남음.

**기능을 어떻게 보증할 수 있는가?**

---
## Binding

- Flutter Scheme
![System Overview](flutter_system_overview.png)
- Layered Cake 이라고 불림
	- 큰 layer 와 작은 layer 로 구성됨
- 구성
	1. The framework level
		- flutter application 을 작성할 때 사용하는 모든 것을 포함함
			- 더 저수준의 엔진 계층과 소통하게 해주는 코드인 service class 들도 포함
	2. The engine level
		- Dart VM, Skia 등 프레임워크 레벨의 기능들을 보증하는 클래스와 라이브러리로 구성되어 있음
	3. The platform level
		- 특정 플랫폼 (iOS, Android, Windows, …) 와 관련된 코드를 포함
- Framework level 중 가장 low-level 인 foundation layer 를 주목하자
	- framework level 에서 가장 근본적이고, 기본적인 계층

> 코어 플러터 프레임워크 기초요소
  - 이 라이브러리에 정의된 기능은 Flutter 프레임워크의 다른 모든 계층에서 사용되는 가장 낮은 수준의 유틸리티 클래스 및 기능입니다.
- 이 계층은 모든 결합 (Bindings) 의 기본 클래스인 BindingBase 도 포함하고 있음
- 결합 (바인딩) 이란?

> 싱글톤 서비스 (" 바인딩 " 이라고도 함) 를 제공하는 mixin 의 기본 클래스입니다. mixin 의 'on' 절에서 이 클래스를 사용하려면 이 클래스를 상속하고 [initInstances()] 를 구현하세요. mixin 은 앱의 수명 동안 한 번만 생성되도록 보장됩니다 (더 정확하게는 체크 모드에서 두 번 생성되면 assertion 됩니다).

- 플러터의 engine level 과 framework level 을 연결하는 역할을 함
- BindingBase 는 기본 추상 클래스임
	- 구체 Binding 예시
		1. ServicesBinding
			- 플랫폼 메시지를 수신 대기하고 들어오는 메시지에 대한 핸들러 (BinaryMessenger) 로 전달
		2. PaintingBinding
			- painting library 에 연결하는 역할
		3. RenderBinding
			- render tree 를 Flutter engine 에 연결하는 역할
		4. WidgetBinding
			- widget tree 를 flutter engine 에 연결하는 역할
		5. SchedulerBinding
			- 다음과 같은 즉각적인 작업을 실행하기 위한 스케줄러
			1. transient callbacks : Window.onBeginFrame callback 에 의해서 호출되는 callback. ex) Ticker, AnimationController events
			2. persistent callbacks : Window.onDrawFrame callback 에 의해서 호출되는 callback. transient callbacks 가 수행되고 난 이후에 화면을 변경하는 역할을 함
			3. post-frame callbacks : persistent callbacks 이후에 수행되는 작업. Window.onDrawFrame 으로부터 리턴되기 전에 호출 됨
			4. non-rendering tasks : 프레임 사이사이 수행되는 작업
		6. SemanticsBinding
			- Semantics layer 과 Flutter engine 을 연결하는 역할
		7. GestureBinding
			- Gesture System 과 연결하는 역할
- 각각의 Binding 은 특정 작업에 대한 책임이 있음

### WidgetsFlutterBinding
- 어떻게 모든 요소들이 함께 동작하는지 이해하기 위해서 Flutter app 의 entry point 에서 이해해보자
```dart
void runApp(Widget app) {
  WidgetsFlutterBinding.ensureInitialized()
	..scheduleAttachRootWidget(app)
	..scheduleWarmUpFrame();
}
```
- runApp 메소드는 binding.dart 에 위치함
	- 위젯을 inflate 시키고 화면에 띄우는 역할을 함
- WidgetsFlutterBinding?
	- 구체화된 Binding 의 구현
	- Widgets framework 에 기반함
	- framework 를 flutter engine 과 연결하는 역할을 함
	- 여러가지 Binding 을 구성으로 가짐
		- _GestureBinding_, _ServicesBinding_, _SchedulerBinding_, _PaintingBinding_, _SemanticsBinding_, _RendererBinding_, _WidgetsBinding_
	- 이 여러가지 Binding 이 application 과 flutter engine 을 모든 방향에서 연결하게 만들어 줌
- scheduleAttachRootWidget?
	- attachRootWidget 메소드의 구현에 예약 (Timer.run) 을 추가한 메소드
	- attachRootMethod 는 WidgetsBinding 의 메소드임
	- 주어진 widget 을 element tree 의 뿌리인 renderViewElement 와 연결하는 역할을 함
```dart
void attachRootWidget(Widget rootWidget) {
   _renderViewElement = RenderObjectToWidgetAdapter<RenderBox>(
	 container: renderView,
	 debugShortDescription: '[root]',
	 child: rootWidget,
   ).attachToRenderTree(buildOwner, renderViewElement);
}

// RenderObject 자리에 renderView를 할당하는데 renderView는 무엇?
// - render tree의 뿌리 element
// - 찾아가보면 RenderView는 RenderObject의 자식 클래스
...

RenderView get renderView => _pipelineOwner.rootNode;
// PipelineOwner는 rendering pipeline을 책임지는 관리자 역할
```
- attachRootWidget 메소드를 확인해보면 생성된 adapter 가 attachToRenderTree 를 호출하는 것을 볼 수 있음
	- attachToRenderTree 에서 파라미터로 사용되는 buildOwner 는 무엇?
		- BuildOwner 는 widgets framework 관리자
		- widgets 의 state 추적
		- 어떤 widgets 을 다시 빌드해야하는지 추적
		- widget tree 의 상태를 업데이트 하는 것과 관련된 중요한 업무들을 가짐
- 이러한 방식으로 세가지 tree (widget: buildOwner, element: renderViewElement, renderObject: renderView) 를 만들고, 세 tree 는 Binding 을 이용해서 저장, 관리 된다

### scheduleWarmUpFrame
- SchedulerBinding 에 속한 메소드
- 시스템의 vsync 신호를 기다리는 것 보다, 최대한 빠르게 수행되기 위해 frame 을 예약하기 위해 사용됨
- 앱이 실행될 때 method 가 수행되기 때문에 (비싼 연산 수행), 첫번째 frame 은 실행되는데 시간이 더 소요됨
- 예약된 프레임이 완료될 때까지 전달되는 이벤트를 잠금
- ![Flutter Diagram](flutter_diagram.png)
! Binding 은 flutter app 에서 작업을 구성하는 매우 중요한 매커니즘
- 앱의 다양한 부분을 묶고 engine 과 연결하는 역할을 함
- 프레임워크의 가장 높은 레벨의 부분을 하위 레벨의 코드를 걱정하지 않고 작성하게 도와줌

## Owners

### Frame building

- 위의 내용에서는 간단하게 Widget, Element, RenderObject 의 상호작용을 설명했지만 실제로는 더 복잡함
- 실제 프로세스를 알기 위해서는 어떻게 flutter 가 frame 을 생성하는지 이해해야 함
	- SchedulerBinding 은 다음과 같은 단계를 가지고 있음
		1. Idle
			- 어떠한 프레임도 처리되지 않음
			- microtasks 같은 일들이 수행되는 단계
		2. TransientCallbacks
			- transient callbacks 들 이 수행되는 단계
			- animation update 를 위해 사용됨
		3. MidFrameMicrotasks
			- transient callbacks 처리에서 예약된 microtasks 들이 처리되는 단계
		4. PersistentCallbacks
			- build, layout, paint pipeline 을 처리하기 위해 사용되는 단계
		5. PostFrameCallbacks
			- 다음 프레임의 작업을 위해 사용되는 단계
	- Idle 을 제외한 모든 상태는 새 frame 을 만들기 위해 사용됨
	- 각 frame 은 다음 10 가지 단계를 완료함
		1. Animation Step
			- handleBeginFrame 을 호출하면서 등록 순서대로 scheduleFrameCallback 에 등록된 모든 콜백의 처리를 시작
			- 가장 일반적인 예는 AnimationController 의 Ticker
			- 모든 수행중인 애니메이션은 이런 방식으로 정보 업데이트를 하게 됨
			- 이 단계가 첫번째로 수행되는 이유?
				- 후의 나머지 단계에서 실제 화면의 애니메이션 변화를 수행하기 때문
		2. Microtasks Step
			- handleBeginFrame 이 끝난 이후 모든 microtasks 시작
		3. Build Step
			- 업데이트가 필요하다고 표시된 모든 element 들 rebuild
		4. Layout Step
			- 업데이트 필요한 RenderObject 들 업데이트
			- 어떠한 RenderObject 가 repaint 되어야 되는지 찾아냄
		5. Composition bits Step
			- 업데이트가 필요한 compositing bits 가 업데이트 됨
		6. Paint Step
			- 모든 dirty RenderObject 들은 다시 paint 됨
			- 이 단계 이후 layout tree 가 생성됨
		7. Composition Step
			- layout tree 는 scene(=그려야하는 것을 설명하는 특수 개체) 으로 변환되어 GPU 로 전송됨
		8. Semantic Step
			- 모든 dirty RenderObject 들이 semantic properties 를 업데이트 함
			- semantic tree 가 만들어짐
				- semantic tree 는 시스템 보조 기술 내에서 의미전달을 돕기 위해 엔진에서 사용
		9. Widgets layer finalization Step
			- widget tree 가 완료됨
			- 사용하지 않는 state 와 element 들이 제거됨
		10. Scheduler finalization Step
			- _addPostFrameCallback_ 에 등록된 모든 callback 들이 수행됨
- 누가 위와 같이 복잡한 단계를 생성하는가?
	- BuildOwner & PipelineOwner

### BuildOwner

- build, update 및 element 의 모든 내부 작업을 관리함
- frame step 중 Build, Widgets layer finalization 을 담당함
- tree 만드는 것을 관리하기 위해서, BuildOwner 는 업데이트가 필요한 element 리스트를 받아야함
	- 내부에 이 리스트를 저장
- 메소드들
	1. scheduleBuildFor
		- element 를 markNeeds~ 상태로 만들어줌
		- element 를 dirty element 리스트에 넣어서 추후에 업데이트 가능하게 만들어줌
	2. lockState
		- 제거될 때 element 가 잘못된 dirty mark 를 사용하지 않게 막아주는 메커니즘
	3. buildScope
		- widget tree 를 업데이트 하기 위한 scope 만들어줌
		- dirty element 리스트 사용함
	4. finalizeTree
		- tree 생성을 마무리함
		- 더이상 active 상태가 아닌 element 를 제거
		- debug 모드 일 때는 복사된 global key 를 체크한다던지 하는 작업을 수행함
	5. reassemble
		- 이것은 HotReload 메커니즘의 핵심 기능
		- HotReload 를 사용하면 변경 사항을 적용하고 새 버전의 코드를 VM 에 보낼 때 애플리케이션을 계속해서 다시 컴파일하는 것을 방지할 수 있음
	- 모든 메소드는 10 단계 내에서 사용됨
	- 예시
```dart
// WidgetsBinding.drawFrame

if (renderViewElement !=null)
	// 3. build step
	buildOwner.buildScope(renderViewElement);
// 4~8 : PipelineOwner 부분에서 설명
super.drawFrame();
// 9. Widgets layer finalization step
buildOwner.finalizeTree();
```
- 모든 것이 합쳐져서 어떻게 동작하는지 보려면 Element.rebuild 메소드를 잠시 확인하고 와야함
- Element.rebuild
	- 언제 호출되는가?
	1. tree 가 만들어질 때, BuildOwner 에 의해서 호출
	2. 처음 tree 에 inflate 될 때, ComponentElement 에 의해서 호출
	3. ComponentElement 가 업데이트 될 때 호출
	![Element.rebuild](flutter_element_rebuild.png)

	- rebuild 메소드는 performRebuild 메소드를 호출함
		- element 마다 구현이 다르기 때문에 흥미로운 메소드
			- RenderObjectElement 에서는 RenderObject 업데이트
			- ComponentElement 에서는 build(StatelessWidget, StatefulWidget 이 가지고 있는 그것)

	![Element.performRebuild](flutter_element_perform_rebuild.png)

	- Element.updateChild 에 보내는 widget 을 리턴
		- widget 은 해당 element 에서 mounted 되거나 updated 될 것임

	![Element.updateChild](flutter_element_update_child.png)

	- BuildOwner.buildScope 일 때는 어떤 일이 발생하는가?
		- dirty 라고 표시된 모든 element 를 rebuild
		- dirty 하게 만드는 방법
		1. 비활성화된 element 를 다시 활성화
		2. 애플리케이션 시작될 때, render tree 에 widget 을 연결했을 때
		3. setState 불렀을 때
		4. HotReload 했을 때
		5. dependency 가 바뀌었을 때

### PipelineOwner
- frame 준비하는 역할을 하는 관리자
- rendering pipeline 을 작동 시킴
- 4. Layout ~ 8) Semantic Step 까지 작동됨
- 코드 참고
```dart
// WidgetsBinding.drawFrame

if (renderViewElement !=null)
		// 3. build step
	buildOwner.buildScope(renderViewElement);
// 4~8 : PipelineOwner 부분에서 설명
super.drawFrame();
// 9. Widgets layer finalization step
buildOwner.finalizeTree();
```
- super.drawFrame?
```dart
/// RendererBinding.drawFrame

@protected
void drawFrame() {
  assert(renderView !=null);
  pipelineOwner.flushLayout(); // 5. Layout Step
  pipelineOwner.flushCompositingBits(); // 6. Composition Step
  pipelineOwner.flushPaint(); // 7. Paint Step
  if (sendFramesToEngine) {
	renderView.compositeFrame();
	pipelineOwner.flushSemantics(); // 8. Semantic Step
	_firstFrameSent =true;
  }
}
```
- BuildOwner, PipelineOwner 모두 업데이트 되야 되는 객체 리스트를 저장함
	- 하지만 PipelineOwner 는 RenderObject 리스트를 저장함
- 메소드 종류
	1. flushLayout
		- 레이아웃이 필요한 모든 RenderObject 가 처리됨
		- 레이아웃이 다시 계산되고 RenderObject 을 다시 칠해야한다고 표시됨
	2. flushCompositingBits
		- 위와 동일하지만, 구성에 직접 참여하는 특수 RenderObject 의 경우를 처리함
		- 이렇게 두 가지 메소드를 처리하면 다시 칠해야하는 RenderObject 들이 모두 정의됨
	3. flushPaint
		- 다시 칠해야된다고 표시된 객체를 다시 칠함
	- 모든 작업이 끝난 이후에 render tree 의 최상단에 있는 compositeFrame 메소드가 불리게 됨
		- Scene 객체를 만들고 engine 에 보내서 화면에 보여줄 수 있게 처리됨
```dart
/// compositeFrame.dart

final ui.SceneBuilder builder = ui.SceneBuilder();
final ui.Scene scene = layer.buildScene(builder);
if (automaticSystemUiAdjustment)
	_updateSystemChrome();
_window.render(scene);
```

### Layout Algorithm
- layout building 에서 중요한 부분
- Flutter 는 초기 레이아웃에 대한 선형 성능과 기존 레이아웃을 후에 업데이트하는 일반적인 경우의 하위 선형 레이아웃 성능을 목표로 함
	- 즉, 이는 레이아웃에 소요된 시간이 RenderObject 의 수보다 느리게 커져야 함을 의미
- 이러한 성능을 보장하기 위해서, Flutter 는 다음과 같은 규칙을 사용함
	1. 제약 조건은 부모에서 자식으로 내려감
	2. 크기는 자식에서 부모로 갈때 커짐
	3. 부모는 자녀를 배치
	- 직접적인 계산은 그다지 효과적이지 않음 ⇒ Flutter 는 까다로운 최적화를 가지고 있기 때문
- 까다로운 최적화 조건 (일부는 무슨 말인지 모르겠음)
	1. 자식 개체가 업데이트에 필요한 자체 레이아웃을 표시하지 않은 경우, 동일한 제약 조건을 받는 동안 다시 계산하지 않음
	2. 부모가 자식의 레이아웃 메서드를 호출할 때마다 크기가 자체 계산에 사용되는지 선언
	3. 부모가 자식 개체의 레이아웃 메서드를 호출할 때마다, 부모는 자식 개체에서 반환한 크기 정보를 사용하는지 여부를 나타냄. 부모가 이 정보를 사용하지 않는 경우가 종종 있음. 즉, 자식이 크기를 변경하더라도 크기를 다시 계산할 필요가 없음. 새로운 크기가 기존 제한 사항을 준수함을 보장.
	4. 엄격한 제약 조건은 하나의 허용된 크기만 충족할 수 있다는 것. 최대 및 최소 높이가 동일하고 최대 및 최소 너비도 동일한 경우 유일한 적절한 크기는 해당 너비와 높이임. 엄격한 제약 조건을 설정하는 경우 부모는 자식이 자신의 크기를 다시 계산할 때 크기를 또 계산하지 않아야 함. 부모가 부모의 새로운 제약 없이 자식의 크기를 조정할 수 없기 때문에, 부모가 레이아웃에서 자식의 크기를 사용한 경우에도 마찬가지임.
	5. enderObject 는 크기를 계산하기 위해 부모가 제공한 제약 조건만 사용한다고 선언할 수 있음. 이는 제약 조건이 업데이트되는 경우를 제외하고는 이 렌더링 개체의 부모 개체를 다시 계산할 필요가 없음을 의미.
