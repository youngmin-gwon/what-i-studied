# APEX 구조

상위 노트: [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

```
apex_file.apex
├── apex_manifest.pb (메타데이터)
├── apex_payload.img (파일 시스템 이미지)
│   ├── bin/
│   ├── lib/
│   ├── lib64/
│   └── etc/
└── apex_pubkey (공개 키)
```
