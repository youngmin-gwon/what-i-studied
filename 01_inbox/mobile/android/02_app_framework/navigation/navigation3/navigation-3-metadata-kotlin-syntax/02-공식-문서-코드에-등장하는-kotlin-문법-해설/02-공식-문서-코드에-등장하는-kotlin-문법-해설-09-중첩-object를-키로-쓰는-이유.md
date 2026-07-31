# 중첩 `object`를 키로 쓰는 이유
```kotlin
class MySceneStrategy<T : Any> : SceneStrategy<T> {
    object MyStringMetadataKey : NavMetadataKey<String>
}
```
* **"이 키를 읽는 주체(MySceneStrategy)와 키 자체를 같은 클래스 안에 묶어놓자"**는 코드 조직화 관례(Convention)입니다.
* 이렇게 하면 `MySceneStrategy.MyStringMetadataKey`로 접근하므로, 어떤 컴포넌트가 이 메타데이터를 사용하는지 이름만으로도 직관적으로 파악할 수 있습니다.
* `NavDisplay` 역시 함수이지만 같은 이름의 `object NavDisplay`를 만들어 그 안에 `TransitionKey`를 넣어둔 것이 같은 관례를 따른 것입니다.

---
