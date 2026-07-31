# 렌더링 성능은 프레임 지연의 원인을 분리한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

매끄러운 화면은 모든 프레임이 제시간에 제출되는 상태다.

일반적인 60Hz 화면에서는 프레임 하나에 약 16ms의 예산이 있다.

고주사율 기기에서는 프레임 예산이 더 짧아진다.

지연 프레임의 수보다 긴 지연이 반복되는 구간을 함께 본다.

입력, 애니메이션, 레이아웃, 그리기, GPU 작업을 분리해 관찰한다.

메인 스레드에서 큰 계산을 하면 UI 이벤트와 그리기가 함께 늦어진다.

Compose에서는 불필요한 재구성과 큰 상태 범위를 먼저 확인한다.

상태를 화면 가까이에 두면 변경 범위를 줄이기 쉽다.

비싼 계산은 입력이 바뀔 때만 수행하고 결과를 재사용한다.

View 기반 화면에서는 중첩 레이아웃과 과도한 바인딩을 줄인다.

RecyclerView는 아이템 재사용과 차이 계산이 정상적으로 작동하는지 확인한다.

큰 이미지, 투명도, 그림자, 복잡한 클리핑은 GPU 비용을 높일 수 있다.

SurfaceView와 TextureView는 표시 방식과 합성 비용이 다르다.

화면 기술을 바꾸기 전에 현재 병목이 CPU인지 GPU인지 확인한다.

`dumpsys gfxinfo`는 앱의 프레임 통계를 빠르게 확인하는 방법이다.

FrameMetrics와 Perfetto는 특정 프레임이 왜 늦었는지 좁힐 때 유용하다.

[렌더링 성능 측정](https://developer.android.com/topic/performance/rendering)은 프레임 시간과 지연 프레임을 해석하는 기준을 제공한다.

[Macrobenchmark 프레임 측정](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)은 스크롤과 애니메이션을 반복 측정하는 데 사용한다.

스크롤 테스트는 같은 목록 크기와 같은 제스처를 사용해야 한다.

수동으로 화면을 빠르게 넘긴 결과는 회귀 기준으로 부족하다.

지연 프레임이 줄어도 화면이 빈번하게 깜박이면 별도 결함이다.

레이아웃 단순화는 콘텐츠 구조와 접근성을 깨지 않는 범위에서 한다.

프레임 문제는 화면 전체를 추측해 고치지 말고 긴 trace 구간부터 확인한다.

메인 스레드가 짧은데 GPU 대기가 길면 그리기와 합성을 조사한다.

메인 스레드가 길면 바인딩, 측정, 재구성, 동기식 작업을 조사한다.

수정 후에는 같은 기기에서 프레임 분포를 다시 비교한다.
