# 사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다

사진 찍기 기능은 좋은 입문 예시지만 단일 API 예시는 아니다. 권한 요청, Activity Result/Intent, CameraX 또는 Camera2, preview Surface, media encoding, file/MediaStore 저장, vendor camera HAL이 함께 관여한다.

그래서 이 예시는 "Android는 계층형 platform이다"를 보여주는 routing example로 남기고, 실제 구현 상세는 camera/media, storage, permission, app components 정본으로 보낸다.

학습 문서가 이 예시 안에 모든 코드를 넣으면 중복이 커진다. 대신 어느 문제를 만나면 어느 정본을 봐야 하는지 알려주는 map으로 유지한다.

관련 노트: [graphics/media runtime](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-media-runtime.md), [file access](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md), [permissions](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-permissions.md), [app components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md).
