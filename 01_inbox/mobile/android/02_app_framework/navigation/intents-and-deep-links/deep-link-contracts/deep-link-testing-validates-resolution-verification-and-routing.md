---
title: deep-link-testing-validates-resolution-verification-and-routing
tags: [android, android/deep-links, android/navigation]
aliases: ["Android Deep Links 와 App Links 테스트 및 디버깅"]
date modified: 2026-08-03 18:11:27 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Deep Links 와 App Links 테스트 및 디버깅

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)

### 테스트 층위

딥 링크는 URI 파싱, Intent 매칭, 도메인 검증, 앱 라우팅을 나눠서 테스트한다.

URI 파싱 테스트는 허용된 scheme, host, path, query 와 잘못된 입력을 검증한다.

Intent 테스트는 매니페스트 필터가 기대한 URI 를 수신하는지 확인한다.

App Links 테스트는 assetlinks.json, 인증서 지문, 기기 검증 상태를 확인한다.

라우팅 테스트는 공개 목적지, 인증 목적지, 오류와 뒤로 가기를 확인한다.

### ADB 로 URI 실행

다음 명령은 브라우저나 다른 앱이 보낸 것과 유사한 VIEW Intent 를 시작한다.

```bash
adb shell am start -a android.intent.action.VIEW \
  -d "https://www.example.com/product/abc123"
```

특정 패키지를 지정하면 해당 앱으로의 실행 결과를 좁혀 확인할 수 있다.

```bash
adb shell am start -a android.intent.action.VIEW \
  -d "https://www.example.com/product/abc123" \
  com.example.app
```

custom scheme 은 별도 명령으로 매칭 여부를 확인하되 App Link 검증과 혼동하지 않는다.

### 도메인 검증 확인

```bash
adb shell pm get-app-links com.example.app
adb shell pm verify-app-links --re-verify com.example.app
adb shell dumpsys package com.example.app
```

`pm get-app-links` 결과에서 host 별 검증 상태를 확인한다.

재검증 명령 직후 결과가 즉시 바뀐다고 가정하지 말고 로그와 상태를 함께 본다.

서버 응답은 실제 기기 네트워크에서 HTTPS, 경로, 인증서, JSON 형식을 확인한다.

debug 와 release 인증서 지문이 서로 다른지 배포 변형별로 확인한다.

### 실패 원인 분류

앱이 목록에 나타나지 않으면 매니페스트의 action, category, data 를 먼저 점검한다.

앱 선택기가 나타나면 host 검증 실패나 여러 앱의 경쟁 가능성을 점검한다.

웹으로만 열리면 assetlinks.json 위치, 패키지 이름, 인증서 지문을 점검한다.

앱은 열리지만 잘못된 화면이면 URI 라우터와 path 변수 변환을 점검한다.

로그인 후 목적지가 사라지면 pending destination 저장과 소비 시점을 점검한다.

### 공식 기준

구성 방식은 [App Links 추가](https://developer.android.com/training/app-links/add-applinks) 를 따른다.

서버 파일은 [assetlinks.json 구성](https://developer.android.com/training/app-links/configure-assetlinks) 을 따른다.

동적 규칙의 범위는 [Dynamic App Links는 선언 범위를 확장하지 않는다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/dynamic-app-links-refine-but-do-not-expand-manifest-scope.md) 에서 확인한다.

알림 클릭 흐름은 [알림은 PendingIntent로 딥 링크 여정을 시작한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/notification-deep-link-needs-explicit-task-and-back-stack-policy.md) 와 함께 검증한다.

### 결론

테스트는 "앱이 열리는가"에서 끝나지 않는다.

올바른 앱, 올바른 목적지, 올바른 인증 상태, 예측 가능한 뒤로 가기까지 확인해야 한다.
