# Layout Debugging

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

##### Layout Inspector

```
Tools → Layout Inspector
```

**기능:**

- 3D 뷰로 레이어 확인
- 각 View 의 속성 확인
- 렌더링 시간 측정

##### Show Layout Bounds

```bash
# 개발자 옵션에서 "레이아웃 경계 표시" 활성화
adb shell setprop debug.layout true
adb shell service call activity 1599295570
```
