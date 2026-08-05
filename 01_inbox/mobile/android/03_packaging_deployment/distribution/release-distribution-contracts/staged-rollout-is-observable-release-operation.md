---
title: staged-rollout-is-observable-release-operation
tags: ["android", "staged-rollout", "play-console", "vitals"]
aliases: ["단계적 출시는 관측 가능한 릴리스 운영 절차다"]
date created: 2026-07-31 17:52:17 +09:00
date modified: 2026-08-05 16:15:00 +09:00
created: 2026-07-31 17:52:17 +09:00
updated: 2026-08-05 16:15:00 +09:00
---

## 단계적 출시는 관측 가능한 릴리스 운영 절차다

### 내부 메커니즘 (Internal Mechanism)
**Staged Rollout (단계적 출시)**는 신규 상용 릴리스 아티팩트를 전 세계 모든 사용자에게 일시에 배포하지 않고, 무작위 타겟 사용자 비율(예: 1% -> 5% -> 20% -> 50% -> 100%)을 점진적으로 높여가며 릴리스의 런타임 영향성을 실시간 관측 및 제어하는 배포 운영 메커니즘이다.

- **실시간 Android Vitals & Crashlytics 지표 관측**: 각 배포 단계에서 구글 플레이 콘솔의 **Android Vitals**(사용자 인지 크래시율, ANR율) 및 Firebase Crashlytics 모니터링 대시보드를 관측하여 잠재적 런타임 회귀 버그를 탐지한다.
- **단계적 출시 즉시 중단 (Halt Rollout)**: 모니터링 중 특정 디바이스 파퓰레이션에서 크래시율이 임계선(1.0%)을 초과하는 이상 징후가 감지되면 진행 중인 단계적 출시를 즉시 중단한다. 이때 이미 업데이트를 다운로드받은 1% 사용자 외에 나머지 99% 사용자에게 버그가 확산되는 것을 완벽히 차단한다.
- **Emergency Hotfix Update (긴급 핫픽스 패치)**: 출시 중단 상태에서 문제 원인을 수정한 핫픽스 아티팩트의 `versionCode`를 1 증가시켜 동일 트랙에 올려 제출하면, 구글 플레이는 핫픽스 아티팩트를 기존 중단되었던 배포 비율(1%)의 사용자에게 우선 덮어씌워 패치하도록 허용한다.

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
