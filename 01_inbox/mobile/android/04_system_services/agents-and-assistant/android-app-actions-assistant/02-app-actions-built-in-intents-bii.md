---
title: 02-app-actions-built-in-intents-bii
tags: []
aliases: []
date modified: 2026-07-31 17:35:48 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## App Actions (Built-in Intents, BII)

사용자가 "Hey Google, [App Name]에서 [Action]해줘"라고 말할 때 앱이 바로 반응하도록 설계되었다.

### `shortcuts.xml` 정의

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <capability android:name="actions.intent.START_EXERCISE">
        <intent
            android:action="android.intent.action.VIEW"
            android:targetPackage="com.example.app"
            android:targetClass="com.example.app.ExerciseActivity">
            <parameter
                android:name="exercise.name"
                android:key="exerciseType" />
        </intent>
    </capability>
</shortcuts>
```

### AndroidManifest 등록

```xml
<meta-data
    android:name="android.app.shortcuts"
    android:resource="@xml/shortcuts" />
```
