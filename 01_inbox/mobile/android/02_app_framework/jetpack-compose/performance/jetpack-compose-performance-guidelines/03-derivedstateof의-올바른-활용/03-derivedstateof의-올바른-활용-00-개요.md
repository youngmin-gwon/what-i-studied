# DerivedStateOf의 올바른 활용 개요

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

`derivedStateOf`는 빈번하게 변경되는 상태(예: 스크롤 픽셀 단위 변화)를 바탕으로 **새로운 가공된 상태(예: 리스트의 첫 번째 아이템 표시 여부 등)를 유도할 때** 사용합니다.
