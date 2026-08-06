---
title: android-paging-map
tags: [android, architecture, paging3, flow, room]
aliases: [Android Paging 지식 지도]
date modified: 2026-08-06 18:35:00 +09:00
date created: 2026-08-04 16:00:00 +09:00
---

# Android Paging 지식 지도

## 1. 개요

Android Paging 3 라이브러리는 대용량 데이터를 메모리 효율적으로 지연 청크 로딩(Lazy Loading)하기 위한 아키텍처 라이브러리입니다.

---

## 2. Paging 3 단일 진실 출처 (SSOT) 및 세부 계약 노드

- **[Paging 3 표준 레퍼런스](../../paging-3.md)** - Paging 3 아키텍처 및 뷔페 음식 접시 비유 (SSOT)
- [Pager 및 PagingData Flow 생성 규칙](paging-contracts/pager-exposes-pagingdata-flow-from-pagingsource-factory.md)
- [PagingSource 청크 로딩 규칙](paging-contracts/paging-source-loads-one-page-and-returns-keys.md)
- [Paging Item Identity 및 Diffing 규칙](paging-contracts/paging-item-identity-and-content-drive-diffing.md)
- [cachedIn 수명주기 결합 규칙](paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md)
