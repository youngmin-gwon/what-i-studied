# Bootloader

Android Bootloader (ABL, 대부분 Qualcomm LK 기반):

- **Verified Boot**: vbmeta 검증 → system/vendor 무결성
- **A/B 슬롯** 선택: 활성 슬롯 부팅 (a, b)
- 커널 + ramdisk 메모리에 로드

**특수 모드**:

- **Fastboot**: `fastboot flash`, `fastboot boot`
- **Recovery**: OTA 업데이트, 공장 초기화
