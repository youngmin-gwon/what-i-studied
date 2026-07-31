# UID (User ID)

상위 노트: [[android-glossary]]

**정의**: 앱마다 부여되는 고유 번호

**상세**:

Linux UID 시스템을 활용하여 앱을 격리한다. 각 앱은 독립된 UID 를 받아 다른 앱의 파일에 접근할 수 없다. SharedUserID 로 여러 앱이 같은 UID 를 공유할 수도 있다.

**범위**:

```
10000-19999: 일반 앱 (User 0)
20000-29999: 격리 프로세스
1000-9999:   시스템 서비스
```

**확인**:

```bash
# 앱의 UID
adb shell dumpsys package com.example | grep userId

# 출력: userId=10123
```

**파일 권한**:

```bash
adb shell ls -la /data/data/com.example

# drwx------  10  u0_a123  u0_a123  files/
#             (UID만 접근 가능)
```

**관련**: [android-security-sandbox](../05_security_privacy/android-security-sandbox.md)

---

---

### V
