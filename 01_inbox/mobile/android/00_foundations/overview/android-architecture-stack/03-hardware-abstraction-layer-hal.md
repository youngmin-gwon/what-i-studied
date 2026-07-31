# 🔌 Hardware Abstraction Layer (HAL)

앱 개발자는 `android.hardware.camera2` 만 알면 됩니다. 하드웨어가 소니 센서인지 삼성 센서인지는 몰라도 됩니다.

- **Legacy HIDL (Hardware Interface Definition Language)**: Android 8.0(Treble) 부터 도입. 하드웨어 드라이버를 별도 프로세스로 분리해, OS 업데이트 시 드라이버를 다시 컴파일하지 않아도 되게 했습니다.
- **Modern AIDL Stability**: Android 11+ 부터는 Binder AIDL 을 HAL 정의에도 사용합니다.

---
