# 🏛️ 1. 핵심 시스템 서비스 (Key native Services)

이 서비스들은 `init.rc` 에 의해 시스템 부팅 시점에 실행되며, 프레임워크 계층에서 Binder IPC 를 통해 호출됩니다.

- **SurfaceFlinger**: 화면 합성을 담당. 앱의 버퍼를 조합하여 디스플레이로 전송.
- **AudioFlinger**: 오디오 재생 및 믹싱 관리. 하드웨어 추상화 계층(HAL)과 오디오 하드웨어 간의 통로.
- **MediaServer**: 카메라, 인코더, 오디오 재생(MediaPlayer) 등 멀티미디어 기능을 실행하는 전용 프로세스.
- **Vold (Volume Daemon)**: 스토리지(SD 카드, USB) 마운트 및 암호화 관리.
- **Logd**: 시스템 로그 처리를 위한 전용 데몬 프로세스.

---
