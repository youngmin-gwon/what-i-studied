# ContentProvider란?

`ContentProvider`는 앱의 데이터를 다른 앱이나 시스템이 정해진 URI로 조회/삽입/수정/삭제할 수 있게 열어주는 컴포넌트입니다.

대표적인 예시는 연락처 앱입니다.

```text
content://contacts/people/3
```

이 URI는 웹의 URL처럼 보이지만, 실제로는 안드로이드 기기 내부에서 특정 앱의 데이터 창구를 가리키는 주소입니다.

```kotlin
val cursor = context.contentResolver.query(
    ContactsContract.Contacts.CONTENT_URI,
    null,
    null,
    null,
    null,
)
```
