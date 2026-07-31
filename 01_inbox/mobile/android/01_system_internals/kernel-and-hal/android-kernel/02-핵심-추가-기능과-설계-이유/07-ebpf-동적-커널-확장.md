# eBPF: 동적 커널 확장

상위 노트: [02-핵심-추가-기능과-설계-이유](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel/02-%ED%95%B5%EC%8B%AC-%EC%B6%94%EA%B0%80-%EA%B8%B0%EB%8A%A5%EA%B3%BC-%EC%84%A4%EA%B3%84-%EC%9D%B4%EC%9C%A0.md)

#### 전통적인 방법의 문제

네트워크 트래픽 통계를 수집하거나, 방화벽을 구현하려면 **커널 모듈**이 필요했다. 하지만:

- 커널 재컴파일 및 재부팅.
- 버그가 있으면 커널 패닉.
- 보안 검증 어려움.

#### eBPF 의 등장

**eBPF**(2014 년 리눅스 메인라인, Android 9 부터 활용) 는 "안전한 커널 프로그램"을 삽입할 수 있게 한다.

**검증기 (Verifier)**가 프로그램을 분석해:

- 무한 루프 불가.
- 잘못된 메모리 접근 불가.
- 허용된 헬퍼 함수만 호출.

통과하면 JIT 컴파일되어 커널에서 실행된다.

#### 안드로이드에서의 활용

**네트워크 통계**:

`netd` 데몬이 eBPF 프로그램을 소켓에 부착해, 앱별 트래픽을 추적한다.

```bash
ls /sys/fs/bpf/map_*
# map_netd_app_uid_stats_map
# map_netd_cookie_tag_map
```

**방화벽**:

UID 기반 패킷 필터링. iptables 보다 빠르다.

```c
// eBPF 프로그램 예시
SEC("cgroup/skb")
int bpf_cgroup_skb(struct __sk_buff *skb) {
    __u32 uid = bpf_get_socket_uid(skb);
    if (uid == BLOCKED_UID)
        return 0;  // drop
    return 1;  // accept
}
```

**성능 향상**:

iptables 는 선형 탐색 (O(n)). eBPF 는 해시 맵으로 O(1).

---
