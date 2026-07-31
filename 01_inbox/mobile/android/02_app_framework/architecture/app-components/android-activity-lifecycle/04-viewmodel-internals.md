---
title: 04-viewmodel-internals
tags: []
aliases: []
date modified: 2026-07-31 16:28:48 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 🛠️ ViewModel Internals

"ViewModel 은 어떻게 Activity 가 죽어도 살아있을까?"

1. **HolderFragment (Old)**: 예전에는 투명한 Fragment(`setRetainInstance(true)`)를 붙여서 유지했습니다.
2. **ActivityClientRecord (Modern)**:
    - `Activity` 가 구성 변경으로 파괴될 때, `ActivityThread` 가 `NonConfigurationInstances` 라는 객체를 따로 챙겨둡니다.
    - 여기에 ViewModelStore 가 들어있습니다.
    - 새 Activity 가 만들어질 때 `attach()` 과정에서 이 객체를 다시 넘겨받습니다.

---
