# Bugreport

상위 노트: [[android-glossary]]

**정의**: 기기 상태를 종합적으로 담은 로그 묶음

**상세**:

시스템 로그, 커널 로그, dumpsys 출력, 메모리 상태, 네트워크 상태 등 모든 디버깅 정보를 zip 파일로 압축한다. 버그 리포트 시 첨부하는 필수 자료다.

**생성**:

```bash
# 버그리포트 생성
adb bugreport bugreport.zip

# 또는 기기에서
# Settings → About Phone → 빌드 번호 7번 탭
# Developer Options → Take Bug Report
```

**포함 내용**:

- logcat 전체
- dmesg (커널 로그)
- dumpsys 모든 서비스
- /proc, /sys 정보
- ANR traces

**관련**: [android-debugging-techniques](../06_testing_performance/android-debugging-techniques.md)

---

---

### C
