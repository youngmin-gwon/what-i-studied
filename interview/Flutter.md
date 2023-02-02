# Flutter interview question

## Flutter?
- 단일 코드베이스에서 모바일, 웹 및 데스크톱용으로 고유하게 컴파일된 아름다운 애플리케이션을 만들기 위한 UI toolkit
- Dart 언어로 만들어짐
---
## Widget Types
1. StatelessWidget
2. StatefulWidget
---
## pubspec.yaml?
- flutter/dart 프로젝트에 필요한 모든 의존성(패키지, 파일 등)을 선언한 곳
- 어플리케이션에 대한 제약조건 설정할 수 있음
- 안드로이드의 build.gradle과 비슷하다고 할 수 있음
---
## Dart? Why Dart for Flutter
- AOT(Ahead of Time) 컴파일을 지원
	- 빠르고, 예상가능한 네이티브 코드로 컴파일 됨
- JIT(Just In Time) 컴파일을 지원
	- hot reload가 가능한 이유
 - Dart는 Flutter가 JSX 또는 XML과 같은 별도의 선언적 레이아웃 언어 또는 별도의 시각적 인터페이스 빌더의 필요성을 피할 수 있게 해줌 
	 - Dart의 선언적, 프로그래밍 레이아웃은 읽고 시각화하기 쉽기 때문.
	 - 모든 레이아웃을 하나의 언어와 한 곳에서, Flutter는 레이아웃을 쉽게 만드는 고급 툴링을 쉽게 제공할 수 있음
---
## mixins?
- Mixin은 특별한 유형의 상속에 사용되며 실제로 부모 Mixin 클래스의 자식이 아니더라도 다른 클래스가 사용할 메서드를 상속할 수 있음 
- 간단히 말해서, Mixin은 클래스를 확장하지 않고 메서드를 빌릴 수 있는 일반적인 일반 클래스
---
## Hot Reload?
- 빠르게 UI를 그리고, 기능 추가하고, 버그를 고칠 수 있게 도와주는 기능
- 새로 업데이트 된 소스 코드 파일을 실행 중인 Dart VM에 주입하는 원리로 동작
	- VM이 새 버전의 필드 및 함수로 클래스를 업데이트한 후 Flutter는 자동으로 위젯 트리를 재구축하여 변경 사항을 빠르게 확인할 수 있음
 ---
## Key란 무엇인가?

- Key에 대한 설명 참고: [[Flutter-Key]]

---
## Flutter는 어떻게 동작하는가?
- Flutter 내부 설명 참고: [[Flutter-Under the hood]]
---
## StatelessWidget vs. StatefulWidget
- Widget
	- element를 위한 설정사항을 정의한 불변 객체
- State
	- UI 를 다시 그리도록 유도할 수 있고, 시간이 지남에 따라 값을 추적하며 바꿀 수 있는 객체
	- Widget의 reference를 가지고 있기 때문에 widget과 state의 값을 모두 접근할 수 있음
	- setState(): state 객체의 property들을 수정하고, UI 업데이트를 유도함
		- state 에 연결된 element를 dirty로 표시함 => 다음 프레임에 자식들을 다시 빌드함
	- state의 유용한 점
		- widget 보다 생명주기가 길어 같은 타입인 경우 기존 widget이 새로운 widget으로 대체되어도 element tree에 계속 존재함
  - StatelessWidget
  - StatefulWidget
---
## InheritedWidget
- Widget tree 안에서 data를 전달하기 위해 사용하는 widget
	- 하위 widget에서 해당 데이터를 사용할 수 있게 됨
- Immutable 하기 때문에 전체 life cycle 동안 데이터가 바뀌지 않음
	- 즉, 데이터를 직접 넣는 것보다, service를 주입하면 됨