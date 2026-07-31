# Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다

Navigation 3의 key는 특정 Composable class가 아니라 destination을 식별하는 navigation state다. key는 equality가 안정적이어야 하고, 필요한 argument만 포함해야 하며, 저장/복원과 deep link 변환을 견딜 수 있어야 한다.

화면 구현 객체, Repository, ViewModel, callback 같은 runtime object를 key에 넣으면 저장과 비교가 깨진다. route key는 domain identifier와 primitive/serializable argument 중심으로 설계한다.

공식 문서: [Navigation 3 basics](https://developer.android.com/guide/navigation/navigation-3/basics)
