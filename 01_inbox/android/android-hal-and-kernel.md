# Linux Kernel + Android HAL #android #android/kernel #android/hal #osdev

커널과 HAL은 안드로이드의 바닥을 책임진다. 처음 보는 말은 [[android-glossary]]에서 확인하자.

## 커널이 하는 기본 일
- 프로세스와 스레드를 스케줄링하고, 메모리를 관리한다. 부족하면 [[android-glossary#lmkd|LMKD]]가 덜 중요한 앱을 닫는다.
- [[android-glossary#selinux|SELinux]]와 seccomp로 위험한 접근을 막는다.
- 전원 관리: [[android-glossary#wakelock|Wakelock]], cpu 주파수, 절전 모드 조정.
- 파일 시스템과 암호화([[android-glossary#fbe|FBE]]), 무결성([[android-glossary#verified-boot|Verified Boot]]), 드라이버(binder, display, audio, camera, sensor).

## HAL이 필요한 이유
- 기기마다 다른 하드웨어를 표준 인터페이스로 감싼다.
- HIDL에서 AIDL HAL로 옮겨가며 테스트와 호환성을 쉽게 한다.
- binderized HAL은 별도 프로세스로 돌며 시스템과 격리되어 안전하다.

## 메모리·I/O 관리
- zram/swap, pressure stall(메모리 압력) 감지로 성능을 유지한다.
- DMABuf/ION(memfd)로 큰 버퍼를 공유해 복사를 줄인다.
- I/O 스케줄러와 F2FS/ext4 튜닝으로 저장소 속도를 챙긴다. [[android-glossary#scoped-storage|Scoped Storage]] 규칙도 여기와 연결된다.

## 네트워크와 전원
- netd/eBPF로 네트워크 계측과 방화벽을 한다. Private DNS, 테더링 오프로딩도 관여한다.
- 타이머를 모아 배터리를 아끼고, 전원 힌트로 성능과 소비를 균형 잡는다.

## 보안 하드닝
- KASLR, CFI 같은 방어 기법을 켜서 커널 자체를 보호한다.
- sepolicy로 도메인/타입을 나누어 “누가 무엇을 만질 수 있는지” 정한다.

## 가상화/컨테이너
- Android Virtualization Framework(AVF)로 보호된 VM을 띄울 수 있다(microdroid).
- VirtIO로 그래픽/입력/네트워크를 전달한다. 컨테이너는 mount 네임스페이스 등을 활용해 격리한다.

## Bring-up 체크
- 커널 커맨드라인, dtb/dtbo, fstab/AVB 설정이 맞는지 본다.
- HAL이 올바른 라이브러리를 찾는지, [[android-glossary#binder|Binder]] 서비스가 등록됐는지 확인한다.
- 문제 시 dmesg/logcat/pstore/trace를 모아본다.

## 링크
[[android-boot-flow]], [[android-architecture-stack]], [[android-binder-and-ipc]], [[android-security-and-sandboxing]].
