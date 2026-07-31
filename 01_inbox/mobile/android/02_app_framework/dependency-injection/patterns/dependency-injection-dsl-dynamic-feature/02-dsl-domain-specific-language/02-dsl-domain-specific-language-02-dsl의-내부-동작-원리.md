# DSL의 내부 동작 원리

코틀린 DSL이 작동하는 배후에는 **2가지 핵심 치트키**가 있습니다:

#### ① 수신 객체 지정 람다 (Lambda with Receiver)

```kotlin
// 일반적인 스타일 (지저분함)
fun buildUser(user: User) {
    user.name = "Youngmin"
    user.age = 31
}

// DSL 스타일 (수신 객체 지정 람다)
fun user(block: User.() -> Unit): User {
    val user = User()
    user.block()
    return user
}

// 사용하는 쪽: 마치 전용 미니 언어처럼 사용
val myUser = user {
    name = "Youngmin"  // this.name에서 this가 생략됨!
    age = 31
}
```

#### ② 스코프 제한자 (`@DslMarker`)

중첩 DSL에서 자식 블록이 부모의 엉뚱한 변수를 건드리지 못하도록 **컴파일러가 감시하는 제약 조건**.
