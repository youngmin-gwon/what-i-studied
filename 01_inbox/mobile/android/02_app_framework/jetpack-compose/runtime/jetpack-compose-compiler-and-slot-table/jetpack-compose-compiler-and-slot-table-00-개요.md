# Jetpack Compose Compiler & Slot Table Deep Dive 개요

이 문서는 Jetpack Compose 내부에서 UI 트리가 어떻게 구성되고 변경 사항을 감지하는지, 그 중심에 있는 `@Composable` 어노테이션의 컴파일러 변환 원리와
런타임 저장 구조인 **Slot Table**, 그리고 **위치 기반 메모이제이션(Positional Memoization)**의 메커니즘을 상세히 다룹니다.

---
