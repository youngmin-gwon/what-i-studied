---
title: android-ndk-jni
tags: []
aliases: []
date modified: 2026-04-07 10:31:48 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-ndk-jni](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni.md)

### Native Development: NDK & JNI

안드로이드에서 C/C++ 코드를 실행하기 위한 **NDK(Native Development Kit)**와 Java/Kotlin 코드와의 가교 역할을 하는 **JNI(Java Native Interface)** 기술을 분석합니다.

성능 최적화, 기존 네이티브 라이브러리 재사용, 그리고 리버스 엔지니어링 방어를 위한 고수준의 보안성 확보가 핵심 목표입니다.

---

---

## 원자 노트

- [💡 Context: 네이티브 개발의 가치](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/01-context-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-%EA%B0%9C%EB%B0%9C%EC%9D%98-%EA%B0%80%EC%B9%98.md)
- [NDK 란](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/02-ndk-%EB%9E%80.md)
- [프로젝트 설정](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/03-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%84%A4%EC%A0%95.md)
- [CMakeLists.txt](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/04-cmakelists-txt.md)
- [JNI 기본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/05-jni-%EA%B8%B0%EB%B3%B8.md)
- [JNI 타입 매핑](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/06-jni-%ED%83%80%EC%9E%85-%EB%A7%A4%ED%95%91.md)
- [문자열 처리](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/07-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%B2%98%EB%A6%AC.md)
- [배열 처리](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/08-%EB%B0%B0%EC%97%B4-%EC%B2%98%EB%A6%AC.md)
- [객체와 메서드 호출](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/09-%EA%B0%9D%EC%B2%B4%EC%99%80-%EB%A9%94%EC%84%9C%EB%93%9C-%ED%98%B8%EC%B6%9C.md)
- [Bitmap 처리](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/10-bitmap-%EC%B2%98%EB%A6%AC.md)
- [전역 참조 (Global Reference)](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/11-%EC%A0%84%EC%97%AD-%EC%B0%B8%EC%A1%B0-global-reference.md)
- [스레딩](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/12-%EC%8A%A4%EB%A0%88%EB%94%A9.md)
- [예외 처리](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/13-%EC%98%88%EC%99%B8-%EC%B2%98%EB%A6%AC.md)
- [성능 최적화](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/14-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [디버깅](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/15-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [See Also](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni/16-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
