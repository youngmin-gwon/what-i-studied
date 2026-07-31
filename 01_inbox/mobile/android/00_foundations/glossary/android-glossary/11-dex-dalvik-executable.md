# DEX (Dalvik Executable)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 안드로이드 앱의 바이트코드 형식

**상세**:

Java/Kotlin 코드를 컴파일하면 JVM `.class` 파일이 생성되고, 이를 `dx` 도구로 `.dex` 로 변환한다. DEX 는 모바일에 최적화되어 있어 파일 크기가 작고 실행 효율이 높다.

**프로세스**:

```
.kt/.java → .class → .dex → .apk
         javac    dx/d8
```

**확인**:

```bash
# APK 내 DEX 파일 확인
unzip -l app.apk | grep dex

# 출력:
# classes.dex
# classes2.dex (MultiDex)
```

**최적화**:

```bash
# dexopt (설치 시)
# → .odex (Optimized DEX)
# → .vdex (Verified DEX, ART)
```

**관련**: [android-zygote-and-runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-zygote-and-runtime.md)

---
