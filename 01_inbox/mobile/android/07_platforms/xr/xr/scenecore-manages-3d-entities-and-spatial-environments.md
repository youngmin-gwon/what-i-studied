---
title: scenecore-manages-3d-entities-and-spatial-environments
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## SceneCore 는 3D entity 와 공간 환경을 다루는 계층이다

상위 문서: [Android XR 계약](./xr.md)

SceneCore 는 일반 화면 컴포저블을 배치하는 계층이 아니라 XR scene graph, entity, 3D model, spatial environment, spatial audio 같은 공간 객체를 다루는 계층이다.

### SceneCore 3D Entity 로딩 및 수명주기 연동 메커니즘

```kotlin
fun loadSpatial3DModel(activity: ComponentActivity) {
    val session = Session.getOrCreate(activity)
    
    activity.lifecycleScope.launch {
        // GLTF 3D 모델 비동기 로딩
        val modelFuture = GltfModel.create(session, "models/product_sample.glb")
        val gltfModel = modelFuture.await()
        
        // SceneGraph Entity 생성 및 Transform 설정
        val entity = GltfModelEntity.create(
            session = session,
            gltfModel = gltfModel,
            pose = Pose(Vector3(0f, 0f, -1.5f), Quaternion.Identity)
        )
        
        // Entity 수명주기는 Activity Session을 초과할 수 없음
    }
}
```

### 언제 쓰는가

- 3D 모델을 UI 주변 또는 실제 공간 기준으로 배치해야 한다.
- panel 보다 낮은 수준에서 entity 이동, 크기 조절, anchor, component 를 제어해야 한다.
- spatial audio, environment, perception 기반 위치 지정이 제품 경험의 일부다.

### 경계

Compose for XR 은 UI 선언과 공간 layout 에 적합하다. SceneCore 는 UI 가 아닌 공간 객체와 scene graph 조작이 필요할 때 선택한다.

SceneCore 객체는 `Session` 에 귀속된다. session 의 activity 가 파괴되면 연결된 spatial UI 와 3D content 도 파괴되고 session 은 더 이상 유효하지 않으므로, entity 참조를 application singleton 처럼 보존하지 않는다. activity recreation 과 현재 알려진 session invalidation 제약도 실제 구성 변경으로 검증한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# SceneCore 3D Entity 생성 및 Scene Graph 덤프 관측
adb logcat -v threadtime | grep -E "SceneCore|GltfModelEntity|SpatialEnvironment"

# Session Invalidation 및 Activity lifecycle 로깅
adb logcat -v threadtime | grep -i "XrSessionDestroyed"
```

### 관련 문서

- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](./compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](./xr-quality-includes-performance-comfort-and-safety.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)

검증일: 2026-08-03. [Access a session](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session), [XR SceneCore releases](https://developer.android.com/jetpack/androidx/releases/xr-scenecore)

