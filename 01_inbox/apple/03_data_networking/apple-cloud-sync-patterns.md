---
title: apple-cloud-sync-patterns
tags: [apple, cloud, sync, icloud, cloudkit, architecture, offline-first]
aliases: []
date modified: 2025-12-18 01:40:00 +09:00
date created: 2025-12-16 16:09:23 +09:00
---

## Cloud Sync Architecture

"로컬에선 잘 되는데 서버랑 붙이니까 꼬여요."
동기화(Sync)는 주니어와 시니어를 가르는 가장 큰 장벽 중 하나입니다.
단순히 API를 호출하는 게 아니라, **"오프라인일 때 쌓인 데이터를 어떻게 할 것인가?"**를 설계해야 하기 때문입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Offline First**: 사용자는 항상 온라인이 아닙니다. 엘리베이터에서 쓴 메모가 전송 실패했다고 사라지면 안 됩니다. 일단 로컬에 저장하고, 나중에 조용히 보내야 합니다(Outbox Pattern).
- **Conflict Resolution**: 아이패드에서 "A"라고 수정하고, 동시에 아이폰에서 "B"라고 수정했다면? 서버는 누구 손을 들어줘야 할까요? 이 정책(Last Writer Wins 등)이 없으면 데이터가 날아갑니다.
- **Battery**: 1초마다 동기화하면 배터리가 녹습니다. 변경 사항을 모아서(Batch) 보내거나, 푸시가 올 때만 당겨오는 전략이 필요합니다.

---

### ☁️ CloudKit & Core Data

애플 생태계에서 동기화를 구현하는 가장 표준적인 방법입니다.

#### 1. NSPersistentCloudKitContainer
Core Data를 쓴다면 코드 한 줄 없이 iCloud 동기화가 됩니다.
- **장점**: 로컬 DB(SQLite)와 클라우드 미러링을 OS가 알아서 해줍니다. 오프라인 변경 사항도 자동으로 큐에 쌓였다가 연결되면 나갑니다.
- **단점**: "내 서버"가 아닙니다. 안드로이드나 웹이랑 공유하기 어렵습니다(CloudKit JS가 있긴 하지만).

#### 2. Public vs Private Database
- **Private**: 사용자 본인만 볼 수 있습니다. (사용자 iCloud 용량 차감)
- **Public**: 모든 사용자가 볼 수 있습니다. (개발자 용량 차감)

---

### 🔄 Sync Patterns (설계 패턴)

REST API를 직접 쓴다면 아래 패턴을 구현해야 합니다.

#### 1. Outbox Pattern (보낼 편지함)
변경 사항을 바로 네트워크로 쏘지 말고, 로컬 큐(Outbox)에 먼저 넣으세요.
1. UI: 로컬 DB에 저장하고 즉시 반영 (낙관적 UI).
2. Background: 네트워크 감지 시 큐에 있는 요청 전송.
3. Fail: 실패하면 재시도 횟수 증가 후 대기(Backoff).

#### 2. Delta Sync (차분 동기화)
"전체 목록 주세요"는 최악입니다.
- 클라이언트: "나 100번 버전까지 있어. 그 뒤에 일어난 일만 줘." (`since_version=100`)
- 서버: 101번(추가), 102번(삭제) 변경 로그만 리턴.

#### 3. Conflict Resolution (충돌 해결)
- **Last Writer Wins (LWW)**: 가장 최근 타임스탬프가 이깁니다. (구현 쉽지만 데이터 유실 위험)
- **Manual Merge**: 사용자에게 "두 버전이 충돌했습니다" 팝업을 띄웁니다. (Git처럼)

---

### 📷 Media Sync (대용량 파일)

사진이나 동영상은 JSON과 같이 보내면 안 됩니다.
1. **2-Phase Upload**:
   - 1단계: 서버에 "사진 올릴게" 요청 -> 서버가 "여기다 올려(Presigned URL)" 응답.
   - 2단계: URL로 바이너리 직접 업로드.
2. **Resumable**: 업로드가 99%에서 끊기면, 처음부터가 아니라 99%부터 다시 보내야 합니다(`Content-Range` 헤더 활용).

### 더 보기
- [[apple-offline-and-resilience]] - 오프라인 큐와 회복 탄력성 상세
- [[apple-coredata-deep-dive]] - 로컬 데이터베이스 설계
