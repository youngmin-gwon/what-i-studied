# [[mobile-security]] > [[android-xr-and-spatial-computing]]

## Android XR: The Spatial Frontier

안드로이드 생태계를 공간 컴퓨팅(Spatial Computing)으로 확장하는 **Android XR** 플랫폼과 핵심 개발 원칙을 분석합니다. 

단순히 2D 앱을 띄우는 것을 넘어, 사용자의 시선과 제스처를 결합한 몰입형 경험을 설계하고 Gemini AI 에이전트와 통합된 미래지향적 인터페이스를 구축하는 것이 목표입니다.

---

### 💡 Context: 공간 중심의 컴퓨팅 패러다임

모바일의 화면 제약을 벗어나 현실 공간에 디지털 정보를 배치하는 아키텍처입니다. 이는 [[android-foundations]]의 시각적 한계를 넘어선 단계이며, [[android-security-and-sandboxing]]이 물리적 공간 정보(Spatial Privacy)로 확장되는 새로운 도전 과제입니다.

---

> [!NOTE] **iOS 비교: visionOS vs Android XR**
> - **iOS/visionOS**: Apple Vision Pro를 중심으로 한 고성능, 폐쇄형 공간 컴퓨팅. **Foveated Streaming**과 **Spatial Audio**의 극도로 정밀한 경험이 강점이다. ([[apple-spatial-computing-visionos]])
> - **Android XR**: 다양한 제조사가 참여하는 개방형 플랫폼. Google의 **Gemini AI**가 시스템 깊숙이 통합되어 사용자의 시선과 음성으로 모든 것을 제어하는 에이전트 경험이 강점이다.
> 자세한 내용은 [[apple-spatial-computing-visionos]]를 참고하세요.

### 1. Android XR 아키텍처

Android XR은 안드로이드 생태계의 풍부한 앱들을 공간 환경으로 확장한다.
- **System-level AI (Gemini)**: 에이전트가 사용자가 보고 있는 환경을 실시간으로 분석(Multimodal)하고, 필요한 앱의 기능을 실행한다.
- **Ecosystem Compatibility**: 기존 안드로이드 앱과 위젯을 별도의 코드 수정 없이 2D 패널 형태로 즉시 띄울 수 있다.

### 2. 가상화 형태 (Hardware Form Factors)

Android XR은 두 가지 핵심 폼 팩터를 지원한다.
- **Galaxy XR (Headset)**: 몰입형 MR 경험을 제공하며, Snapdragon XR2+ Gen 2 칩셋을 통해 고해상도 그래픽과 NPU 연산을 처리한다.
- **AI Smart Glasses**: 안경형 경량 기기(약 50g)로, 상시 착용이 가능하며 Gemini AI와 시각 비서를 주 목적으로 한다. (Qualcomm AR1 플랫폼)

### 3. 개발 프레임워크: Compose for XR

공간상의 3D 컴포넌트와 2D 레이아웃을 선언형으로 작성할 수 있다.

```kotlin
// Compose for XR 예시
@Composable
fun SpatialCard() {
    SpatialPanel(
        modifier = Modifier.size(400.dp, 300.dp),
        zDistance = 1.5.m // 공간상의 거리 설정
    ) {
        Content()
    }
}
```

---

### 🏛️ 공간 컴퓨팅 시대의 앱 설계

이제 앱은 화면 안의 픽셀이 아닌, 사용자 주변의 **공간(Volume)**을 점유한다.

> [!TIP] **Devil's Advocate : 2D 레이아웃에 갇히지 마라**
> 기존 안드로이드 앱을 2D 패널로 띄우는 것은 시작일 뿐이다. 진정한 XR 앱은 **사용자의 맥락(Context)**을 이해해야 한다. 사용자가 주방에 있을 때 레시피 앱이 자동으로 벽면에 나타나고, 배달 에이전트가 실제 거실 테이블 위에 도착 정보를 띄워주는 식의 **공간적 사용자 경험(Spatial UX)**이 경쟁력이 될 것이다.

### See Also

- [[android-appfunctions-and-ai-agents]]
- [[android-desktop-windowing-and-multitasking]]
- [[android-ui-system]]
