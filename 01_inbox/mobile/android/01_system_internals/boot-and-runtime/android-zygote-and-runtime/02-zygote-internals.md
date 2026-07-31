# 🦠 Zygote Internals

Zygote 는 **"모든 앱의 부모 프로세스"**입니다.

#### 1. Boot Logic (The Warm-up)

1. 안드로이드가 부팅될 때 가장 먼저 (`init` 다음으로) Zygote 프로세스가 뜹니다.
2. **Preloading**: `framework.jar`, `androidx`, `drawable` 등 모든 앱이 공통으로 쓰는 4,000 여 개의 클래스와 리소스를 메모리에 미리 로드합니다.
3. **Socket Listen**: 로딩을 다 마치면 `/dev/socket/zygote` 를 열고 "새끼 칠 준비"를 마친 채 잠듭니다.

#### 2. Fork & Copy-on-Write (COW)

앱 실행 요청이 오면, Zygote 는 자기 자신을 **복제(`fork()`)**합니다.

- **Magic**: `fork()` 는 자식 프로세스에게 부모의 메모리를 그대로 물려줍니다.
- **COW**: 처음에는 메모리를 실제로 복사하지 않고 **공유(Share)**만 합니다. 앱이 데이터를 **쓰는(Write)** 순간에만 그 페이지만 뚝 떼어서 복사합니다.
- **Result**: 앱 100 개를 띄워도 `Framework` 클래스 메모리는 딱 1 개 분량만 듭니다.

---
