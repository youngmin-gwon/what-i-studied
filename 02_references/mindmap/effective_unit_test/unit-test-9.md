---
title: unit-test-9
tags: []
aliases: []
date modified: 2025-11-07 08:44:53 +09:00
date created: 2024-12-09 21:31:10 +09:00
mindmap-plugin: basic
---

## Speeding up<br/>test execution

### how to make<br/>test code run faster
- Don't sleep unless you are tired
   - thread.sleep
   - a surprisingly common issue
- Watch out for redundant setup and teardown
   - it runs regardless of whether they need
   - redundancy is harder to see and<br/>sometimes your trivial fix doesn't work<br/>because there is no redundancy after all
      - Instead, perform an immutable,<br/>side-effect-free operation again and again
- Be picky about who you invite to your test
   - Run less code as part of those tests
   - Replace compute-intensive components<br/>with test doubles
- Stay local, stay fast
   - network down or web service timeout
   - Avoid making network call in your unit tests
- Resist the temptation to hit the database
   - Fake the collaborator<br/>as close to the code under test as possible
- There is no slower I/O than file I/O
   - Cache data in memory
   - Turning off logging is huge

### why speed needs?
- we lose the flow
- we trigger off the build
- delayed feedback causes trouble
   - if test is slow, then devs only run a subset of
      their test suites before checking in

### how to find the bottleneck
- Identify the hot spots and<br/>and figure out why<br/>the performance is what it is
- Avoid making assumptions<br/>about what the problem is, and,<br/>instead, gather data about the situation<br/>by analyzing the test execution
- Profile test
