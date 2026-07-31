# App-specific Files

상위 노트: [[android-storage-and-databases]]

App-specific files는 앱만 사용하는 파일을 저장하는 영역입니다.

대표 API:

```kotlin
context.filesDir
context.cacheDir
context.getExternalFilesDir(...)
context.getExternalCacheDir()
```

여기서 `context`는 앱 저장소 위치를 OS에 물어보기 위한 Android `Context`입니다. 저장소 객체가 오래 살아야 한다면 Activity Context가 아니라
Application Context를 쓰는 편이 안전합니다. Context의 종류와 수명
차이는 [[android-context]]를
참조하세요.

특징:

- 앱 삭제 시 함께 제거됨
- 내부 저장소의 app-specific file은 다른 앱이 접근할 수 없음
- 이미지/영상이라도 사용자에게 공유할 목적이 없으면 MediaStore보다 app-specific directory가 맞을 수 있음

맞는 경우:

```text
임시 이미지 처리 파일
운동 분석 중간 산출물
네트워크 다운로드 캐시
앱 내부 export 준비 파일
```

---
