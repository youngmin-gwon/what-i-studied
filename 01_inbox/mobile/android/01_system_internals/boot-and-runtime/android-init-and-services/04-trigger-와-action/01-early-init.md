# early-init

가장 먼저 실행. 파일시스템 마운트, 커널 파라미터 설정.

```bash
on early-init
    # cgroup 마운트
    mount cgroup none /dev/cpuctl cpu
    mount cgroup none /dev/cpuset cpuset
    
    # SELinux 시작
    start ueventd
    
    # 기본 디렉토리
    mkdir /dev/socket 0755 root root
    mkdir /dev/graphics 0775 root graphics
```
