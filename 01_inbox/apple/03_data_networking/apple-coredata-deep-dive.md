---
title: apple-coredata-deep-dive
tags: [apple, coredata, database, persistence, internals, performance]
aliases: []
date modified: 2025-12-17 20:20:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Core Data Deep Dive

"Core Data는 데이터베이스가 아닙니다."
이 유명한 말은 반은 맞고 반은 틀립니다. Core Data는 SQLite를 훌륭하게 추상화한 **객체 그래프 관리자(Object Graph Manager)**입니다. 
CRUD(Create, Read, Update, Delete)를 넘어, 객체 간의 **관계(Relationship)**와 **메모리 수명(Lifecycle)**을 관리하는 것이 핵심입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **DB가 아닌 이유**: SQL을 날리는 것이 아니라, `department.employees.count`처럼 점(dot)으로 객체에 접근하면 Core Data가 알아서 "필요할 때" DB를 다녀옵니다. 이 마법(Faulting)을 이해해야 성능을 잡을 수 있습니다.
- **메모리 관리**: 수만 개의 데이터를 다 로드하면 앱이 죽습니다. Core Data는 어떻게 수천만 건의 데이터를 다루면서도 메모리를 10MB만 쓸 수 있는지 알아야 합니다.
- **경쟁자**: Realm이나 GRDB보다 설정은 어렵지만, iCloud 동기화(`CloudKit`)와의 무료 연동은 강력한 무기입니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 (Official Docs)
- [Core Data Documentation](https://developer.apple.com/documentation/coredata)
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html) (아카이브되었지만 개념 설명은 최고입니다)

#### 🎥 WWDC 세션
- [WWDC 2019: Making Apps with Core Data](https://developer.apple.com/videos/play/wwdc2019/230/)
- [WWDC 2020: Optimize Core Data Performance](https://developer.apple.com/videos/play/wwdc2020/10017/) (Batch Insert)

---

### 🔍 내부 동작 원리 (Internals)

#### 1. Faulting (게으른 로딩)
Core Data 성능의 핵심입니다.
- **Managed Object**를 처음 가져오면, 데이터가 비어있는 껍데기(Fault) 상태입니다.
- 프로퍼티(`person.name`)에 접근하는 순간(Fire Fault), Core Data가 즉시 SQL을 실행해 데이터를 채워 넣습니다.
- **Debugging**: `-com.apple.CoreData.SQLDebug 1` 아규먼트를 켜면 실제 나가는 SQL 쿼리를 볼 수 있습니다.

#### 2. NSManagedObjectContext (MOC)
"메모장" 혹은 "트랜잭션 공간"입니다.
- 변경 사항(Insert, Update, Delete)은 `save()`를 호출하기 전까지는 메모리(MOC)에만 있습니다.
- **Parent-Child Context**: 백그라운드 작업을 위해 MOC를 계층적으로 둡니다. 자식 MOC에서 저장하면 부모 MOC로 변경 사항이 올라가고, 최종적으로 Root MOC가 디스크(SQLite)에 씁니다.

#### 3. SQLite Backing Store
Core Data는 내부적으로 SQLite를 사용하지만, 스키마가 매우 복잡합니다.
- `Z_PK` (Primary Key), `Z_ENT` (Entity ID), `Z_OPT` (Optimistic Locking) 같은 숨겨진 컬럼들이 있습니다.
- **Index**: 모델 에디터에서 `Indexing`을 체크하면 SQLite의 Index가 생성되어 검색 속도가 빨라집니다.

---

### 🛡️ 실무 최적화 패턴

#### 1. Batch Operations (iOS 13+)
수천 개의 데이터를 지우거나 업데이트할 때, 객체를 하나하나 메모리에 올리는 건 비효율적입니다. DB 레벨에서 한 방에 처리하세요.

```swift
func batchUpdate() {
    let request = NSBatchUpdateRequest(entityName: "Task")
    request.propertiesToUpdate = ["isCompleted": true] // 모든 태스크 완료 처리
    request.resultType = .updatedObjectIDsResultType
    
    do {
        let result = try context.execute(request) as? NSBatchUpdateResult
        // 주의: MOC(메모리)에는 반영 안 됨. mergeChanges로 동기화 필요.
        let objectIDs = result?.result as? [NSManagedObjectID] ?? []
        NSManagedObjectContext.mergeChanges(fromRemoteContextSave: [NSUpdatedObjectsKey: objectIDs], into: [context])
    } catch {
        print(error)
    }
}
```

#### 2. Heavyweight Migration
앱 스키마가 변경되었을 때, 단순 매핑(Lightweight)으로 안 되면 `NSEntityMigrationPolicy`를 상속받아 커스텀 로직을 짜야 합니다.
- 예: `fullName` 필드를 `firstName`과 `lastName`으로 쪼개서 이사 가기.

#### 3. Concurrency (동시성)
`MOC`는 스레드 안전하지 않습니다(Thread-Unsafe). 반드시 `perform` 블록 안에서 접근해야 합니다.

```swift
let backgroundContext = container.newBackgroundContext()

// ❌ 나쁜 예: 다른 스레드에서 바로 접근
// backgroundContext.fetch(...) 

// ✅ 좋은 예: perform 블록 사용
backgroundContext.perform {
    do {
        let results = try backgroundContext.fetch(request)
        // ...
    } catch { ... }
}
```

### 🧱 Core Data Stack Setup (Modern)

이제 `NSPersistentContainer`가 귀찮은 설정을 다 해줍니다.

```swift
lazy var persistentContainer: NSPersistentContainer = {
    let container = NSPersistentContainer(name: "Model")
    container.loadPersistentStores { (storeDescription, error) in
        if let error = error as NSError? {
            fatalError("Unresolved error \(error), \(error.userInfo)")
        }
    }
    // 뷰 업데이트를 위해 자동 병합 설정
    container.viewContext.automaticallyMergesChangesFromParent = true
    return container
}()
```

### 더 보기
- [[apple-app-lifecycle-and-ui]] - 앱 종료 시 저장(`saveContext`) 시점
- [[apple-combine-framework]] - Core Data 변경 사항을 Combine으로 구독하기
