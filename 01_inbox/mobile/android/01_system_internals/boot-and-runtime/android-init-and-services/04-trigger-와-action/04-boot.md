# boot

앱 시작 준비 완료.

```bash
on boot
    # 서비스 클래스 시작
    class_start main
    class_start late_start
    
    # 부팅 완료 property
    setprop sys.boot_completed 1
```

### Property 트리거

Property 값 변화에 반응:

```bash
# 사용자 잠금 해제 시
on property:vold.decrypt=trigger_restart_framework
    class_start main
    class_start late_start

# USB 연결 시
on property:sys.usb.config=mtp,adb
    start adbd
```

---
