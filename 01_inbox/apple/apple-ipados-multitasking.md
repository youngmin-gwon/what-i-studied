---
title: apple-ipados-multitasking
tags: [apple, ipados, multitasking]
aliases: []
date modified: 2025-12-16 16:15:30 +09:00
date created: 2025-12-16 16:14:02 +09:00
---

## iPadOS Multitasking & Productivity apple ipados multitasking

iPadOS 에서 멀티 윈도우/포인터/외장 디스플레이를 다룰 때 알아둘 포인트를 쉽게 정리했다. 용어는 [[apple-glossary]].

### 멀티 윈도우
- Scene 기반으로 여러 창을 만들 수 있다. UIScene/WindowGroup 을 활용.
- Stage Manager: 창을 겹치고 크기를 조절. 외장 디스플레이에 별도 워크스페이스를 둘 수 있다.
- Split View/Slide Over: 두세 개 앱을 나란히 띄울 수 있는 전통 멀티태스킹.

### 입력
- 포인터/트랙패드/마우스: Hover 효과, 커스텀 포인터 모양 지정 가능.
- 펜슬: 저지연 필기, Scribble(텍스트 입력), 예측/샘플링 속도 최적화 필요.
- 키보드: 단축키, 커맨드 메뉴, 하드웨어 키보드 이벤트 처리.

### 레이아웃
- Size Class/traitCollection 을 적극 활용. 가로/세로, 분할/풀스크린마다 레이아웃이 달라진다.
- 외장 디스플레이: 해상도/scale/색역이 달라질 수 있다. 새 창을 어느 화면에 띄울지 결정해야 한다.

### 드래그&드롭
- UIKit/SwiftUI 모두 지원. 파일/텍스트/이미지 등 유니버설 타입. 여러 창/앱 간 전송 가능.
- 드롭 대상은 적절한 UTI/UTType 을 선언하고, 샌드박스 규칙에 맞춰 파일을 복사한다.

### 파일 접근
- Files 앱과 긴밀히 통합. UIDocumentPicker 로 사용자 선택 파일에 접근, Security-scoped bookmark 필요.
- 외장 스토리지/네트워크 드라이브도 Files 를 통해 접근.

### 성능/전력
- 큰 화면/여러 창으로 CPU/GPU 사용량이 늘 수 있다. 프레임 타깃/리소스 사용을 조정.
- 백그라운드 제한은 여전히 iOS 와 비슷하므로, 많은 창이 있어도 작업 시간을 남용할 수 없다.

### 링크

[[apple-app-lifecycle-and-ui]], [[apple-rendering-and-media]], [[apple-storage-and-filesystems]], [[apple-platform-differences]].
