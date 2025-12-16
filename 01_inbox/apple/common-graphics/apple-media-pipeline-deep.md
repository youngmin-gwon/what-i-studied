# Media Pipeline Deep Dive (공통) #apple #media #avfoundation

오디오/비디오/캡처/재생 흐름을 쉽게 풀어쓴다. 용어는 [[apple-glossary]].

## 큰 그림
- AVFoundation이 카메라/마이크/파일/네트워크 스트림을 관리한다.
- 캡처, 인코딩, 디코딩, 합성, 출력까지 파이프라인이 이어져 있다.
- 권한(TCC), 전원, 성능을 항상 고려해야 한다.

## 캡처(AVCapture)
- Session → Input(카메라/마이크) → Output(사진, 동영상, 데이터) 구성.
- 프리셋으로 해상도/프레임/코덱을 선택. 기기별 지원 목록 확인.
- 권한: NSCameraUsageDescription/NSMicrophoneUsageDescription 필수.
- 카메라 위치/줌/포커스/노출/화이트밸런스 제어 가능. 값 변경 시 스레드 안전 주의.

## 사진/비디오 저장
- 사진 라이브러리에 저장하려면 Photo Library 권한이 필요. Photos picker(제한 접근) 권장.
- 파일 크기가 크면 백그라운드 업로드/저장, HLS/HEVC/ProRes는 기기 지원 확인.

## 재생(AVPlayer)
- AVPlayer/AVPlayerItem/AVPlayerLayer 또는 SwiftUI VideoPlayer.
- HLS 스트리밍이 기본. 적응형 비트레이트로 네트워크 상태에 따라 품질을 바꾼다.
- Picture-in-Picture(iOS/iPadOS/tvOS) 지원 시 오디오 세션/백그라운드 모드 설정.

## 오디오 세션
- AVAudioSession 카테고리 설정(Playback, Record, PlayAndRecord, SoloAmbient 등).
- 중단(전화/Siri/알림) 알림을 받고 복구한다.
- Bluetooth/이어폰/스피커 라우팅, AirPlay/Handoff 고려.

## 오디오 엔진
- AVAudioEngine/AudioUnit로 저지연 처리. 샘플레이트/버퍼 크기 설정으로 지연을 조절.
- watchOS는 지연/전력 제약이 크므로 단순 경로 권장.

## DRM/FairPlay
- FPS로 라이선스 키를 받아 암호화 스트림을 해독한다.
- 키 요청/응답은 안전한 채널로, 테스트/프로덕션 환경을 구분.

## 자막/텍스트
- AVPlayerItemLegibleOutput로 자막, 여러 언어 트랙. WebVTT/CEA-608/708 지원.
- 접근성: 자막 스타일, 오디오 설명 제공.

## 성능/전력 팁
- 캡처 해상도를 필요 이상으로 높이지 않는다.
- 디코딩/인코딩은 CPU/GPU 부담이 크므로, 비트레이트/프레임레이트를 상황에 맞게 조정.
- 배터리: 백그라운드 재생/캡처는 정책에 맞는지 확인, 오디오 전용 모드를 활용.

## 테스트 시나리오
- 네트워크 지연/품질 변화(HLS 적응 확인).
- 카메라/마이크 권한 거부/취소.
- 백그라운드/포그라운드 전환, 화면 잠금, 전화/알림 중단.
- 기기/해상도/색역(HDR vs SDR)별 호환성.

## 디버깅
- `AVPlayerItem` status/에러, KVO로 로딩 상태 확인.
- `log stream --predicate 'subsystem == "com.apple.coremedia"'`로 미디어 로그.
- Instruments Media/Time Profiler로 CPU/GPU 사용량 추적.

## 링크
[[apple-rendering-and-media]], [[apple-performance-and-debug]], [[apple-networking-and-cloud]], [[apple-visionos-spatial]].
