# Perfetto

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 시스템 전체 성능을 추적하는 도구

**상세**:

CPU, 메모리, 디스크, 네트워크, 프레임 렌더링 등을 시간 순서대로 기록한다. Systrace 의 후속으로 더 많은 정보와 분석 기능을 제공한다.

**수집**:

```bash
# 10초 trace
adb shell perfetto \
  -c - --txt \
  -o /data/local/tmp/trace <<EOF
buffers: {
    size_kb: 65536
}
data_sources: {
    config {
        name: "linux.ftrace"
    }
}
duration_ms: 10000
EOF

# trace 가져오기
adb pull /data/local/tmp/trace trace.perfetto-trace

# 분석: https://ui.perfetto.dev/
```

**관련**: [android-profiling-tools](01_inbox/mobile/android/06_testing_performance/performance/android-profiling-tools.md), [android-performance-and-debug](01_inbox/mobile/android/06_testing_performance/performance/android-performance-and-debug.md)

---

### S
