# Android 현대화는 privacy, updatability, adaptive form factor 쪽으로 이동했다

Android의 큰 변화는 단순한 UI feature 추가보다 platform constraint 강화에 가깝다. Background execution, permission, package visibility, scoped storage, notification permission, intent hardening은 앱이 system resource와 사용자 데이터를 다루는 방식을 바꿨다.

동시에 Mainline, APEX, SDK Extensions, Treble, GKI는 업데이트와 호환성 경계를 더 잘게 나눴다. Large screen, desktop windowing, XR 같은 form factor 변화는 layout/navigation을 고정 phone screen에서 adaptive model로 옮기고 있다.

history 문서는 이 흐름을 설명하고 세부 구현은 각 canonical map으로 넘긴다.

관련 정본: [platform modularity](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md), [large screen](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md), [XR](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/android-security-practices.md).
