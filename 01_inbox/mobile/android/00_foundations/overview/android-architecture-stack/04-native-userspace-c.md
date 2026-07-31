# 🦾 Native Userspace (C++)

자바 (Java/Kotlin) 프레임워크 아래에는 고성능 C++ 데몬들이 있습니다.

- **SurfaceFlinger**: 모든 앱의 `Surface` 를 받아서 화면에 합성 (Composite) 합니다. iOS 의 Render Server 와 같습니다.
- **AudioFlinger**: 여러 앱의 소리를 섞습니다 (Mixing).
- **Netd**: `iptables` 규칙을 설정하고 네트워크 트래픽을 제어합니다.

---
