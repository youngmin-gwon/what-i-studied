# 💡 Why it matters (Context)

- **Launch Speed**: 앱을 켤 때마다 JVM 을 새로 부팅한다면 스마트폰을 쓸 수 없을 것입니다. Zygote 덕분에 우리는 "즉시 실행"을 경험합니다.
- **Memory Sharing**: 수천 개의 앱이 똑같은 `String`, `TextView` 클래스를 씁니다. Zygote 가 없으면 메모리는 순식간에 동납니다.
- **Static Initialization Issues**: `static` 블록에 무거운 코드를 넣으면, 앱 시작 속도뿐만 아니라 **시스템 전체 부팅 속도**를 느리게 할 수 있습니다 (Preload 클래스의 경우).

---
