---
title: appops-and-permissions
tags:
  - android
  - security
  - permissions
  - appops
---

# 안드로이드 권한 시스템 & AppOps (AppOps and Permissions)

안드로이드 운영체제는 앱이 사용자의 민감한 데이터(위치, 연락처, 카메라 등)나 기기 기능(마이크, 센서 등)에 무단으로 접근하는 것을 방지하기 위해 다중 계층 보안 모델을 적용합니다. 이 모델의 핵심 프레임워크가 바로 **권한 시스템(Permission System)**과 **AppOps(Application Operations)**입니다.

---

## 1. 안드로이드 권한 시스템 (Permission System) 개요

안드로이드 권한 시스템은 앱이 실행될 때 특정 리소스나 시스템 API에 접근할 수 있는지 여부를 결정하는 1차 관문입니다. 앱 개발자는 `AndroidManifest.xml`에 필요한 권한을 선언하고, 안드로이드 OS는 이 선언과 사용자의 동의를 바탕으로 접근을 허용하거나 차단합니다.

---

## 2. 런타임 권한 (Runtime Permissions) vs 설치 시점 권한 (Install-time Permissions)

안드로이드 권한은 보호 수준(Protection Level)과 승인 시점에 따라 크게 **설치 시점 권한**과 **런타임 권한**으로 나뉩니다.

### 2.1 설치 시점 권한 (Install-time Permissions)
앱을 구글 플레이 스토어 등에서 설치할 때 자동으로 부여되는 권한입니다.
* **일반 권한 (Normal Permissions)**
  * 앱 외부 데이터나 사용자 개인정보에 위험을 주지 않는 일반적인 권한입니다.
  * 예: 인터넷 접근 (`INTERNET`), 네트워크 상태 확인 (`ACCESS_NETWORK_STATE`), 알람 설정 (`SET_ALARM`).
  * 사용자에게 별도의 팝업을 띄우지 않고 설치 완료 시 자동 승인됩니다.
* **서명 권한 (Signature Permissions)**
  * 동일한 인증서 서명키로 서명된 앱들 사이에서만 공유할 수 있는 특수 권한입니다.
  * 시스템 앱이나 개발사의 다른 앱과 데이터/기능을 안전하게 공유할 때 사용됩니다.

### 2.2 런타임 권한 (Runtime Permissions / Dangerous Permissions)
Android 6.0(API 레벨 23, Marshmallow)부터 도입된 모드로, 사용자의 개인정보나 기기 제어에 직접적인 영향을 주는 **위험 권한(Dangerous Permissions)**이 이에 해당합니다.
* **대상 권한**: 위치 정보(`ACCESS_FINE_LOCATION`), 카메라(`CAMERA`), 마이크(`RECORD_AUDIO`), 연락처(`READ_CONTACTS`) 등.
* **작동 방식**: 앱 설치 시점이 아니라, **해당 기능이 실제로 필요한 시점(Runtime)**에 사용자에게 권한 요청 대화상자(Dialog)를 띄워 직접 동의를 받습니다.
* **권한 철회**: 사용자는 설정 앱에서 언제든지 이미 부여한 런타임 권한을 취소할 수 있습니다.

---

## 3. AppOps (Application Operations): 세밀한 접근 제어

### 3.1 AppOps란 무엇인가?
**AppOps(Application Operations)**는 Android 4.3부터 도입된 내부 트래킹 및 세밀한 접근 제어(Fine-grained Access Control) 메커니즘입니다.

* 권한 시스템이 "앱이 이 API를 호출할 수 있는가?"라는 **이분법적 여부**를 판단한다면, AppOps는 **실제 런타임 동작 시점에서 해당 작업을 허용할지, 거부할지, 혹은 추적/기록할지**를 제어합니다.
* 예를 들어, 사용자가 카메라 권한은 허용했지만 시스템 설정이나 보안 정책에 의해 백그라운드 상태에서의 카메라 접근이 차단된 경우, 권한 자체는 켜져 있어도 AppOps 단계에서 거부될 수 있습니다.

### 3.2 AppOps의 핵심 기능
1. **세밀한 모니터링 (Tracking & Auditing)**: 앱이 마이크, 카메라, 위치 등을 언제 마지막으로 사용했는지 타임스탬프와 횟수를 추적합니다. (상단 바의 녹색 점 indicator 등이 AppOps 트래킹 기반으로 구현됨)
2. **조건부 차단 (Fine-grained Control)**: 포그라운드/백그라운드 상태 구분 차단, 묵시적 거부(Silent Ignore - 에러를 발생시키지 않고 빈 데이터 반환) 등의 정교한 제어를 수행합니다.
3. **AppOpsManager**: 프레임워크 수준에서 `AppOpsManager` 서비스 API를 통해 각 앱의 Operation 상태(`MODE_ALLOWED`, `MODE_IGNORED`, `MODE_ERRORED` 등)를 검사하고 관리합니다.

---

## 4. SecurityException 메커니즘

앱이 적절한 권한을 얻지 못한 상태에서 보호된 API(예: `LocationManager.getLastKnownLocation()`, `Camera.open()`)를 호출하면, 안드로이드 프레임워크는 작업을 거부하고 예외를 던집니다.

### 4.1 발생 및 검증 흐름
1. **API 호출**: 앱이 프레임워크 API를 호출합니다.
2. **권한 검증 (`checkCallingPermission`)**:
   * 시스템 서비스(예: `LocationManagerService`)는 IPC 요청을 수신할 때 Binder 통신을 통해 호출한 앱의 UID와 PID를 확인합니다.
   * `Context.checkCallingPermission()` 또는 `AppOpsManager.noteOp()` 메서드를 호출하여 권한 및 AppOps 상태를 검증합니다.
3. **`SecurityException` 던짐**:
   * 권한이 없거나 거부된 경우, 시스템 서비스는 `SecurityException`을 발생시켜 Binder 응답으로 앱 프로세스에 전달합니다.
4. **앱 크래시 또는 예외 처리**:
   * 앱이 `try-catch` 블록으로 `SecurityException`을 처리하지 않았다면 앱이 강제 종료(Crash)됩니다.

---

## 5. 연관 문서 및 참고

* [안드로이드 시스템 서비스 (system-server)](../04_system_services/system-server.md)
