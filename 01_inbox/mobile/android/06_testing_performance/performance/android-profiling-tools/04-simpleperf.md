# Simpleperf

상위 노트: [[android-profiling-tools]]

CPU 프로파일링 (네이티브 코드 포함).

```bash
# 1. 앱 프로파일링
adb shell simpleperf record -p <pid> -o /data/local/tmp/perf.data

# 2. 파일 가져오기
adb pull /data/local/tmp/perf.data

# 3. 리포트 생성
simpleperf report -i perf.data

# 4. 플레임 그래프
simpleperf report -i perf.data --gui
```
