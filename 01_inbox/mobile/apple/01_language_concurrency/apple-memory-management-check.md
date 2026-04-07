---
title: apple-memory-management-check
tags: [apple, interview, memory, swift]
aliases: []
date modified: 2026-04-06 18:01:32 +09:00
date created: 2026-04-06 17:58:00 +09:00
---

## [[apple-memory-management]] > [[apple-memory-management-check]]

### Memory Management Self-Diagnosis & Interview Prep

Apple 플랫폼(Swift/Obj-C)의 메모리 관리 핵심 개념을 점검하고 면접에 대비하기 위한 자가 진단 가이드입니다.

---

#### ✅ 핵심 개념 체크리스트 (Self-Check)

1. [ ] **ARC vs GC**: ARC 와 가비지 컬렉션(GC)의 결정적인 차이점(런타임 vs 컴파일 타임)을 설명할 수 있는가?
2. [ ] **Reference Counting**: 객체의 참조 카운트가 0 이 되는 정확한 시점과 그 이후의 프로세스를 이해하고 있는가?
3. [ ] **Weak vs Unowned**: 둘 다 순환 참조를 방지하지만, 내부적으로 Side Table 사용 여부와 '해제된 앱 접근 시 동작'의 차이를 아는가?
4. [ ] **Closure Capture List**: 클로저 내에서 `[weak self]` 를 사용하는 이유와 `guard let self = self` 패턴의 장점을 설명할 수 있는가?
5. [ ] **Autoreleasepool**: 현대 Swift 환경에서도 `autoreleasepool` 이 필요한 구체적인 상황을 예로 들 수 있는가?

---

#### 💬 실전 면접 예상 질문 (Interview Questions)

**Q. Swift 에서 `unowned` 보다 `weak` 사용이 권장되는 이유는 무엇인가요?**

>**A**: `unowned` 는 참조하는 객체가 해제된 후 접근하면 런타임 에러(Crash)를 유발하지만, `weak` 은 안전하게 `nil` 을 반환하기 때문입니다. 객체의 생명주기가 완벽하게 일치한다는 보장이 없다면 보안과 안정성 측면에서 `weak` 이 더 선호됩니다.

**Q. 순환 참조(Retain Cycle)를 발견하는 자신만의 노하우가 있나요?**

>**A**: 우선 코드를 작성할 때 클로저나 델리게이트 패턴에서 `weak` 을 습관적으로 검토합니다. 런타임에는 Xcode 의 **Memory Graph Debugger**를 통해 노란색 경고나 보라색 리테인 사이클 그래프를 시각적으로 확인하며, 복잡한 누수는 **Instruments 의 Leaks/Allocations** 도구를 활용해 Dirty Memory 의 점진적 증가를 추적합니다.

**Q. Side Table 이란 무엇이며 언제 생성되나요?**

>**A**: 객체의 강한 참조 카운트 외에 `weak` 참조가 발생하거나 참조 카운트가 오버플로우될 때 할당되는 별도의 메모리 블록입니다. 객체 헤더의 공간 부족을 해결하고, 객체가 해제된 후에도 `weak` 참조자가 `nil` 임을 확인할 수 있도록 돕습니다.

---

#### 🧪 실전 케이스 분석 (Case Study)

*다음 코드에서 메모리 누수가 발생하는 지점은 어디일까요?*

```swift
class Job {
    var onComplete: (() -> Void)?
    deinit { print("Job Deinitialized") }
}

class Worker {
    let job = Job()
    init() {
        job.onComplete = {
            self.doWork() // 여기서 self를 강하게 캡처함
        }
    }
    func doWork() { print("Working...") }
    deinit { print("Worker Deinitialized") }
}
```

**해설**: `Worker -> Job -> Closure -> Worker` 순서로 강한 참조 순환이 발생합니다. `{ [weak self] in self?.doWork() }` 와 같이 캡처 리스트를 사용해 고리를 끊어야 합니다.

---

#### 📚 연관 학습

- [[apple-memory-management]] - ARC 및 메모리 레이아웃 상세
- [[apple-performance-and-debug]] - 실전 디버깅 및 분석 도구 활용
- [[apple-runtime-and-swift]] - 런타임 메타데이터와 객체 구조
