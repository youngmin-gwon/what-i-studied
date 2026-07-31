# Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다

Navigation 3에서는 앱이 back stack을 소유한다. 따라서 configuration change와 process death 뒤에도 사용자가 있던 navigation 위치를 복원하려면 saveable back stack 전략이 필요하다.

`rememberNavBackStack`은 `NavKey` 기반 back stack을 기억하고 저장/복원하는 편의 API다. 이 API를 쓰려면 key가 `NavKey`를 구현하고 serialization 요구사항을 만족해야 한다.

Back stack state와 screen UI state는 다르다. 어떤 화면이 stack에 있는지와 그 화면 안의 form/input/loading state를 같은 객체에 섞으면 복원과 deep link 처리가 불안정해진다.

공식 문서: [Save and manage navigation state](https://developer.android.com/guide/navigation/navigation-3/save-state), [rememberNavBackStack](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/rememberNavBackStack.composable)
