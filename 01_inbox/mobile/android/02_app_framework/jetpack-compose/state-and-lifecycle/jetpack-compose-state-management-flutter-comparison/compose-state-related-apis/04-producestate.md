# `produceState`

외부 async source를 Compose `State<T>`로 변환합니다.

```kotlin
val image by produceState<Image?>(initialValue = null, url) {
    value = imageRepository.load(url)
}
```

앱 아키텍처에서는 ViewModel/Repository로 빼는 편이 더 명확한 경우가 많습니다.
