# 제공 방식: AppFunctionService와 런타임 등록

공식 API 기준으로 앱은 기능을 두 방식으로 제공할 수 있습니다.

| 제공 방식                | 언제 적합한가                                   | 핵심 API                                      |
|:---------------------|:------------------------------------------|:--------------------------------------------|
| `AppFunctionService` | 앱 전체에서 항상 제공 가능한 기능                       | `AppFunctionService`, `onExecuteFunction()` |
| 런타임 등록               | 특정 Activity나 foreground service 상태에 묶인 기능 | `AppFunctionManager.registerAppFunction()`  |

`AppFunctionService` 방식은 시스템이 필요할 때 앱을 깨워 기능을 실행할 수 있습니다.

```xml

<service android:name=".NoteAppFunctionService"
    android:permission="android.permission.BIND_APP_FUNCTION_SERVICE" android:exported="true">
    <property android:name="android.app.appfunctions" android:value="note_app_functions.xml" />
    <intent-filter>
        <action android:name="android.app.appfunctions.AppFunctionService" />
    </intent-filter>
</service>
```

```kotlin
class NoteAppFunctionService : AppFunctionService() {
    override fun onExecuteFunction(
        request: ExecuteAppFunctionRequest,
        callingPackage: String,
        callingPackageSigningInfo: SigningInfo,
        cancellationSignal: CancellationSignal,
        callback: OutcomeReceiver<ExecuteAppFunctionResponse, AppFunctionException>,
    ) {
        when (request.functionIdentifier) {
            "createNote" -> {
                // repository.createNote(...)
                callback.onResult(ExecuteAppFunctionResponse(...))
            }
            else -> {
                callback.onError(
                    AppFunctionException(
                        AppFunctionException.FUNCTION_NOT_FOUND,
                        "Unknown function: ${request.functionIdentifier}",
                    )
                )
            }
        }
    }
}
```

> [!NOTE]
> App Functions는 함수 메타데이터를 XML asset으로 선언하고, 이를 `android.app.appfunctions` property로 연결합니다. Android
> SDK 문서 기준으로 앱 하나에는 활성 `AppFunctionService` 구현이 하나만 있을 수 있습니다.
