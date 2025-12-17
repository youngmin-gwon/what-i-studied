---
title: apple-coredata-deep-dive
tags: [apple, coredata, persistence, database]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Core Data Deep Dive apple coredata persistence database

Core Data 를 사용한 데이터 영속화. 기본은 [[apple-storage-and-filesystems]] 참고.

### Core Data 개요

객체 그래프 관리 프레임워크. SQLite 위의 ORM 이 아니라 더 높은 수준의 추상화.

**핵심 구성요소:**
- **NSManagedObjectModel**: 데이터 모델 (스키마)
- **NSPersistentStoreCoordinator**: 저장소 관리
- **NSManagedObjectContext**: 작업 공간
- **NSManagedObject**: 데이터 객체

### 스택 설정

```swift
import CoreData

class PersistenceController {
    static let shared = PersistenceController()
    
    let container: NSPersistentContainer
    
    init() {
        container = NSPersistentContainer(name: "Model")
        
        container.loadPersistentStores { description, error in
            if let error = error {
                fatalError("Unable to load persistent stores: \(error)")
            }
        }
        
        // 자동 병합
        container.viewContext.automaticallyMergesChangesFromParent = true
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
    }
    
    var viewContext: NSManagedObjectContext {
        container.viewContext
    }
}
```

### 데이터 모델

**Entity 정의:**
```swift
// Xcode Data Model Editor 에서 생성하거나 코드로:
@objc(Person)
public class Person: NSManagedObject {
    @NSManaged public var name: String
    @NSManaged public var age: Int16
    @NSManaged public var email: String?
    @NSManaged public var posts: NSSet?
}

@objc(Post)
public class Post: NSManagedObject {
    @NSManaged public var title: String
    @NSManaged public var content: String
    @NSManaged public var createdAt: Date
    @NSManaged public var author: Person?
}
```

### CRUD 작업

#### Create

```swift
func createPerson(name: String, age: Int) {
    let context = PersistenceController.shared.viewContext
    
    let person = Person(context: context)
    person.name = name
    person.age = Int16(age)
    person.email = "\(name.lowercased())@example.com"
    
    do {
        try context.save()
    } catch {
        print("Failed to save: \(error)")
    }
}
```

#### Read (Fetch)

```swift
func fetchAllPeople() -> [Person] {
    let context = PersistenceController.shared.viewContext
    let fetchRequest: NSFetchRequest<Person> = Person.fetchRequest()
    
    do {
        return try context.fetch(fetchRequest)
    } catch {
        print("Failed to fetch: \(error)")
        return []
    }
}

// 조건부 조회
func fetchPeopleOlderThan(_ age: Int) -> [Person] {
    let context = PersistenceController.shared.viewContext
    let fetchRequest: NSFetchRequest<Person> = Person.fetchRequest()
    
    fetchRequest.predicate = NSPredicate(format: "age > %d", age)
    fetchRequest.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]
    
    do {
        return try context.fetch(fetchRequest)
    } catch {
        print("Failed to fetch: \(error)")
        return []
    }
}
```

#### Update

```swift
func updatePerson(_ person: Person, newName: String) {
    let context = PersistenceController.shared.viewContext
    
    person.name = newName
    
    do {
        try context.save()
    } catch {
        print("Failed to update: \(error)")
    }
}
```

#### Delete

```swift
func deletePerson(_ person: Person) {
    let context = PersistenceController.shared.viewContext
    
    context.delete(person)
    
    do {
        try context.save()
    } catch {
        print("Failed to delete: \(error)")
    }
}
```

### NSFetchRequest 고급

#### Predicate

```swift
// 문자열 검색
let predicate = NSPredicate(format: "name CONTAINS[cd] %@", "john")

// 범위
let predicate = NSPredicate(format: "age BETWEEN {18, 65}")

// 날짜
let startDate = Date()
let endDate = Date().addingTimeInterval(86400)
let predicate = NSPredicate(format: "createdAt >= %@ AND createdAt <= %@", startDate as NSDate, endDate as NSDate)

// Relationship
let predicate = NSPredicate(format: "author.name == %@", "John")

// 복합 조건
let predicate = NSCompoundPredicate(andPredicateWithSubpredicates: [
    NSPredicate(format: "age > %d", 18),
    NSPredicate(format: "email != nil")
])
```

#### Sort Descriptor

```swift
fetchRequest.sortDescriptors = [
    NSSortDescriptor(key: "age", ascending: false),
    NSSortDescriptor(key: "name", ascending: true)
]
```

#### Fetch Limit

```swift
fetchRequest.fetchLimit = 10
fetchRequest.fetchOffset = 20 // 페이지네이션
```

#### Batch Size

```swift
fetchRequest.fetchBatchSize = 20 // 한 번에 20개씩 로드
```

### NSFetchedResultsController

UITableView/UICollectionView 와 통합.

```swift
class PeopleViewController: UITableViewController {
    var fetchedResultsController: NSFetchedResultsController<Person>!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let context = PersistenceController.shared.viewContext
        let fetchRequest: NSFetchRequest<Person> = Person.fetchRequest()
        fetchRequest.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]
        
        fetchedResultsController = NSFetchedResultsController(
            fetchRequest: fetchRequest,
            managedObjectContext: context,
            sectionNameKeyPath: nil,
            cacheName: "PeopleCache"
        )
        
        fetchedResultsController.delegate = self
        
        do {
            try fetchedResultsController.performFetch()
        } catch {
            print("Failed to fetch: \(error)")
        }
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return fetchedResultsController.sections?.count ?? 0
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return fetchedResultsController.sections?[section].numberOfObjects ?? 0
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        let person = fetchedResultsController.object(at: indexPath)
        cell.textLabel?.text = person.name
        return cell
    }
}

extension PeopleViewController: NSFetchedResultsControllerDelegate {
    func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
        tableView.beginUpdates()
    }
    
    func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {
        switch type {
        case .insert:
            if let newIndexPath = newIndexPath {
                tableView.insertRows(at: [newIndexPath], with: .automatic)
            }
        case .delete:
            if let indexPath = indexPath {
                tableView.deleteRows(at: [indexPath], with: .automatic)
            }
        case .update:
            if let indexPath = indexPath {
                tableView.reloadRows(at: [indexPath], with: .automatic)
            }
        case .move:
            if let indexPath = indexPath, let newIndexPath = newIndexPath {
                tableView.deleteRows(at: [indexPath], with: .automatic)
                tableView.insertRows(at: [newIndexPath], with: .automatic)
            }
        @unknown default:
            break
        }
    }
    
    func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
        tableView.endUpdates()
    }
}
```

### Relationship

#### To-One

```swift
// Post → Person (author)
let post = Post(context: context)
post.title = "Hello"
post.author = person
```

#### To-Many

```swift
// Person → Posts
let person = Person(context: context)
person.name = "John"

let post1 = Post(context: context)
post1.title = "First Post"
post1.author = person

let post2 = Post(context: context)
post2.title = "Second Post"
post2.author = person

// person.posts 에 자동으로 추가됨 (inverse relationship)
```

#### Cascade Delete

```swift
// Data Model 에서 Delete Rule 설정:
// - Nullify: 관계만 제거
// - Cascade: 연관 객체도 삭제
// - Deny: 연관 객체 있으면 삭제 불가
// - No Action: 아무것도 안 함 (위험)
```

### Concurrency

#### Parent-Child Context

```swift
func saveInBackground() {
    let context = PersistenceController.shared.viewContext
    let backgroundContext = NSManagedObjectContext(concurrencyType: .privateQueueConcurrencyType)
    backgroundContext.parent = context
    
    backgroundContext.perform {
        // 백그라운드 작업
        let person = Person(context: backgroundContext)
        person.name = "Background Person"
        
        do {
            try backgroundContext.save()
            
            // 부모 컨텍스트에 저장
            context.perform {
                do {
                    try context.save()
                } catch {
                    print("Failed to save parent context: \(error)")
                }
            }
        } catch {
            print("Failed to save background context: \(error)")
        }
    }
}
```

#### Private Queue Context

```swift
let container = PersistenceController.shared.container

container.performBackgroundTask { context in
    // 백그라운드 작업
    let person = Person(context: context)
    person.name = "Background Person"
    
    do {
        try context.save()
    } catch {
        print("Failed to save: \(error)")
    }
}
```

### Batch Operations

#### Batch Insert

```swift
func batchInsert(people: [[String: Any]]) {
    let context = PersistenceController.shared.viewContext
    
    let batchInsert = NSBatchInsertRequest(entity: Person.entity(), objects: people)
    
    do {
        try context.execute(batchInsert)
    } catch {
        print("Failed to batch insert: \(error)")
    }
}
```

#### Batch Update

```swift
func incrementAgeForAll() {
    let context = PersistenceController.shared.viewContext
    
    let batchUpdate = NSBatchUpdateRequest(entityName: "Person")
    batchUpdate.propertiesToUpdate = ["age": NSExpression(forFunction: "add:to:", arguments: [
        NSExpression(forKeyPath: "age"),
        NSExpression(forConstantValue: 1)
    ])]
    batchUpdate.resultType = .updatedObjectIDsResultType
    
    do {
        let result = try context.execute(batchUpdate) as? NSBatchUpdateResult
        if let objectIDs = result?.result as? [NSManagedObjectID] {
            let changes = [NSUpdatedObjectsKey: objectIDs]
            NSManagedObjectContext.mergeChanges(fromRemoteContextSave: changes, into: [context])
        }
    } catch {
        print("Failed to batch update: \(error)")
    }
}
```

#### Batch Delete

```swift
func deleteAllPeople() {
    let context = PersistenceController.shared.viewContext
    
    let fetchRequest: NSFetchRequest<NSFetchRequestResult> = Person.fetchRequest()
    let batchDelete = NSBatchDeleteRequest(fetchRequest: fetchRequest)
    batchDelete.resultType = .resultTypeObjectIDs
    
    do {
        let result = try context.execute(batchDelete) as? NSBatchDeleteResult
        if let objectIDs = result?.result as? [NSManagedObjectID] {
            let changes = [NSDeletedObjectsKey: objectIDs]
            NSManagedObjectContext.mergeChanges(fromRemoteContextSave: changes, into: [context])
        }
    } catch {
        print("Failed to batch delete: \(error)")
    }
}
```

### Migration

#### Lightweight Migration

```swift
let container = NSPersistentContainer(name: "Model")

let description = container.persistentStoreDescriptions.first
description?.shouldMigrateStoreAutomatically = true
description?.shouldInferMappingModelAutomatically = true

container.loadPersistentStores { description, error in
    if let error = error {
        fatalError("Unable to load persistent stores: \(error)")
    }
}
```

**Lightweight Migration 조건:**
- 속성 추가/삭제
- 속성 이름 변경 (Renaming ID 사용)
- 관계 추가/삭제
- Optional ↔ Required 변경

#### Custom Migration

```swift
class MigrationManager {
    func migrateStore(at storeURL: URL, from sourceModel: NSManagedObjectModel, to destinationModel: NSManagedObjectModel) throws {
        let mappingModel = NSMappingModel(from: nil, forSourceModel: sourceModel, destinationModel: destinationModel)!
        
        let migrationManager = NSMigrationManager(sourceModel: sourceModel, destinationModel: destinationModel)
        
        let destinationURL = storeURL.deletingLastPathComponent().appendingPathComponent("Temp.sqlite")
        
        try migrationManager.migrateStore(
            from: storeURL,
            sourceType: NSSQLiteStoreType,
            options: nil,
            with: mappingModel,
            toDestinationURL: destinationURL,
            destinationType: NSSQLiteStoreType,
            destinationOptions: nil
        )
        
        // 기존 파일 삭제 후 새 파일로 교체
        try FileManager.default.removeItem(at: storeURL)
        try FileManager.default.moveItem(at: destinationURL, to: storeURL)
    }
}
```

### CloudKit 동기화

```swift
let container = NSPersistentCloudKitContainer(name: "Model")

container.loadPersistentStores { description, error in
    if let error = error {
        fatalError("Unable to load persistent stores: \(error)")
    }
}

// 자동으로 iCloud 동기화됨
```

**주의사항:**
- Unique constraints 사용
- Relationship 은 cascade delete 권장
- 충돌 해결 정책 설정

### 성능 최적화

#### Faulting

```swift
// Fault: 실제 데이터는 아직 로드 안 됨
let person = fetchedPerson
print(person.isFault) // true

// 프로퍼티 접근 시 로드
let name = person.name
print(person.isFault) // false
```

#### Prefetching

```swift
let fetchRequest: NSFetchRequest<Person> = Person.fetchRequest()
fetchRequest.relationshipKeyPathsForPrefetching = ["posts"]

let people = try context.fetch(fetchRequest)
// posts 도 함께 로드됨 (N+1 문제 방지)
```

#### Property Fault

```swift
fetchRequest.returnsObjectsAsFaults = false // 모든 프로퍼티 즉시 로드
```

### 더 보기

[[apple-storage-and-filesystems]], [[apple-swift-concurrency]], [[apple-swiftui-deep-dive]], [[apple-performance-and-debug]]
