---
title: 02-런타임-권한-android-6-0
tags: []
aliases: []
date modified: 2026-07-31 17:11:53 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 런타임 권한 (Android 6.0+)

**위험 권한(Dangerous Permissions)** 은 앱 실행 중에 요청해야 하며, 사용자는 이를 거부할 권리가 있습니다.

```kotlin
// 현대적인 권한 요청 패턴 (ActivityResultLauncher)
private val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { isGranted: Boolean ->
    if (isGranted) {
        // 권한 허용됨: 기능 수행
    } else {
        // 권한 거부됨: 사용자에게 필요성 설명 또는 기능 제한
    }
}

fun checkAndRequestCamera() {
    when {
        ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PERMISSION_GRANTED -> {
            accessCamera()
        }
        shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> {
            // 이전에 거부했을 경우 교육용 UI 표시
            showRationaleDialog { requestPermissionLauncher.launch(Manifest.permission.CAMERA) }
        }
        else -> {
            requestPermissionLauncher.launch(Manifest.permission.CAMERA)
        }
    }
}
```
