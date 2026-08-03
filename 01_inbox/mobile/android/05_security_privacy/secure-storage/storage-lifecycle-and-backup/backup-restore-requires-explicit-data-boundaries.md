---
title: backup-restore-requires-explicit-data-boundaries
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:39 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## 백업과 복원에서 데이터 경계를 설계하기

상위 문서: [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)

관련 노트: [Android 보안 저장소는 저장 금지와 백업 정책까지 포함한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-policy-includes-what-not-to-store-and-backup.md)

### 한 문장 정의

백업은 저장된 모든 파일을 복사하는 기능이 아니라, 새 기기에서 복원할 가치와 위험을 선별하는 정책이다.

복원 가능한 데이터와 다시 만들어야 하는 데이터를 처음부터 구분해야 한다.

### 백업 대상 후보

- 사용자가 만든 기록처럼 재생성이 어려운 정본 데이터
- 복원 뒤에도 의미가 유지되는 사용자 설정
- 서버와 재동기화할 때 필요한 최소 식별 상태
- 마이그레이션 버전과 데이터 스키마 정보

### 기본 제외 후보

- `cache/` 아래의 네트워크 응답과 썸네일
- 임시 다운로드 조각과 변환 중간 산출물
- 세션 토큰, refresh token, 장치에 종속된 비밀값
- 만료된 데이터와 서버에서 다시 받을 수 있는 오프라인 복사본
- 복원 시 충돌을 일으킬 수 있는 잠금 파일과 작업 큐

### 규칙 파일의 의미

Android Auto Backup 은 포함과 제외 규칙으로 앱 데이터의 백업 범위를 조정한다.

```xml
<full-backup-content>
    <include domain="file" path="important.txt" />
    <exclude domain="file" path="cache/" />
    <exclude domain="database" path="temp.db" />
</full-backup-content>
```

규칙은 민감 데이터가 실수로 이동하지 않게 하는 보호 장치다.

하지만 규칙만으로 토큰을 안전하게 만들 수는 없다.

백업 경로, 기기 간 복원, 제조사별 동작 차이를 공식 정책으로 확인한다.

### 암호화 키와 복원의 관계

앱 파일을 별도 암호화했다면 암호문과 키의 복원 가능성이 함께 설계되어야 한다.

키가 새 기기에서 복원되지 않는데 암호문만 복원하면 데이터는 읽을 수 없다.

반대로 장치에 종속된 키를 백업하면 비밀값의 이동 경계가 커질 수 있다.

고가치 데이터는 서버 재인증이나 사용자 복구 절차를 통해 복원하는 편이 더 적합할 수 있다.

### 복원 후 초기화

복원된 앱은 캐시를 다시 채우고, 만료 토큰을 폐기하며, 데이터 버전을 검증해야 한다.

복원된 파일을 현재 기기의 신뢰된 상태라고 가정하지 않는다.

서버에서 권한과 세션을 다시 확인하고, 복원 실패 시 부분 데이터만 노출하지 않는다.

### 점검 질문

- 이 데이터는 사용자가 잃으면 안 되는 정본인가?
- 백업본이 유출되었을 때 피해가 허용 가능한가?
- 복원 뒤에도 장치와 사용자에 맞는 데이터인가?
- 캐시와 임시 파일이 백업 대상에 섞이지 않았는가?
- 키, 토큰, 백업본의 수명과 폐기 절차가 일치하는가?
