# Navigation 3 metadata 예제의 Kotlin 문법은 navigation 계약이 아니다

Navigation 3 metadata 예제에는 `Map`, `Any`, `object`, `data object`, trailing lambda, infix function, `when`, operator overloading 같은 Kotlin 문법이 함께 등장한다. 이 문법은 예제를 읽기 위한 배경지식이지 navigation state의 핵심 계약은 아니다.

Navigation 관점에서 중요한 것은 metadata가 route entry에 표시 정책을 붙이고, SceneStrategy나 decorator가 그 metadata를 읽어 렌더링을 바꾼다는 점이다. Kotlin 문법 설명은 이 구조를 이해하기 위한 보조 설명으로만 둔다.

따라서 문서를 정리할 때 Kotlin syntax 챕터를 Navigation 3의 독립 도메인으로 유지하지 않는다. metadata의 의미는 [Metadata와 SceneStrategy는 표시 정책을 전달한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md)에 흡수하고, route identity와 stack 상태는 별도 계약으로 읽는다.
