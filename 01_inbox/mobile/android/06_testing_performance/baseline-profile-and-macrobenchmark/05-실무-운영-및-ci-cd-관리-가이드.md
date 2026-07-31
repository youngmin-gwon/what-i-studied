# 실무 운영 및 CI/CD 관리 가이드

상위 노트: [[baseline-profile-and-macrobenchmark]]

### 5-1. 로컬 기반의 최적화 생성 및 관리 프로세스 (반자동 방식)
수동 기기 설정이나 CI 가상 리소스 제한으로 인해 수동 방식을 많이 활용합니다.

1. **기기 연결**: 루팅된 AOSP 에뮬레이터 또는 API 33+ 실제 디바이스를 연결합니다.
2. **태스크 실행**:
   ```bash
   ./gradlew :app:generateBaselineProfile
   ```
3. **결과 확인**: 플러그인이 빌드 완료 후 자동으로 최적화 지도인 `baseline-prof.txt`를 생성하여 `:app/src/main/baselineProfiles/` 디렉터리에 이식합니다.
4. **버전 관리**: 새로 추출되거나 업데이트된 `baseline-prof.txt` 파일을 **반드시 Git 저장소에 커밋**해야 빌드 파이프라인에서 정상 작동합니다.

### 5-2. CI/CD 가상 파이프라인 자동화 (AOT 가상 구동 방식 - GMD)
물리적인 디바이스가 없는 CI/CD 서버 환경(GitHub Actions, Bitrise 등)에서 Baseline Profile을 자동으로 빌드하려면 **GMD (Gradle Managed Device)** 설정을 이용해 가상 단말을 헤드리스(Headless) 모드로 띄워 캡처해야 합니다.

#### 1) GMD 설정 방식 (`baselineprofile/build.gradle.kts`)
가장 가볍고 백그라운드 노이즈가 없는 **AOSP 이미지**를 기반으로 가상 단말을 선언해 둡니다.

```kotlin
android {
    testOptions {
        managedDevices {
            localDevices {
                create("pixel6Api31") {
                    device = "Pixel 6"
                    apiLevel = 31
                    systemImageSource = "aosp" // 구글 API 서비스가 생략된 가벼운 이미지
                }
            }
        }
    }
}
```

#### 2) CI/CD 환경에서의 자동 생성 설정 (`app/build.gradle.kts`)
기본적으로 빌드 시 매번 테스트를 수행하면 빌드가 매우 느려집니다. 따라서 CI/CD 환경(예: 깃허브 액션, Codemagic, Bitrise 등의 플랫폼이 자동으로 제공하는 `CI` 환경 변수가 `true`인 경우)에서만 자동으로 생성 후 패키징하도록 제어합니다.

```kotlin
baselineProfile {
    // CI/CD 환경(환경 변수 CI=true)에서만 릴리즈 빌드(assembleRelease 등) 시 프로필을 자동 생성하여 포함시킵니다.
    automaticGenerationDuringBuild = System.getenv("CI") == "true"
}
```

#### 3) CI/CD 플랫폼별 실행 명령어 (Fastlane 연동)
Fastlane을 사용하여 Codemagic, Bitrise, Azure Pipelines 등에서 배포 파이프라인을 자동화할 때 사용할 수 있는 명령어 예시입니다.

* **수동/자동 갱신 실행**: GMD를 이용해 가상 단말을 띄우고 Baseline Profile을 생성할 때는 다음과 같이 디바이스 타겟 아규먼트를 주어 실행합니다.
  ```bash
  # pixel6Api31 GMD 단말을 띄워서 백그라운드 생성 실행
  ./gradlew :app:generateBaselineProfile -Pandroid.testInstrumentationRunnerArguments.device=pixel6Api31
  ```
  이때 Gradle은 UI(디스플레이 환경)가 없는 CI 머신임을 감지하고 자동으로 `-no-window`(Headless) 및 `-no-audio` 옵션을 에뮬레이터에 적용하여 무화면 상태로 테스트를 수행한 뒤 자동 종료합니다.

* **Fastlane Lane 연동 예시**:
  ```ruby
  lane :release_build do
    # 1. GMD를 이용해 최신 Baseline Profile 생성 (AOSP 헤드리스)
    gradle(
      task: ":app:generateBaselineProfile",
      properties: {
        "android.testInstrumentationRunnerArguments.device" => "pixel6Api31"
      }
    )
    # 2. 프로필이 빌드본에 심어진 상태로 릴리즈 빌드 및 배포 패키지 생성
    gradle(
      task: "bundle",
      flavor: "Production",
      buildType: "Release"
    )
    # 3. Google Play 배포 실행
    upload_to_play_store(track: 'internal')
  end
  ```

> [!NOTE]
> GMD 헤드리스 에뮬레이션은 내부 중첩 가상화(Nested Virtualization)를 활용하므로, CI 빌드 서버가 가상화 가속 기술(예: KVM, macOS 전용 하드웨어 지원)을 지원하는 성능 좋은 요금제 머신(예: Codemagic/Bitrise의 macOS/Linux premium instance)이어야 원활하게 작동합니다. 성능이 부족한 가상 머신 환경에서는 빌드 시간이 극도로 길어지거나 가상 에뮬레이터 에러로 멈출 수 있으므로 테스트 후 적용하시기 바랍니다.


---
