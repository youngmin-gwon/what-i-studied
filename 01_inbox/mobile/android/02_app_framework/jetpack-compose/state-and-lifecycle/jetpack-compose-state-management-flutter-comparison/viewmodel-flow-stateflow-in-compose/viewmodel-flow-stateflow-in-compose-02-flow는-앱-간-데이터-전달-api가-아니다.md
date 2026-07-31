# Flow는 앱 간 데이터 전달 API가 아니다

`Flow`는 Kotlin 객체가 같은 앱 프로세스 안에서 값을 주고받는 방식입니다.

```text
Room -> Flow -> Repository -> ViewModel -> Compose
DataStore -> Flow -> SessionRepository -> RootViewModel
callback API -> callbackFlow -> ViewModel
```

다른 앱으로 데이터를 공개하거나 전달하려면 Flow가 아니라 Android 플랫폼 경계를 사용해야 합니다.

| 목적                          | 사용하는 도구                       |
|:----------------------------|:------------------------------|
| 다른 앱이 내 구조화 데이터를 조회         | `ContentProvider`             |
| 다른 앱에 파일 공유                 | `FileProvider`                |
| 다른 앱/시스템에 한 번의 작업 요청        | `Intent` / `PendingIntent`    |
| 웹 링크로 앱 진입                  | App Link / Deep Link          |
| 시스템/AI agent가 앱 기능을 검색하고 실행 | App Functions                 |
| 낮은 수준의 프로세스 간 바인딩           | Bound Service / Binder / AIDL |

> [!IMPORTANT]
> Flow는 "앱 안의 상태 흐름"이고, ContentProvider/Intent/FileProvider/App Functions는 "앱 밖과 만나는 통로"입니다. 이 둘을 섞어
> 생각하면 아키텍처 경계가 흐려집니다.

---
