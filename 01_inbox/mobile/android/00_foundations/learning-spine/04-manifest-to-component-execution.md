---
title: 04-manifest-to-component-execution
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Manifest to component execution"]
date modified: 2026-08-04 10:10:40 +09:00
date created: 2026-08-03 20:10:00 +09:00
---

## 매니페스트에서 컴포넌트 실행까지

3 장은 소스가 산출물을 거쳐 기기에 등록된 패키지가 되는 과정, 그리고 그 등록이 문자열 식별자·서명·숫자 appId·컴포넌트 registry 라는 여러 축으로 이뤄진다는 사실을 다뤘다. 그러나 그 registry 에 올라간 컴포넌트 중 어떤 것이, 누구의 요청으로, 어느 프로세스에서 실제로 실행되는지는 아직 설명하지 않았다. 이 장은 그 연결을 다룬다.

이 장의 핵심 질문은 다음과 같다.

>매니페스트에 선언된 컴포넌트는 어떻게 시스템이 발견할 수 있는 진입점이 되고, Intent 는 그중 하나를 어떻게 선택하며, 선택된 컴포넌트는 어떤 프로세스 상태 확인을 거쳐 실제로 실행되는가?

이 장은 Intent 필터 문법이나 XML 속성 목록을 처음부터 가르치지 않는다. 개별 속성의 상세 규칙은 각 원자 노트가 다루는 수준으로 남겨두고, 여기서는 선언에서 실행까지 이어지는 인과 흐름과 그 흐름이 끊기는 지점을 설명한다.

### 1. 매니페스트 선언은 컴포넌트를 OS-visible entry point 로 등록한다

3 장에서 본 것처럼 설치 시 PackageManager 는 패키지를 검증하고 UID 를 배정한 뒤, 매니페스트에 선언된 Activity, Service, BroadcastReceiver, ContentProvider 를 컴포넌트 registry 에 등록한다. 이 registry 가 없으면 앱 코드에 클래스가 존재해도 시스템은 그 클래스를 진입점으로 인식하지 못한다.

등록되는 정보는 클래스 이름만이 아니다.

- 어떤 `action`, `category`, `data` 를 받을 수 있는지(`intent-filter`)
- 다른 앱이 직접 호출할 수 있는지(`exported`)
- 호출에 어떤 권한이 필요한지(`permission`)
- ContentProvider 라면 어떤 `authority` 로 URI 를 공개하는지

이 registry 는 런타임에 매번 다시 스캔되는 것이 아니라 설치·업데이트 시점에 갱신되는 시스템 쪽 상태다. 그래서 매니페스트를 수정하고 다시 빌드했는데도 이전 필터가 남아 있다면, 실행 중인 프로세스의 문제가 아니라 설치된 패키지의 등록 상태 자체를 의심해야 한다.

### 2. Intent 는 명시적 또는 암시적 방식으로 컴포넌트를 지정한다

컴포넌트가 registry 에 등록돼 있다는 사실과, 특정 요청이 그 컴포넌트로 연결되는 과정은 다른 문제다. 이를 잇는 것이 Intent 다.

**명시적 Intent**는 패키지와 클래스 이름을 직접 지정한다. 시스템은 후보를 찾을 필요 없이 지정된 컴포넌트가 registry 에 존재하는지만 확인한다.

**암시적 Intent**는 대상을 지정하지 않고 `action`, `category`, `data`(URI/MIME 타입)만 제시한다. 시스템은 설치된 앱들의 registry 를 순회하며 이 세 조건을 모두 만족하는 `intent-filter` 를 찾는다. 하나라도 어긋나면 그 컴포넌트는 후보에서 빠진다. 흔한 실패는 `category.DEFAULT` 가 필터에 없어서 일반적인 `startActivity()` 호출이 아무 후보도 찾지 못하는 경우다.

즉 명시적 Intent 는 "이 컴포넌트를 실행해달라"는 요청이고, 암시적 Intent 는 "이 조건을 만족하는 아무 컴포넌트나 실행해달라"는 위임이다. 후자는 시스템의 registry 조회 없이는 어떤 컴포넌트가 응답할지 요청 시점에 알 수 없다.

### 3. exported 와 permission 은 어느 호출자가 그 진입점에 도달할 수 있는지를 결정한다

registry 에 등록됐고 Intent 가 해석까지 됐다고 해서 호출이 항상 성공하는 것은 아니다. `exported` 는 다른 UID 의 프로세스가 이 컴포넌트를 시작할 수 있는지를 결정하는 별도의 게이트다.

- `exported="false"` 인 컴포넌트를 다른 앱이 명시적 Intent 로 호출하면 시스템은 그 요청을 거부한다. 다만 이 거부가 항상 "권한이 거부됐다"는 신호로 나타나는 것은 아니다. 공식 문서는 Activity 의 경우 이 상황에서 시스템이 `ActivityNotFoundException` 을 던진다고 명시한다. 즉 호출자 입장에서는 컴포넌트가 실제로 registry 에 없을 때와 똑같은 신호를 받으며, 예외 이름만으로는 registry 미등록과 exported 거부를 구분할 수 없다.
- targetSdkVersion 31(Android 12) 이상을 대상으로 하는 앱은 `intent-filter` 가 있는 Activity/Service/Receiver 의 `exported` 값을 반드시 명시적으로 선언해야 한다. 선언하지 않으면 해당 값을 추론해 실행되는 것이 아니라 Android 12 이상 기기에 아예 설치되지 않는다.
- 설치된 다른 앱의 존재나 처리 가능 여부를 사전에 조회하는 것은 호출 자체와는 또 다른 문제다. Android 11 부터는 이런 조회 범위가 `<queries>` 선언으로 제한되며, 선언하지 않은 조회는 그 패키지가 존재하지 않는 것처럼 보이는 실패로 나타난다.

이 절의 요점은 "호출이 실패했다"는 하나의 증상 뒤에 registry 미등록, Intent 해석 실패, exported 거부, package visibility 제한이라는 서로 다른 원인이 있을 수 있다는 것이다.

### 4. 컴포넌트 활성화 요청은 프로세스가 이미 살아 있는지 확인부터 시작한다

registry 조회와 exported 검사를 통과했다고 곧바로 앱 코드가 실행되는 것도 아니다. 이 요청은 앱이 아니라 system_server 의 [ActivityManagerService](../../04_system_services/activity-manager-service.md)([AMS](../../04_system_services/activity-manager-service.md))가 조율한다.

1. [AMS](../../04_system_services/activity-manager-service.md) 는 대상 컴포넌트가 속한 패키지의 프로세스가 이미 실행 중인지 확인한다.
2. 이미 실행 중이면 그 프로세스 안에 컴포넌트 인스턴스를 만들도록 요청한다. 이 경로는 새 프로세스를 만드는 비용이 없다.
3. 실행 중이 아니면(최초 실행이거나, 메모리 부족으로 이미 회수된 cached 프로세스였다면) [AMS](../../04_system_services/activity-manager-service.md) 는 Zygote socket 에 fork 를 요청한다. Zygote 는 새 프로세스를 만들고 UID/GID, 프로세스 이름 같은 specialization 을 마친다.
4. specialization 이 끝난 프로세스는 `ActivityThread.main()` 경로로 framework 에 attach 하고, 그 뒤에야 요청된 컴포넌트가 그 프로세스 안에서 생성된다.

같은 컴포넌트를 실행하는 요청이라도, 대상 프로세스가 foreground/visible 상태로 살아 있었는지 아니면 메모리 압박으로 회수된 cached 상태였는지에 따라 체감 지연이 크게 달라지는 이유가 여기 있다. 프로세스 중요도(foreground → visible → service → cached)는 어떤 프로세스가 먼저 회수될지를 정하는 시스템 쪽 정책일 뿐, 앱이 그 생존을 보장받는다는 뜻은 아니다.

### 5. 하나의 앱은 여러 컴포넌트, 여러 프로세스로 나뉠 수 있다

기본적으로 한 앱의 모든 컴포넌트는 하나의 프로세스에서 실행된다. 하지만 매니페스트의 `android:process` 속성으로 특정 컴포넌트를 다른 이름의 프로세스에서 실행하도록 선언할 수 있다. 이렇게 분리된 프로세스는 각자 독립적인 프로세스 중요도와 생존 주기를 갖는다.

프로세스가 나뉘면 컴포넌트 간 직접적인 인메모리 호출은 더 이상 성립하지 않는다. Activity/Service/Receiver 를 시작하는 통신은 Intent 가, bound service 의 메서드 호출은 Binder 가, ContentProvider 의 데이터 접근은 URI 와 `ContentResolver` 가, 시스템에 위임된 미래 실행은 PendingIntent 가 각각 맡는다. 같은 프로세스 안에서 객체 참조로 되던 통신이 프로세스 경계를 넘으면 이 중 하나의 계약으로 바뀐다는 것이 이 절의 핵심이다.

### 6. 실패 사례: exported=false 컴포넌트를 외부에서 명시적으로 호출한다

다른 앱이 이 앱의 `DetailActivity`(`exported="false"`)를 패키지와 클래스 이름을 지정해 명시적으로 호출한다고 하자.

1. 시스템은 registry 에서 `DetailActivity` 를 정확히 찾는다. 컴포넌트 자체는 존재한다.
2. 시스템은 호출자의 UID 가 이 앱과 다르다는 것을 확인한다.
3. `exported` 가 `false` 이므로 시스템은 이 UID 의 호출을 거부한다. 이 시점에는 아직 대상 프로세스가 실행 중인지 확인하는 단계까지도 가지 않는다.
4. 호출자에게는 `ActivityNotFoundException` 이 던져진다. 이 예외 이름은 "컴포넌트가 없다"는 뜻처럼 보이지만, 실제 원인은 registry 미등록이 아니라 exported 거부다.

이 사례가 보여주는 것은 실패 신호(예외 이름)만으로 원인을 단정하면 안 된다는 것이다. `ActivityNotFoundException` 은 registry 에 정말 없는 경우와 exported 가 막은 경우 모두에서 나타날 수 있으므로, 두 원인을 구분하려면 같은 앱 내부에서 먼저 호출해 registry 존재 여부부터 분리해야 한다. 같은 앱의 컴포넌트끼리, 또는 같은 서명·같은 UID 를 공유하는 컴포넌트끼리 호출하는 경우는 이 게이트의 적용을 받지 않는다. 그래서 "내 앱에서는 되는데 다른 앱에서 호출하면 안 된다"는 증상은 흔히 exported 경계 문제이지 Intent 필터 문제가 아니다.

### 조사 방법: 컴포넌트 실행 실패를 분류한다

1. **registry 에 등록됐는가?** 매니페스트에 선언했는지, 최신 빌드가 실제로 설치됐는지 확인한다.
2. **Intent 가 올바르게 해석되는가?** 명시적 호출이면 대상 클래스명을, 암시적 호출이면 `resolveActivity()` 나 `queryIntentActivities()` 로 실제 후보를 확인한다.
3. **exported/permission 게이트를 통과하는가?** 호출자와 대상이 같은 UID/서명인지, `exported` 값과 필요한 permission 이 무엇인지 확인한다.
4. **package visibility 에 막혔는가?** 대상 패키지나 대상 Intent 가 `<queries>` 에 선언돼 있는지 확인한다.
5. **프로세스가 새로 만들어졌는가, 재사용됐는가?** `dumpsys activity` 나 `adb shell am start` 의 로그로 프로세스 생성 여부와 지연 원인을 구분한다.
6. **실패 로그가 무엇을 가리키는가?** "Permission Denial"(SecurityException 계열)은 대체로 명시적인 권한/exported 거부를 가리키지만, Activity 의 `ActivityNotFoundException` 은 registry 미등록과 exported 거부를 모두 가리킬 수 있어 예외 이름만으로 원인을 확정할 수 없다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| 매니페스트에 선언만 하면 즉시 실행 가능한 진입점이 된다. | 선언은 설치 시점에 registry 로 반영돼야 하고, 실행은 그 registry 조회를 거쳐야 한다. |
| exported 를 명시하지 않으면 필터 유무로 시스템이 알아서 안전하게 판단해준다. | targetSdkVersion 31 이상에서는 intent-filter 가 있는 컴포넌트의 exported 미선언 자체가 설치 실패 사유다. |
| 암시적 Intent 실패는 항상 필터가 없어서다. | `category.DEFAULT` 누락, scheme/MIME 불일치, package visibility 제한도 같은 증상을 만든다. |
| 명시적 Intent 로 호출했으니 대상 앱의 권한 검사는 통과한 것이다. | 컴포넌트를 정확히 찾는 것과 exported/permission 게이트를 통과하는 것은 별개의 단계다. |
| 같은 앱이면 컴포넌트는 항상 같은 프로세스에서 실행된다. | `android:process` 로 특정 컴포넌트를 다른 프로세스에 배치할 수 있고, 그 순간부터 통신은 IPC 계약을 따른다. |
| 프로세스가 이미 존재하면 컴포넌트 실행은 즉시 이뤄진다. | 존재해도 프로세스 중요도에 따라 이미 회수됐을 수 있고, 이 경우 Zygote fork 부터 다시 시작한다. |
| `ActivityNotFoundException` 이 뜨면 그 컴포넌트가 존재하지 않는 것이다. | Activity 의 exported 거부도 같은 예외로 나타나므로, 예외 이름만으로 registry 미등록과 exported 거부를 구분할 수 없다. |

### 확인 질문

1. 매니페스트의 컴포넌트 선언은 설치 이후 어떤 시스템 상태로 반영되는가?
2. 명시적 Intent 와 암시적 Intent 는 컴포넌트를 찾는 방식이 어떻게 다른가?
3. `action`, `category`, `data` 중 하나라도 불일치하면 어떤 결과가 되는가?
4. `exported` 는 어떤 호출자를 막고, 어떤 호출자는 막지 않는가?
5. targetSdkVersion 31 이상에서 `exported` 를 명시하지 않으면 어떤 일이 벌어지는가?
6. package visibility 제한은 Intent 실행과 무엇을 다르게 취급하는가?
7. 대상 프로세스가 이미 실행 중일 때와 회수된 상태일 때, 컴포넌트 실행 경로는 어떻게 달라지는가?
8. 하나의 앱이 여러 프로세스로 나뉘면 컴포넌트 간 통신 수단은 왜 달라지는가?

### 다음 장으로 이어지는 질문

이 장은 등록된 컴포넌트가 Intent 해석과 프로세스 상태 확인을 거쳐 실제로 시작되는 경로를 설명했다. 그러나 시작된 뒤 화면 회전, task 제거, 메모리 회수로 인한 process death 상황에서 그 컴포넌트와 사용자 상태가 어떻게 되는지는 아직 다루지 않았다.

다음 장에서는 task, process, lifecycle 과 사용자 상태가 왜 함께 죽지 않는지를 다룬다.

- configuration change 와 process death 는 컴포넌트에 각각 어떤 재생성을 요구하는가?
- task 제거, 뒤로 가기, force-stop, uninstall 은 각각 어떤 상태를 남기는가?
- 어떤 상태를 저장해야 하고 어떤 상태는 다시 계산해도 되는가?

### 관련 정본

- [AndroidManifest.xml은 OS에 앱의 컴포넌트를 선언한다](../../02_app_framework/navigation/intents-and-deep-links/manifest-component-entry-points.md)
- [AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다](../../02_app_framework/architecture/app-components/manifest-component-declarations.md)
- [안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다](../../02_app_framework/architecture/app-components/components-as-entry-points.md)
- [명시적 Intent와 암시적 Intent를 선택하는 기준](../../02_app_framework/navigation/intents-and-deep-links/explicit-vs-implicit-intents.md)
- [action, category, data 매칭은 서로 다른 조건이다](../../02_app_framework/navigation/intents-and-deep-links/intent-filter-matching-rules.md)
- [exported는 컴포넌트의 외부 호출 경계를 결정한다](../../02_app_framework/navigation/intents-and-deep-links/exported-attribute-security.md)
- [Package visibility는 다른 앱 조회 범위를 제한한다](../../02_app_framework/navigation/intents-and-deep-links/package-visibility-queries.md)
- [컴포넌트 통신은 Intent, Binder, URI, PendingIntent 경계로 나눈다](../../02_app_framework/architecture/app-components/component-communication-boundaries.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](../../01_system_internals/boot-and-runtime/system-server/ams-app-process-lifecycle.md)
- [Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-socket-interface.md)
- [앱 프로세스 특화와 ActivityThread 연결 (Specialization)](../../01_system_internals/boot-and-runtime/zygote-runtime/app-process-specialization.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](../../01_system_internals/boot-and-runtime/system-server/process-priority-oom-score.md)

### 공식 근거

- [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
- [App Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro)
- [`<activity>` exported 속성](https://developer.android.com/guide/topics/manifest/activity-element#exported)
- [Android 12 behavior changes: Safer component exporting](https://developer.android.com/about/versions/12/behavior-changes-12#safer-exporting)
- [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
- [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote)

검증일: 2026-08-03. targetSdkVersion 별 exported 강제 조건과 package visibility 정책은 릴리스에 따라 바뀔 수 있으므로 실제 개발 시점에 다시 확인한다.
