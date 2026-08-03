---
title: "Scoped Storage는 앱이 자신의 공간과 공유 미디어에만 접근하도록 제한하는 저장소 모델이다"
tags: ["android", "android/glossary"]
aliases: ["Android scoped storage"]
date modified: 2026-08-01 01:07:32 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# Scoped Storage는 앱이 자신의 공간과 공유 미디어에만 접근하도록 제한하는 저장소 모델이다

정의: Scoped Storage 는 shared external storage 에 대한 직접 파일 경로 접근을 제한하고, app-specific directory, MediaStore, SAF, photo picker 같은 목적별 access surface 를 사용하게 하는 storage policy 다.

혼동 방지: Scoped Storage 는 모든 파일 접근 금지가 아니다. 파일의 소유자와 공개 목적에 따라 API 선택이 달라지고, 권한 요청보다 user-mediated access 가 더 적합한 경우가 많다.

정본 링크:

- [Scoped storage contract](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/scoped-storage-limits-direct-shared-storage-access.md)
- [File storage selection](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-storage-is-selected-by-owner-and-public-purpose.md)
