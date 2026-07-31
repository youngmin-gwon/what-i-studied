# Photo Picker: 사진 선택에 필요한 최소 접근

상위 문서: [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)


Photo Picker는 사용자가 사진이나 동영상을 고르고 앱에 선택 결과만 전달하는 시스템 UI다.
앱이 전체 미디어 라이브러리를 직접 조회하지 않아도 되는 흐름에 맞는다.
프로필 사진이나 운동 영상처럼 선택 항목이 제한된 기능의 첫 후보로 둔다.

## 왜 우선 검토하는가

사용자에게 한두 개 미디어를 선택하게 하면서 전체 저장소 권한을 요구하면
기능에 비해 접근 범위가 커진다.
Photo Picker는 선택을 사용자의 명시적 동작에 묶는다.
앱은 선택된 `Uri`를 받고 필요한 동안 그 URI를 읽는다.
전체 갤러리 목록을 앱의 데이터 모델로 복사할 필요가 없다.

```kotlin
val pickMedia = registerForActivityResult(
    ActivityResultContracts.PickVisualMedia()
) { uri ->
    uri ?: return@registerForActivityResult
    contentResolver.openInputStream(uri)?.use { input ->
        // 선택된 원본을 앱 전용 작업 파일로 복사하거나 바로 처리한다.
    }
}

pickMedia.launch(
    PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly)
)
```

여러 항목이 필요하면 `PickMultipleVisualMedia`를 사용한다.
이미지와 영상 중 어떤 형식을 허용할지 요청 단계에서 좁힌다.
반환된 URI는 파일 경로가 아니라 ContentProvider 리소스 식별자다.
처리 시간이 길면 앱 전용 디렉터리에 필요한 사본을 만들 수 있다.
사본이 사용자에게 공개될 필요가 없다면 MediaStore로 다시 저장하지 않는다.

## MediaStore와의 경계

Photo Picker는 기존 미디어 중 사용자가 고르는 입력 경로다.
MediaStore는 앱이 만든 결과물을 갤러리와 공유 컬렉션에 등록하는 출력 경로다.
앱이 사용자의 전체 미디어를 검색·정렬해야 한다면 MediaStore 직접 조회가 필요할 수 있다.
그 경우에는 플랫폼 버전에 따른 미디어 권한과 거부 상태를 별도로 처리한다.

선택된 URI 접근이 장기 작업보다 오래 필요한지는 기능별로 확인한다.
작업이 끝나면 임시 사본을 삭제하고, 원본 URI를 영구 보관해야 한다면
플랫폼이 제공하는 권한 계약과 앱의 데이터 보존 정책을 함께 검토한다.

이 선택은 권한을 전혀 생각하지 않아도 된다는 뜻이 아니다.
사용 목적, 보관 기간, 서버 업로드 여부, 삭제 요청 처리까지 함께 설계해야 한다.
