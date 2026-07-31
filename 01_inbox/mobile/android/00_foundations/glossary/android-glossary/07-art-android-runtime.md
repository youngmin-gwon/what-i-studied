# ART (Android Runtime)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 안드로이드 앱 실행 엔진 (Dalvik 의 후속)

**상세**:

Android 5.0 부터 기본값. DEX 바이트코드를 실행하며, 설치 시 AOT 컴파일과 실행 중 JIT 컴파일을 병행한다. Profile-Guided Optimization 으로 자주 사용하는 코드를 최적화한다.

**진화**:

```
Dalvik (2008-2013):
  JIT만 → 매번 컴파일 → 느림

ART (2014-현재):
  AOT + JIT + Profile-Guided → 빠름
```

**확인**:

```bash
# 런타임 확인
adb shell getprop persist.sys.dalvik.vm.lib.2

# 출력: libart.so
```

**관련**: [android-zygote-and-runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-zygote-and-runtime.md)

---

### B
