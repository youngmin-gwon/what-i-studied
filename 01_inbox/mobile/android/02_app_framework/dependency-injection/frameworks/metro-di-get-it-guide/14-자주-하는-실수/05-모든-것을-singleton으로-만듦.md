# 모든 것을 singleton으로 만듦

`get_it`을 오래 쓰면 모든 것을 `registerSingleton`으로 등록하고 싶어질 수 있습니다.

하지만 Metro에서는 먼저 이렇게 생각하는 편이 좋습니다.

```text
상태가 없고 가벼운 객체인가?
-> unscoped로 시작

생성 비용이 크거나 공유 상태를 가져야 하나?
-> scope 적용

Activity/ViewModel 수명에 묶여야 하나?
-> AppScope에 넣지 말고 더 좁은 graph 고려
```

---
