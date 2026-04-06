---
title: apple-swiftdata-deep-dive
tags: [apple, data, ios17, persistence, swift, swiftdata]
aliases: []
date modified: 2026-04-06 18:07:54 +09:00
date created: 2026-04-03 23:58:00 +09:00
---

## SwiftData Deep Dive

Core Data 가 20 년간 해온 일을, Swift 네이티브 문법으로 다시 쓴 것이 **SwiftData** (iOS 17+)입니다.

`NSManagedObject` 를 상속받고, `.xcdatamodeld` 파일과 싸우고, `NSFetchRequest` 를 타이핑하던 시대는 끝났습니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Swift-First**: `@Model` 매크로 하나로 모델 정의, 스키마 생성, 변경 추적이 모두 자동화됩니다. Core Data 의 장황한 보일러플레이트가 사라집니다.
- **SwiftUI 통합**: `@Query` 프로퍼티 래퍼로 데이터를 뷰에 바인딩하면, 데이터가 바뀔 때 자동으로 UI 가 갱신됩니다. `NSFetchedResultsController` 가 필요 없습니다.
- **내부 엔진은 Core Data**: SwiftData 는 Core Data 위에 구축되어 있습니다. SQLite → Core Data → SwiftData 순으로 추상화 수준이 높아진 것입니다. 따라서 Core Data 의 Faulting, 배치 처리 등 내부 원리를 아는 것은 여전히 유효합니다.

---

### 🏗️ Architecture (아키텍처)

#### 1. `@Model` 매크로 (Entity 정의)

Swift 클래스에 `@Model` 만 붙이면 됩니다. `.xcdatamodeld` 파일이 필요 없습니다.

```swift
import SwiftData

@Model
class Todo {
    var title: String
    var isDone: Bool
    var createdAt: Date
    
    // 관계(Relationship)도 자연스러운 Swift 프로퍼티
    @Relationship(deleteRule: .cascade)
    var subtasks: [Subtask]
    
    init(title: String) {
        self.title = title
        self.isDone = false
        self.createdAt = .now
        self.subtasks = []
    }
}
```

- 매크로가 컴파일 시점에 `PersistentModel` 프로토콜을 자동으로 구현합니다.
- `@Attribute(.unique)` 로 고유 제약, `@Attribute(.externalStorage)` 로 대용량 데이터(이미지 등)를 외부 파일로 저장할 수 있습니다.

#### 2. ModelContainer & ModelContext

- **ModelContainer**: 데이터베이스(저장소) 자체입니다. 앱 전체에서 하나만 만들면 됩니다.
- **ModelContext**: 작업 공간(Unit of Work)입니다. 변경을 모아뒀다가 한 번에 저장합니다.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // 앱 전체에 ModelContainer 주입
        .modelContainer(for: [Todo.self, Subtask.self])
    }
}
```

SwiftUI 뷰에서는 `@Environment(\.modelContext)` 로 컨텍스트에 접근합니다.

---

### 🔍 Data Fetching (`@Query`)

SwiftUI 뷰에서 데이터를 가져오는 가장 간단한 방법입니다.

```swift
struct TodoListView: View {
    // 자동으로 데이터를 가져오고, 변경 시 뷰를 갱신합니다
    @Query(sort: \Todo.createdAt, order: .reverse)
    private var todos: [Todo]
    
    @Environment(\.modelContext) private var context
    
    var body: some View {
        List(todos) { todo in
            Text(todo.title)
        }
    }
}
```

#### `#Predicate` 매크로 (Type-Safe 필터링)

`NSPredicate` 의 문자열 기반 쿼리를 Swift 코드로 대체합니다. **컴파일 타임**에 오류를 잡아줍니다.

```swift
// 타입 안전한 쿼리!
@Query(filter: #Predicate<Todo> { todo in
    !todo.isDone && todo.title.contains("중요")
})
private var importantTodos: [Todo]
```

#### `FetchDescriptor` (비 -SwiftUI 환경)

ViewModel 이나 Service 레이어에서 데이터를 가져올 때 사용합니다.

```swift
func fetchIncompleteTodos(context: ModelContext) throws -> [Todo] {
    let descriptor = FetchDescriptor<Todo>(
        predicate: #Predicate { !$0.isDone },
        sortBy: [SortDescriptor(\.createdAt)]
    )
    return try context.fetch(descriptor)
}
```

---

### 💾 CRUD Operations

```swift
// Create
let newTodo = Todo(title: "SwiftData 공부하기")
context.insert(newTodo)

// Update (자동 추적 — 그냥 프로퍼티를 수정하면 됩니다)
newTodo.isDone = true

// Delete
context.delete(newTodo)

// Save (명시적 저장. 앱 종료 시 자동 저장도 됩니다)
try context.save()
```

>[!TIP] **자동 저장(Autosave)**
>SwiftData 의 `ModelContext` 는 기본적으로 자동 저장이 켜져 있습니다. 명시적 `save()` 호출이 필수는 아니지만, 중요한 작업 후에는 호출하는 것이 안전합니다.

---

### 🆕 WWDC 2024 & 2025 주요 업데이트

#### 1. `@Index` 매크로 (WWDC 2024)

검색·정렬 성능을 크게 향상시킵니다. 대량 데이터에서 `#Predicate` 필터링이 느리다면 인덱스를 추가하세요.

```swift
@Model
class Todo {
    @Attribute(.unique) var id: UUID
    var title: String
    var createdAt: Date
    
    // 인덱스 선언 (개별 또는 복합)
    static let indexes: [[IndexColumn<Todo>]] = [
        [.init(\.createdAt)],
        [.init(\.title), .init(\.createdAt)]
    ]
}
```

#### 2. `@Unique` 매크로 (WWDC 2024)

속성의 고유 제약을 선언합니다. 동일한 값 삽입 시 **Upsert(업데이트 또는 삽입)** 동작을 합니다.

#### 3. `DataStore` 프로토콜 (WWDC 2024)

SQLite 이외의 커스텀 저장소(JSON 파일, 원격 서버 등)를 SwiftData 백엔드로 사용할 수 있습니다.

#### 4. Model Inheritance (WWDC 2025)

`@Model` 클래스의 상속이 가능해졌습니다. Core Data 의 Entity Inheritance 와 유사합니다.

---

### 🔄 Core Data 와의 공존

기존 Core Data 앱에서 SwiftData 로 점진적으로 마이그레이션할 수 있습니다.

1. **동일한 SQLite 파일**: 같은 `.xcdatamodeld` 스키마를 기반으로 SwiftData 모델을 생성할 수 있습니다.
2. **공존 가능**: 하나의 앱에서 Core Data 와 SwiftData 를 동시에 사용할 수 있습니다 (같은 저장소 또는 별도 저장소).
3. **Lightweight Migration**: 프로퍼티 추가/이름 변경 등 단순한 변경은 자동 마이그레이션됩니다.

>[!WARNING] **Devil's Advocate : SwiftData 의 현실적 한계**
>SwiftData 는 빠르게 성숙하고 있지만, Core Data 의 모든 기능을 대체하지는 못합니다:
> 1. **NSFetchedResultsController 의 섹션화(Sectioned Fetch)**: SwiftData `@Query` 는 iOS 17 기준으로 섹션 그룹핑이 제한적입니다.
> 2. **Background Context 패턴**: Core Data 의 `performBackgroundTask` 만큼 유연한 백그라운드 처리가 아직 부족합니다. `ModelActor` 를 사용해야 합니다.
> 3. **CloudKit 동기화**: Core Data + CloudKit 은 NSPersistentCloudKitContainer 로 성숙한 반면, SwiftData 의 CloudKit 통합은 아직 초기 단계입니다.
>**결론**: 신규 프로젝트는 SwiftData 우선, 기존 프로젝트는 점진적 마이그레이션을 권장합니다.

### 더 보기

- [apple-coredata-deep-dive](apple-coredata-deep-dive.md) - SwiftData 의 기반 엔진인 Core Data 내부 동작
- [apple-storage-and-filesystems](apple-storage-and-filesystems.md) - 앱 컨테이너와 파일 저장 정책
- [apple-swift-concurrency](../01_language_concurrency/apple-swift-concurrency.md) - `ModelActor` 백그라운드 처리에 필요한 Actor 이해
