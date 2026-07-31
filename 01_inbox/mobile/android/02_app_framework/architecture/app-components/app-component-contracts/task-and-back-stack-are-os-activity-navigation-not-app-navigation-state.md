# Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다

Android task와 back stack은 사용자가 Activity들을 어떤 작업 흐름으로 지나왔는지를 OS가 관리하는 기록이다. Compose Navigation이나 Navigation 3의 route/back stack은 앱 내부 화면 상태이고, Android task stack과 같은 층위가 아니다.

`launchMode`, intent flags, document mode, deep link entry point는 Activity 인스턴스가 어느 task에 들어갈지 바꾼다. 하지만 앱 내부 화면 전환을 모두 launch mode로 해결하려 하면 testability와 상태 복구가 나빠진다.

일반 앱 화면 전환은 app-owned navigation state로 다루고, 외부 진입점, task affinity, notification/deep link 복귀 정책처럼 OS와 맞닿는 부분만 Activity task 정책으로 결정한다.

관련 정본: [Android task와 app back stack](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md), [navigation 정본](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [intent/manifest 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md).

공식 문서: [Tasks and back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)
