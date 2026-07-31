# 접근성 Service와 Manifest 등록

Jetpack Compose 시대에도 `AndroidManifest.xml`에 `<service>` 태그를 등록해야 하는 특수한 경우가 있습니다.

### 7-1. 일반 앱의 접근성 지원 vs. 접근성 서비스 (AccessibilityService)

| 구분 | 일반 앱의 접근성 지원 | 접근성 서비스 (코드랩 내용) |
|:---|:---|:---|
| **목적** | 시각 장애인 등이 **내 앱**을 편하게 쓰도록 돕기 | 스마트폰 **화면 전체**를 감시하고 타사 앱들을 제어 |
| **Compose 전환** | ⭕ `Modifier.semantics` 등으로 완벽 대체 | ❌ 여전히 `Service` + 매니페스트 필수 |

### 7-2. Compose에서의 접근성 지원 방법

```kotlin
@Composable
fun ShoppingCartButton(onClick: () -> Unit) {
    IconButton(
        onClick = onClick,
        modifier = Modifier.semantics {
            contentDescription = "장바구니에 담기 버튼"
        }
    ) {
        Icon(Icons.Default.ShoppingCart, contentDescription = null)
    }
}
```

### 7-3. 현재도 AccessibilityService가 필요한 특수한 앱들

* **물리 버튼 리매퍼**: 볼륨 버튼 길게 누르면 손전등 켜기
* **자동 클릭커 / 매크로 앱**: 화면의 특정 좌표를 자동으로 클릭
* **보이스피싱 방지 기능**: 원격 제어 앱 실행 감시

이런 앱들은 Compose의 권한 밖(OS 레벨)이므로, 매니페스트에 Service 등록이 반드시 필요합니다.

```xml
<service
    android:name=".GlobalActionBarService"
    android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"
    android:exported="true">
    <intent-filter>
        <action android:name="android.accessibilityservice.AccessibilityService" />
    </intent-filter>
    <meta-data
        android:name="android.accessibilityservice"
        android:resource="@xml/global_action_bar_service" />
</service>
```

> [!NOTE]
> 인텐트와 인텐트 필터의 기초 개념은 [intent-and-deep-link](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-and-deep-link.md)를 참조하세요.
> Navigation 라이브러리의 딥 링크 처리 방식은 [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)를 참조하세요.
