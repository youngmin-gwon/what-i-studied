# Property 시스템

상위 노트: [[android-init-and-services]]

### 개요

key-value 저장소로 시스템 전역 상태 공유.

```bash
# 설정
setprop sys.example.key "value"

# 읽기
getprop sys.example.key

# 대기 (값이 설정될 때까지 블록)
wait_for_prop sys.boot_completed 1
```

### Property 네임스페이스

| 접두사 | 설명 | 예시 |
|--------|------|------|
| `ro.*` | 읽기 전용 (부팅 시 1 회만 설정) | `ro.build.version.sdk` |
| `persist.*` | 재부팅 후에도 유지 | `persist.sys.timezone` |
| `sys.*` | 시스템 property | `sys.boot_completed` |
| `ctl.*` | 서비스 제어 (특수) | `ctl.start`, `ctl.stop` |
| `vendor.*` | Vendor partition | `vendor.audio.hal` |

### Property Contexts ([[selinux|SELinux]])

```bash
# /system/etc/selinux/plat_property_contexts
sys.boot_completed  u:object_r:system_boot_completed_prop:s0
persist.sys.        u:object_r:system_prop:s0
vendor.             u:object_r:vendor_prop:s0
```

권한이 없는 프로세스가 property 설정 시도 → 거부:

```bash
# 앱이 시도
setprop sys.boot_completed 0

# 로그
avc: denied { set } for property=sys.boot_completed \
     scontext=u:r:untrusted_app:s0 \
     tcontext=u:object_r:system_boot_completed_prop:s0
```

### 서비스 제어 Property

```bash
# 서비스 시작
setprop ctl.start zygote

# 서비스 정지
setprop ctl.stop zygote

# 서비스 재시작
setprop ctl.restart adbd
```

---
