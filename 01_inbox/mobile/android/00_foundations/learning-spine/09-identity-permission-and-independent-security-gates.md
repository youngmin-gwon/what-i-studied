---
title: 09-identity-permission-and-independent-security-gates
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Identity, permission, and independent security gates"]
date modified: 2026-08-04 10:10:45 +09:00
date created: 2026-08-03 23:00:00 +09:00
---

## Identity, 권한과 독립적인 security gate

8 장은 데이터가 어느 owner 에 의해 보존되고 실패 이후 어떻게 복구되는지를 다뤘다. 그러나 그 데이터나 기능에 접근하는 호출 자체가 왜 성공하거나 실패하는지는 아직 다루지 않았다. 권한을 승인받았는데도 호출이 실패하는 경우가 흔한 이유는, 그 호출이 하나의 검사가 아니라 서로 독립적인 여러 gate 를 차례로 지나야 하기 때문이다.

이 장의 핵심 질문은 다음과 같다.

>권한이 있어 보이는데도 호출이 실패하는 이유는 무엇이며, package/서명 identity 와 사용자별 UID 는 어떤 독립적인 gate 들과 연결되는가?

이 장은 개별 permission API 의 요청 절차를 처음부터 가르치지 않는다. 요청 UX 나 특정 권한의 세부 조건은 원자 노트가 다루는 수준으로 남겨두고, 여기서는 3 장의 identity 가 어떻게 여러 독립적인 보안 gate 의 입력이 되는지, 그리고 그 gate 들이 왜 하나의 순차 파이프라인이 아닌지를 연결한다.

### 1. 3 장의 identity 가 이 장의 모든 판정의 출발점이다

3 장은 설치된 패키지가 문자열 식별자(`applicationId`), 서명 인증서, 숫자 appId/UID 라는 서로 다른 축의 identity 를 갖는다는 것을 다뤘다. 이 장에서 다루는 모든 보안 판정은 이 identity, 그중에서도 특히 사용자별 UID 와 서명을 입력으로 삼는다. "이 앱이 어떤 권한을 가졌는가"라는 질문은 실제로는 "이 UID/서명을 가진 프로세스가 무엇을 할 수 있는가"라는 질문이다.

### 2. Sandbox 는 가장 먼저 있는 기본 격리다

Android app sandbox 는 각 앱을 별도 Linux UID 와 프로세스 경계 안에 둔다. 기본 상태에서 앱은 다른 앱의 private data, process memory 에 직접 접근할 수 없다. 앱 간 협력은 직접 접근이 아니라 [binder ipc](../../01_system_internals/binder-ipc.md), Intent, ContentProvider, permission 같은 명시적 경계를 통해서만 일어난다. 이 장에서 다루는 permission, AppOps, SELinux 는 모두 이 기본 격리 위에 쌓이는 추가 gate 이지, sandbox 를 대체하는 것이 아니다.

### 3. Binder 호출은 호출자가 주장한 것이 아니라 커널이 확인한 UID/PID 로 판정된다

6 장은 프로세스 경계를 넘는 호출이 Binder thread pool 에서 처리된다는 것을 다뤘다. 이 장에서 더할 사실은, system_server 의 서비스가 이 호출을 판정할 때 앱이 스스로 주장하는 식별자를 신뢰하지 않는다는 것이다.

1. 앱 프로세스가 Binder 호출을 보낸다.
2. 커널의 Binder driver 가 호출자의 실제 UID/PID 를 요청에 첨부한다. 이 값은 앱이 위조할 수 없다.
3. system_server 서비스는 `checkPermission()` 계열 API 로 이 UID 가 필요한 permission 을 실제로 부여받았는지 다시 질의한다.
4. permission 이 없으면 서비스마다 다른 방식(예외, 빈 값, 조용한 실패)으로 거부한다.

이 검사가 신뢰하는 것은 매니페스트에 적힌 선언이 아니라 커널이 확인한 호출자의 실제 UID 다. 이것이 이 장의 모든 gate 가 공유하는 전제다.

### 4. 매니페스트 선언, protection level, 런타임 승인은 서로 다른 사실이다

권한의 protection level 은 누가 그 권한을 승인하는지를 정한다. 공식 문서는 세 수준을 이렇게 구분한다.

>"These permissions allow access to data and actions that extend beyond your app's sandbox but present very little risk to the user's privacy and the operation of other apps. The system assigns the normal protection level to normal permissions."
>
>"Runtime permissions, also known as dangerous permissions, give your app additional access to restricted data or let your app perform restricted actions that more substantially affect the system and other apps."
>
>"The system grants a signature permission to an app only when the app is signed by the same certificate as the app or the OS that defines the permission."

`normal` 권한은 설치 시 자동으로 허용될 수 있지만, `dangerous` 권한은 사용자가 실행 중에 직접 승인해야 하고, `signature` 권한은 3 장에서 다룬 서명 identity 가 같아야만 승인된다. 즉 매니페스트에 권한을 선언하는 것과 그 권한이 실제로 부여된 상태인 것은 다른 사실이며, 어떤 권한은 사용자 승인으로도 얻을 수 없고 서명 관계로만 얻을 수 있다.

공식 문서는 이 승인 상태를 앱이 함부로 가정하지 말라고도 명시한다.

>"Don't assume that these permissions have been previously granted—check them and, if needed, request them before each access."

### 5. Permission 을 통과해도 AppOps 가 또 한 번 거부할 수 있다

Permission 검사를 통과했다는 사실이 곧 그 동작이 항상 성공한다는 뜻은 아니다. AppOpsManager(AppOps)는 permission 과 별개로 동작하는 실행 시점 정책 계층이다.

각 dangerous permission 은 대응하는 app-op 코드를 가진다(`android.permission.CAMERA` ↔ `OP_CAMERA`). system_server 서비스는 permission 검사를 통과한 뒤 별도로 `noteOp()` 나 `checkOp()` 를 호출해 app-op 모드를 확인한다. 이 모드가 `MODE_IGNORED` 나 `MODE_ERRORED` 면, permission 은 여전히 granted 상태여도 시스템은 요청을 조용히 무시하거나 거부한다.

이 gate 는 사용자의 세부 설정("이 앱 사용 중에만 허용" 같은 위치 옵션), 배터리·개인정보 관리 기능의 자동 개입, OS 의 background 제한에 의해 permission grant 상태와 독립적으로 바뀔 수 있다. 그래서 permission 이 granted 인데 API 가 예외 없이 빈 데이터나 stale 데이터를 반환한다면, permission 보다 AppOps 모드를 먼저 의심해야 한다.

### 6. Special app access 는 이 두 gate 와도 다른 유형이다

다른 앱 위에 그리기, 모든 파일 접근처럼 위험도가 큰 capability 는 일반 runtime permission 다이얼로그로 얻는 권한이 아니다. 이런 capability 는 별도 설정 화면과 사용자 확인을 통해 관리되며, 사용자가 설정에서 언제든 끌 수 있다. 이 gate 는 "요청하면 허용될 수 있는 기능"이 아니라 애초에 이 capability 가 정말 필요한지부터 증명해야 하는 영역이다.

### 7. SELinux 는 이 모든 gate 보다 낮은 층에서 mandatory policy 를 강제한다

지금까지의 gate 는 모두 "이 UID 가 무엇을 할 수 있는가"를 앱과 시스템 서비스 수준에서 판정한다. SELinux 는 이보다 낮은 층에서, Linux UID 기반 권한 위에 mandatory access control 을 추가한다. 프로세스는 domain 을, 파일과 socket 같은 객체는 type 을 가지며, 정책이 허용하지 않는 접근은 root 권한으로도 통과할 수 없다.

이 계층의 역할은 sandbox 가 깨졌을 때 피해 범위를 줄이는 것이다. 앱 프로세스가 취약한 native 경로를 통해 더 높은 권한을 얻더라도, SELinux domain 과 정책은 시스템 파티션, device node, 다른 서비스 접근을 별도로 제한한다. 앱 개발자가 이 정책을 직접 다루는 일은 드물지만, permission denied 나 device 접근 실패를 Linux 파일 권한만으로 판단하면 원인을 놓친다.

### 8. 클라이언트 쪽 검사는 authorization 을 대체하지 않는다

지금까지의 gate 는 모두 기기 안에서 일어난다. 그러나 서버가 최종적으로 신뢰해야 하는 것은 클라이언트의 자기 보고가 아니다. Play Integrity 같은 API 는 기기·앱·계정에 대한 무결성 신호를 제공하지만, 이 신호 자체가 권한을 부여하지 않는다.

>Play Integrity token 은 서버가 Google Play Developer API 로 검증해야 하는 위험 신호이며, 기기가 신뢰 가능해 보인다는 사실이 사용자가 해당 리소스를 볼 권한이 있는지를 대신 증명하지 않는다.

Android 보안 실무의 목적은 클라이언트를 완전히 신뢰하게 만드는 것이 아니라 공격 비용을 높이고 서버 검증 지점을 명확히 하는 것이다. exported component, deep link, ContentProvider, local storage 는 각각 다른 입력 경계를 만들며, 민감한 결정은 클라이언트에서 숨기는 것보다 서버의 권한 검사, replay 방지, idempotency, 감사 로그로 보호해야 한다. 이 원칙은 8 장에서 다룬 서버 반영(동기화)이 왜 idempotency key 같은 서버 쪽 안전장치를 필요로 하는지와도 연결된다.

### 하나의 순차 파이프라인이 아닌 이유

| Gate | 판정 주체 | 판정 시점 | 통과해도 다음 gate 가 별도로 거부할 수 있다 | 실패 시 의심할 층위 |
| --- | --- | --- | --- | --- |
| Sandbox(UID/프로세스 경계) | 커널 | 프로세스 생성 시(4 장) | 명시적 경계(Binder/Intent/ContentProvider) 없이는 애초에 접근 대상이 아니다 | kernel/platform policy |
| Binder 호출자 UID/PID 확인 | 커널 Binder driver + system_server | 매 호출마다 | 위조 불가능한 UID 이지만, 이것만으로 permission 을 증명하지는 않는다 | kernel/platform policy |
| Manifest 선언 / protection level | PackageManager(설치 시), 서명 비교(signature) | 설치·서명 검증 시(3 장) | 선언과 서명이 맞아도 dangerous 권한은 런타임 승인이 별도로 필요하다 | 앱 코드(선언 누락) 또는 framework policy(승인 규칙) |
| Runtime permission grant | 사용자 | 기능 사용 시점 | 승인돼도 AppOps 가 실행 시점에 추가로 거부할 수 있다 | 앱 코드(요청/재확인 누락) |
| AppOps | 시스템 정책, 사용자 세부 설정 | 실제 동작 실행 시점(`noteOp`) | permission 과 독립적으로 모드가 바뀔 수 있다 | framework policy |
| Special app access | 사용자, 설정 화면 | 설정에서 언제든 | runtime permission dialog 로는 얻거나 확인할 수 없다 | framework policy |
| SELinux | 커널 mandatory policy | 모든 접근 시도 | root 권한으로도 우회할 수 없는 별도 계층이다 | kernel/platform policy |
| 서버 authorization | 백엔드 | 요청이 서버에 도달했을 때 | 기기 쪽 신호가 전부 통과해도 서버가 별도로 검증해야 한다 | 앱 코드/framework policy 밖의 영역(서버 쪽 책임) |

마지막 열은 8 장이 예고한 "이 실패가 앱 코드, framework policy, kernel/platform policy 중 어디에 속하는가"라는 질문에 대한 답이다. 같은 "권한 거부"라는 증상도 원인이 앱의 선언·재확인 누락(앱 코드)인지, 시스템이 실행 시점에 적용하는 정책(framework policy)인지, 커널 수준 강제 정책(kernel/platform policy)인지에 따라 수정 위치가 달라진다.

이 표가 보여주는 것은 "권한이 있다"는 하나의 사실이 아니라, 서로 다른 시점에 서로 다른 주체가 독립적으로 내리는 여러 판정이 모두 통과해야 호출이 성공한다는 것이다. 어느 하나가 다른 것을 자동으로 보장하지 않는다.

### Worked example: 카메라 촬영이 실패한다

사용자가 카메라 기능을 눌렀는데 실패한다고 하자. 조사 순서는 이 gate 들을 하나씩 좁혀가는 것이다.

1. 매니페스트에 `CAMERA` 권한이 선언돼 있는가?
2. 런타임에 이 권한이 실제로 granted 상태인가(`dumpsys package` 의 runtime permissions)?
3. 권한이 granted 인데도 실패한다면 AppOps 모드를 확인한다(`dumpsys appops`). 사용자가 설정에서 개별적으로 껐을 수 있다.
4. 이 앱이 foreground 상태나 특정 조건에서만 카메라를 쓸 수 있게 제한돼 있지는 않은가?
5. 여기까지 모두 통과했는데도 실패한다면, SELinux 정책이나 기기별 카메라 서비스 상태(`dumpsys media.camera`)까지 내려가서 본다.

증상은 하나("카메라가 안 열린다")이지만 원인은 이 다섯 층 중 어디에나 있을 수 있다.

### 실패 사례: "권한을 받았으니 항상 가능하다"고 가정한 코드

앱이 위치 권한을 한 번 승인받은 뒤, 이후의 모든 위치 요청 코드에서 권한 확인 없이 API 를 호출한다고 하자. 사용자가 나중에 설정에서 "이 앱 사용 중에만 허용"으로 바꾸거나, 시스템이 오래 사용하지 않은 권한을 자동으로 회수하면, 이 코드는 예외 없이 조용히 실패하거나 stale 데이터를 반환할 수 있다. "권한이 있는가"를 한 번만 확인하고 다시 확인하지 않는 설계는 AppOps 와 권한 자동 회수라는, permission grant 와는 독립적으로 변하는 상태를 놓친다.

### 조사 방법: 실패가 어느 gate 에서 생겼는지 분류한다

1. **매니페스트 선언과 런타임 grant 상태를 분리해서 본다.** 하나만 봐서는 부족하다.
2. **AppOps 모드를 별도로 확인한다.** permission 이 granted 여도 `MODE_IGNORED`/`MODE_ERRORED` 일 수 있다.
3. **호출자 UID 가 기대한 UID 인지 확인한다.** `sharedUserId` 나 다중 프로세스 구성에서는 이 구분이 특히 중요하다.
4. **서버 응답이 클라이언트 신호만으로 결정되지 않았는지 확인한다.** 서버 로그에서 실제 authorization 판단 근거를 본다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| 매니페스트에 권한을 선언하면 그 권한을 가진 것이다. | dangerous 권한은 런타임 승인이, signature 권한은 서명 일치가 별도로 필요하다. |
| 권한이 granted 면 해당 동작은 항상 성공한다. | AppOps 가 permission 과 독립적으로 실행 시점에 동작을 거부할 수 있다. |
| root 권한을 얻으면 모든 시스템 자원에 접근할 수 있다. | SELinux mandatory policy 는 root 권한으로도 우회할 수 없는 별도 계층이다. |
| 클라이언트의 무결성 검사를 통과하면 서버가 그 요청을 신뢰해도 된다. | Play Integrity 같은 신호는 서버가 검증해야 하는 위험 신호일 뿐 authorization 을 대체하지 않는다. |
| 한 번 권한을 확인했으면 이후 호출에서는 다시 확인할 필요가 없다. | 사용자가 설정에서 회수하거나 시스템이 자동으로 회수할 수 있으므로 매 접근 전 확인이 권장된다. |
| Binder 호출에서 앱이 자신의 identity 를 주장하면 시스템이 그것을 그대로 받아들인다. | system_server 는 커널이 확인한 실제 UID/PID 로 판정하며 앱의 자기 신고를 신뢰하지 않는다. |

### 확인 질문

1. 3 장의 package/서명 identity 와 UID 는 이 장의 어떤 판정들의 입력이 되는가?
2. Sandbox, permission, AppOps, SELinux 는 각각 무엇을 격리하거나 판정하는가?
3. Binder 호출에서 시스템이 신뢰하는 것은 앱의 어떤 값인가?
4. normal, dangerous, signature protection level 은 각각 누가 승인 주체인가?
5. AppOps 가 permission 과 독립적인 gate 라는 것은 실무에서 어떤 규칙으로 이어지는가?
6. SELinux 가 "root 권한으로도 우회할 수 없다"는 것은 어떤 시나리오에서 의미가 있는가?
7. 클라이언트 무결성 신호와 서버 authorization 은 왜 같은 것으로 취급하면 안 되는가?
8. 카메라 촬영 실패 사례에서 다섯 개의 gate 중 어디가 원인인지 어떻게 좁혀 가는가?

### 다음 장으로 이어지는 질문

이 장은 identity 가 왜 서로 독립적인 여러 security gate 의 입력이 되는지를 다뤘다. 그러나 앱이 기기 기능이나 지속 작업이 필요할 때 이를 어떤 시스템 계약으로 발견하고 사용하는지는 아직 다루지 않았다.

다음 장에서는 기능 발견에서 manager/service 호출, 필요하면 하드웨어까지 이어지는 경로와, 그 경로마다 이 장에서 다룬 gate 들이 어떻게 다르게 조합되는지를 다룬다.

- 앱은 기기가 특정 capability 를 지원하는지 어떻게 미리 확인하는가?
- 같은 capability 라도 AOSP platform, Google 서비스, OEM 구현에 따라 경로가 왜 달라지는가?
- capability 가 없거나 거부됐을 때 앱은 어느 단계에서 이를 발견하고 대체해야 하는가?

### 관련 정본

- [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](../../05_security_privacy/platform-hardening/platform-security/android-app-sandbox-is-uid-and-process-boundary.md)
- [system_server의 서비스는 호출자 UID/PID로 권한을 검사한다](../../04_system_services/service-lookup/service-lookup/system-server-uid-pid-check.md)
- [Permission protection level은 접근 승인 주체를 정의한다](../../05_security_privacy/permissions-and-sandbox/permissions/permission-protection-level-defines-who-can-grant-access.md)
- [Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다](../../05_security_privacy/permissions-and-sandbox/permissions/runtime-permission-is-user-mediated-access.md)
- [AppOps는 권한 이후의 민감 작업 실행 상태를 관찰하고 제어한다](../../05_security_privacy/permissions-and-sandbox/permissions/appops-observes-and-gates-sensitive-operations-after-permission.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup/appops-permission-denial.md)
- [Special app access는 일반 runtime permission이 아니라 설정 기반 capability다](../../05_security_privacy/permissions-and-sandbox/permissions/special-app-access-is-settings-mediated-capability.md)
- [권한 디버깅은 manifest, grant state, AppOps를 분리해 확인한다](../../05_security_privacy/permissions-and-sandbox/permissions/permission-debugging-separates-manifest-grant-and-appops-state.md)
- [SELinux는 Linux 사용자 권한을 넘어 mandatory policy를 강제한다](../../05_security_privacy/platform-hardening/platform-security/selinux-enforces-mandatory-policy-beyond-linux-user-permissions.md)
- [Play Integrity token은 서버가 검증하는 위험 신호이지 권한 자체가 아니다](../../05_security_privacy/integrity-and-attestation/integrity/play-integrity-token-is-server-verified-risk-signal-not-authorization.md)
- [Android 보안 실무는 클라이언트 신뢰가 아니라 방어 계층 설계다](../../05_security_privacy/security-practices/security-practice/android-security-practice-is-defense-in-depth-not-client-trust.md)
- [Context.getSystemService()](../../04_system_services/get-system-service.md)

### 공식 근거

- [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview)
- [Request runtime permissions](https://developer.android.com/training/permissions/requesting)
- [Play Integrity API overview](https://developer.android.com/google/play/integrity/overview)

검증일: 2026-08-03. AppOps 의 개별 op 코드, 자동 회수 조건, SELinux 정책 세부는 Android 버전과 기기 구현에 따라 달라지므로 실제 적용 시점에 다시 확인한다.
