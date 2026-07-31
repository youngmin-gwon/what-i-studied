# 기기 Bring-up
- `device/<vendor>/<product>` 트리에 BoardConfig, init 스크립트, fstab, [sepolicy](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md#selinux), 오버레이를 둔다.
- VINTF manifest/matrix 가 HAL 버전을 맞추는지 확인한다.
- [AVB](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md#verified-boot) 키와 [boot](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md#boot-image) 구성이 맞지 않으면 부팅이 막힌다.
