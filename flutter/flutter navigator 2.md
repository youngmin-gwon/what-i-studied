---
title: flutter navigator 2.0
created at: 2024-12-12
tags:
  - concept
  - flutter
  - navigator
aliases:
---

## Overlay Widget

특별한 형태의 Stack Widget

전체 Navigation System 을 동작하게 하는 위젯

`OverlayEntry` 라는 객체 리스트를 가짐

`OverlayEntry` 의 `builder` 라는 field 에 widget 을 제공하여 `Overlay` Widget 에 자식 Widget 을 제공한다

`Overlay` 위젯에 `OverlayEntry` 자식을 추가하거나 제거하는 경우, widget tree 에서 가장 가까운 `Overlay` 를 찾아야 한다

- 대부분의 경우 가장 가까운 `Overlay` 는 `Navigator` widget 에 의해 생성됨

```dart
void showValueIndicator() {
  if (overlayEntry == null) {
    overlayEntry = OverlayEntry(
      builder: (BuildContext context) {
        return CompositedTransformFollower(
          link: _layerLink,
          child: _ValueIndicatorRenderObjectWidget(
            state: this,
          ),
        );
      }
    );
    Overlay.of(context).insert(overlayEntry);
  }
}
```

## Navigator Widget

대부분 widget tree 최상단에 위치함

stack 자료형 방법을 이용하여 route 들을 관리함

## Route Class

`Navigator` widget 이 관리하는 entry

`2 가지 종류` 의 `Route`. 1. 화면 전체를 변경, 2. 이전 route 위에 덮어버리는 Popup

`Route` 는 widget 이 아님을 유의

`RouteSettings` 라는 객체를 가짐.
nullable 한 `name` 과 `arguments` 로 구성.

각 `Route` class 는 `Navigator` 의 `Overlay` widget 이 관리하는 `OverlayEntry` 목록을 가짐

## Page class

imperative API 에서는 `Route` 객체는 Navigator 의 static 함수를 호출하며 관리함

```dart
onPressed: () {
  Navigator.of(context).push(
    MaterialRoute(builder: (context)=> MyRoute()),
  );
}
  
```

declarative API 에서 `Page` 라는 것을 소개함

> `Page` 는 기본적으로 `Route` 의 구성을 설명하기 때문에 확장 버전의 RouteSettings 같음

모든 `Page` 는 상응하는 `Route` 객체를 갖게 됨

Navigation stack 은 `Page` 객체들의 순서를 이용해서 만듫어짐

`Navigator` 객체는 `Page` 의 `Key` 값을 이용하여 `Page` 의 값이 기존 widget tree 에 있는 것과 같은지 다른지 판별함
`Key` 값이 다르거나, `Page` 가 아직 stack list 에 없다면 `Page` 의 `createRoute` 메소드를 호출

## RouteInormation Class

`Route` 에 대한 정보를 가지고 있는 클래스

2 가지 field: `location`, `state`

- `location`: === URL string
- `state`: 해당 `Route` 에 대한 상태를 보관

## Router Widget

`Navigator` 를 감싸고 navigation 기록을 사용자 상호작용에 따라 변화시킴

`Router` 은 자신의 일을 구성요소들에게 할당함

- `RouterDelegate`
- `RouteInformationParser`
- `RouteInformationProvider`
- `BackButtonDispatcher`

## RouterDelegate

App 의 상태에 따라 `Navigator` widget 을 생성하는 클래스

pop 요청을 처리함

`Router` widget 에서 가장 중요한 요소: 어떻게 `Navigator` 을 생성하는지 알려주기 때문

listenable 하게 만들기 위해 `ChangeNotifier` mixin 을 구현한 것

listener 들에게 알리고 난 후, `build()` method 를 호출함 => `Navigator` 를 반환함

`Router` widget 이 pop 요청을 받는 경우, `RouterDelegate` 의 `popRoute` 를 호출하므로 역할을 대신하게 함

- `RouterDelegate` 을 만들 때, `PopNavigatorRouterDelegateMixin` 을 구현할 수도 있는데, 이렇게 하면 `Router` 의 `popRoute` 가 `Navigator` 의 `maybePop` 를 호출하게 됨
  - `RouteDelegate` 에 `popRoute` 를 구현할 필요 없음. 대신 `onPopPage` callback 제공해야함

Navigation 의 `심장` 같은 역할을 함 => 없으면 존재할 수 없음

## RouteInformationParser

OS 로 부터 들어오는 route 정보를 해석 해서 `RouteDelegate` 가 app 상태를 변경할 수 있게 함

app 상태 변경에 따라 route 정보를 복구 하여 OS 가 navigation 기록에 맞춰 최신 상태로 유지하게 함

Navigation 의 `팔` 같은 역할을 함 => 없어도 살 수 있지만 불편함

`RouteInformationParser` 없이 `Router` 를 생성할 수 있음

## RouteInformationProvider

OS intents 로 부터 route 정보를 생성함

e.g. Web browser address bar 에 URL 입력하면 정보를 해석해서 `Router` widget 이 내부적으로 쓰는 entity 로 전달함

Navigation 의 `입,귀` 같은 역할을 함 => `Router` 의 `귀` 처럼 새로운 정보를 해석하고, `Router` 의 `입` 처럼 변경된 route 정보를 OS 에 전달함

## BackButtonDispatcher

system level 의 `pop` 이벤트를 보고하는 역할
¬
Navigation 의 `귀` 같은 역할 => OS 로부터 시그널을 전달함
