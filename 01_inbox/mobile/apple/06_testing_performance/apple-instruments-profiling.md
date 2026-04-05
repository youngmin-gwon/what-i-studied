---
title: apple-instruments-profiling
tags: [apple, instruments, performance, profiling, xcode]
aliases: []
date modified: 2026-04-05 17:45:42 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Instruments Profiling Deep Dive

>[!TIP] **Devil's Advocate : Swift Concurrency 시대의 Profiling**
>전통적인 Time Profiler 만으로는 최신 Swift Concurrency(`async/await`, `actor`)의 병목을 추적하기 극히 어렵습니다. 스레드가 중단(Suspend)된 건지 대기 중인지 타임라인에 명확히 표기되지 않기 때문입니다. **현실적으로 현대 앱 프로파일링은 `Swift Concurrency` 템플릿 사용법 숙지가 우선**됩니다.

Instruments 는 Xcode 에 딸려오는 "부록"이 아닙니다.

오히려 Xcode 보다 더 강력한, Apple 엔지니어링의 정수입니다.

"내 앱은 왜 느릴까?"라는 막연한 질문을 "A 함수의 B 루프가 45ms 를 쓴다"는 명확한 팩트로 바꿔줍니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **추측 금지**: "이미지 처리가 느린가?"라고 예상하고 최적화했는데, 실제로는 `DateFormatter` 가 범인인 경우가 허다합니다. 프로파일링 없는 최적화는 시간 낭비입니다.
- **Main Thread Hang**: Time Profiler 를 돌려보면 메인 스레드에서 뭘 하느라 화면이 멈췄는지 초 단위로 보입니다.
- **Release Mode**: 반드시 `Release` 빌드로 프로파일링해야 합니다. Debug 모드는 컴파일러 최적화가 꺼져있어서 실제 성능과 전혀 다릅니다.

---

### ⏱️ Time Profiler (CPU)

가장 자주 쓰게 될 도구입니다. 실행 중인 앱의 Call Stack 을 1ms 마다 샘플링합니다.

#### 1. Invert Call Tree & Hide System Libraries

Call Tree 옵션에서 이 두 가지를 체크하세요.

- **Invert Call Tree**: 함수를 바닥부터 뒤집어서 보여줍니다. 즉, CPU 를 직접 쓰고 있는 말단 함수(Leaf)가 맨 위에 뜹니다. 범인을 잡기 가장 쉽습니다.
- **Hide System Libraries**: UIKit 이나 Foundation 내부 코드는 내가 못 고칩니다. 내 코드만 발라내서 보여줍니다.

#### 2. Heaviest Stack Trace

오른쪽 패널(Extended Detail View)을 보면, 가장 무거운 실행 경로가 하이라이트됩니다.

더블 클릭하면 해당 소스 코드로 바로 이동합니다. "아, 여기서 for 문을 돌리면 안 되는구나"를 바로 깨닫게 됩니다.

---

### 🚦 Swift Concurrency Profiler (Modern iOS 17+)

`async/await` 환경에서 데드락이나 우선순위 역전(Priority Inversion), 행(Hang)이 발생했을 때 해결하는 필수 도구입니다.

- **Task Lifecycle**: Task 가 생성되고(Created) 실행 대기(Runnable), 실행(Running), 멈춤(Suspended) 상태로 변하는 흐름을 타임라인으로 보여줍니다.
- **Actor Serialization**: 두 개 이상의 Task 가 동일한 Actor 의 데이터에 접근하려다 병목이 생기는 "Actor Reentrancy / Block" 현상을 시각화하여 보여줍니다.
- 이 도구 없이는 `Task` 병목 현상을 Time Profiler 만으로 분석하는 것이 불가능에 가깝습니다.

---

### 💾 Allocations (Memory)

"앱을 오래 쓰면 점점 느려지다가 죽어요." -> 100% 메모리 이슈입니다.

#### 1. Anonymous VM vs Heap
- **Heap**: 내 객체(UIView, Person 등)가 사는 곳.
- **Anonymous VM**: 이미지 데이터, 비트맵 등이 사는 곳.
"메모리가 200MB 나 찼는데 힙에는 10MB 밖에 없어요?" -> 이미지가 범인입니다.

#### 2. Generations (Marking)

Snapshot(Mark Generation) 기능을 활용하세요.

1. A 화면 진입 전 'Mark'
2. A 화면 진입 및 사용
3. A 화면 탈출
4. 'Mark'
이 과정을 반복했을 때 스냅샷 사이에 메모리가 계속 늘어난다면(Growth), 그 객체는 줄줄 새고 있는 겁니다.

---

### ⚡️ Energy Log (Battery)

"앱 켜니까 폰이 뜨거워져요."

- **Overhead**: CPU 사용량이 20% 만 되어도 배터리는 녹습니다.
- **Networking**: 라디오(LTE/5G) 모듈을 켜는 것이 배터리를 가장 많이 씁니다. 요청을 모아서(Batch) 한 번에 보내는 게 낫습니다.
- **Location**: GPS(High Accuracy)는 배터리 킬러입니다. 필요 없을 땐 과감히 꺼야 합니다.

### 더 보기
- [apple-performance-and-debug](apple-performance-and-debug.md) - 성능 최적화 목표 설정
- [apple-memory-management](../01_language_concurrency/apple-memory-management.md) - 메모리 누수 원리 (ARC)
