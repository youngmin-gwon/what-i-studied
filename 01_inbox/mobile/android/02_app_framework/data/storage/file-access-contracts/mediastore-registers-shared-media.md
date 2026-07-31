# MediaStore: 공유 미디어의 등록과 접근

상위 문서: [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)
관련 정본: [Photo Picker는 필요한 미디어 접근 범위를 줄인다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/photo-picker-minimizes-media-access.md)


MediaStore는 앱 전용 데이터베이스가 아니다.
Android가 관리하는 공유 미디어 컬렉션을 조회하고 변경하는 ContentProvider API다.
앱은 `ContentResolver`를 통해 요청하고, 결과는 주로 `content://` URI로 받는다.

## 대상 컬렉션

| 컬렉션 | 대표 대상 |
| --- | --- |
| `MediaStore.Images` | 사진과 스크린샷 |
| `MediaStore.Video` | 동영상 |
| `MediaStore.Audio` | 음악과 녹음 |
| `MediaStore.Downloads` | 다운로드 파일 |

MediaStore가 맞는 기준은 다른 앱과 사용자에게 공개할 필요가 있는가이다.
갤러리에 보여야 하는 사진, 공유 가능한 영상 export가 대표 사례다.
`sessionKey`, 분석 이력, 서버 응답 캐시는 MediaStore의 대상이 아니다.

## 저장 흐름

```kotlin
val values = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "result.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
    put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
    put(MediaStore.Images.Media.IS_PENDING, 1)
}

val uri = resolver.insert(
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
    values
)
uri?.let {
    resolver.openOutputStream(it)?.use { stream -> bitmap.compress(Bitmap.CompressFormat.JPEG, 95, stream) }
    resolver.update(it, ContentValues().apply {
        put(MediaStore.Images.Media.IS_PENDING, 0)
    }, null, null)
}
```

Android 10 이상에서는 `RELATIVE_PATH`로 논리적 미디어 폴더를 지정한다.
파일 시스템 절대 경로를 직접 조립하는 방식은 피한다.
`IS_PENDING`을 1로 두면 쓰기 중인 항목을 사용자에게 노출하지 않을 수 있다.
출력이 완성되면 0으로 갱신해 공개 상태로 전환한다.
실패 시 미완성 항목을 삭제하는 정리 경로도 둔다.

## 읽기 흐름

`query()`에서 필요한 열만 projection으로 요청한다.
`_ID`, 표시 이름, 추가 시각처럼 실제 화면에 필요한 열만 선택한다.
반환된 ID를 collection URI에 붙여 개별 `content://` URI를 만든다.
파일 경로를 얻어 장시간 보관하기보다 URI와 접근 권한을 중심으로 설계한다.
커서는 반드시 `use`로 닫고, 큰 미디어는 스트림으로 처리한다.

기존 미디어를 직접 광범위하게 조회하는 경우에는 버전별 미디어 권한을 검토한다.
사용자가 몇 개만 고르는 흐름은 [Photo Picker로 선택 범위 줄이기](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/photo-picker-minimizes-media-access.md)가 더 적합하다.
