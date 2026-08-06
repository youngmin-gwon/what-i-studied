---
title: ce-vs-de-storage
tags: ["android", "android/security-privacy"]
aliases: ["CE vs DE 저장소 비교", "Credential Encrypted vs Device Encrypted Storage"]
date modified: 2026-08-06 18:20:00 +09:00
date created: 2026-08-06 18:20:00 +09:00
---

## CE vs DE 저장소 (Credential Encrypted vs Device Encrypted Storage)

Android **FBE(File-Based Encryption)** 환경에서 디바이스 저장소는 **CE(Credential Encrypted)** 저장소와 **DE(Device Encrypted)** 저장소의 두 물리적/암호학적 경계로 구분된다.

### 1. 초보자를 위한 비유와 핵심 개념 (Concept & Analogy)

* 🔐 **CE (Credential Encrypted) 저장소 = 사용자 비밀번호로 잠긴 개인 금고**
  * **원리**: 사용자가 기기 잠금(PIN/패턴/비밀번호)을 해제해야만 커널 메모리에 암호화 키가 로드되어 금고가 열린다.
  * **용도**: 개인 사진, 메시지 DB, 사용자 인증 토큰 등 개인정보와 기밀성이 보장되어야 하는 대부분의 앱 데이터.
* 🔓 **DE (Device Encrypted) 저장소 = 기기 하드웨어가 관리하는 공용 물품 보관함**
  * **원리**: 사용자가 잠금을 해제하지 않아도(전원 켜진 부팅 직후 Direct Boot 상태) 기기 하드웨어 자물쇠로 즉시 열린다.
  * **용도**: 기기가 부팅되었을 때 사용자가 비밀번호를 입력하기 전이라도 울려야 하는 알람, 긴급 전화/통화 서비스 데이터 등 최소한의 실행 데이터.

```mermaid
flowchart TD
    Boot[기기 전원 On / 부팅 완료] --> HWKey[하드웨어 마스터 키 자동 언락]
    HWKey --> DE_Storage["DE 저장소 (/data/user_de/0/)<br/>Direct Boot 상태 접근 가능 (알람, 긴급 서비스)"]
    
    UserUnlock[사용자 PIN/비밀번호 잠금 해제] --> SyntheticPass[Synthetic Password 파생 및 TEE 검증]
    SyntheticPass --> CE_Key[CE 마스터 키 언락 (커널 메모리 로드)]
    CE_Key --> CE_Storage["CE 저장소 (/data/user/0/)<br/>기본 앱 데이터, 개인정보, DB, SharedPreferences"]
```

### 2. 내부 동작 메커니즘 (Internal Mechanism)

1. **암호화 키의 소유권 및 언락 조건 분리**:
   - **CE Key**: 사용자가 입력한 PIN/패스워드 기반의 **Synthetic Password**와 TEE(Trusted Execution Environment) 게이트키퍼에 의해 이중 암호화된다. 첫 잠금 해제 전에는 마스터 키가 존재하지 않아 파일 접근이 불가능하다.
   - **DE Key**: 사용자의 비밀번호와 무관하게 부트로더 및 TEE 하드웨어 Root of Trust 검증 성공 직후 커널 키링(Keyring)에 자동 로드된다.
2. **저장소 파일 경로 및 컨텍스트 격리**:
   - **CE 경로**: `/data/user/0/<package_name>/` (`context.filesDir`로 접근하는 기본 영역)
   - **DE 경로**: `/data/user_de/0/<package_name>/` (`context.createDeviceProtectedStorageContext()`로 접근하는 보호 영역)
3. **가용성(Availability) 및 접근 시점 차이**:
   - **Direct Boot 단계 (User Locked)**: `UserManager.isUserUnlocked`가 `false`이며, 오직 DE 저장소만 읽기/쓰기가 가능하다.
   - **User Unlocked 단계**: `UserManager.isUserUnlocked`가 `true`가 되며 CE 저장소와 DE 저장소 모두 접근 가능하다.

### 3. CE vs DE 저장소 분기 구현 예시 (Kotlin)

```kotlin
import android.content.Context
import android.os.UserManager
import java.io.File

class StorageContextHelper(private val context: Context) {

    /**
     * 현재 사용자 잠금 상태에 따라 적절한 저장소 디렉터리를 반환한다.
     */
    fun getAvailableFilesDir(): File {
        val userManager = context.getSystemService(Context.USER_SERVICE) as UserManager

        return if (userManager.isUserUnlocked) {
            // 사용자 잠금 해제 완료 -> CE 저장소 (기본 앱 데이터 저장소)
            context.filesDir
        } else {
            // Direct Boot 상태 (잠김) -> DE 저장소 (Device Protected Context)
            val deContext = context.createDeviceProtectedStorageContext()
            deContext.filesDir
        }
    }
}
```

### 4. 관찰 가능한 증거 (Observable Evidence)

- **adb 셸을 통한 경로 접근성 확인**:
  - 사용자 잠금 상태에서 CE 경로(`/data/user/0/`) 파일 조회 시: `ENOKEY (Required key not available)` 오류 또는 접근 거부.
  - 전원 부팅 직후 DE 경로(`/data/user_de/0/`) 파일 조회 시: 아무런 제약 없이 정상 접근 가능.
- **Direct Boot 시점에 CE 저장소 접근 시 발생하는 런타임 예외**:
  ```text
  java.lang.IllegalStateException: SharedPreferences in credential encrypted storage are not available until after user is unlocked
      at android.app.ContextImpl.getSharedPreferences(ContextImpl.java:...)
  ```
- **`UserManager.isUserUnlocked` 값 변화**:
  - 부팅 직후(Direct Boot): `false`
  - PIN/패턴 입력 해제 후: `true`

### 5. 판단 기준 및 저장소 경계 (Decision Criteria & Boundary Rules)

- **CE 저장소 선택 기준**: 앱의 99% 일반 데이터(개인정보, DB, 인증 토큰, SharedPreferences, 일반 캐시)는 기밀성이 높은 CE 저장소에 위치해야 한다.
- **DE 저장소 선택 기준**: Direct Boot 모드에서 반드시 작동해야 하는 아침 알람 시각, 푸시 토큰 갱신용 보조 데이터 등 극히 일부의 non-sensitive 데이터에만 제한 사용한다.
- **보안 경계 원칙**: DE 저장소는 기기 부팅만 되면 언제든 접근할 수 있으므로, 복호화 키, PII(개인식별정보), 비밀번호, Access Token 등을 절대로 DE 저장소에 저장해선 안 된다.

상위 문서: [저장소 생명주기와 백업 계약](storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)

관련 노트:
- [FBE에서 CE와 DE를 나누는 저장소 경계](storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
- [Direct Boot에서 허용되는 데이터와 실행 수명](storage-lifecycle-and-backup/direct-boot-requires-minimal-device-protected-data.md)
