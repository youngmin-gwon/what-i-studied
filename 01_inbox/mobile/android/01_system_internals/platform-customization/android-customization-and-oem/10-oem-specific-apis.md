# OEM-specific APIs

상위 노트: [[android-customization-and-oem]]

### Samsung Knox

```java
// Knox SDK
KnoxContainerManager kcm = KnoxContainerManager.getInstance(context);
ContainerConfigurationPolicy ccp = kcm.getContainerConfigurationPolicy();
ccp.setPasswordMinimumLength(8);
```

### Xiaomi MIUI APIs

```java
// MIUI 전용
import miui.os.Build;

if (Build.IS_MIUI) {
    // MIUI 전용 기능
}
```

**문제**: AOSP 호환성 깨질 수 있음

---
