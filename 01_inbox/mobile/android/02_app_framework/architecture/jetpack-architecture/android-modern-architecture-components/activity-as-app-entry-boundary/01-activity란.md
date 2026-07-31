# Activity란?

`Activity`는 유저가 눈으로 보고 터치하는 화면을 담당하는 컴포넌트입니다.

전통적인 Android View System 시대에는 화면 하나마다 Activity를 만드는 방식이 흔했습니다.

```plaintext
LoginActivity
MainActivity
ProductListActivity
ProductDetailActivity
SettingsActivity
```

이 구조에서는 화면 이동도 Activity 이동이었습니다.

```kotlin
val intent = Intent(this, ProductDetailActivity::class.java).apply {
    putExtra("productId", 3)
}
startActivity(intent)
```
