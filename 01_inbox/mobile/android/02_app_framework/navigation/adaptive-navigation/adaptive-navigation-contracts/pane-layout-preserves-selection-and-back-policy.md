---
title: "Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다"
tags: [android, android/navigation, android/adaptive]
aliases: ["Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다

List-detail이나 supporting pane layout에서는 보이는 pane 수와 선택된 content state가 같은 것이 아니다. Expanded window에서는 list와 detail을 동시에 보여줄 수 있지만 compact window에서는 같은 선택 상태를 단일 pane navigation으로 표현해야 한다.

따라서 pane visibility, selected item, detail route, back action을 분리해서 설계한다. 창 크기가 바뀌어도 사용자가 선택한 대상과 back 의미가 바뀌지 않아야 한다.

## 판단 기준

- selected item은 pane visibility보다 오래 살아야 하는 screen state로 둔다.
- compact에서 detail로 들어간 뒤 back이 list로 돌아오는지 검증한다.
- expanded에서 list와 detail을 동시에 보여도 route stack 의미는 유지한다.
- back policy와 pane transition을 별도 boolean으로 흩뜨리지 말고 상태 전이로 표현한다.

관련 노트: [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)

공식 문서: [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)
