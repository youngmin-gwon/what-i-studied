# Netd (Network Daemon)

상위 노트: [android-connectivity-and-networking](01_inbox/mobile/android/01_system_internals/connectivity/android-connectivity-and-networking.md)

```bash
# Netd 명령
adb shell cmd netd network list

# Routing table
adb shell ip route

# iptables 규칙
adb shell iptables -L -n -v
```

**Netd 역할**:

- 네트워크 인터페이스 설정
- 라우팅 테이블 관리
- 방화벽 (iptables/nftables)
- DNS 해석
- 대역폭 제어 (tc - traffic control)

---
