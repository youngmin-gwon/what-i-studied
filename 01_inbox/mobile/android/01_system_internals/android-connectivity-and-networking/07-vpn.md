# VPN

상위 노트: [[android-connectivity-and-networking]]

### VpnService

```kotlin
class MyVpnService : VpnService() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val builder = Builder()
            .addAddress("10.0.0.2", 24)
            .addRoute("0.0.0.0", 0)  // 모든 트래픽
            .addDnsServer("8.8.8.8")
            .setSession("MyVPN")
        
        val vpnInterface = builder.establish()
        
        // 패킷 읽기/쓰기
        thread {
            val buffer = ByteBuffer.allocate(32767)
            while (true) {
                val length = vpnInterface.read(buffer)
                // 패킷 처리 (암호화, 터널링 등)
            }
        }
        
        return START_STICKY
    }
}
```

**작동 원리**:

```
앱 → VPN Interface (tun0) → VpnService
VpnService → 암호화 → VPN 서버
VPN 서버 → 인터넷
```

### Always-On VPN

```bash
# 설정
adb shell settings put secure always_on_vpn_app com.example.vpn
adb shell settings put secure always_on_vpn_lockdown 1

# VPN 없으면 네트워크 차단
```

---
