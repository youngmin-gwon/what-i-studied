# 무거운 프레임 (Heavy Frames) 분해 및 스케줄링

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

한 프레임(16ms 또는 8.3ms) 내에 너무 많은 컴포저블을 한 번에 그리려고 하면 16ms 윈도우를 초과하여 프레임이 떨어집니다.

### 9-1. 무거운 프레임을 여러 프레임으로 분해하는 방법

1. **LazyList의 `contentType` 지정**:
   * LazyColumn/LazyRow 사용 시 `contentType`을 지정하면 불필요한 ViewHolder 및 Composition 재생성을 방지하고 리사이클링 효율을 극대화합니다.
2. **Composable 지연 렌더링 (Deferred Rendering)**:
   * 덜 중요한 컴포저블(예: 하단 다이얼로그, 세부 정보 섹션)은 `LaunchedEffect`나 `withContext(Dispatchers.Default)` 이후 상태를 넘겨 다음 프레임으로 렌더링을 분산시킵니다.
3. **`Modifier.drawWithCache` 활용**:
   * Draw 단계에서 매번 Canvas 객체나 Brush, Path를 새로 생성하지 않고 이전 렌더링 오브젝트를 재사용하여 프레임 당 드로잉 타임을 단축합니다.
