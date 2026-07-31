# 기기 Bring-up
- `device/<vendor>/<product>` 트리에 BoardConfig, init 스크립트, fstab, [[android-glossary#selinux|sepolicy]], 오버레이를 둔다.
- VINTF manifest/matrix 가 HAL 버전을 맞추는지 확인한다.
- [[android-glossary#verified-boot|AVB]] 키와 [[android-glossary#boot-image|boot]] 구성이 맞지 않으면 부팅이 막힌다.
