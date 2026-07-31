# 💡 Why it matters (Context)

안드로이드는 단순한 앱 실행 환경이 아닌, 수십억 개의 기기에서 작동하는 복잡한 분산 시스템입니다.

- **Resource Constraints**: 배터리와 메모리가 제한된 환경에서 수십 개의 앱이 동시에 구동되어야 합니다.
- **Security by Design**: 모든 앱은 고유한 **UID**를 가지며, 자신의 샌드박스 안에서만 안전하게 동작합니다.
- **Inter-process Communication**: 서로 다른 앱과 시스템은 **Binder**라는 고속 통신 통로를 통해 데이터를 주고받습니다.

---
