---
title: SAF: 사용자가 고른 문서와 폴더에 접근하기
tags: [android, android/data, android/storage, android/file-access-contracts]
aliases: ["SAF: 사용자가 고른 문서와 폴더에 접근하기"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# SAF: 사용자가 고른 문서와 폴더에 접근하기

상위 문서: [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)


Storage Access Framework는 앱이 저장소 전체를 탐색하는 API가 아니다.
시스템 파일 picker를 열고 사용자가 고른 문서나 폴더에 권한을 위임받는 방식이다.
일반 문서와 임의의 파일 위치를 다룰 때 MediaStore보다 적합하다.

## 사용 사례

- PDF, CSV, EPUB 가져오기
- 사용자가 지정한 위치로 파일 내보내기
- 특정 폴더를 백업 대상으로 선택하기
- 파일 확장자와 무관한 문서 열기

문서 하나를 열 때는 `OpenDocument`를 사용한다.
새 파일 위치를 사용자에게 정하게 할 때는 `CreateDocument`를 사용한다.
폴더 트리 전체를 선택받을 때는 `OpenDocumentTree`를 사용한다.

```kotlin
val openDocument = registerForActivityResult(
    ActivityResultContracts.OpenDocument()
) { uri ->
    uri ?: return@registerForActivityResult
    contentResolver.openInputStream(uri)?.use { input ->
        input.bufferedReader().use { reader ->
            val text = reader.readText()
        }
    }
}

openDocument.launch(arrayOf("text/plain", "application/pdf"))
```

앱은 선택 결과인 URI를 받고 `ContentResolver`로 읽는다.
URI를 일반 파일 경로로 변환하는 것을 기본 전제로 삼지 않는다.
제공자가 스트림 접근을 지원하도록 `openInputStream`과 `openOutputStream`을 사용한다.

## 새 파일과 폴더

`CreateDocument`는 표시 이름을 초기값으로 제안하고 최종 위치는 사용자가 정한다.
`OpenDocumentTree`는 선택된 트리 URI 아래에서 파일을 나열하거나 생성할 수 있다.
폴더 접근을 다시 사용해야 하면 persistable URI permission을 저장한다.

```kotlin
contentResolver.takePersistableUriPermission(
    treeUri,
    Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
)
val folder = DocumentFile.fromTreeUri(context, treeUri)
folder?.listFiles()?.forEach { file -> println(file.name) }
```

사용자가 준 권한은 앱이 임의로 다른 폴더까지 확장할 수 있다는 뜻이 아니다.
URI가 더 이상 유효하지 않거나 사용자가 권한을 철회할 수 있으므로 오류를 처리한다.
대용량 파일은 백그라운드 작업에서 스트리밍하고 진행 상태를 제공한다.

MediaStore는 미디어 컬렉션 중심이고 SAF는 사용자 선택 문서 중심이다.
사진 한두 장 선택만 필요한 경우에는 [Photo Picker](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/photo-picker-minimizes-media-access.md)를 먼저 검토한다.
