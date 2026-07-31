# 개발 프레임워크: Compose for XR

공간상의 3D 컴포넌트와 2D 레이아웃을 선언형으로 작성할 수 있다.

```kotlin
// Compose for XR 예시
@Composable
fun SpatialCard() {
    SpatialPanel(
        modifier = Modifier.size(400.dp, 300.dp),
        zDistance = 1.5.m // 공간상의 거리 설정
    ) {
        Content()
    }
}
```
