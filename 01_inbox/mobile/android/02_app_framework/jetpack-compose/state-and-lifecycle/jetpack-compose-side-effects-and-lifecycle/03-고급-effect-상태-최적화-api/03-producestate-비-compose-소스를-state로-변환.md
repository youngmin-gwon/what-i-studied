# `produceState` (비-Compose 소스를 State로 변환)
* **목적**: RxJava, Flow, Callbacks, 외부 Promise 등 Compose가 아닌 비동기 데이터 소스를 Compose가 읽을 수 있는 `State<T>` 형태로 변환합니다.
* **동작**: `LaunchedEffect`와 상태 저장이 합쳐진 형태의 간편 API입니다.

```kotlin
@Composable
fun loadNetworkImage(url: String, imageRepository: ImageRepository): State<ImageState> {
    // url이 바뀔 때마다 실행되며 결과를 Compose State로 노출
    return produceState<ImageState>(initialValue = ImageState.Loading, url) {
        value = try {
            val image = imageRepository.downloadImage(url)
            ImageState.Success(image)
        } catch (e: Exception) {
            ImageState.Error(e)
        }
    }
}
```

---
