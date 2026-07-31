# Paging item diffing은 identity와 content 비교를 분리한다

Paging UI는 새 page가 들어올 때 전체 list를 다시 그리는 대신 item identity와 content 비교로 변경 범위를 계산한다. RecyclerView에서는 `DiffUtil.ItemCallback`, Compose에서는 안정적인 key/content type 설계가 이 역할을 한다.

`areItemsTheSame`은 같은 도메인 객체인지 판단하고, `areContentsTheSame`은 표시 내용이 바뀌었는지 판단한다. identity와 content를 섞으면 item animation, scroll position, partial update가 흔들릴 수 있다.
