---
title: platform channel - Native Platform 과 연결하는 방법
created at: 2024-12-12
tags:
  - concept
  - flutter
  - platform-channel
aliases:
---

## 1. MethodChannel

`RPC` 처럼 1 회성 요청을 사용할 때 사용

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

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class ChannelScreen extends StatefulWidget {
  const ChannelScreen({super.key});

  @override
  State<ChannelScreen> createState() => _ChannelScreenState();
}

class _ChannelScreenState extends State<ChannelScreen> {
  int counter = 0;
  String randomName = '';

  static const methodPlatform = MethodChannel('example.com/channel/method');

  Future<void> _generateRandomNumber() async {
    int random;
    try {
      random = await methodPlatform.invokeMethod<int>('getRandomNumber') ?? -1;
    } on PlatformException {
      random = 0;
    }

    setState(() {
      counter = random;
    });
  }

  Future<void> _generateRandomString() async {
    String name;
    try {
      final arguments = {
        'len': 8,
        'prefix': 'fl_',
      };
      name = await methodPlatform.invokeMethod<String>(
            'getRandomStringWithNamedArguments',
            arguments,
          ) ??
          '';
    } on PlatformException {
      name = 'Something went wrong!';
    }

    setState(() {
      randomName = name;
    });
  }

  Future<void> _generateRandomStringWithPositionalArgument() async {
    String name;
    try {
      name = await methodPlatform.invokeMethod<String>(
            'getRandomStringWithPositionArgument',
            3,
          ) ??
          '';
    } on PlatformException {
      name = 'Something went wrong!';
    }

    setState(() {
      randomName = name;
    });
  }

  Future<void> _generateError() async {
    String name;
    try {
      name = await methodPlatform.invokeMethod<String>('getError') ?? '';
    } on PlatformException catch (e) {
      name = '''
PlatformException:
  Code: ${e.code}
  Message: ${e.message}
''';
    }

    setState(() {
      randomName = name;
    });
  }

  void _onEvent(dynamic event) {
    setState(() {
      theme = event == true ? 'dark' : 'light';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MethodChannel example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Kotlin generates the following number:',
            ),
            Text(
              randomName,
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        // onPressed: _generateRandomNumber,
        // onPressed: _generateRandomString,
        // onPressed: _generateRandomStringWithPositionalArgument,
        onPressed: _generateError,
        tooltip: 'Generate',
        child: const Icon(Icons.refresh),
      ),
    );
  }
}
```

## 2. EventChannel

`Stream` 처럼 비동기적 Event 가 들어올 때 사용

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

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class ChannelScreen extends StatefulWidget {
  const ChannelScreen({super.key});

  @override
  State<ChannelScreen> createState() => _ChannelScreenState();
}

class _ChannelScreenState extends State<ChannelScreen> {
  String theme = '';

  static const eventPlatform = EventChannel('example.com/channel/event');

  @override
  void initState() {
    super.initState();
    eventPlatform.receiveBroadcastStream().listen(_onEvent);
  }

  void _onEvent(dynamic event) {
    setState(() {
      theme = event == true ? 'dark' : 'light';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MethodChannel example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'System color theme:',
            ),
            Text(
              theme,
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
    );
  }
}
```
