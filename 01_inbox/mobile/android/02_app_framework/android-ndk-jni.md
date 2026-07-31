---
title: android-ndk-jni
tags: []
aliases: []
date modified: 2026-04-07 10:31:48 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-ndk-jni]]

### Native Development: NDK & JNI

안드로이드에서 C/C++ 코드를 실행하기 위한 **NDK(Native Development Kit)**와 Java/Kotlin 코드와의 가교 역할을 하는 **JNI(Java Native Interface)** 기술을 분석합니다.

성능 최적화, 기존 네이티브 라이브러리 재사용, 그리고 리버스 엔지니어링 방어를 위한 고수준의 보안성 확보가 핵심 목표입니다.

---

---

## 원자 노트

- [[01-context-네이티브-개발의-가치|💡 Context: 네이티브 개발의 가치]]
- [[02-ndk-란|NDK 란]]
- [[03-프로젝트-설정|프로젝트 설정]]
- [[04-cmakelists-txt|CMakeLists.txt]]
- [[05-jni-기본|JNI 기본]]
- [[06-jni-타입-매핑|JNI 타입 매핑]]
- [[07-문자열-처리|문자열 처리]]
- [[08-배열-처리|배열 처리]]
- [[09-객체와-메서드-호출|객체와 메서드 호출]]
- [[10-bitmap-처리|Bitmap 처리]]
- [[11-전역-참조-global-reference|전역 참조 (Global Reference)]]
- [[12-스레딩|스레딩]]
- [[13-예외-처리|예외 처리]]
- [[14-성능-최적화|성능 최적화]]
- [[15-디버깅|디버깅]]
- [[16-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
