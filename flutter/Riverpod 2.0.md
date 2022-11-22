- WidgetRef
	- BuildContext 와 비슷하게 동작함
	- BuildContext를 이용하여 상위 Widget Tree 에 포함된 요소에 접근가능
	- WidgetRef는 코드베이스의 모든 Provider에 접근할 수 있게 됨.  Provider가 global로 선언되었기 때문
- Provider 종류
1.  `Provider`
2.  `StateProvider` (legacy)
3.  `StateNotifierProvider` (legacy)
4.  `FutureProvider`
5.  `StreamProvider`
6.  `ChangeNotifierProvider` (legacy)
7.  `NotifierProvider` **(new in Riverpod 2.0)**
8.  `AsyncNotifierProvider` **(new in Riverpod 2.0)**

### 1.  `Provider`
- 
### 2.  `StateProvider`
- enum, String, bool 및 int와 같은 간단한 상태 변수를 저장하는 데 이상적 
- Notifier은 같은 목적으로 사용될 수 있으며 더 유연함
- 더 복잡하거나 비동기적인 상태의 경우, AsyncNotifierProvider, FutureProvider 또는 StreamProvider를 사용 권장

### 3.  `StateNotifierProvider`
- StateNotifierProvider와 StateNotifier는 이벤트나 사용자 상호 작용에 대한 반응이 바뀔 수 있는 상태를 관리하는 데 이상적