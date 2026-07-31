# LMKD (Low Memory Killer Daemon)

상위 노트: [[android-glossary]]

**정의**: 메모리 부족 시 프로세스를 종료하는 데몬

**상세**:

프로세스마다 OOM Adjuster 가 부여한 우선순위를 기반으로 메모리가 부족하면 낮은 우선순위 프로세스부터 종료한다. 커널의 OOM Killer 를 대체한다.

**우선순위**:

```
0    - Foreground (사용자 보는 앱)
100  - Visible
200  - Perceptible (음악 재생)
500  - Service
900+ - Cached (백그라운드)
```

**확인**:

```bash
# 프로세스별 OOM 점수
adb shell cat /proc/$(pidof com.example)/oom_score_adj

# LMKD 로그
adb logcat | grep lmkd
```

**관련**: [[android-kernel]], [[android-activity-manager-and-system-services]]

---

### O
