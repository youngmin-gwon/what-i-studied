---
title: android-large-screens
tags: []
aliases: []
date modified: 2026-04-05 17:43:10 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-large-screens]]

### Large Screens: Adaptive Layouts

태블릿, 폴더블, 가로 모드 및 데스크톱 환경(Samsung DeX, ChromeOS)에 대응하는 **Adaptive Layout** 설계 기법을 분석합니다.

단순히 화면을 크게 보여주는 것을 넘어, **WindowSizeClass**를 기반으로 최적화된 사용자 경험(UX)을 제공하고, Android 15 에서 강화된 **데스크톱 윈도우(Desktop Windowing)** 환경에서의 앱 안정성을 확보하는 것이 목표입니다.

---

#### 💡 Context: 대화면 지원의 필연성

안드로이드 생태계는 더 이상 스마트폰에 국한되지 않습니다. 폴더블 기기의 대중화와 태블릿 시장의 성장으로 인해, 다양한 화면 비율과 상태(Fold/Unfold)에 유연하게 대응하는 앱 설계는 현대적인 안드로이드 개발의 핵심 요구사항입니다. [[android-compose-internals]] 와 밀접하게 연관됩니다.

---

#### 화면 크기 분류

| 크기 | 너비 (dp) | 예시 |
|------|-----------|------|
| Compact | < 600 | 스마트폰 (세로) |
| Medium | 600 - 839 | 스마트폰 (가로), 작은 태블릿 |
| Expanded | ≥ 840 | 태블릿, 폴더블 (펼침) |

#### WindowSizeClass

화면 크기에 따라 레이아웃 조정.

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.compose.material3:material3-window-size-class:1.1.2")
}

@Composable
fun AdaptiveLayout() {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> {
            // 스마트폰: 단일 패널
            SinglePaneLayout()
        }
        WindowWidthSizeClass.Medium -> {
            // 작은 태블릿: 리스트-디테일
            ListDetailLayout()
        }
        WindowWidthSizeClass.Expanded -> {
            // 큰 태블릿: 3패널
            ThreePaneLayout()
        }
    }
}
```

#### Adaptive Layout

##### Navigation Rail (중형 화면)

```kotlin
@Composable
fun MediumScreenLayout() {
    Row {
        NavigationRail {
            items.forEach { item ->
                NavigationRailItem(
                    icon = { Icon(item.icon, null) },
                    label = { Text(item.label) },
                    selected = item == selectedItem,
                    onClick = { selectedItem = item }
                )
            }
        }
        
        // 메인 컨텐츠
        MainContent(modifier = Modifier.weight(1f))
    }
}
```

##### List-Detail (대형 화면)

```kotlin
@Composable
fun ListDetailLayout() {
    Row {
        // 리스트 (1/3)
        ItemList(
            modifier = Modifier.weight(1f),
            onItemClick = { selectedItem = it }
        )
        
        // 디테일 (2/3)
        ItemDetail(
            item = selectedItem,
            modifier = Modifier.weight(2f)
        )
    }
}
```

#### 폴더블 지원

##### Jetpack WindowManager

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.window:window:1.2.0")
}

@Composable
fun FoldableAwareLayout() {
    val windowInfoTracker = WindowInfoTracker.getOrCreate(LocalContext.current)
    val displayFeatures by windowInfoTracker.windowLayoutInfo(LocalContext.current as Activity)
        .collectAsStateWithLifecycle(initialValue = WindowLayoutInfo(emptyList()))
    
    val foldingFeature = displayFeatures.displayFeatures
        .filterIsInstance<FoldingFeature>()
        .firstOrNull()
    
    when {
        foldingFeature != null && foldingFeature.state == FoldingFeature.State.HALF_OPENED -> {
            // 반 접힌 상태 (Book mode)
            TwoPageLayout(foldingFeature)
        }
        foldingFeature != null && foldingFeature.isSeparating -> {
            // 힌지가 컨텐츠를 분리
            SplitLayout(foldingFeature)
        }
        else -> {
            // 일반 레이아웃
            StandardLayout()
        }
    }
}

@Composable
fun TwoPageLayout(foldingFeature: FoldingFeature) {
    BoxWithConstraints {
        val foldPosition = with(LocalDensity.current) {
            foldingFeature.bounds.left.toDp()
        }
        
        Row {
            // 왼쪽 화면
            LeftPane(modifier = Modifier.width(foldPosition))
            
            // 오른쪽 화면
            RightPane(modifier = Modifier.fillMaxWidth())
        }
    }
}
```

##### 폴더블 상태 감지

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        lifecycleScope.launch {
            lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
                WindowInfoTracker.getOrCreate(this@MainActivity)
                    .windowLayoutInfo(this@MainActivity)
                    .collect { windowLayoutInfo ->
                        val foldingFeature = windowLayoutInfo.displayFeatures
                            .filterIsInstance<FoldingFeature>()
                            .firstOrNull()
                        
                        when (foldingFeature?.state) {
                            FoldingFeature.State.FLAT -> {
                                // 완전히 펼쳐짐
                                Log.d("Foldable", "Flat")
                            }
                            FoldingFeature.State.HALF_OPENED -> {
                                // 반 접힘 (텐트 모드, 북 모드)
                                Log.d("Foldable", "Half-opened")
                            }
                            else -> {
                                // 접힘 또는 폴더블 아님
                                Log.d("Foldable", "Folded or not foldable")
                            }
                        }
                    }
            }
        }
    }
}
```

#### 멀티 윈도우

##### 멀티 윈도우 활성화

```xml
<!-- AndroidManifest.xml -->
<activity
    android:name=".MainActivity"
    android:resizeableActivity="true"
    android:supportsPictureInPicture="true">
    
    <!-- 최소 크기 지정 -->
    <layout
        android:defaultWidth="600dp"
        android:defaultHeight="400dp"
        android:minWidth="300dp"
        android:minHeight="200dp" />
</activity>
```

##### 멀티 윈도우 상태 감지

```kotlin
override fun onMultiWindowModeChanged(isInMultiWindowMode: Boolean, newConfig: Configuration) {
    super.onMultiWindowModeChanged(isInMultiWindowMode, newConfig)
    
    if (isInMultiWindowMode) {
        // 멀티 윈도우 모드 진입
        // 레이아웃 조정
        showCompactLayout()
    } else {
        // 전체 화면 모드
        showExpandedLayout()
    }
}
```

#### Picture-in-Picture (PiP)

```kotlin
// build.gradle.kts
android {
    defaultConfig {
        minSdk = 26 // PiP 는 Android 8.0+
    }
}

class VideoPlayerActivity : AppCompatActivity() {
    
    override fun onUserLeaveHint() {
        super.onUserLeaveHint()
        
        if (isVideoPlaying) {
            enterPictureInPictureMode(createPipParams())
        }
    }
    
    private fun createPipParams(): PictureInPictureParams {
        val aspectRatio = Rational(16, 9)
        
        return PictureInPictureParams.Builder()
            .setAspectRatio(aspectRatio)
            .setActions(createPipActions())
            .build()
    }
    
    private fun createPipActions(): List<RemoteAction> {
        val playPauseIntent = PendingIntent.getBroadcast(
            this,
            0,
            Intent(ACTION_PLAY_PAUSE),
            PendingIntent.FLAG_IMMUTABLE
        )
        
        val playPauseAction = RemoteAction(
            Icon.createWithResource(this, R.drawable.ic_play_pause),
            "Play/Pause",
            "Play or pause video",
            playPauseIntent
        )
        
        return listOf(playPauseAction)
    }
    
    override fun onPictureInPictureModeChanged(
        isInPictureInPictureMode: Boolean,
        newConfig: Configuration
    ) {
        super.onPictureInPictureModeChanged(isInPictureInPictureMode, newConfig)
        
        if (isInPictureInPictureMode) {
            // PiP 모드: 컨트롤 숨기기
            hideControls()
        } else {
            // 전체 화면: 컨트롤 표시
            showControls()
        }
    }
}
```

#### 드래그 앤 드롭

대형 화면에서 앱 간 드래그 앤 드롭 지원.

```kotlin
// 드롭 수신
class DropTargetView : View {
    init {
        setOnDragListener { view, event ->
            when (event.action) {
                DragEvent.ACTION_DRAG_STARTED -> {
                    // 드래그 시작
                    event.clipDescription.hasMimeType(ClipDescription.MIMETYPE_TEXT_PLAIN)
                }
                DragEvent.ACTION_DRAG_ENTERED -> {
                    // 뷰 위로 진입
                    view.alpha = 0.5f
                    true
                }
                DragEvent.ACTION_DRAG_EXITED -> {
                    // 뷰 밖으로 나감
                    view.alpha = 1.0f
                    true
                }
                DragEvent.ACTION_DROP -> {
                    // 드롭됨
                    val item = event.clipData.getItemAt(0)
                    val text = item.text
                    handleDrop(text.toString())
                    true
                }
                DragEvent.ACTION_DRAG_ENDED -> {
                    view.alpha = 1.0f
                    true
                }
                else -> false
            }
        }
    }
}

// 드래그 시작
fun startDrag(view: View, text: String) {
    val clipData = ClipData.newPlainText("label", text)
    val shadowBuilder = View.DragShadowBuilder(view)
    
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        view.startDragAndDrop(clipData, shadowBuilder, null, View.DRAG_FLAG_GLOBAL)
    } else {
        view.startDrag(clipData, shadowBuilder, null, 0)
    }
}
```

#### 키보드/마우스 지원

##### 단축키

```kotlin
override fun onKeyDown(keyCode: Int, event: KeyEvent): Boolean {
    return when {
        event.isCtrlPressed && keyCode == KeyEvent.KEYCODE_S -> {
            // Ctrl+S: 저장
            save()
            true
        }
        event.isCtrlPressed && keyCode == KeyEvent.KEYCODE_Z -> {
            // Ctrl+Z: 실행 취소
            undo()
            true
        }
        else -> super.onKeyDown(keyCode, event)
    }
}
```

##### 마우스 호버

```kotlin
view.setOnHoverListener { v, event ->
    when (event.action) {
        MotionEvent.ACTION_HOVER_ENTER -> {
            // 마우스 진입
            v.elevation = 8.dp.toPx()
            true
        }
        MotionEvent.ACTION_HOVER_EXIT -> {
            // 마우스 나감
            v.elevation = 0f
            true
        }
        else -> false
    }
}
```

##### 컨텍스트 메뉴

```kotlin
view.setOnContextClickListener {
    val popup = PopupMenu(context, it)
    popup.menuInflater.inflate(R.menu.context_menu, popup.menu)
    popup.setOnMenuItemClickListener { menuItem ->
        when (menuItem.itemId) {
            R.id.action_copy -> {
                copy()
                true
            }
            R.id.action_paste -> {
                paste()
                true
            }
            else -> false
        }
    }
    popup.show()
    true
}
```

#### 데스크톱 모드 및 윈도우 (Desktop Windowing)

##### 1. Android 15 Desktop Windowing (New ✅)

Android 15 부터 태블릿에서 여러 앱을 자유로운 크기의 창(Freeform Windows)으로 실행할 수 있는 **데스크톱 윈도우** 기능이 공식 지원됩니다.

- **고정된 가로세로비 설정**: 앱이 자유로운 창 크기 조정을 지원하지 않더라도, `android:screenOrientation` 이나 `android:minAspectRatio` 를 통해 안정적인 비율을 유지할 수 있습니다.
- **Taskbar 활용**: 대화면 하단의 태스크바를 통해 앱 간 드래그 앤 드롭 및 퀵 런칭이 더욱 고도화되었습니다.

##### 2. Samsung DeX & Chrome OS

```kotlin
// 데스크톱 모드 감지
fun isDesktopMode(context: Context): Boolean {
    val uiModeManager = context.getSystemService(Context.UI_MODE_SERVICE) as UiModeManager
    return uiModeManager.currentModeType == Configuration.UI_MODE_TYPE_DESK
}

// 설정 변경 감지
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    
    if (newConfig.uiMode and Configuration.UI_MODE_TYPE_MASK == Configuration.UI_MODE_TYPE_DESK) {
        // 데스크톱 모드로 전환
        enableDesktopLayout()
    } else {
        // 모바일 모드로 전환
        enableMobileLayout()
    }
}
```

#### 반응형 레이아웃 패턴

##### Canonical Layout

```kotlin
@Composable
fun CanonicalLayout(
    listContent: @Composable () -> Unit,
    detailContent: @Composable () -> Unit
) {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> {
            // 스마트폰: 네비게이션으로 전환
            NavHost(navController, startDestination = "list") {
                composable("list") { listContent() }
                composable("detail") { detailContent() }
            }
        }
        else -> {
            // 태블릿: 나란히 표시
            Row {
                Box(modifier = Modifier.weight(1f)) { listContent() }
                Box(modifier = Modifier.weight(2f)) { detailContent() }
            }
        }
    }
}
```

##### Supporting Pane

```kotlin
@Composable
fun SupportingPaneLayout(
    mainContent: @Composable () -> Unit,
    supportingContent: @Composable () -> Unit
) {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> {
            // 스마트폰: 메인만 표시
            mainContent()
        }
        WindowWidthSizeClass.Medium -> {
            // 중형: 메인 + 작은 서포팅
            Row {
                Box(modifier = Modifier.weight(2f)) { mainContent() }
                Box(modifier = Modifier.weight(1f)) { supportingContent() }
            }
        }
        WindowWidthSizeClass.Expanded -> {
            // 대형: 메인 + 큰 서포팅
            Row {
                Box(modifier = Modifier.weight(1f)) { mainContent() }
                Box(modifier = Modifier.weight(1f)) { supportingContent() }
            }
        }
    }
}
```

#### 테스트

```kotlin
@Test
fun testAdaptiveLayout_compact() {
    composeTestRule.setContent {
        CompositionLocalProvider(
            LocalConfiguration provides Configuration().apply {
                screenWidthDp = 400
            }
        ) {
            AdaptiveLayout()
        }
    }
    
    // Compact 레이아웃 확인
    composeTestRule.onNodeWithTag("single_pane").assertExists()
}

@Test
fun testAdaptiveLayout_expanded() {
    composeTestRule.setContent {
        CompositionLocalProvider(
            LocalConfiguration provides Configuration().apply {
                screenWidthDp = 1000
            }
        ) {
            AdaptiveLayout()
        }
    }
    
    // Expanded 레이아웃 확인
    composeTestRule.onNodeWithTag("list_pane").assertExists()
    composeTestRule.onNodeWithTag("detail_pane").assertExists()
}
```

#### 베스트 프랙티스

##### 1. 유연한 레이아웃

```kotlin
// ❌ 고정 크기
Box(modifier = Modifier.size(300.dp, 200.dp))

// ✅ 비율 기반
Box(modifier = Modifier
    .fillMaxWidth()
    .aspectRatio(16f / 9f)
)
```

##### 2. 적응형 네비게이션

```kotlin
@Composable
fun AdaptiveNavigation() {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> BottomNavigation()
        WindowWidthSizeClass.Medium -> NavigationRail()
        WindowWidthSizeClass.Expanded -> PermanentNavigationDrawer()
    }
}
```

##### 3. 터치 타겟 크기

```kotlin
// 최소 48dp 터치 타겟
Button(
    onClick = { },
    modifier = Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)
) {
    Text("Click")
}
```

##### 4. 폰트 스케일링

```kotlin
// 사용자 폰트 크기 설정 존중
Text(
    text = "Hello",
    fontSize = 16.sp // dp 아닌 sp 사용
)
```

#### See Also

- [[android-compose-internals]]
- [[android-jetpack-architecture]]
- [[android-app-components-deep-dive]]
- [[android-testing-and-quality]]
