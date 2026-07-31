# APEX 빌드 (AOSP)

상위 노트: [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

```python
# Android.bp
apex {
    name: "com.android.mymodule",
    manifest: "apex_manifest.json",
    file_contexts: ":mymodule-file_contexts",
    key: "com.android.mymodule.key",
    certificate: ":com.android.mymodule.certificate",
    
    native_shared_libs: [
        "libmymodule",
    ],
    
    binaries: [
        "mymodule_daemon",
    ],
    
    prebuilts: [
        "mymodule_config",
    ],
    
    updatable: true,
    min_sdk_version: "30",
}
```

```json
// apex_manifest.json
{
  "name": "com.android.mymodule",
  "version": 1,
  "versionName": "1.0.0"
}
```
