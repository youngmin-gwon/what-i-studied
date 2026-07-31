---
title: "Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다"
tags: ["android", "android/packaging-deployment"]
---

# Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

## 빌드

- [ ] release variant에서 AAB를 생성했다.
- [ ] application ID가 기존 Play 앱과 같다.
- [ ] version code가 기존 배포 버전보다 높다.
- [ ] version name과 변경 로그가 릴리스 목적에 맞다.
- [ ] min SDK, target SDK, ABI, 언어, 리소스 구성을 검토했다.

## 서명

- [ ] AAB가 등록된 업로드 키로 서명됐다.
- [ ] Play App Signing의 앱 서명 인증서 지문을 확인했다.
- [ ] Google API, OAuth, Maps, App Links 등 외부 서비스에 올바른 지문을 등록했다.
- [ ] 업로드 keystore와 비밀번호가 CI 로그나 저장소에 노출되지 않는다.
- [ ] 키 분실·침해 시 업로드 키 재설정과 앱 서명 키 업그레이드를 구분했다.

## 검증

- [ ] 내부 앱 공유로 Play 재서명과 설치를 확인했다.
- [ ] 내부 테스트 트랙에서 설치, 신규 설치, 업데이트를 시험했다.
- [ ] 비공개 또는 공개 테스트 대상과 opt-in 상태를 확인했다.
- [ ] 여러 트랙의 version code가 의도치 않게 사용자 선택을 덮지 않는다.
- [ ] 대표 기기에서 분할 APK와 동적 기능의 지연·실패 UI를 확인했다.

## 출시

- [ ] 첫 공개 게시인지 업데이트인지 구분했다.
- [ ] 업데이트라면 단계적 출시가 가능한 상태인지 확인했다.
- [ ] 초기 대상, 국가 제한, 확대 기준, 관찰 시간을 기록했다.
- [ ] 충돌·ANR·핵심 기능·문의 지표의 담당자를 정했다.
- [ ] 중지 시 이미 업데이트된 사용자는 자동 복귀하지 않음을 알고 대응안을 마련했다.

## 사후 조치

- [ ] 단계적 비율을 수동으로 확대하고 각 시점을 기록했다.
- [ ] 문제가 있으면 추가 배포를 중지하고 수정 version code를 준비한다.
- [ ] 100% 이후 Play Console의 최종 상태와 릴리스 아티팩트를 보관한다.
- [ ] 다음 릴리스에서 재사용할 키·트랙·테스터 정보를 정리한다.

## 승인 기록

- [ ] 빌드 승인자와 Play Console 게시 승인자를 기록했다.
- [ ] 릴리스 version code와 단계적 출시 시작 시각을 기록했다.
- [ ] 장애 시 연락할 담당자와 중지 권한 보유자를 확인했다.

공식 문서: [앱 서명](https://developer.android.com/studio/publish/app-signing), [앱 업데이트](https://developer.android.com/guide/playcore/in-app-updates), [테스트 설정](https://support.google.com/googleplay/android-developer/answer/9845334), [단계적 출시](https://support.google.com/googleplay/android-developer/answer/6346149)

기준일: 2026-07-31. 정책, 검토 절차, 계정 요구사항은 릴리스 직전에 Play Console의 현재 안내를 확인한다.
