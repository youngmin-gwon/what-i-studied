# Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다

Navigation animation은 실제 navigation state와 분리된 장식이 아니다. `NavDisplay` transition, pop transition, predictive back 중간 상태는 모두 같은 back stack 변경을 기준으로 움직여야 한다.

사용자가 back gesture를 취소하거나 완료할 때 app back stack, visible entry, transition state가 서로 다르면 화면은 되돌아왔지만 state는 pop된 상태 같은 불일치가 생긴다. 시스템 back과 앱 내부 back action은 하나의 stack mutation policy로 모은다.
