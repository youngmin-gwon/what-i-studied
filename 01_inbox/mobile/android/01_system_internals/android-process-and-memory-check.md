---
title: android-process-and-memory-check
tags: [android, interview, memory, process]
aliases: []
date modified: 2026-04-06 18:00:41 +09:00
date created: 2026-04-06 17:59:00 +09:00
---

## [[android-process-and-memory]] > [[android-process-and-memory-check]]

### Process & Memory Management Self-Diagnosis & Interview Prep

안드로이드의 프로세스 수명 주기와 메모리 관리 메커니즘을 점검하고 면접에 대비하기 위한 가이드입니다.

---

#### ✅ 핵심 개념 체크리스트 (Self-Check)

1. [ ] **Zygote Fork**: 모든 앱이 Zygote 에서 fork 되는 이유와 이 방식이 메모리 공유(COW)에 미치는 영향을 설명할 수 있는가?
2. [ ] **Process Priority (oom_adj)**: Foreground, Visible, Service, Cached 프로세스의 차이와 시스템이 메모리 부족 시 어떤 순서로 종료하는지 아는가?
3. [ ] **LMKD (Low Memory Killer Daemon)**: 커널 수준의 OOM Killer 와 안드로이드 LMKD 의 차이점을 이해하고 있는가?
4. [ ] **Memory Leak in Android**: `Context` 누수가 발생하는 대표적인 상황(Static variable, Singleton, Inner class)을 설명할 수 있는가?
5. [ ] **ART GC**: 안드로이드 런타임(ART)의 가비지 컬렉션 방식(Concurrent GC 등)이 앱 성능(Jank)에 미치는 영향을 이해하는가?

---

#### 💬 실전 면접 예상 질문 (Interview Questions)

**Q. 안드로이드 앱에서 메모리 누수(Memory Leak)를 방지하기 위해 가장 주의해야 할 점은 무엇인가요?**

>**A**: `Context` 객체, 특히 `Activity Context` 의 참조를 오래 유지하지 않는 것이 가장 중요합니다. `Static` 변수에 View 나 Activity 를 저장하거나, 비동기 작업(Thread, Handler)에서 Activity 의 참조를 캡처한 뒤 Activity 가 종료되어도 작업을 계속하는 경우 누수가 발생합니다. 이를 방지하기 위해 `WeakReference` 를 사용하거나, 생명주기에 맞춰 작업을 취소(Cancel)해야 합니다.

**Q. Zygote 프로세스가 메모리 효율성에 기여하는 방식은 무엇인가요?**

>**A**: Zygote 는 부팅 시 수백 개의 프레임워크 클래스와 리소스를 미리 로드하여 메모리에 적재합니다. 새로운 앱이 실행될 때 `fork()` 를 통해 Zygote 의 주소 공간을 공유하며, **Copy-on-Write (COW)** 기술 덕분에 실제 수정이 일어나기 전까지는 동일한 메모리 페이지를 공유하여 전체 메모리 사용량을 획기적으로 줄입니다.

**Q. LMKD 가 프로세스를 죽이는 기준인 `oom_adj` 에 대해 설명해주세요.**

>**A**: `oom_adj` 는 프로세스의 중요도를 숫자로 나타낸 값입니다. 사용자가 보고 있는 포그라운드 앱은 가장 낮은 값을 가지며, 백그라운드에 오래 머문 앱일수록 높은 값을 가집니다. 시스템 가용 메모리가 특정 임계치(Threshold) 이하로 떨어지면 LMKD 가 깨어나 점수가 높은(중요도가 낮은) 프로세스부터 차례로 종료하여 시스템 전체의 안정성을 확보합니다.

---

#### 🛠️ 진단 도구 활용 (Diagnosis Tools)

- **Android Profiler**: 실전 런타임 메모리 사용량(Heap, Native, Graphics 등)을 실시간 모니터링하고 Heap Dump 를 분석합니다.
- **LeakCanary**: 개발 단계에서 메모리 누수를 자동으로 탐지하여 참조 체계(Reference Path)를 시각적으로 보여주는 필수 라이브러리입니다.

---

#### 📚 연관 학습

- [[android-process-and-memory]] - 프로세스 및 메모리 관리 아키텍처
- [[android-zygote-and-runtime]] - Zygote 와 런타임 심화
- [[android-performance-and-debug]] - 성능 최적화 및 디버깅 실전
