# 비동기 이미지 로딩 (Asynchronous Image Loading)

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

화면에 네트워크 URL이나 고해상도 이미지가 포함되어 있을 때 메인 쓰레드에서 비트맵을 직접 디코딩하면 **화면이 수십 ms 동안 멈추는 프레임 멈춤(Jank)**이 발생합니다.

### 8-1. `AsyncImage` vs `rememberAsyncImagePainter` vs `painterResource`
* **`painterResource(R.drawable.xxx)`**: **앱 내 정적 로컬 리소스(vector, small png)**를 불러올 때 사용합니다. 네트워크 URL이나 무거운 외부 비트맵 디코딩에는 사용할 수 없습니다.
* **`AsyncImage` (Coil 고도화 API - 권장 🐳)**:
  * 내부적으로 `SubcomposeAsyncImage`나 `Image` 컴포저블을 래핑하여 백그라운드 I/O 디코딩, 캐싱, Placeholder 렌더링을 최적화합니다.
  * 별도의 `remember` 선언 없이 컴포저블 파이프라인 안에서 가장 깔끔하고 성능 효율적으로 비동기 이미지를 로딩합니다.
* **`rememberAsyncImagePainter` (Low-level Painter API)**:
  * `Image(painter = rememberAsyncImagePainter(...))` 형태로 custom `Painter` 호환성이 꼭 필요한 특수한 경우(예: 확장 Modifier와의 직접 결합)에만 제한적으로 사용합니다.

### 8-2. `placeholder` 및 `error` 처리 시 `rememberAsyncImagePainter` 활용
* **로컬 드로어블 Placeholder**: `placeholder = painterResource(R.drawable.placeholder)` 처럼 앱 패키지 내 정적 리소스를 쓸 때는 `painterResource`를 바로 전달합니다.
* **비동기/네트워크 Placeholder 및 Error Image**:
  * 만약 Placeholder나 Error 이미지 자체도 로컬 정적 리소스가 아닌 **비동기로 로드해야 하는 URL이나 외부 이미지인 경우**, `placeholder = rememberAsyncImagePainter(model = placeholderUrl)` 형태로 `rememberAsyncImagePainter`를 지정해야 합니다.

```kotlin
// 🐳 1) 일반적인 로컬 드로어블을 Placeholder로 사용하는 경우
AsyncImage(
    model = imageUrl,
    contentDescription = "프로필 이미지",
    modifier = Modifier
        .size(60.dp)
        .clip(CircleShape),
    placeholder = painterResource(R.drawable.placeholder_avatar)
)

// 🐳 2) Placeholder 자체도 비동기/네트워크 이미지를 사용하는 경우 (rememberAsyncImagePainter 사용)
AsyncImage(
    model = imageUrl,
    contentDescription = "프로필 이미지",
    modifier = Modifier
        .size(60.dp)
        .clip(CircleShape),
    placeholder = rememberAsyncImagePainter(model = placeholderUrl),
    error = rememberAsyncImagePainter(model = fallbackUrl)
)
```

---
