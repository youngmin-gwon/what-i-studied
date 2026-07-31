# FBE (File-Based Encryption)

상위 노트: [[android-glossary]]

**정의**: 파일별로 다른 키로 암호화하는 방식

**상세**:

전체 디스크 암호화 (FDE) 와 달리 사용자 잠금 상태에 따라 일부 파일은 접근 가능하다. Direct Boot 기능으로 부팅 후 잠금 해제 전에도 알람/전화 수신이 가능하다.

**저장 영역**:

```
/data/user_de/0/com.example/  # Device Encrypted (항상 복호화)
/data/user/0/com.example/     # Credential Encrypted (잠금 시 암호화)
```

**사용**:

```kotlin
// DE Storage
val deContext = context.createDeviceProtectedStorageContext()
val deFile = File(deContext.filesDir, "alarm.txt")

// CE Storage (기본)
val ceFile = File(context.filesDir, "user_data.txt")
```

**관련**: [[android-security-sandbox]]

---

### H
