# APEX는 APK 모델로 다루기 어려운 lower-level system module을 담는다

APEX(Android Pony EXpress)는 Android 10에서 도입된 package/container format이다. ART, native service, class library, HAL처럼 APK 설치 모델만으로는 boot timing과 system integration을 다루기 어려운 lower-level component를 업데이트하기 위해 만들어졌다.

APEX 파일은 package identity와 version metadata, payload image, public key 같은 요소를 포함하고, apexd가 boot 과정에서 activation을 관리한다. 어떤 APEX는 매우 이른 boot 단계에 필요하므로 일반 APK처럼 PackageManager가 준비된 뒤에만 다루는 모델이 맞지 않는다.

APEX는 "앱 배포 포맷의 다른 이름"이 아니다. platform partition, verified payload, boot activation, rollback, signing key가 얽힌 system update 경계다.

관련 정본: [APEX activation/rollback](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md), [boot/runtime 정본](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [platform-modularity hub](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md).

공식 문서: [APEX file format](https://source.android.com/docs/core/ota/apex)
