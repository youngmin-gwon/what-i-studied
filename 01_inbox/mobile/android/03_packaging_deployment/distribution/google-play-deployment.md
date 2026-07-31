---
title: google-play-deployment
tags: [android, deployment, google-play, ci-cd]
aliases: [구글 플레이 배포 가이드]
date modified: 2026-04-07 10:40:00 +09:00
date created: 2026-04-04 15:20:00 +09:00
---

## [[android-gradle-build-system]] > [[google-play-deployment]]

### Google Play Store: Publishing & App Bundle Management

안드로이드 앱을 전 세계 사용자에게 배포하기 위한 구글 플레이 스토어의 핵심 프로세스와 관련 기술적 요구사항을 정리합니다.

---

#### 📦 1. 저장방식의 변화: AAB (Android App Bundle)

구글은 기존의 APK 배포 방식을 지양하고 **Android App Bundle (.aab)** 형식을 강제하고 있습니다.

- **Dynamic Delivery**: 사용자의 기기 사양(화면 밀도, CPU 아키텍처, 언어)에 맞는 최적화된 APK 만 생성하여 전송 (다운로드 크기 15~20% 감소).
- **Asset Packs**: 대용량 게임 에셋 등을 사용자가 필요한 시점에 다운로드하도록 설정 가능.
- **Play Core Library**: 앱 업데이트 확인 및 다운로드를 앱 실행 중에 제어.

---

#### 🔐 2. Play App Signing (구글 관리 서명)

배포용 키(Signing Key)를 구글이 안전하게 보관하고 관리하는 시스템입니다.

- **Upload Key**: 개발자가 구글 플레이 콘솔로 번들을 올릴 때 사용하는 키.
- **Deployment Key**: 구글이 최종 사용자에게 전달할 APK 로 재서명할 때 사용하는 키.
- **Key Recovery**: 업로드 키 분실 시 구글을 통해 재설정이 가능하여 영구적인 배포 중단 방지.

---

#### 🧪 3. 릴리스 관리 및 테스팅

- **내부 테스트**: 최대 100명에게 즉시 배포하여 팀 내부 검증.
- **비공개 테스트 (Alpha/Beta)**: 특정 그룹 또는 화이트리스트 사용자 대상.
- **공개 테스트**: 스토어 검색을 통해 누구나 참여 가능한 오픈 베타.
- **단계적 출시 (Staged Rollout)**: 신규 버전을 1% -> 5% -> 20% 등 점진적으로 확대하며 예기치 못한 크래시나 사용자 피드백 대응.

---

#### 🛡️ 4. 배포 안전성 도구

- **Play Integrity API**: 기기가 루팅되었거나 수정한 흔적이 있는지, 앱이 원본인지 서버 측에서 무결성 검증.
- **Store Listing Experiment**: A/B 테스트를 통한 앱 아이콘, 스크린샷, 설명 문구의 전환율 최적화.

---

#### 📚 See Also
- [[android-gradle-build-system]] - 아티팩트 생성 및 서명(Signing)
- [[android-cicd-patterns]] - 자동화된 배포 파이프라인
- [[android-security-play-integrity]] - Play Integrity API 실무
