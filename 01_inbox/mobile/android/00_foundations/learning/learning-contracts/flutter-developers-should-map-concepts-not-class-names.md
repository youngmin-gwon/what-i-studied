# Flutter 개발자는 class 이름보다 개념 경계를 대응시켜야 한다

Flutter 경험이 있는 개발자는 Widget과 Composable, BuildContext와 Android Context, Provider/Riverpod과 Compose state observation을 이름으로 바로 대응시키기 쉽다. 하지만 실제 boundary는 다르다.

Compose의 Composable은 state를 UI로 계산하는 함수에 가깝고, Android Context는 UI tree 위치가 아니라 platform capability다. ViewModel은 StatefulWidget의 State가 아니라 screen state holder와 external work coordinator에 가깝다.

이 매핑은 Compose/state 문서와 Context 문서로 연결하고, learning resource 문서 안에서 반복 설명하지 않는다.

관련 정본: [Compose runtime/state](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md), [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md/state-management/viewmodel/viewmodel.md).
