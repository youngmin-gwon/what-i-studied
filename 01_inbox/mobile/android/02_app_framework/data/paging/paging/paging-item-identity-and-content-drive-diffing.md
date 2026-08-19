---
title: paging-item-identity-and-content-drive-diffing
tags: [android, android/data, android/paging]
aliases: ["Paging item diffing은 identity와 content 비교를 분리한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Paging item diffing 은 identity 와 content 비교를 분리한다

Paging UI 는 새 page 가 들어올 때 전체 list 를 다시 그리는 대신 item identity 와 content 비교로 변경 범위를 계산한다. RecyclerView 에서는 `DiffUtil.ItemCallback`, Compose 에서는 안정적인 key/content type 설계가 이 역할을 한다.

`areItemsTheSame` 은 같은 도메인 객체인지 판단하고, `areContentsTheSame` 은 표시 내용이 바뀌었는지 판단한다. identity 와 content 를 섞으면 item animation, scroll position, partial update 가 흔들릴 수 있다.

```kotlin
object BenefitDiffCallback : DiffUtil.ItemCallback<Benefit>() {
    override fun areItemsTheSame(old: Benefit, new: Benefit): Boolean =
        old.id == new.id // 서버 id: 지속적 정체성

    override fun areContentsTheSame(old: Benefit, new: Benefit): Boolean =
        old == new // data class 전체 비교: 표시 내용 변경 여부
}
```

`areItemsTheSame` 에 `old == new` 처럼 content 비교를 넣으면, 같은 항목이라도 필드 값이 바뀌는 순간 `DiffUtil` 은 이를 "삭제 후 새 항목 삽입"으로 판단해 불필요한 item animation 과 함께 `RecyclerView` 의 스크롤 위치가 튀는 형태로 버그가 드러난다. 반대로 `areItemsTheSame` 에 항상 `true` 를 반환하면 서로 다른 항목이 같은 것으로 취급되어 갱신이 누락된다.

### 판단 기준

- identity 는 database primary key 나 server id 처럼 항목의 지속적 정체성을 나타내야 한다.
- content 비교는 화면에 표시되는 값의 변경 여부를 기준으로 한다.
- Compose Lazy list 에서는 stable key 를 주어 item state 와 scroll anchoring 이 흔들리지 않게 한다.
- placeholder 를 쓰는 경우 null item 과 실제 item 의 rendering path 를 분리한다.

관련 노트: [LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다](./loadstate-models-refresh-append-and-prepend-ui-states.md)
