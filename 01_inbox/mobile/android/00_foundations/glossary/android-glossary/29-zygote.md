# Zygote

상위 노트: [[android-glossary]]

**정의**: 모든 앱 프로세스를 생성하는 부모 프로세스

**상세**:

부팅 시 Framework 클래스와 리소스를 미리 로드 (Preload) 한 후 대기한다. 앱 시작 요청이 오면 자신을 fork 하여 새 프로세스를 빠르게 만든다. Copy-on-Write 로 메모리를 절약한다.

**프로세스**:

```
Zygote (PID 1234, 4000개 클래스 Preload)
  ↓ fork
앱 A (PID 5678, Preload 공유)
앱 B (PID 5679, Preload 공유)
```

**확인**:

```bash
# Zygote 프로세스
adb shell ps -A | grep zygote

# Preload 클래스 수
adb shell getprop dalvik.vm.preloadedclasses

# 출력: ~4000
```

**소켓**:

```bash
# Zygote 소켓
adb shell ls -la /dev/socket/zygote*

# /dev/socket/zygote
# /dev/socket/zygote_secondary (32-bit)
```

**관련**: [[android-zygote-and-runtime]]

---

### 기타
