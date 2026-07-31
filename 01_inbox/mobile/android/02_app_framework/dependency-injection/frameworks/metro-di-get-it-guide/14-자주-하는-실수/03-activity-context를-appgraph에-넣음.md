# Activity Context를 AppGraph에 넣음

AppGraph가 앱 전체 수명이라면 Activity Context를 넣으면 안 됩니다.

```kotlin
// 나쁜 예
factory.create(this) // Activity this
```

```kotlin
// 좋은 예
factory.create(applicationContext)
```
