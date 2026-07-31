# Captive Portal 감지

상위 노트: [android-connectivity-and-networking](01_inbox/mobile/android/01_system_internals/connectivity/android-connectivity-and-networking.md)

```kotlin
// 커피숍 Wi-Fi 등의 로그인 페이지 감지
val cm = getSystemService(ConnectivityManager::class.java)
val capabilities = cm.getNetworkCapabilities(network)

if (capabilities?.hasCapability(
    NetworkCapabilities.NET_CAPABILITY_CAPTIVE_PORTAL) == true) {
    // Captive portal 존재
    startCaptivePortalApp(network)
}
```

**감지 방법**:

```
1. 연결 후 http://connectivitycheck.gstatic.com/generate_204 접근
2. HTTP 204 응답 예상
3. 302 Redirect 받으면 → Captive Portal
4. 브라우저 팝업
```

---
