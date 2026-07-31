# action, category, data 매칭은 서로 다른 조건이다

상위 문서: [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
관련 정본: [intent-filter는 컴포넌트의 수신 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-is-component-receiving-contract.md)


## 매칭의 기본

시스템은 암시적 Intent와 후보 컴포넌트의 필터를 비교한다.
세부 규칙은 `action`, `category`, `data` 각각에 적용된다.
하나라도 필요한 조건을 만족하지 못하면 그 필터는 후보에서 제외된다.

## action

Intent의 action은 필터에 선언된 action 중 하나와 일치해야 한다.
필터에 action이 없으면 action이 있는 일반적인 요청을 받을 수 없다.
사용자 정의 action을 쓸 때는 패키지 이름을 포함해 충돌 가능성을 낮춘다.

```xml
<action android:name="com.example.app.action.SHOW_ORDER" />
```

## category

Intent가 가진 모든 category는 필터에도 존재해야 한다.
반대로 필터에 category가 더 있다고 해서 항상 실패하는 것은 아니다.
암시적 액티비티 호출의 기본 조건을 위해 `DEFAULT`를 선언한다.
브라우저나 웹 링크에서 시작될 수 있는 진입점에는 `BROWSABLE`을 사용한다.
런처 진입점은 `MAIN` action과 `LAUNCHER` category 조합으로 표현한다.

## data

data 매칭은 URI와 MIME 타입을 함께 고려한다.
URI는 scheme, host, port, path, pathPrefix, pathPattern으로 좁힐 수 있다.
MIME 타입은 `text/plain`처럼 정확히 쓰거나 `image/*`처럼 범위를 허용한다.
링크 필터의 host를 넓게 잡으면 의도하지 않은 호스트까지 진입점이 될 수 있다.

```xml
<data
    android:scheme="https"
    android:host="example.com"
    android:pathPrefix="/orders" />
```

## 흔한 실패 원인

1. `DEFAULT`가 빠져 일반적인 `startActivity()` 호출이 매칭되지 않는다.
2. Intent의 scheme과 필터의 scheme이 다르다.
3. URI는 맞지만 MIME 타입이 달라 파일 공유가 실패한다.
4. `CATEGORY_BROWSABLE`이 필요한 외부 링크인데 요청 맥락이 맞지 않는다.
5. `<data>`를 여러 개 작성했지만 원하는 조합으로 이해하지 않았다.

## 디버깅 관점

실제 Intent의 action, categories, data, type을 로그로 확인한다.
`resolveActivity()`와 `adb shell am start`로 해석 결과를 분리해 검증한다.
필터를 바꾼 뒤에는 설치된 APK의 병합 Manifest와 기기 설정도 확인한다.
