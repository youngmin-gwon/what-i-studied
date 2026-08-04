---
title: private-dns-encrypts-dns-but-does-not-replace-app-tls-validation
tags: [android, android/connectivity, android/security, android/dns]
aliases: [Private DNS, DoT, DNS-over-TLS, DnsResolver]
date modified: 2026-08-04 15:50:00 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Private DNS는 DNS를 암호화하지만 앱 TLS 검증을 대체하지 않는다

상위 문서: [Connectivity contracts](connectivity-contracts.md)

Android 9(API 28)부터 도입된 **Private DNS (DNS-over-TLS: DoT)**는 시스템 네이티브 해결사(`netd resolv`)가 DNS 쿼리를 전송할 때 포트 853을 통해 쿼리를 암호화함으로써 ISP나 중간 감청자의 DNS 스누핑과 DNS Spoofing을 방지한다. 하지만 이는 **도메인 IP 주소 조회 통로의 암호화일 뿐이며, 애플리케이션의 HTTPS TLS 핸드셰이크 및 서버 인증서 신뢰 검증(Certificate Pinning)을 대체하지 못한다.**

### 메커니즘: Private DNS(netd)와 앱 TLS(Conscrypt) 계층 분리

1. **DNS Lookup Phase (Private DNS / netd)**:
   - 앱이 `dns.resolve("api.example.com")`를 시도하면, `netd` 내의 `DnsResolver`가 설정된 Private DNS Provider(예: `dns.google`, `one.one.one.one`)로 TLS 연결(Port 853)을 통해 IP 주소를 비공개 조회한다.

2. **HTTP Application Connection Phase (App / TLS Handshake)**:
   - 반환받은 IP 주소로 소켓을 연 후, 앱의 TLS 엔진(Conscrypt / OkHttp)은 서버의 X.509 인증서 서명 체인과 SNI 도메인을 직접 검증한다.
   - Private DNS가 유효하더라도 서버 인증서가 만료되었거나 위조된 경우 TLS 핸드셰이크는 실패한다.

```mermaid
graph TD
    App[App Network Engine: OkHttp] -->|1. getByName("api.example.com")| NetdDNS[netd DnsResolver]
    
    subgraph Private DNS Layer (Port 853)
        NetdDNS -->|Encrypted DoT Query| PrivateDNSServer[Private DNS Server: dns.google]
        PrivateDNSServer -->>NetdDNS: IP: 93.184.216.34 (Encrypted Result)
    end

    NetdDNS -->>App: IP Address Returned

    subgraph Application TLS Layer (Port 443)
        App -->|2. TCP Connect & TLS Handshake| WebServer[Target Web Server]
        App -->|3. Certificate Chain & Pinning Check| TrustManager[Conscrypt TrustManager]
        TrustManager -->>App: Valid TLS Session Established
    end
```

### Kotlin DnsResolver API 직접 사용 및 Private DNS 상태 확인

```kotlin
import android.net.DnsResolver
import android.net.Network
import android.os.CancellationSignal
import java.net.InetAddress
import java.util.concurrent.Executor

fun resolveDomainWithPrivateDns(
    network: Network,
    domain: String,
    executor: Executor,
    onResolved: (List<InetAddress>) -> Unit
) {
    val resolver = DnsResolver.getInstance()
    val cancellationSignal = CancellationSignal()

    // system_server 및 netd Private DNS 설정이 적용된 DnsResolver 사용
    resolver.query(
        network,
        domain,
        DnsResolver.FLAG_EMPTY,
        executor,
        cancellationSignal,
        object : DnsResolver.Callback<List<InetAddress>> {
            override fun onAnswer(answer: List<InetAddress>, rcode: Int) {
                if (rcode == 0) {
                    onResolved(answer)
                }
            }

            override fun onError(error: DnsResolver.DnsException) {
                // Private DNS 서버 연결 불가 또는 strict mode 검증 실패 시 발생
            }
        }
    )
}
```

### 관찰 신호: dumpsys dnsresolver Private DNS 상태 확인

```bash
# netd dnsresolver의 Private DNS (Strict Mode vs Opportunistic Mode) 덤프
adb shell dumpsys dnsresolver

# 주요 관찰 사항:
# - Private DNS mode: STRICT (specific provider) vs AUTOMATIC
# - Server validation status: SUCCESS (TLS port 853 handshake OK)
# - DnsQueryLog: 암호화된 DNS 쿼리 처리 통계
```

### 관련 문서

- [Network Security Config는 앱 신뢰, cleartext, pinning 정책을 선언한다](network-security-config-declares-app-trust-cleartext-and-pinning-policy.md)
- [netd는 라우팅, DNS, 방화벽, tethering 명령을 실행한다](netd-enforces-routing-dns-firewall-and-tethering-operations.md)

공식 문서: [Android Private DNS Features](https://developer.android.com/about/versions/pie/android-9.0-changes-28#private-dns)
