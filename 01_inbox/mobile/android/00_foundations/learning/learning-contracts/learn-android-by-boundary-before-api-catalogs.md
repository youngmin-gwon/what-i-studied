# Android는 API catalog보다 boundary 단위로 먼저 배운다

Android를 처음 배울 때 모든 API를 나열하면 오래 가지 않는다. 먼저 app lifecycle, process, state owner, permission, storage, background work, rendering, packaging 같은 boundary를 잡아야 한다.

그 뒤에 Compose, ViewModel, Flow, Room, WorkManager, Navigation, Hilt 같은 도구를 각 boundary에 배치한다. 이 순서가 잡히면 새 API가 나와도 어디에 넣어야 하는지 판단하기 쉽다.

관련 정본: [Android Foundations](01_inbox/mobile/android/00_foundations/android-foundation-map.md), [app architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md), [Compose runtime](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md).
