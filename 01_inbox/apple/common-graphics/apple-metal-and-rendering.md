# Metal & Rendering Basics #apple #metal #graphics #common

Metal과 렌더링 기본을 쉽게 설명한다. 모르는 용어는 [[apple-glossary]].

## 왜 Metal인가?
- CPU 부담을 줄이고 GPU를 효율적으로 쓰기 위해 설계된 그래픽/컴퓨팅 API.
- iOS/iPadOS/watchOS/macOS/tvOS/visionOS에서 공통으로 사용.

## 렌더링 흐름 한눈에
1) 앱이 버텍스/인덱스/텍스처 같은 데이터를 준비.
2) Metal 커맨드 버퍼에 드로우 명령을 쌓음.
3) GPU가 실행, 결과를 프레임버퍼/텍스처에 기록.
4) WindowServer/Backboardd/Reality compositor가 최종 합성해 화면에 표시.

## 필수 개념
- Device: GPU 핸들.
- Command Queue/Buffer: GPU 작업을 담는 줄/상자.
- Render/Compute Pipeline: 셰이더와 상태를 묶은 실행 계획.
- Texture/Buffer: 이미지/데이터 저장소.
- Synchronization: CPU-GPU 간 자원 접근 타이밍 관리.

## 성능 팁
- 드로우콜 줄이기: 인스턴싱, 멀티드로우 인덱스.
- 메모리 대역폭 절약: 압축 텍스처(ASTC), 적절한 픽셀 포맷.
- 타일 기반 GPU 특성 고려: 깊이/스텐실/컬러 첨부 개수 최소화.
- GPU/CPU 동기화 최소화: Blit/compute를 적절히 분리, fence/event 사용.

## 프레임 스케줄
- 디스플레이 vsync에 맞춰 프레임을 제출한다.
- ProMotion(최대 120Hz)에서는 프레임 타깃을 상황에 맞게 설정.
- watchOS/저성능 기기는 60Hz 이하일 수 있으므로 부하를 낮춘다.

## 셰이더
- Metal Shading Language(C++17 유사). 버텍스/프래그먼트/컴퓨트 셰이더 작성.
- Argument Buffers/Function Constants로 유연성과 성능 확보.
- macOS/Apple Silicon에서 Ray Tracing(미리보기) 지원 여부 확인.

## 멀티 플랫폼 고려
- iOS/visionOS: 타일 기반 GPU, 에너지 제약. 드로우콜/해상도 줄이기.
- macOS: 데스크탑급 GPU(Apple Silicon/Intel/Radeon). 더 큰 파이프라인/해상도 가능.
- watchOS: Metal 지원(Series 5+), 하지만 GPU 예산이 매우 작다.

## 디버깅
- Xcode GPU Frame Capture로 파이프라인 상태/리소스/타이밍을 본다.
- Metal System Trace(Instruments)로 CPU→GPU 제출, 스케줄, 시간 소모를 확인.
- GPU Counters(AGI)로 병목을 찾는다.

## 흔한 문제와 해결
- 과도한 오버드로우: 레이어 정리, 알파 최소화, Z 정렬.
- 텍스처 메모리 폭발: 압축/아틀라스/LOD 사용.
- 드로우콜 폭증: 배칭/인스턴싱/멀티 드로우.
- CPU 스톨: 동기 호출/락 최소화, 비동기 준비.

## 링크
[[apple-rendering-and-media]], [[apple-performance-and-debug]], [[apple-visionos-spatial]], [[apple-platform-differences]].
