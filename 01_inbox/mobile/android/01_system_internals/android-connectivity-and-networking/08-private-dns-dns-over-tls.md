# Private DNS (DNS-over-TLS)

상위 노트: [[android-connectivity-and-networking]]

```bash
# 설정
adb shell settings put global private_dns_mode hostname
adb shell settings put global private_dns_specifier dns.google

# 확인
adb shell getprop net.dns1  # 1.1.1.1 (Cloudflare)
```

**동작**:

```
앱 → getaddrinfo() → netd
netd → DNS-over-TLS (포트 853)
→ dns.google (8.8.8.8)
```

**이점**:

- ISP 가 DNS 쿼리 감청 불가
- DNS 변조 방지

---
