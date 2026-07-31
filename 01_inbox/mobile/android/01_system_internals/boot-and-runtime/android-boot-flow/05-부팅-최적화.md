# 부팅 최적화

### Bootchart

```bash
# 활성화
adb shell 'touch /data/bootchart/enabled'
adb reboot

# 데이터 수집
adb pull /data/bootchart
```

### Perfetto Trace

```bash
# 부팅 중 trace
adb shell setprop persist.debug.atrace.boottrace 1
adb reboot

# Trace 가져오기
adb pull /data/misc/perfetto-traces/
```

### 최적화 포인트

1. **서비스 지연 시작**: `class late_start`
2. **병렬 실행**: 의존성 없는 서비스 동시 시작
3. **Preload 최소화**: 불필요한 클래스 제거

---
