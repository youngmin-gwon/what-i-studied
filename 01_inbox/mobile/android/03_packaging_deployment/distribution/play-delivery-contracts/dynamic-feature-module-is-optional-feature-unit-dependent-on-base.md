# Dynamic Feature Module은 base module에 의존하는 선택 기능 단위다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)
관련 정본: [AAB는 Play가 기기별 APK를 생성하는 게시 아티팩트다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)

## 모듈 관계

기본 앱 모듈은 `com.android.application` 플러그인을 사용한다.
동적 기능 모듈은 `com.android.dynamic-feature` 플러그인을 사용한다.
앱 모듈의 `android.dynamicFeatures`에 기능 모듈을 등록한다.

```kotlin
// app/build.gradle.kts
android {
    dynamicFeatures += setOf(":feature:photo-editor")
}

// feature/photo-editor/build.gradle.kts
plugins {
    id("com.android.dynamic-feature")
}
```

기능 모듈의 manifest에는 배포 정책을 선언한다.
별도 정책이 없으면 install-time이 기본값이다.

```xml
<manifest xmlns:dist="http://schemas.android.com/apk/distribution">
    <dist:module dist:title="@string/title_photo_editor">
        <dist:delivery>
            <dist:on-demand />
        </dist:delivery>
    </dist:module>
</manifest>
```

## 설계 규칙

- base는 기능 모듈의 공개 진입점과 공통 계약을 제공한다.
- 기능 모듈에서 사용하는 공통 타입은 base 또는 별도 일반 라이브러리에 둔다.
- 다운로드 전 모듈의 클래스, 리소스, activity를 참조하지 않는다.
- 다른 앱이 직접 호출할 수 있도록 기능 activity를 exported로 만들지 않는다.
- 코드가 없는 feature module은 manifest의 `android:hasCode`를 검토한다.
- 모듈 이름은 런타임 요청 이름과 정확히 일치해야 한다.

## 제거 가능 install-time 모듈

설치 때 필요하지만 이후 사용하지 않는 기능은 removable install-time 모듈로
구성하고, 실제 제거 가능성 및 재설치 흐름을 함께 검증한다.
removable을 많이 사용하면 split 수가 늘어 설치 시간이 증가할 수 있다.

## 검증

Android Studio에서 bundle을 빌드하고 bundletool로 APK set을 생성한다.
지원 기기에서 설치한 뒤 모듈 존재 여부와 앱 업데이트 동작을 확인한다.
Play Console 내부 테스트에서도 실제 Play 전달 경로를 검증한다.

## 공식 문서

- [Overview of Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)
- [Configure install-time delivery](https://developer.android.com/guide/playcore/feature-delivery/install-time)
- [Manage installed modules](https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage-installed-modules)
