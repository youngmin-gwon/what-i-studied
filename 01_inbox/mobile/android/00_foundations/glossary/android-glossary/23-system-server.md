# system_server

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 시스템 서비스들이 실행되는 Java 프로세스

**상세**:

Zygote 가 fork 하여 생성하며, ActivityManager, WindowManager, PackageManager 등 100 여 개 서비스를 호스팅한다. system_server 가 크래시하면 기기 재부팅된다.

**확인**:

```bash
# system_server 프로세스
adb shell ps -A | grep system_server

# 포함된 서비스
adb shell service list
```

**크래시 시**:

```
system_server 죽음 → Zygote가 재시작 감지 → 기기 재부팅
```

**관련**: [android-activity-manager-and-system-services](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-activity-manager-and-system-services.md)

---

### U
