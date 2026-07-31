# 실무 안티패턴과 모범 사례 (Anti-Patterns & Best Practices)

## 원자 노트

### 개요
- [04-실무-안티패턴과-모범-사례-anti-patterns-best-practices-00-개요](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices-00-%EA%B0%9C%EC%9A%94.md)

### ❌ 안티패턴 1: Composable 영역에서 직접 API 호출
- [01-안티패턴-1-composable-영역에서-직접-api-호출](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/01-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4-1-composable-%EC%98%81%EC%97%AD%EC%97%90%EC%84%9C-%EC%A7%81%EC%A0%91-api-%ED%98%B8%EC%B6%9C.md)

### 모범 사례 1: ViewModel 상태 수집 및 Action 처리
- [02-모범-사례-1-viewmodel-상태-수집-및-action-처리](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/02-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-1-viewmodel-%EC%83%81%ED%83%9C-%EC%88%98%EC%A7%91-%EB%B0%8F-action-%EC%B2%98%EB%A6%AC.md)

### ❌ 안티패턴 2: 비-코루틴 콜백에서 LaunchedEffect 실행 시도
- [03-안티패턴-2-비-코루틴-콜백에서-launchedeffect-실행-시도](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/03-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4-2-%EB%B9%84-%EC%BD%94%EB%A3%A8%ED%8B%B4-%EC%BD%9C%EB%B0%B1%EC%97%90%EC%84%9C-launchedeffect-%EC%8B%A4%ED%96%89-%EC%8B%9C%EB%8F%84.md)

### 모범 사례 2: `rememberCoroutineScope` 사용
- [04-모범-사례-2-remembercoroutinescope-사용](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/04-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-2-remembercoroutinescope-%EC%82%AC%EC%9A%A9.md)

### ❌ 안티패턴 3: State 업데이트 지연을 방지하고자 Effect를 무분별하게 재생성
- [05-안티패턴-3-state-업데이트-지연을-방지하고자-effect를-무분별하게-재생성](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/05-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4-3-state-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8-%EC%A7%80%EC%97%B0%EC%9D%84-%EB%B0%A9%EC%A7%80%ED%95%98%EA%B3%A0%EC%9E%90-effect%EB%A5%BC-%EB%AC%B4%EB%B6%84%EB%B3%84%ED%95%98%EA%B2%8C-%EC%9E%AC%EC%83%9D%EC%84%B1.md)

### 모범 사례 3: `rememberUpdatedState`로 해결
- [06-모범-사례-3-rememberupdatedstate로-해결](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices/06-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-3-rememberupdatedstate%EB%A1%9C-%ED%95%B4%EA%B2%B0.md)
