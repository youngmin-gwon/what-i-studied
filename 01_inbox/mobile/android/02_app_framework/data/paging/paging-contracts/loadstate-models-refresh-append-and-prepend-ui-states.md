---
title: "LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다"
tags: [android, android/data, android/paging]
aliases: ["LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다

Paging의 loading/error UI는 별도 boolean 몇 개로 흩어뜨리기보다 `LoadState`로 표현한다. `refresh`는 초기 또는 전체 갱신, `append`는 뒤쪽 추가 loading, `prepend`는 앞쪽 추가 loading 상태를 나타낸다.

각 상태는 loading, error, not loading을 구분하고 retry UI와 empty/loading/error surface를 결정하게 한다. `RemoteMediator`를 쓰면 source와 mediator load state가 나뉘므로, cache가 비어 있는지와 network sync 중인지를 구분해 표현해야 한다.

## 판단 기준

- full-screen loading은 보통 `refresh`와 item count를 함께 보고 결정한다.
- append/prepend loading은 list footer/header처럼 기존 content를 유지한 상태로 표현한다.
- retry는 실패한 load type에 맞게 연결하고 전체 새로고침과 page retry를 섞지 않는다.
- empty state는 loading이 끝났고 item이 없는 상태인지 확인한 뒤 보여준다.

관련 노트: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md), [RemoteMediator는 network page와 local cache를 연결한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/remote-mediator-connects-network-pages-to-local-cache.md)

공식 문서: [Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state)
