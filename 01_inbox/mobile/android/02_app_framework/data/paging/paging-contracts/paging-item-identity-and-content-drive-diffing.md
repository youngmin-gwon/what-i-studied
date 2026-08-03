---
title: paging-item-identity-and-content-drive-diffing
tags: [android, android/data, android/paging]
aliases: ["Paging item diffing은 identity와 content 비교를 분리한다"]
date modified: 2026-08-03 18:07:56 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Paging item diffing 은 identity 와 content 비교를 분리한다

Paging UI 는 새 page 가 들어올 때 전체 list 를 다시 그리는 대신 item identity 와 content 비교로 변경 범위를 계산한다. RecyclerView 에서는 `DiffUtil.ItemCallback`, Compose 에서는 안정적인 key/content type 설계가 이 역할을 한다.

`areItemsTheSame` 은 같은 도메인 객체인지 판단하고, `areContentsTheSame` 은 표시 내용이 바뀌었는지 판단한다. identity 와 content 를 섞으면 item animation, scroll position, partial update 가 흔들릴 수 있다.

### 판단 기준

- identity 는 database primary key 나 server id 처럼 항목의 지속적 정체성을 나타내야 한다.
- content 비교는 화면에 표시되는 값의 변경 여부를 기준으로 한다.
- Compose Lazy list 에서는 stable key 를 주어 item state 와 scroll anchoring 이 흔들리지 않게 한다.
- placeholder 를 쓰는 경우 null item 과 실제 item 의 rendering path 를 분리한다.

관련 노트: [LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/loadstate-models-refresh-append-and-prepend-ui-states.md)
