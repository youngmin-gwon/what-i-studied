---
title: 04-bom-매핑-및-릴리즈-규칙
tags: []
aliases: []
date modified: 2026-07-31 17:35:57 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## BOM 매핑 및 릴리즈 규칙

- **BOM 버전 표기**: 연도, 월, 일 단위의 날짜(`YYYY.MM.DD`) 형식으로 정의됩니다.
- **매핑 목록 확인**: 각 BOM 날짜 버전이 구체적으로 어떤 하위 Compose 라이브러리 버전을 들고 있는지 확인하려면 [Compose BOM-to-library mapping table](https://developer.android.com/develop/ui/compose/bom/bom-mapping) 공식 페이지를 참조해야 합니다.
- **릴리즈 반영**: 새 BOM 버전이 출시된다고 해서 모든 Compose 라이브러리의 버전이 다 오르는 것은 아닙니다. 업데이트가 없는 모듈은 이전 버전으로 매핑이 그대로 유지됩니다.

---
