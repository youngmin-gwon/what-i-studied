---
title: "Signing config는 로컬 서명과 Play 배포 정체성을 연결한다"
tags: ["android", "android/packaging-deployment"]
---

# Signing config는 로컬 서명과 Play 배포 정체성을 연결한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)
관련 노트: [Play App Signing은 upload key와 app signing key를 분리한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)

## 서명이 필요한 이유

Android 패키지는 서명되어야 설치·업데이트·배포될 수 있다.
같은 앱의 업데이트는 기존 배포와 호환되는 서명 정체성을 유지해야 한다.
debug와 release의 키를 분리하면 개발용 설치가 배포 키를 사용하지 않게 된다.

## Signing config

`signingConfigs`는 keystore 위치와 인증 정보를 모델링하고, build type이 이를 선택한다.

```kotlin
android {
    signingConfigs {
        create("release") {
            storeFile = file(providers.gradleProperty("releaseStoreFile").get())
            storePassword = providers.gradleProperty("releaseStorePassword").get()
            keyAlias = providers.gradleProperty("releaseKeyAlias").get()
            keyPassword = providers.gradleProperty("releaseKeyPassword").get()
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
        }
    }
}
```

## 비밀 관리

keystore 파일과 비밀번호를 소스 저장소에 커밋하지 않는다.
로컬에서는 무시되는 보호 파일을 사용하고, CI에서는 암호화된 secret과 임시 파일을 사용한다.
로그, 예외 메시지, Gradle 캐시, 아티팩트에 비밀 값이 노출되지 않는지도 확인한다.

## Play 배포 모델

Play App Signing을 사용하는 경우 업로드 키와 앱 서명 키의 역할을 구분한다.
키를 잃거나 교체해야 하는 상황을 고려해 복구 절차와 접근 권한을 문서화한다.

## 릴리스 변형 점검

- release가 의도한 signing config를 참조하는가?
- debug·staging이 release applicationId와 충돌하지 않는가?
- AAB 생성과 업로드 키 사용이 CI에서 재현되는가?
- `versionCode`가 이전 배포보다 증가했는가?
- 서명 정보가 출력 로그에 남지 않는가?

## R8와의 경계

코드 축소, 난독화, 리소스 축소는 이 문서의 주제가 아니다.
릴리스 변형에서 최적화 옵션을 연결할 때는 별도 R8 정본을 참조 후보로 삼는다.
R8 공식 연결 후보: https://developer.android.com/topic/performance/app-optimization/enable-app-optimization

## 참고

앱 서명 공식 문서: https://developer.android.com/studio/publish/app-signing
앱 ID와 서명 구성: https://developer.android.com/build/build-variants
