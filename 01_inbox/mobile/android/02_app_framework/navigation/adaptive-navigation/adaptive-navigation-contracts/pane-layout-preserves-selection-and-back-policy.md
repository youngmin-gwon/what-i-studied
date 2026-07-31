# Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다

List-detail이나 supporting pane layout에서는 보이는 pane 수와 선택된 content state가 같은 것이 아니다. Expanded window에서는 list와 detail을 동시에 보여줄 수 있지만 compact window에서는 같은 선택 상태를 단일 pane navigation으로 표현해야 한다.

따라서 pane visibility, selected item, detail route, back action을 분리해서 설계한다. 창 크기가 바뀌어도 사용자가 선택한 대상과 back 의미가 바뀌지 않아야 한다.

공식 문서: [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)
