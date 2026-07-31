# init

기본 서비스 시작, 파티션 마운트.

```bash
on init
    # /data 마운트
    wait /dev/block/bootdevice/by-name/userdata
    mount_all /vendor/etc/fstab.${ro.hardware} --early
    
    # Property 초기화
    setprop ro.build.version.sdk ${ro.system.build.version.sdk}
    
    # 클래스 시작
    class_start core
```
