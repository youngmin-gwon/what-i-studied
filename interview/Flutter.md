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
	- Flutter의 거의 모든 코드가 Dart로 쓰여질 수 있는 이유
- JIT(Just In Time) 컴파일을 지원
	- hot reload가 가능한 이유
---
## mixins?
- Mixin은 특별한 유형의 상속에 사용되며 실제로 부모 Mixin 클래스의 자식이 아니더라도 다른 클래스가 사용할 메서드를 상속할 수 있음 
- 간단히 말해서, Mixin은 클래스를 확장하지 않고 메서드를 빌릴 수 있는 일반적인 일반 클래스
---
## Hot Reload?
- 빠르게 UI를 그리고, 기능 추가하고, 버그를 고칠 수 있게 도와주는 기능
- 새로 업데이트 된 소스 코드 파일을 실행 중인 Dart VM에 주입하는 원리로 동작
	- VM이 새 버전의 필드 및 함수로 클래스를 업데이트한 후 Flutter는 자동으로 위젯 트리를 재구축하여 변경 사항을 빠르게 확인할 수 있음