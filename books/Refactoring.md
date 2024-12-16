---
aliases: []
date created: 2024-12-16 12:12:44 +09:00
date modified: 2024-12-16 13:53:25 +09:00
tags: [architecture, book, code-quality, ddd]
title: Refactoring
---
## 1 장. 리팩토링 예시

### 1 단계

- 리팩토링하기 전에 제대로 된 테스트를 마련한다. 테스트는 반드시 자가진단하도록 한다.

### Extract Function

### Inline Variable

- variable 자리를 function 으로 대체하기

### Replace Temp(variable) with Query(function)

### Change Function Declaration

- `Inline Variable` 와 함께 사용됨
- `amountFor(perf, play)` => `amountFor(perf, playFor(perf));`

### Slide Statements

- variable 을 사용되는 곳 근처로 가져옴
- 추후 `Split Loop` 등을 위해 가져옴

### Split Loop

- loop 안에 있는 다른 목적의 로직들을 따로 분리함
- 성능상의 문제? => 부하가 크지 않은 이상 큰 문제가 되지 않고 오히려 분리하는 것이 가독성이 좋아 성능개선에 도움을 줌

### Split Phase

- `Extract Function` 을 사용하는 예시를 보여준다
