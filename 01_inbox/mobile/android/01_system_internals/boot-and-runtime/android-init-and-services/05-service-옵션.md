# Service 옵션

상위 노트: [[android-init-and-services]]

### 기본 옵션

```bash
service <name> <executable>
    class <class_name>      # 서비스 그룹 (core, main, late_start)
    user <username>         # UID
    group <groupname>       # GID
    seclabel <context>      # SELinux 컨텍스트
    capabilities <caps>     # Linux capabilities
    priority <priority>     # 스케줄링 우선순위
    ioprio <class> <level>  # I/O 우선순위
```

### 재시작 정책

```bash
service example /system/bin/example
    # 한 번만 실행
    oneshot
    
    # 비활성화 (수동 시작만)
    disabled
    
    # 크래시 시 재시작
    restart_period 5  # 5초 타임아웃
    
    # 재시작 시 액션
    onrestart restart dependent-service
    onrestart exec -- /system/bin/cleanup.sh
```

### 리소스 제한

```bash
service memory-intensive /system/bin/service
    # OOM 점수 (낮을수록 보호)
    oom_score_adjust -900
    
    # cgroup 설정
    writepid /dev/cpuset/system-background/tasks
    
    # 파일 디스크립터 제한
    rlimit RLIM_NOFILE 8192 8192
```

---
