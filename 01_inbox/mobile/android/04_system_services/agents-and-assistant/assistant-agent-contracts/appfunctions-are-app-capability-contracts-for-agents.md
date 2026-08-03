---
title: "AppFunctions는 에이전트용 앱 기능 계약이다"
tags: ["android", "android/system-services"]
---

# AppFunctions는 에이전트용 앱 기능 계약이다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)

## 현재 상태

AppFunctions는 앱의 기능과 데이터를 Android 시스템의 registry에 제공해 에이전트와 assistant가 작업을 발견하고 실행하도록 하는 Android 16+ API다.
2026-08-03 기준 Android Developers 문서는 API를 **experimental preview**로 설명한다.
Jetpack 최신 안정 버전은 없고 `androidx.appfunctions:appfunctions:1.0.0-alpha10`이 공개되어 있다.
Gemini와의 end-to-end 통합도 문서상 trusted tester 대상 private preview로 안내된다.
따라서 이 API의 annotation, 결과 타입, 호출자 정책은 변경될 수 있다.

## 앱 개발자의 책임

- 사용자가 실제로 기대하는 작업 단위만 함수로 노출한다.
- 함수 이름, parameter, 반환값을 에이전트가 오해하지 않도록 KDoc과 타입을 명확히 한다.
- 함수 내부에서 인증, 앱 상태, 도메인 권한, 입력 범위를 다시 검사한다.
- 함수가 UI 없이 실행될 수 있는지, 사용자 확인이 필요한지 명시적으로 설계한다.
- 성공·실패·재시도 가능성을 구조화된 결과로 표현한다.

```kotlin
@AppFunctionServiceEntryPoint(
    serviceName = "MyAppFunctionService",
    appFunctionXmlFileName = "my_service"
)
abstract class BaseMyAppFunctionService : AppFunctionService() {
    @AppFunction
    suspend fun createNote(title: String, content: String): CreateNoteResult {
        return repository.createNote(title, content)
    }
}
```

위 코드는 개념 예시다.
실제 프로젝트는 해당 preview 버전의 API reference와 샘플에 맞춰 entry point, generated service, XML schema, compiler 설정, 결과 타입을 확인해야 한다.

## 통합 조건

- compileSdk 36 이상을 요구하는 공식 통합 가이드를 따른다.
- Jetpack library와 KSP compiler를 함께 구성한다.
- Android 16 미지원 환경에서는 library의 지원 확인 결과를 처리한다.
- AppFunctions를 App Actions의 대체품으로 단정하지 말고 서로 다른 호출 계약으로 유지한다.

공식 문서: [AppFunctions 개요](https://developer.android.com/ai/appfunctions), [추가 방법](https://developer.android.com/ai/appfunctions/add-appfunctions), [Jetpack release notes](https://developer.android.com/jetpack/androidx/releases/appfunctions)

검증일: 2026-08-03. Android 16+ 가용성, experimental preview, Gemini private preview, Jetpack `1.0.0-alpha10`을 공식 문서에서 확인했다.

## API 안정성에 대한 주의

preview 단계에서는 샘플 코드가 정식 호환성 계약이 아니다.
특정 Android 버전이나 assistant 제품에서 동작한다는 설명과 공개 SDK의 일반 가용성을 구분한다.
릴리스 앱은 함수가 호출되지 않는 경우에도 기존 UI와 일반 앱 흐름이 정상 동작해야 한다.
AppFunctions를 도입할 때는 현재 alpha release notes의 변경점과 API reference를 함께 검토한다.

또한 “에이전트가 여러 앱의 함수를 자동으로 조합한다”는 서술은 가능한 사용 시나리오이지,
모든 기기와 assistant에서 보장되는 실행 정책은 아니다.
실제 조합 가능성, 노출 대상, 사용자 확인 정책은 호출자와 플랫폼 버전에 따라 달라진다.
