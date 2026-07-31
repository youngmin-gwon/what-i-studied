# Mipmap

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 앱 아이콘을 저장하는 리소스 디렉토리

**상세**:

Drawable 과 달리 런처가 아이콘을 로딩할 때 최적화되어 있다. 다양한 화면 밀도 (mdpi, hdpi, xhdpi 등) 별로 제공해야 한다.

**구조**:

```
res/
├─ mipmap-mdpi/ic_launcher.png     (48x48)
├─ mipmap-hdpi/ic_launcher.png     (72x72)
├─ mipmap-xhdpi/ic_launcher.png    (96x96)
├─ mipmap-xxhdpi/ic_launcher.png   (144x144)
└─ mipmap-xxxhdpi/ic_launcher.png  (192x192)
```

**사용**:

```xml
<application
    android:icon="@mipmap/ic_launcher"
    ...>
```

---

### 관련 문서

[android-overview](01_inbox/mobile/android/00_foundations/overview/android-overview.md) - 시스템 전체 개요

[android-evolution-history](01_inbox/mobile/android/00_foundations/history/android-evolution-history.md) - 기술 진화

[android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md) - 디버깅 도구
