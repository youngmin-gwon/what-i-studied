---
title: manifest-declares-components-permissions-features-and-exported-boundaries
tags: [android, android/app-components, android/architecture]
aliases: ["Manifest는 컴포넌트, 권한, 기능, exported 경계를 선언한다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## OS가 읽는 manifest는 source 한 장이 아니라 build variant별 merge 결과다

소스의 `AndroidManifest.xml`은 component, permission, feature와 외부 진입 경계를 선언하지만 OS가 설치 시 읽는 것은 main·build type·product flavor·variant·library manifest를 합친 최종 packaged manifest다. 앱 source에서 보이지 않던 provider, permission, intent filter가 dependency manifest에서 들어올 수 있다.

### Merge 메커니즘

높은 우선순위의 variant/build type/flavor manifest가 main보다 우선하고, imported library manifest는 더 낮은 우선순위를 가진다. 같은 key의 element와 충돌하는 attribute는 자동 결합되거나 conflict error가 되며, 의도를 아는 상위 manifest만 `tools:replace`, `tools:remove`, `tools:node`로 해결한다.

```xml
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <application>
        <service
            android:name="com.partner.UploadService"
            android:exported="false"
            tools:replace="android:exported" />
    </application>
</manifest>
```

`tools:replace`는 오류를 숨이는 만능 옵션이 아니다. library의 외부 API 계약을 실제로 닫아도 되는지 확인한 뒤 최종 값의 소유권을 명시할 때만 쓴다. `<intent-filter>`는 manifest 간 동일 항목으로 합쳐지지 않고 각각 보존되므로 예상하지 못한 exported surface가 늘 수 있다.

### OS entry point와 선언 경계

Activity·Service·ContentProvider와 manifest receiver는 최종 manifest에 없으면 시스템이 component로 찾지 못한다. 예외적으로 context-registered receiver는 runtime 등록으로 알려진다. class 파일이 APK에 존재하는 것과 OS entry point로 등록된 것은 별개다.

### 실패·관찰 신호

- attribute 값이 충돌하면 보통 install이 아니라 manifest merge/build 단계에서 conflict error가 난다.
- Android Studio의 Merged Manifest 탭에서 각 값의 source와 merge marker 적용 결과를 확인한다.
- `apkanalyzer manifest print <apk>`로 CI artifact의 component, permission, feature, exported 값을 검사한다.
- dependency update 뒤 새 provider/receiver/permission이 나타나면 packaged manifest diff를 보안 변경으로 review한다.

상위 문서: [App Component Contracts](./app-component-contracts.md)

공식 문서: [Manage manifest files](https://developer.android.com/build/manage-manifests), [App manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro)
