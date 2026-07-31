# 큰 그림

상위 노트: [[android-storage-and-databases]]

Android 저장소는 "DB를 쓸까 말까"보다 먼저 **무엇을 저장하는가**로 나누는 편이 안전합니다.

공식 Android storage overview는 앱 데이터 저장 선택지를 크게 다음처럼 나눕니다.

| 저장 대상             | 권장 저장소                   | 대표 예                                            |
|:------------------|:-------------------------|:------------------------------------------------|
| 작은 key-value 설정   | DataStore                | session flag, feature flag, user preference     |
| 구조화된 앱 내부 데이터     | Room                     | training record, measure history, offline cache |
| 앱 전용 파일           | App-specific files       | 앱 내부 캐시, 임시 다운로드, private export file           |
| 유저가 다른 앱에서도 볼 미디어 | MediaStore               | 사진, 동영상, 오디오                                    |
| 유저가 직접 고르는 문서     | Storage Access Framework | PDF, EPUB, CSV, 일반 파일 import/export             |

관련 공식 문서:

- [Data and file storage overview](https://developer.android.com/training/data-storage)
- [DataStore](https://developer.android.com/topic/libraries/architecture/datastore)
- [Save data in a local database using Room](https://developer.android.com/training/data-storage/room)
- [Access media files from shared storage](https://developer.android.com/training/data-storage/shared/media)

---
