# Mainline은 선택된 system component를 정규 플랫폼 release 밖에서 업데이트한다

Mainline은 Android 10에서 도입된 modular system components 구조다. 목적은 일부 system component를 Android 전체 OS release와 분리해 critical bug fix와 개선을 더 빠르고 넓게 배포하는 것이다.

Mainline update는 Google Play system update 인프라나 partner OTA를 통해 전달될 수 있다. GMS 기기에서는 Google 서명과 `com.google.android.*` package prefix가 보일 수 있고, AOSP key로 서명된 기기는 `com.android.*` prefix를 쓸 수 있다.

공식 문서 기준으로 Android 11 이하 Mainline support는 2025년 Q4에 종료되었다. 따라서 오래된 기기까지 같은 update path가 계속 유지된다고 쓰면 안 된다.

Mainline module은 아무 system component나 마음대로 뜯어낸 것이 아니다. 공식 compatibility, stable API/interface, CTS 조건을 만족할 수 있는 component만 module boundary를 가진다.

관련 노트: [Mainline module 목록](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-module-list-is-device-and-release-dependent-metadata.md), [APEX package 경계](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/android-security-practices.md).

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system)
