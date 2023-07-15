# Navigator 2

## Overlay Widget

특별한 형태의 Stack Widget

전체 Navigation System 을 동작하게 하는 위젯

`OverlayEntry` 라는 객체 리스트를 가짐

`OverlayEntry` 의 `builder` 라는 field에 widget을 제공하여 `Overlay` Widget에 자식 Widget을 제공한다

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

stack 자료형 방법을 이용하여 route들을 관리함

## Route Class

`Navigator` widget 이 관리하는 entry

`2 가지 종류`의 `Route`. 1. 화면 전체를 변경, 2. 이전 route 위에 덮어버리는 Popup 

`Route`는 widget이 아님을 유의

`RouteSettings` 라는 객체를 가짐.
nullable한 `name` 과 `arguments`로 구성.

각 `Route` class 는 `Navigator`의 `Overlay` widget이 관리하는 `OverlayEntry` 목록을 가짐

## Page class

imperative API 에서는 `Route` 객체는 Navigator의 static 함수를 호출하며 관리함

```dart
onPressed: () {
  Navigator.of(context).push(
    MaterialRoute(builder: (context)=> MyRoute()),
  );
}
  
```

declarative API 에서 `Page` 라는 것을 소개함

> `Page`는 기본적으로 `Route`의 구성을 설명하기 때문에 확장 버전의 RouteSettings 같음

모든 `Page` 는 상응하는 `Route` 객체를 갖게 됨

Navigation stack은 `Page` 객체들의 순서를 이용해서 만듫어짐

`Navigator` 객체는 `Page`의 `Key` 값을 이용하여 `Page`의 값이 기존 widget tree에 있는 것과 같은지 다른지 판별함 
`Key` 값이 다르거나, `Page` 가 아직 stack list 에 없다면 `Page`의 `createRoute` 메소드를 호출

## RouteInormation Class

`Route` 에 대한 정보를 가지고 있는 클래스

2가지 field: `location`, `state`
- `location`: === URL string
- `state`: 해당 `Route` 에 대한 상태를 보관

## Router Widget

`Navigator`를 감싸고 navigation 기록을 사용자 상호작용에 따라 변화시킴

`Router` 은 자신의 일을 구성요소들에게 할당함
- `RouterDelegate`
- `RouteInformationParser`
- `RouteInformationProvider`
- `BackButtonDispatcher`

## RouterDelegate

App의 상태에 따라 `Navigatior` widget 을 생성하는 클래스

pop 요청을 처리함

Navigation의 심장 같은 역할을 함

## RouteInformationParser

## RouteInformationProvider

## BackButtonDispatcher