# late-init

대부분의 서비스 시작.

```bash
on late-init
    # 모든 서비스 시작
    trigger early-fs
    trigger fs
    trigger post-fs
    trigger late-fs
    trigger post-fs-data
    
    # Boot animation 시작
    trigger load_persist_props_action
    trigger firmware_mounts_complete
    
    # Main 클래스 시작 (Zygote!)
    trigger early-boot
    trigger boot
```
