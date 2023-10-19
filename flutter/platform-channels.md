# Platform Channel: Native Platform 과 연결하는 방법

## 1. MethodChannel

`RPC` 처럼 1회성 요청을 사용할 때 사용

Example

```kotlin
package ...

import kotlin.random.Random
import androidx.annotation.NonNull

import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel


class MainActivity: FlutterActivity() {
  private val METHOD_CHANNEL = "example.com/channel/method"

  override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, METHOD_CHANNEL).setMethodCallHandler {
      call, result ->
        // argument 없는 경우
        if(call.method == "getRandomNumber") {
          val rand = Random.nextInt(100)
          result.success(rand)
        }
        // named arguments 있는 경우 
        else if (call.method == "getRandomStringWithNamedArguments") {
          val limit = call.argument("len") ?: 4
          val prefix = call.argument("prefix") ?: ""
          val rand = ('a'..'z')
                      .shuffled()
                      .take(limit)
                      .joinToString(prefix = prefix, separator = "")
          result.success(rand)
        }
        // positional argument(1개) 있는 경우
        else if (call.method == "getRandomStringWithPositionArgument") {
          val len = call.arguments() ?: 4
          val rand = ('a'..'z')
                      .shuffled()
                      .take(len)
                      .joinToString("")
          result.success(rand)
        }
        // 에러 처리
        else if (call.method == "getError") {
          result.error("ALWAYS", "This method always returns error", null)
        }
        else {
          result.notImplemented()
        }
    }
  }
}
```

## 2. EventChannel

`Stream` 처럼 비동기적 Event가 들어올 때 사용

```kotlin
package ...

import androidx.annotation.NonNull
import android.os.Bundle
import android.content.res.Configuration
import android.content.pm.ActivityInfo
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.EventChannel
import io.flutter.plugin.common.EventChannel.EventSink
import io.flutter.plugin.common.EventChannel.StreamHandler

class MainActivity: FlutterActivity() {
  private val EVENT_CHANNEL = "example.com/channel/event"
  private var events: EventSink? = null
  private var oldConfig: Configuration? = null

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    oldConfig = Configuration(getContext().getResources().getConfiguration())
  }

  override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    EventChannel(flutterEngine.dartExecutor.binaryMessenger, EVENT_CHANNEL).setStreamHandler(
      object: StreamHandler {
        override fun onListen(arguments: Any?, es: EventSink) {
          events = es
          events?.success(isDarkMode(oldConfig))
        }

        override fun onCancel(arguments: Any?) {
        }
      }
    );
  }

  override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    if (isDarkModeConfigUpdated(newConfig)) {
      events?.success(isDarkMode(newConfig))
    }
    oldConfig = Configuration(newConfig)
  }

  fun isDarkModeConfigUpdated(config: Configuration): Boolean {
    return (config.diff(oldConfig) and ActivityInfo.CONFIG_UI_MODE) != 0
      && isDarkMode(config) != isDarkMode(oldConfig);
  }

  fun isDarkMode(config: Configuration?): Boolean {
    return config!!.uiMode and Configuration.UI_MODE_NIGHT_MASK == Configuration.UI_MODE_NIGHT_YES
  }
}
```

