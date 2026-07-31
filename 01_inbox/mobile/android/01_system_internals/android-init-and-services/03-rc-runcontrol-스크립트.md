# RC (RunControl) 스크립트

상위 노트: [[android-init-and-services]]

### 문법 구조

**파일 위치**:

```
/system/etc/init/          # AOSP 기본
/vendor/etc/init/          # OEM/칩셋 벤더
/odm/etc/init/             # ODM
/apex/*/etc/init/          # APEX 모듈
```

**기본 문법**:

```bash
# 주석

# 서비스 정의
service <name> <pathname> [ <argument> ]*
    <option>
    <option>
    ...

# 액션 정의
on <trigger> [&& <trigger>]*
    <command>
    <command>
    ...

# Import
import /vendor/etc/init/hw/init.$(ro.hardware).rc
```

### 핵심 예시

**Zygote 시작**:

```bash
# /system/etc/init/zygote64.rc
service zygote /system/bin/app_process64 -Xzygote /system/bin --zygote --start-system-server --socket-name=zygote
    class main
    priority -20
    user root
    group root readproc reserved_disk
    socket zygote stream 660 root system
    socket usap_pool_primary stream 660 root system
    onrestart exec_background - system system -- /system/bin/vdc volume abort_fuse
    onrestart write /sys/power/state on
    onrestart restart audioserver
    onrestart restart cameraserver
    onrestart restart media
    onrestart restart netd
    onrestart restart wificond
    task_profiles ProcessCapacityHigh MaxPerformance
```

**분석**:

- `class main`: 서비스 그룹
- `priority -20`: 최고 우선순위
- `socket zygote stream 660`: Unix 도메인 소켓 생성 (`/dev/socket/zygote`)
- `onrestart`: Zygote 재시작 시 다른 서비스도 재시작 (앱 프로세스 전부 죽기 때문)

---
