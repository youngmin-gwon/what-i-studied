---
title: "Android 메모리는 사용량보다 회수되지 않는 객체를 본다"
tags: ["android", "android/testing-performance"]
---

# Android 메모리는 사용량보다 회수되지 않는 객체를 본다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

메모리 문제는 순간 사용량과 지속적인 보유를 구분해야 한다.

큰 힙 사용량이 곧바로 누수라는 뜻은 아니다.

GC 이후에도 화면 객체가 남아 있으면 참조 경로를 조사한다.

화면을 열고 닫는 시나리오를 여러 번 반복한다.

GC 전후의 힙 덤프를 비교하면 회수되지 않는 객체를 찾기 쉽다.

Activity와 Fragment 인스턴스가 반복해서 증가하면 누수를 의심한다.

수명보다 긴 객체가 Context, View, 콜백을 잡고 있는지 확인한다.

리스너, 코루틴, 관찰자, 스레드가 화면 종료 뒤에도 살아 있을 수 있다.

큰 이미지와 버퍼는 Java 힙 외의 Native 또는 Graphics 메모리를 사용할 수 있다.

따라서 Java 힙만 보고 메모리 압박을 판단하지 않는다.

`dumpsys meminfo`로 Java, Native, Graphics 비율을 함께 본다.

Android Studio Memory Profiler는 객체, 할당 위치, 참조 경로를 확인하는 데 사용한다.

Allocation Tracking은 특정 동작에서 반복 할당되는 경로를 찾는다.

짧은 임시 객체가 많으면 GC 빈도와 프레임 지연이 함께 증가할 수 있다.

큰 목록은 필요한 범위만 읽고 Paging으로 나눈다.

이미지는 적절한 크기로 디코드하고 필요하지 않은 원본 버퍼를 보유하지 않는다.

캐시는 상한과 퇴출 정책이 있어야 한다.

무제한 캐시는 누수처럼 보이는 메모리 증가를 만든다.

[앱 메모리 관리](https://developer.android.com/topic/performance/memory)는 힙, 메모리 압박, 객체 수명 문제를 구분하는 기준이다.

[메모리 프로파일러](https://developer.android.com/studio/profile/memory-profiler)는 힙 덤프와 할당을 조사할 때 사용한다.

LeakCanary는 개발 중 Activity와 Fragment 누수를 빠르게 발견하는 보조 도구다.

네이티브 누수는 Java 참조 그래프만으로 설명되지 않을 수 있다.

이 경우 Perfetto, `meminfo`, 네이티브 할당 도구를 함께 사용한다.

메모리 회귀 테스트에는 화면 반복 진입과 데이터 크기 증가를 포함한다.

수정의 성공 기준은 피크 감소와 GC 이후 안정화 여부다.

프로세스가 종료되지 않았다는 사실만으로 메모리가 건강하다고 판단하지 않는다.
