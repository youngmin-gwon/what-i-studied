---
title: staged-rollout-is-observable-release-operation
tags: ["android", "staged-rollout", "play-console", "vitals"]
aliases: ["단계적 출시는 관측 가능한 릴리스 운영 절차다"]
date created: 2026-07-31 17:52:17 +09:00
date modified: 2026-08-04 15:35:00 +09:00
created: 2026-07-31 17:52:17 +09:00
updated: 2026-08-04 15:35:00 +09:00
---

## 단계적 출시는 관측 가능한 릴리스 운영 절차다

### 내부 메커니즘 (Internal Mechanism)
**단계적 출시 (Staged Rollout)**는 신규 프로덕션 릴리스의 영향을 전체 사용자 데이터베이스로 일시에 전파하지 않고, 무작위 사용자 비율(예: 1% -> 5% -> 20% -> 50% -> 100%)을 점진적으로 상향시키는 릴리스 관측 운영 절차다.
- **실시간 비탈스 모니터링**: 릴리스 각 단계에서 Google Play Console의 Android Vitals (Crash Rate, ANR Rate) 및 Firebase Crashlytics 지표를 모니터링한다.
- **출시 중단 (Halt Rollout)**: 치명적인 런타임 크래시가 포착되면 진행 중인 단계적 출시를 중단할 수 있다. (이미 다운로드받은 사용자 외 추가 사용자에게 전파 금지)
- **Emergency Hotfix Update**: 중단 상태에서 동일 트랙에 `versionCode`를 높인 핫픽스 AAB를 등록하면 기존 출시 비율을 유지하면서 핫픽스 패치가 덮어씌워진다.

```mermaid
flowchart TD
    StartRollout["Start Staged Rollout (1% Target Audience)"] --> MonitorVitals{"Monitor Android Vitals & Crashlytics"}
    MonitorVitals -->|Crash Rate < 1.0%| IncreasePercentage["Increase Rollout (5% -> 20% -> 100%)"]
    MonitorVitals -->|Crash Rate > 1.0% (Anomaly)| Halt["Halt Rollout Immediately"]
    Halt --> Hotfix["Build & Upload Hotfix AAB (versionCode + 1)"]
    Hotfix --> Resume["Resume Rollout with Hotfix"]
    IncreasePercentage --> Production100["100% Fully Released"]
```

### 코드 예시 (Play Publisher Gradle Staged Rollout Config)
```kotlin
// app/build.gradle.kts (Gradle Play Publisher)
play {
    track.set("production")
    userFraction.set(0.10) // 10% 단계적 출시 지정
    releaseStatus.set(com.github.triplet.gradle.play.enum.ReleaseStatus.IN_PROGRESS)
}
```

### 관측 가능 증거 (Observable Evidence)
Play Developer API를 통해 관측된 현재 릴리스 버전의 단계적 출시 비율 및 상태 로그를 관측할 수 있다:

```bash
# Play Developer API Track Status Query
gcloud play-developer-api tracks get --package-name com.example.app --track production

# Output Response Example:
# {
#   "releases": [{
#     "name": "1.2.0",
#     "userFraction": 0.10,
#     "status": "inProgress"
#   }]
# }
```

관련 노트: [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md), [Play 릴리스와 배포 계약](release-distribution-contracts.md)
