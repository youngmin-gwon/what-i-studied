# R8 컴파일러 & 코드 최적화(Code Shrinking) 가이드

이 문서는 Android 앱 패키지(APK/AAB) 용량을 줄이고 실행 성능 및 보안을 극대화하기 위해 **R8 컴파일러(ProGuard 기술 기반)**를 활용하는 가이드와 프로젝트 내 코드 수축/최적화 규칙을 정리합니다.

본 문서는 Google의 R8 Optimization 가이드 세션 및 최신 AGP (Android Gradle Plugin) 릴리즈 기준을 반영하여 작성되었습니다.

---

## 1. R8 컴파일러의 5대 핵심 기능

R8은 코틀린/자바 바이트코드를 Android DEX 바이트코드로 변환하는 과정에서 다음과 같은 최적화를 수행합니다.

### 1-1. Tree Shaking (코드 수축, Code Shrinking)
* 앱의 진입점(예: `AndroidManifest.xml`에 등록된 Component)을 시작점으로 그래프를 탐색하여 **호출되지 않는 모든 코드, 클래스, 필드, 메서드를 추적해 바이너리에서 삭제**합니다.
* 사용하지 않는 라이브러리/SDK 내부의 불필요한 클래스들이 이때 대거 제거됩니다.

### 1-2. Resource Shrinking (리소스 수축 & Precise Mode)
* `isShrinkResources = true` 옵션과 연동하여, 코드에서 참조되지 않는 `res/` 폴더 내의 미사용 이미지, XML, 레이아웃 리소스를 제거하거나 0바이트 껍데기로 대체합니다.
* 문자열 식별자(`resources.getIdentifier()`)로 동적 참조되는 리소스도 정적 코드 파싱을 거쳐 정밀하게 도려냅니다.

### 1-3. Optimization (코드 최적화)
* **Inlining (함수 인라이닝)**: 호출 오버헤드가 있는 짧은 함수들을 호출부에 직접 삽입하여 스택 프레임 생성 오버헤드를 줄입니다.
* **Class Merging (클래스 병합)**: 사용성이 적은 인터페이스 구현체나 상속 구조 클래스를 하나로 합쳐 DEX 클래스 개수를 줄입니다.
* **Dead Code Elimination (사행 코드 제거)**: 실행될 수 없는 `if(false)` 조건절이나 사용되지 않는 변수 할당을 제거합니다.
* **Constant Folding (상수 사전 계산)**: 컴파일 타임에 결정되는 상수 연산식을 미리 계산 결과로 치환합니다.

### 1-4. Obfuscation (난독화 & 이름 축소)
* 클래스명, 메서드명, 변수명을 `a`, `b`, `c`와 같이 1자 형태의 짧은 문자열로 변경합니다.
* 앱 용량을 대폭 감소시킴과 동시에 디컴파일러를 통한 reverse engineering을 어렵게 만들어 앱 보안을 강화합니다.

### 1-5. Kotlin Metadata 스트리핑 (Kotlin Metadata Optimization)
* 코틀린 컴파일러는 디버깅 및 Reflection을 위해 클래스 파일마다 `@Metadata` 어노테이션을 부착합니다.
* R8은 릴리즈 빌드 시 Reflection에 사용되지 않는 불필요한 코틀린 메타데이터 스트링 파라미터를 도려내어 DEX 용량을 추가로 절감합니다.

---

## 2. R8 Full Mode vs Compatibility Mode

R8은 ProGuard와의 하위 호환성을 유지하는 **Compatibility Mode**와 더 적극적이고 강하게 최적화를 적용하는 **Full Mode**를 지원합니다.

* **Full Mode (`android.enableR8.fullMode=true`)**:
  * 최신 AGP 환경에서는 기본적으로 **Full Mode가 활성화**되어 있습니다.
  * 계층 구조 최적화 및 인라이닝이 훨씬 강력하게 동작하지만, **Reflection(반사 API)**이나 디시리얼라이제이션(JSON 변환)을 사용하는 코드에서 명시적인 규칙(`-keep`)이 없으면 런타임에 에러가 발생할 수 있습니다.

---

## 3. Kotlin & Compose 환경에서의 R8 극대화 지침

R8은 Kotlin 언어 특성(람다, 인라인 함수, Data Class)과 결합될 때 최적화 시너지가 매우 큽니다.

### 3-1. Reflection 기반 라이브러리 배제
* Gson, Java Reflection API 등 런타임에 클래스 필드 이름을 탐색하는 라이브러리는 R8이 해당 클래스의 이름을 난독화하거나 필드를 깎아내지 못하게 막습니다.
* **대안**: 컴파일 타임에 Serializer 코드를 자동 생성하는 **`kotlinx.serialization`**이나 **Metro / Hilt** (Compile-time DI)를 사용하면 R8이 불필요한 클래스를 제약 없이 수축(Shrink)시킬 수 있습니다.

### 3-2. Compose UI와 R8
* `@Composable` 함수는 컴파일 타임에 Compose Compiler 플러그인에 의해 바이트코드가 변환되며, R8은 미사용 컴포저블 함수 및 파라미터 람다 객체를 효과적으로 인라이닝하여 DEX 바이너리 크기를 단축시킵니다.

---

## 4. Gradle 프로젝트 설정 (`app/build.gradle.kts`)

프로젝트의 `release` 빌드 타입에서 R8 수축 및 최적화가 정상 동작하도록 설정합니다.

```kotlin
android {
    buildTypes {
        release {
            optimization {
                enable = true
                // 코드 수축 및 난독화 활성화
                isMinifyEnabled = true
                // 미사용 리소스 제거 (용량 최적화)
                isShrinkResources = true
            }
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

> [!IMPORTANT]
> `proguard-android-optimize.txt`는 구글이 검증한 최적화 알고리즘이 적용된 ProGuard 기본 파일이므로, 최적화가 없는 일반 `proguard-android.txt` 대신 반드시 `-optimize` 버전 기본 프로필을 사용하는 것을 권장합니다.

---

## 5. R8 프로가드 규칙 (`proguard-rules.pro`) 작성 모범 사례

### 5-1. 과도한 `-keep` 지정 금지 (Anti-Pattern)
* **나쁜 예**: ` -keep class com.benefit.virtualmate.** { *; }`
* 패키지 전체에 `*`를 지정하면 해당 패키지의 모든 코드 수축, 난독화, 인라이닝이 중단되어 R8 도입 효과가 무력화됩니다.

### 5-2. 올바른 `-keep` 규칙 지정 예시
1. **Reflection이나 Dynamic Loading이 꼭 필요한 클래스만 개별 지정**:
   ```proguard
   // 특정 Enum 또는 Native C/C++ JNI 연동 클래스만 지정
   -keepclassmembers enum * {
       public static **[] values();
       public static ** valueOf(java.lang.String);
   }
   ```
2. **라이브러리 자체 Consumer Rules 활용 (`consumer-rules.pro`)**:
   * 라이브러리 모듈(`core:network` 등)을 만들 때 자체 `consumer-rules.pro` 파일에 필요한 최소한의 keep 규칙을 명시하면, 해당 모듈을 참조하는 App 모듈 빌드 시 R8에 자동 포함됩니다.

### 5-3. `res/raw/keep.xml`을 통한 동적 리소스 수축(Resource Shrinking) 세부 제어
코드에서 `getResources().getIdentifier("icon_" + name, ...)`처럼 동적으로 리소스를 읽는 경우 R8이 해당 리소스를 미사용으로 착각해 지울 수 있습니다. 이때 `res/raw/keep.xml`을 통해 정밀 제어합니다:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@drawable/icon_*"
    tools:discard="@drawable/unused_banner"
    tools:shrinkMode="strict" />
```

---

## 6. R8 결과물 분석 및 디버깅 툴링

R8 최적화 빌드 후 결과 파일들은 `app/build/outputs/mapping/<variant>/` 경로에 생성됩니다.

### 6-1. 주요 리포팅 파일 종류
* **`mapping.txt`**: 난독화 전후의 클래스/메서드/라인 번호 매핑 지도입니다. **Crashlytics 원복(De-obfuscation) 및 Crash StackTrace 복구에 필수적이므로 릴리즈 배포 시 저장소에 보관해야 합니다.**
* **`seeds.txt`**: `-keep` 규칙에 의해 R8 수축 대상에서 제외되어 유지된(Kept) 클래스 및 메서드 목록입니다.
* **`usage.txt`**: R8에 의해 미사용 코드로 판단되어 **삭제된(Stripped) 클래스 및 메서드 목록**입니다.
* **`configuration.txt`**: Gradle 및 라이브러리 `consumer-rules`가 모두 병합된 최종 R8 ProGuard 설정 파일입니다.

### 6-2. R8 삭제(Stripping) 관련 Crash 디버깅 절차
1. 릴리즈 빌드에서 `ClassNotFoundException` 또는 `NoSuchMethodError` 발생 시.
2. `seeds.txt`와 `usage.txt`를 확인하여 의도한 클래스가 `usage.txt`(삭제 목록)에 들어갔는지 검증.
3. 해당 클래스만 핀포인트로 `proguard-rules.pro`에 최소한의 `-keep` 레벨(예: `-keepclassmembers`)로 보정 후 재검증.

---

## 7. Profile-Guided R8 최적화 및 Android Studio 툴링연동

R8 컴파일러는 단순히 정적 분석으로만 코드를 자르는 것을 넘어, **Baseline Profile 및 Startup Profile 지도를 입력받아 실행 최적화를 극대화**합니다.

### 7-1. Baseline Profile & Startup Profile과 R8의 시너지 (Profile-Guided Optimization)
* R8은 Baseline Profile(`baseline-prof.txt`) 및 Startup Profile(`startup-prof.txt`)에 기록된 코드 경로를 기반으로:
  1. **Startup Hot Path 메서드의 인라이닝 우선순위 결정**: 시작 단계에서 호출되는 메서드를 더 적극적으로 호출부에 Direct Inlining시킵니다.
  2. **DEX Layout 최적화 (Dex Layout Reordering / DEX Layout Optimization)**: 핫 코드를 DEX 파일의 첫 번째 페이지(First Page)로 모아 배치함으로써, 앱 구동 시 OS가 메모리 페이지를 가져오는 디스크 I/O 횟수와 Page Fault 오버헤드를 최소화합니다.

### 7-2. APK Analyzer를 활용한 R8 검증
Android Studio의 **APK Analyzer** (`Build > Analyze APK...`)를 활용하면:
* R8 적용 전후의 DEX 메서드 수(DEX count) 변화 추이 확인.
* 특정 패키지 및 라이브러리가 R8에 의해 얼마나 줄어들었는지 바이트 단위로 실시간 확인 및 검증할 수 있습니다.

---

## 8. Google Play Console 연동 및 실서비스 모니터링 (App Size & Vitals)

R8 최적화 결과는 수동 검증뿐만 아니라 **Google Play Console**과의 연동을 통해 지속 모니터링됩니다.

### 8-1. Android App Bundle (AAB) 및 Dynamic Delivery와의 시너지
* R8은 AAB 빌드 시 디바이스 아키텍처(arm64-v8a 등) 및 화면 밀도(density)에 따라 Split APK 단위로 미사용 코드를 정밀 수축시킵니다.
* Google Play Console의 **App Size 리포트**를 통해 실제 사용자가 Play 스토어에서 다운로드하는 용량(Download Size)과 기기 설치 용량(On-device Size)을 트래킹합니다.

### 8-2. Play Console Android Vitals 모니터링
* R8 최적화 및 Obfuscation(난독화) 적용 시 Play Console에 `mapping.txt`를 업로드하면, Crash 및 ANR 발생 시 난독화된 StackTrace가 **실제 소스 코드의 라인 번호와 클래스명으로 자동 De-obfuscation되어 수집**됩니다.
* 이를 통해 프로덕션 환경의 Crash rate 및 시작 시간 지표를 정밀 모니터링할 수 있습니다.

