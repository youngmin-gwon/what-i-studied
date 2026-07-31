# Custom ROM 개발

상위 노트: [[android-customization-and-oem]]

### LineageOS

AOSP 기반, Google 없이:

**특징**:

- Privacy Guard
- Trust (보안 상태 표시)
- Lineage Recovery
- microG 지원 (GMS 대체)

**빌드**:

```bash
# 소스 다운로드
repo init -u https://github.com/LineageOS/android.git -b lineage-20.0
repo sync

# 환경 설정
source build/envsetup.sh
breakfast <device>

# 빌드
brunch <device>
```

### GrapheneOS (Privacy-focused)

**강화 사항**:

- Hardened malloc
- Exec spawning
- MAC randomization
- 센서 권한 강화

---
