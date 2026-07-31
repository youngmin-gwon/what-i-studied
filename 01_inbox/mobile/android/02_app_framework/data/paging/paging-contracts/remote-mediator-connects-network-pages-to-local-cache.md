# RemoteMediator는 network page와 local cache를 연결한다

`RemoteMediator`는 network와 local database가 함께 있는 layered source에서 boundary 역할을 한다. UI는 local cache에서 읽고, mediator는 refresh/append/prepend 시점에 network page를 가져와 database를 갱신한다.

이 구조에서는 source of truth가 network response가 아니라 local database가 된다. offline, retry, sync indicator, invalidation 정책은 paging 자체보다 persistence와 synchronization contract로 같이 판단해야 한다.

관련 정본: [Persistence contracts](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).
