# Battery Historian

상위 노트: [[android-profiling-tools]]

배터리 사용 분석.

```bash
# 1. 배터리 통계 초기화
adb shell dumpsys batterystats --reset

# 2. 앱 사용

# 3. 통계 수집
adb bugreport bugreport.zip

# 4. Battery Historian 실행
docker run -p 9999:9999 gcr.io/android-battery-historian/stable:3.1 --port 9999

# 5. http://localhost:9999 에서 bugreport.zip 업로드
```
