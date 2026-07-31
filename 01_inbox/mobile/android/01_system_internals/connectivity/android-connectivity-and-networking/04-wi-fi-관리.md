# Wi-Fi 관리

상위 노트: [android-connectivity-and-networking](01_inbox/mobile/android/01_system_internals/connectivity/android-connectivity-and-networking.md)

### WifiManager

```kotlin
val wifiManager = getSystemService(WifiManager::class.java)

// Wi-Fi 상태
val isEnabled = wifiManager.isWifiEnabled

// 스캔
wifiManager.startScan()

// 스캔 결과
val results = wifiManager.scanResults
for (result in results) {
    Log.d(TAG, "SSID: ${result.SSID}, Level: ${result.level} dBm")
}
```

### WPA Supplicant

사용자 공간 Wi-Fi 데몬:

```bash
# 설정 파일
/data/misc/wifi/wpa_supplicant.conf

network={
    ssid="MyNetwork"
    psk="password"
    key_mgmt=WPA-PSK
}
```

**연결 과정**:

```
1. WifiManager.connect()
2. WifiService → wpa_supplicant
3. wpa_supplicant → 인증 (WPA2/WPA3)
4. DHCP로 IP 할당
5. ConnectivityService에 알림
```

### Wi-Fi Aware (거리 인식 네트워크)

```kotlin
val wifiAwareManager = getSystemService(WifiAwareManager::class.java)

wifiAwareManager.attach(object : AttachCallback() {
    override fun onAttached(session: WifiAwareSession) {
        val config = PublishConfig.Builder()
            .setServiceName("MyService")
            .build()
        
        session.publish(config, object : DiscoverySessionCallback() {
            override fun onPublishStarted(session: PublishDiscoverySession) {
                // 발행 시작
            }
        }, null)
    }
}, null)
```

---
