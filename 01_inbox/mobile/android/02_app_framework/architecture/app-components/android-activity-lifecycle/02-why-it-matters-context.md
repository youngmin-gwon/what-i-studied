---
title: 02-why-it-matters-context
tags: []
aliases: []
date modified: 2026-07-31 16:28:41 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 💡 Why it matters (Context)

- **Data Loss**: 사용자가 긴 글을 쓰다가 홈 화면으로 나갔습니다. 유튜브 좀 보다가 돌아왔는데 글이 다 날아갔다면? 이는 **Process Death** 처리를 안 했기 때문입니다.
- **Wrong Architecture**: `ViewModel` 은 회전에는 살아남지만, 프로세스 킬에서는 죽습니다. 이를 모르면 "ViewModel 이 만능이다"라고 착각하게 됩니다.
- **Memory Leaks**: `Context` 를 `static` 변수나 싱글톤에 잘못 저장하면 Activity 가 영원히 메모리에서 해제되지 않습니다.

---
