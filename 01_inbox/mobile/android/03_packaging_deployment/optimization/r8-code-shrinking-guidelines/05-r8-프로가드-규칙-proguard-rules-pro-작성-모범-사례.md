# R8 프로가드 규칙 (`proguard-rules.pro`) 작성 모범 사례

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
