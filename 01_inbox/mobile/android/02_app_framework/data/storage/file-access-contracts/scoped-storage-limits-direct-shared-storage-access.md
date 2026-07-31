# Scoped Storage: 저장소 접근 경계를 선택하는 규칙

상위 문서: [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)
관련 노트: [Scoped Storage와 암호화는 서로 다른 경계를 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/scoped-storage-and-encryption-protect-different-boundaries.md)


Scoped Storage는 앱이 기기 전체 파일을 직접 훑는 모델에서 벗어나게 한 저장소 규칙이다.
Android 10부터 앱은 자신의 파일을 직접 다루고, 공유 파일은 플랫폼 API를 통한다.
핵심은 저장소 권한을 먼저 요청하는 것이 아니라 파일의 소유권과 공개 목적을 먼저 정하는 것이다.

## 세 가지 접근 경계

1. 앱 전용 파일은 `filesDir`, `cacheDir`, 앱 전용 외부 디렉터리를 사용한다.
2. 공유 미디어는 MediaStore 컬렉션과 `ContentResolver`를 사용한다.
3. 일반 문서와 사용자 지정 폴더는 SAF picker로 사용자의 선택을 받는다.

앱 전용 파일은 다른 앱에 공개할 필요가 없는 데이터다.
공유 미디어는 갤러리나 다른 앱에서 발견·열 수 있어야 하는 결과물이다.
SAF 문서는 앱이 위치를 소유하지 않고 사용자가 파일 또는 폴더를 지정한다.

## 권한 최소화

예전의 전체 외부 저장소 접근을 기본값으로 두지 않는다.
사진 한두 장을 고르는 기능은 [Photo Picker](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/photo-picker-minimizes-media-access.md)를 먼저 검토한다.
앱이 생성한 사진이나 영상을 공개 컬렉션에 쓰는 경우에는 MediaStore를 사용한다.
이미 존재하는 미디어 전체를 검색해야 하는 경우에만 필요한 미디어 권한을 검토한다.
권한의 필요 여부는 target SDK, Android 버전, 읽기·쓰기 목적에 따라 달라진다.

```text
앱 내부 처리 파일       -> App-specific directory
갤러리에 보일 결과물    -> MediaStore
사용자가 고른 PDF/폴더   -> SAF
사용자가 고른 사진       -> Photo Picker
```

## 경로 중심 사고의 한계

공유 영역의 절대 경로를 문자열로 만들어 직접 접근하는 방식을 피한다.
MediaStore와 SAF는 URI와 ContentResolver를 통해 제공자 경계를 존중한다.
URI를 받았다고 해서 그 자원이 영구적으로 존재한다고 가정하지 않는다.
스트림이 열리지 않거나 권한이 철회된 경우를 사용자 흐름의 정상 오류로 처리한다.

Scoped Storage는 단순한 제약이 아니라 데이터 공개 범위를 코드에 반영하는 계약이다.
파일을 어디에 저장할지보다 누가 소유하고 누가 봐야 하는지를 먼저 결정한다.
이 원칙을 따르면 권한 요청, 삭제 수명, 백업 범위도 함께 명확해진다.
