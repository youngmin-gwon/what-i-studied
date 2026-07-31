# ⚔️ Comparison: RecyclerView vs LazyColumn

##### RecyclerView (View)
- **Recycling**: 뷰 객체(`ViewHolder`)를 버리지 않고 재활용합니다.
- **Adapter**: 데이터와 뷰를 연결하는 **지루한 보일러플레이트**가 필요합니다.
- **ViewType**: 뷰 종류가 많아지면 `getItemViewType()` 관리가 지옥이 됩니다.

##### LazyColumn (Compose)
- **No Recycling**: Compose 는 뷰 객체가 없으므로 재활용할 필요가 없습니다. 그냥 필요한 컴포저블을 **새로 호출(Emit)**하면 됩니다. (Gap Buffer 덕분에 비용이 매우 쌉니다)
- **Code**: `items(list) { item -> Text(item) }`. 끝입니다.

---
