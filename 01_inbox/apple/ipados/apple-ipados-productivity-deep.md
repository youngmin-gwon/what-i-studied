# iPadOS Productivity Deep Dive #apple #ipados #productivity

iPadOS의 큰 화면과 멀티태스킹을 살려 생산성 앱을 만들기 위한 가이드. 용어는 [[apple-glossary]].

## 큰 화면 전략
- 사이드바/3-pane 레이아웃: 탐색/리스트/디테일 구조로 정보를 많이 보여준다.
- 키보드/포인터/펜슬/터치 모두 고려. 포인터 hover, 키보드 단축키, 펜슬 더블탭.
- 외장 디스플레이: 별도 해상도/비율/색역. 어느 디스플레이에 창을 띄울지 설계.

## 멀티 윈도우/스테이지 매니저
- UIScene/SwiftUI WindowGroup으로 여러 창을 만든다.
- Stage Manager에서 창을 겹치고 크기를 조절할 수 있다. 최소/최대 사이즈를 잘 지원.
- Split View/Slide Over도 여전히 사용되므로 레이아웃이 유연해야 한다.

## 입력 & 드래그
- 포인터: 커스텀 포인터 모양, hover 상태 피드백, 작은 터치 타깃 피하기.
- 펜슬: Scribble 텍스트 입력, 필기 영역 감지, 샘플링/압력/기울기 처리.
- Drag & Drop: 파일/텍스트/이미지를 다른 앱/창으로 이동. UTType 선언, 임시 파일/보안 북마크 처리.

## 파일/스토리지
- Files 앱 통합: UIDocumentPicker, 보안 북마크, App Groups로 공유 컨테이너 활용.
- 외장 드라이브/네트워크 드라이브(NAS) 지원. 대용량 파일은 스트리밍/청크 업로드.

## 생산성 기능
- 단축키(Command/Option/Control)와 커맨드 메뉴(UIKeyCommand/UIMenu) 제공.
- 검색/Spotlight/Shortcuts 통합으로 빠른 진입점 제공.
- 멀티 셀렉션, 컨텍스트 메뉴(UIContextMenuInteraction)로 마우스/터치 모두 친화적 인터랙션.

## 협업/공유
- Share extension/SharePlay/Facetime 통합. 실시간 협업은 WebSocket/CloudKit으로 동기화.
- iCloud Drive/CloudKit/서버 기반 협업 시 충돌 해결 정책 명시.

## 성능/전원
- 여러 창이 있어도 백그라운드 제한은 iOS와 비슷. 무거운 작업은 분할/비동기로.
- 메모리 사용이 커질 수 있으니 이미지/데이터 캐시를 관리.

## 접근성/국제화
- 큰 화면에서 Dynamic Type/RTL/다국어 확장을 고려. 포인터/키보드/펜슬 사용자도 접근성 대상.
- 멀티 윈도우 상태에서도 VoiceOver 포커스가 올바르게 이동하는지 확인.

## 테스트 시나리오
- Split View/Slide Over/Stage Manager/외장 디스플레이 조합.
- 포인터/터치/펜슬/키보드 입력 혼합.
- 파일 선택/드래그/보안 북마크/권한 흐름.

## 링크
[[apple-ipados-multitasking]], [[apple-app-lifecycle-and-ui]], [[apple-storage-and-filesystems]], [[apple-network-basics]], [[apple-performance-and-debug]].
