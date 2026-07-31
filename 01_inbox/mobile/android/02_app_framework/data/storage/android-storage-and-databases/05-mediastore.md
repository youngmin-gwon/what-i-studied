# MediaStore

상위 노트: [android-storage-and-databases](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases.md)

MediaStore는 앱 내부 DB가 아닙니다.

MediaStore는 Android 시스템이 제공하는 **공유 미디어 저장소의 인덱스와 접근 API**입니다. 사진, 동영상, 오디오, 다운로드 같은 사용자 미디어를 앱들이
공통으로 찾고 열 수 있게 해주는 system content provider라고 보는 편이 정확합니다.

중요한 점:

- 앱이 schema를 만들지 않습니다.
- 앱이 migration을 관리하지 않습니다.
- 앱 전용 데이터 저장소가 아닙니다.
- Android 시스템이 media collection을 관리합니다.
- 앱은 `ContentResolver`로 query/insert/update/delete 요청을 보냅니다.
- 반환되는 것은 파일 경로보다 `content://` URI 중심입니다.

MediaStore가 다루는 대표 collection:

| Collection             | 대상          |
|:-----------------------|:------------|
| `MediaStore.Images`    | 사진, 스크린샷    |
| `MediaStore.Video`     | 동영상         |
| `MediaStore.Audio`     | 음악, 녹음, 알림음 |
| `MediaStore.Downloads` | 다운로드 파일     |

MediaStore가 맞는 경우:

```text
사용자가 갤러리에서 볼 사진 저장
운동 자세 분석 결과 영상을 갤러리에 저장
사용자가 다른 앱에서도 열 수 있는 이미지/동영상 export
기기 내 사진/영상 목록에서 유저가 고른 미디어를 읽기
```

MediaStore가 맞지 않는 경우:

```text
sessionKey 저장
training record 저장
measure history 저장
앱 내부 캐시 저장
서버 응답 cache table 저장
```

즉 MediaStore는 "DB처럼 query할 수 있는 API"를 제공하지만, 우리가 앱 도메인 데이터를 넣는 database가 아닙니다.

### Photo Picker와의 관계

사용자가 기존 사진/동영상을 선택하기만 하면 Photo Picker가 더 나은 선택일 수 있습니다.

```text
Photo Picker
 -> 유저가 파일을 선택
 -> 앱은 선택된 URI에 접근
 -> 전체 미디어 라이브러리 권한을 요구하지 않음

MediaStore 직접 접근
 -> 앱이 media collection을 query
 -> use case에 따라 READ_MEDIA_IMAGES / READ_MEDIA_VIDEO 등이 필요할 수 있음
```

이 프로젝트에서 사용자가 프로필 사진이나 운동 영상을 선택하는 기능을 만들면, 먼저 Photo Picker를 검토합니다. 앱이 직접 만든 결과물을 갤러리에 저장해야 하면
MediaStore를 검토합니다.

---
