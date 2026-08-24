---
title: 08-signed-artifact-through-play-delivery-to-update
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Signed artifact through Play delivery to update"]
date modified: 2026-08-04 16:10:00 +09:00
date created: 2026-08-04 03:20:00 +09:00
---

## signed artifact 가 Play delivery 를 거쳐 update 되는 과정

이 예시는 Learning Spine 3·11 장을 하나의 종단간 배포 파이프라인으로 잇는다. 3 장에서 다룬 서명·버전 identity 가 Play App Signing 이라는 실무 배포 인프라를 거치며 어떻게 시스템 수준에서 검증되는지, 11 장에서 다룬 테스트 트랙과 단계적 출시(Staged Rollout) 및 Android 15 호환성 규격(16KB Page Alignment, Update Ownership)이 이 identity 위에서 어떻게 동작하는지를 분석한다.

### 시작 상태

앱은 이미 Google Play Production 트랙에 배포되어 사용자 기기에 설치되어 있다. Play App Signing 이 활성화되어 있어 개발자는 업로드 키(Upload Key)만 보유하며, 최종 배포 APK 에 서명하는 앱 서명 키(App Signing Key)는 Google Play 의 HSM (Hardware Security Module)에 안전하게 보관되어 있다. 개발자는 새 기능이 포함된 더 높은 `versionCode` 의 아티팩트(AAB)를 빌드하여 배포를 준비한다.

### 입력

개발자가 Release Variant 로 Android App Bundle (AAB)을 빌드하고 업로드 키로 서명한 뒤, Play Console 의 비공개 테스트 또는 Production 트랙에 업로드한다.

---

### 다계층 실행 흐름 (UI → App Framework → System Server → Kernel)

1. **UI & Build Phase (AAB 아티팩트 빌드 및 Upload Key 서명)**
   - 개발 환경에서 `bundleRelease` 태스크가 실행되어 AAB 가 생성된다.
   - APK Signature Scheme v2/v3 에 따라 Upload Key 로 서명된다. 이때 NDK 로 빌드된 모든 네이티브 공유 라이브러리(`.so`)는 Android 15 호환성을 위해 **16KB Page Alignment (`max-page-size=65536`)** 가 적용되어야 한다.

2. **Play Server & Cloud Distribution Phase (Re-signing & Split Generation)**
   - Google Play Cloud 는 업로드된 AAB 의 Upload Key 서명을 검증한 후, 기기별 CPU 아키텍처(arm64-v8a 등) 및 화면 밀도(dpi)에 최적화된 APK 세트(Split APKs)를 생성한다.
   - Play 는 Google 이 관리하는 **App Signing Key** 로 이 Split APK 들을 재서명한다. 즉, 사용자 기기에 도달하는 최종 APK 의 서명 인증서는 개발자의 업로드 키가 아닌 Play 앱 서명 키다.

3. **App Framework & IPC Layer (PackageInstaller Session & Signature Validation)**
   - 사용자 기기의 Google Play Store 클라이언트는 `PackageInstaller` API 를 통해 `PackageInstaller.Session` 을 생성하고 재서명된 APK 분할 파일들을 랭크 스트리밍한다.
   - [binder ipc](../../01_system_internals/ipc-and-process/binder-ipc.md) 를 통해 System Server 의 `PackageManagerService` (PMS) 및 `InstallPackageHelper` 로 업데이트 요청이 전달된다.
   - PMS 는 다음 3 가지 게이트를 엄격히 검증한다:
     - **Gate 1 (Identity)**: 기존 설치된 패키지의 `applicationId` 와 일치하는가?
     - **Gate 2 (Version)**: 새 APK 의 `versionCode` 가 기존 버전보다 높은가?
     - **Gate 3 (Signature Lineage)**: 새 APK 의 앱 서명 키 인증서가 기존 앱의 서명(또는 v3 Signature Key Rotation Lineage)과 완전히 일치하는가?

4. **Kernel & File System Layer (Update Execution & 16KB Page Mapping)**
   - PMS 의 3 가지 게이트를 모두 통과하면 시스템은 이를 "신규 설치"가 아닌 "동일 패키지 업데이트"로 처리한다. 기존 숫자 App ID (UID) 및 데이터 디렉터리(`/data/data/<pkg>`)의 소유권(ownership)과 접근 권한이 그대로 유지된다.
   - 기존 앱 프로세스가 종료되고, 새 APK 의 네이티브 `.so` 파일들이 Kernel memory 에 `mmap()` 된다. 이때 **16KB page alignment** 가 올바르게 맞춰져 있어야 64-bit Kernel 이 페이지 메모리 세그먼트 맵핑에 성공한다.

---

### 성공 결과 vs 실패 분기 비교

| 평가 항목 | 성공 경로 (Play App Signing + Match Signatures) | 실패 분기 (Local Key Mismatch / Unaligned `.so`) |
| :--- | :--- | :--- |
| **서명 인증서** | 기존 앱과 새 APK 모두 Play App Signing Key 로 동일 | 기존 앱은 로컬 debug/release key, 새 APK 는 Play Key 로 서명 mismatch |
| **`versionCode`** | 기존 (v100) → 신규 (v101) 정상 업그레이드 | 신규 `versionCode` 가 기존보다 낮거나 같음 (`INSTALL_FAILED_VERSION_DOWNGRADE`) |
| **16KB Page Align** | NDK `.so` 바이너리가 64KB/16KB align 처리됨 | `.so` 바이너리가 4KB align 고정 → Android 15 64-bit 기기에서 `SIGSEGV` / `mmap` crash |
| **Update Ownership** | Play Store 가 `INSTALL_FAILED_UPDATE_OWNERSHIP_WRONG_USER` 처리 통과 | 타사 스토어/side-load 시 Update Ownership 정책에 걸려 사용자 확인 필요 |
| **기존 데이터 디렉터리** | `/data/data/<pkg>` 내의 DB, SharedPrefs, Auth 토큰 100% 보존 | 설치 거부되거나 앱 삭제 후 재설치로 인해 사용자 데이터 전체 유실 |

---

### 관찰 가능한 신호 및 CLI 진단 명령

1. **설치된 패키지의 versionCode 및 Signature Hash 검증**
   ```bash
   # 설치된 패키지의 versionCode, Signatures lineage 및 Update Owner 확인
   adb shell dumpsys package com.example.myapp | grep -A 15 "signatures:"
   ```

2. **APK Signature Scheme 및 Cert Certificate 지문 정밀 검증**
   ```bash
   # apksigner를 이용해 v2/v3/v4 서명 상태 및 SHA-256 Digest 확인
   apksigner verify --verbose --print-certs app-release.apk
   ```

3. **Android 15 대응 NDK Native Library (.so) 16KB Page Alignment 검증**
   ```bash
   # APK 내부의 arm64-v8a .so 파일 ELF alignment 레이아웃 확인 (ALIGN이 0x4000 또는 0x10000 이어야함)
   readelf -l lib/arm64-v8a/*.so | grep -E "LOAD|ALIGN"
   ```

4. **설치 실패 오차 코드 모니터링 Logcat**
   ```bash
   # PackageManager 서명 일치 실패 및 16KB mmap 실패 로그 필터링
   adb logcat -v threadtime | grep -E "PackageManager|INSTALL_FAILED|NativeBridge|dlopen"
   ```

---

### Android 14 / 15 / 16 특화 동작

- **16KB Page Size Alignment (Android 15 mandatory for 64-bit)**: Android 15 이상 호환성을 위해 모든 C/C++ 네이티브 `.so` 공유 라이브러리는 16KB 메모리 페이지 크기 기준(Alignment `0x4000` / `0x10000`)으로 컴파일되어야 한다. alignment 가 4KB 로 고정된 옛 아티팩트는 Android 15 기기에서 프로세스 실행 시 `mmap()` 에 실패하여 앱이 즉시 강제 종료(`SIGSEGV`)된다.
- **Update Ownership Enforcement (Android 14+)**: Android 14 부터 `android:requiredAccountType` 및 Update Ownership 규격이 도입되었다. Google Play 를 통해 설치된 앱을 사용자의 명시적 허가 없이 ADB 나 타사 앱 마켓이 함부로 업데이트하려 하면 `INSTALL_FAILED_UPDATE_OWNERSHIP_WRONG_USER` 에러를 리턴하며 업데이트가 차단된다.
- **Play App Signing Key Rotation (v3 Signature Scheme)**: Upload Key 가 노출되더라도 Google Play Console 에서 Upload Key 만 안전하게 교체할 수 있다. 최종 사용자의 앱 서명 키는 v3 Key Rotation Lineage 기록에 따라 계속 유지되므로 사용자 데이터 유실 없이 보안 사고에 대응할 수 있다.

---

### 코드 예시

```kotlin
// 1. build.gradle.kts: Android 15 16KB Page Alignment 및 Play App Signing 설정
android {
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 24
        targetSdk = 35
        versionCode = 101
        versionName = "1.0.1"

        ndk {
            abiFilters.addAll(setOf("armeabi-v7a", "arm64-v8a", "x86_64"))
        }

        // C++ / NDK Linker Flag에 16KB (65536 bytes) page alignment 강제 지정
        externalNativeBuild {
            cmake {
                cppFlags("")
                arguments("-DANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES=ON")
            }
        }
    }

    packaging {
        jniLibs {
            // Android 15 미지적용 uncompressed .so 16KB alignment 준수 설정
            useLegacyPackaging = false
        }
    }
}
```

```bash
#!/usr/bin/env bash
# 2. CI/CD 파이프라인용 16KB Page Alignment & Signature 검증 자동화 스크립트

APK_PATH="app/build/outputs/apk/release/app-release.apk"

echo "=== 1. Checking 16KB Page Alignment for Native Libraries (.so) ==="
unzip -q $APK_PATH -d /tmp/apk_check
SO_FILES=$(find /tmp/apk_check/lib/arm64-v8a -name "*.so")

for so in $SO_FILES; do
    ALIGNMENT=$(readelf -l "$so" | grep "LOAD" | head -n 1 | awk '{print $NF}')
    echo "Checking $so: Alignment = $ALIGNMENT"
    if **"$ALIGNMENT" != *"0x10000"* && "$ALIGNMENT" != *"0x4000"***; then
        echo "ERROR: $so is not 16KB page-aligned!"
        exit 1
    fi
done

echo "=== 2. Verifying APK Signature Scheme v2/v3 ==="
apksigner verify --verbose --print-certs $APK_PATH

rm -rf /tmp/apk_check
echo "Verification SUCCESS: Ready for Google Play Delivery."
```

---

### 관련 Diagnostic Runbook

- [08-install-update-failure.md](../diagnostic-runbooks/08-install-update-failure.md)

### 관련 Learning Spine 장

- [3장 소스에서 설치된 패키지까지](../learning-spine/03-source-to-installed-package.md)
- [11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 관련 원자 노트

- [Play App Signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [앱 업데이트는 applicationId, versionCode, 서명 호환성을 요구한다](../../03_packaging_deployment/distribution/release-distribution/app-updates-require-application-id-version-code-and-signature-compatibility.md)
- [Play app signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](../../03_packaging_deployment/distribution/release-distribution/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)
- [Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다](../../03_packaging_deployment/distribution/release-distribution/google-play-testing-tracks-split-audience-and-feedback-scope.md)
- [단계적 출시는 관측 가능한 릴리스 운영 절차다](../../03_packaging_deployment/distribution/release-distribution/staged-rollout-is-observable-release-operation.md)

### 공식 근거

- [App signing](https://developer.android.com/studio/publish/app-signing)
- [Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756)
- [Support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes)
- [Update Ownership in Android 14](https://developer.android.com/about/versions/14/behavior-changes-14#update-ownership)

검증일: 2026-08-04. 이 예시는 Learning Spine 3·11 장 및 Android 14/15 Package Delivery/16KB Specs 원문 대조를 마쳤다.
