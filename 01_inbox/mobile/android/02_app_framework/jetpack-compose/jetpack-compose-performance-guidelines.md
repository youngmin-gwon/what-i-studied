# Jetpack Compose 코드 수준 성능 최적화 가이드

이 문서는 Android Dev Summit ("More performance tips for Jetpack Compose") 세션 내용을 바탕으로, Jetpack Compose UI 작성 시 불필요한 리컴포지션(Recomposition)을 차단하고 렌더링 성능을 극대화하기 위한 **코드 수준의 최적화 규칙**을 정리합니다.

---

---

## 원자 노트

- [[01-성능-최적화의-대전제-loop-cycle-measure-debug-improve|성능 최적화의 대전제: Loop Cycle (Measure -> Debug -> Improve)]]
- [[02-상태-읽기-지연-defer-state-reads|상태 읽기 지연 (Defer State Reads)]]
- [[03-derivedstateof의-올바른-활용|DerivedStateOf의 올바른 활용]]
- [[04-reportfullydrawn-api를-이용한-시작-성능-최적화|`reportFullyDrawn` API를 이용한 시작 성능 최적화]]
- [[05-system-tracing-perfetto-기반-원인-디버깅|System Tracing & Perfetto 기반 원인 디버깅]]
- [[06-boxwithconstraints-사용-시-주의사항-및-대체-방안|BoxWithConstraints 사용 시 주의사항 및 대체 방안]]
- [[07-remember-내-무거운-연산-heavy-computation-격리|`remember` 내 무거운 연산(Heavy Computation) 격리]]
- [[08-비동기-이미지-로딩-asynchronous-image-loading|비동기 이미지 로딩 (Asynchronous Image Loading)]]
- [[09-무거운-프레임-heavy-frames-분해-및-스케줄링|무거운 프레임 (Heavy Frames) 분해 및 스케줄링]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
