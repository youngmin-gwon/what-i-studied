# 1 Install-time Delivery (설치 시 배포)

| 항목           | 설명                         |
|--------------|----------------------------|
| **동작**       | 앱 설치 시 자동으로 함께 다운로드        |
| **사용 가능 시점** | 앱을 처음 열 때 즉시 사용 가능         |
| **제거 가능 여부** | `removable` 옵션으로 나중에 제거 가능 |

```groovy
// build.gradle (feature module)
android {
    dynamicFeatures = [':feature_camera']
}

// feature module의 build.gradle
plugins {
    id 'com.android.dynamic-feature'
}

android {
    // install-time이 기본값
}
```

**AndroidManifest.xml 설정:**

```xml

<manifest xmlns:dist="http://schemas.android.com/apk/distribution"
    package="com.example.feature.camera">
    <dist:module dist:instant="false" dist:title="@string/title_camera">
        <dist:delivery>
            <dist:install-time />
        </dist:delivery>
    </dist:module>
</manifest>
```

> [!TIP]
> `removable="true"` 를 설정하면 나중에 기기 용량이 부족할 때 Play Store가 자동으로 해당 모듈을 제거할 수 있습니다. 사용 빈도가 낮은 기능에
> 유용합니다.

**적합한 상황:**

- 앱 실행 시 반드시 필요한 핵심 기능
- 단, 일부 기기에서만 필요하거나, 나중에 제거해도 되는 기능 → `removable` 옵션 활용

---
