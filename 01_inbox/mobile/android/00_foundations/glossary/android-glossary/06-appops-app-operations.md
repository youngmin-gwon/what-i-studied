# AppOps (App Operations)

상위 노트: [[android-glossary]]

**정의**: 권한보다 세밀한 앱 동작 제어 시스템

**상세**:

언제, 얼마나 자주 특정 권한을 사용했는지 추적하고 제한할 수 있다. 시스템 내부적으로 사용되며 일부 기기는 설정에서 노출한다.

**예시**:

```bash
# 앱의 AppOps 확인
adb shell appops get com.example.app

# 출력:
# COARSE_LOCATION: allow; time=+2d3h (running)
# CAMERA: allow; time=+5h30m

# 특정 operation 차단
adb shell appops set com.example.app CAMERA deny
```

**관련**: [[android-security-permissions]]

---
