---
title: apple-combine-framework
tags: [apple, combine, reactive, async]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Combine Framework apple combine reactive async

Combine 을 사용한 반응형 프로그래밍. 기본은 [[apple-runtime-and-swift]] 참고.

### Combine 개요

Apple 의 반응형 프로그래밍 프레임워크. 비동기 이벤트 스트림을 선언적으로 처리.

**핵심 개념:**
- **Publisher**: 값을 방출
- **Subscriber**: 값을 수신
- **Operator**: 값을 변환/필터링

### Publisher

값을 시간에 따라 방출하는 타입.

```swift
import Combine

// Just: 단일 값 방출
let justPublisher = Just(42)

justPublisher.sink { value in
    print(value) // 42
}

// Future: 비동기 단일 값
let futurePublisher = Future<String, Error> { promise in
    DispatchQueue.global().asyncAfter(deadline: .now() + 1) {
        promise(.success("Done"))
    }
}

futurePublisher.sink(
    receiveCompletion: { completion in
        print("Completed: \(completion)")
    },
    receiveValue: { value in
        print("Value: \(value)")
    }
)
```

#### @Published

프로퍼티 변경을 자동으로 방출.

```swift
class ViewModel: ObservableObject {
    @Published var username = ""
    @Published var isLoading = false
    @Published var items: [Item] = []
}

let viewModel = ViewModel()

viewModel.$username
    .sink { newValue in
        print("Username changed: \(newValue)")
    }
```

### Subject

값을 수동으로 방출할 수 있는 Publisher.

#### PassthroughSubject

현재 구독자에게만 방출. 이전 값 저장 안 함.

```swift
let subject = PassthroughSubject<String, Never>()

// 구독 전 방출 (받지 못함)
subject.send("First")

let subscription = subject.sink { value in
    print(value)
}

subject.send("Second") // 출력: Second
subject.send("Third")  // 출력: Third
```

#### CurrentValueSubject

현재 값을 저장. 새 구독자는 즉시 현재 값 수신.

```swift
let subject = CurrentValueSubject<Int, Never>(0)

print(subject.value) // 0

subject.send(1)
print(subject.value) // 1

let subscription = subject.sink { value in
    print("Received: \(value)") // 즉시 1 출력
}

subject.send(2) // Received: 2
```

### Operator

#### map

값을 변환.

```swift
[1, 2, 3].publisher
    .map { $0 * 2 }
    .sink { print($0) }
// 출력: 2, 4, 6
```

#### filter

조건에 맞는 값만 통과.

```swift
[1, 2, 3, 4, 5].publisher
    .filter { $0 % 2 == 0 }
    .sink { print($0) }
// 출력: 2, 4
```

#### compactMap

nil 제거 및 변환.

```swift
["1", "2", "abc", "3"].publisher
    .compactMap { Int($0) }
    .sink { print($0) }
// 출력: 1, 2, 3
```

#### flatMap

Publisher 를 평탄화.

```swift
struct User {
    let id: Int
    let name: String
}

func fetchUser(id: Int) -> AnyPublisher<User, Error> {
    Just(User(id: id, name: "User \(id)"))
        .setFailureType(to: Error.self)
        .eraseToAnyPublisher()
}

[1, 2, 3].publisher
    .setFailureType(to: Error.self)
    .flatMap { id in
        fetchUser(id: id)
    }
    .sink(
        receiveCompletion: { _ in },
        receiveValue: { user in
            print(user.name)
        }
    )
```

#### combineLatest

여러 Publisher 의 최신 값 결합.

```swift
let publisher1 = PassthroughSubject<String, Never>()
let publisher2 = PassthroughSubject<Int, Never>()

publisher1.combineLatest(publisher2)
    .sink { text, number in
        print("\(text): \(number)")
    }

publisher1.send("A") // 아직 출력 없음 (publisher2 값 없음)
publisher2.send(1)   // 출력: A: 1
publisher1.send("B") // 출력: B: 1
publisher2.send(2)   // 출력: B: 2
```

#### merge

여러 Publisher 를 하나로 병합.

```swift
let publisher1 = PassthroughSubject<Int, Never>()
let publisher2 = PassthroughSubject<Int, Never>()

publisher1.merge(with: publisher2)
    .sink { print($0) }

publisher1.send(1) // 1
publisher2.send(2) // 2
publisher1.send(3) // 3
```

#### zip

여러 Publisher 의 값을 쌍으로 묶음.

```swift
let numbers = [1, 2, 3].publisher
let letters = ["A", "B", "C"].publisher

numbers.zip(letters)
    .sink { number, letter in
        print("\(number)\(letter)")
    }
// 출력: 1A, 2B, 3C
```

### Scheduler

작업을 실행할 스레드/큐 지정.

```swift
URLSession.shared.dataTaskPublisher(for: url)
    .map(\.data)
    .decode(type: User.self, decoder: JSONDecoder())
    .receive(on: DispatchQueue.main) // 메인 스레드에서 수신
    .sink(
        receiveCompletion: { _ in },
        receiveValue: { user in
            // UI 업데이트
        }
    )
```

**주요 Scheduler:**
- `DispatchQueue.main`: 메인 스레드
- `DispatchQueue.global()`: 백그라운드
- `RunLoop.main`: Run Loop
- `ImmediateScheduler`: 즉시 실행

### 에러 처리

#### catch

에러를 다른 Publisher 로 대체.

```swift
fetchData()
    .catch { error -> Just<Data> in
        print("Error: \(error)")
        return Just(Data()) // 빈 데이터 반환
    }
    .sink { data in
        print("Received: \(data)")
    }
```

#### retry

실패 시 재시도.

```swift
fetchData()
    .retry(3) // 최대 3회 재시도
    .sink(
        receiveCompletion: { completion in
            if case .failure(let error) = completion {
                print("Failed after retries: \(error)")
            }
        },
        receiveValue: { data in
            print("Success: \(data)")
        }
    )
```

#### replaceError

에러를 기본값으로 대체.

```swift
fetchData()
    .replaceError(with: Data())
    .sink { data in
        print(data)
    }
```

### Cancellable 관리

#### AnyCancellable

구독을 취소할 수 있는 토큰.

```swift
class ViewModel {
    private var cancellables = Set<AnyCancellable>()
    
    func loadData() {
        fetchData()
            .sink { data in
                print(data)
            }
            .store(in: &cancellables) // 자동 관리
    }
    
    deinit {
        // cancellables 가 자동으로 취소됨
    }
}
```

#### 수동 취소

```swift
let cancellable = timer
    .sink { _ in
        print("Tick")
    }

// 나중에 취소
cancellable.cancel()
```

### 실전 예시

#### 네트워크 요청

```swift
class NetworkService {
    func fetchUsers() -> AnyPublisher<[User], Error> {
        let url = URL(string: "https://api.example.com/users")!
        
        return URLSession.shared.dataTaskPublisher(for: url)
            .map(\.data)
            .decode(type: [User].self, decoder: JSONDecoder())
            .receive(on: DispatchQueue.main)
            .eraseToAnyPublisher()
    }
}

class ViewModel: ObservableObject {
    @Published var users: [User] = []
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    private let networkService = NetworkService()
    private var cancellables = Set<AnyCancellable>()
    
    func loadUsers() {
        isLoading = true
        
        networkService.fetchUsers()
            .sink(
                receiveCompletion: { [weak self] completion in
                    self?.isLoading = false
                    if case .failure(let error) = completion {
                        self?.errorMessage = error.localizedDescription
                    }
                },
                receiveValue: { [weak self] users in
                    self?.users = users
                }
            )
            .store(in: &cancellables)
    }
}
```

#### 폼 검증

```swift
class FormViewModel: ObservableObject {
    @Published var email = ""
    @Published var password = ""
    @Published var isValid = false
    
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        Publishers.CombineLatest($email, $password)
            .map { email, password in
                self.isValidEmail(email) && password.count >= 8
            }
            .assign(to: &$isValid)
    }
    
    private func isValidEmail(_ email: String) -> Bool {
        email.contains("@") && email.contains(".")
    }
}
```

#### 검색 디바운싱

```swift
class SearchViewModel: ObservableObject {
    @Published var searchText = ""
    @Published var results: [String] = []
    
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        $searchText
            .debounce(for: .milliseconds(300), scheduler: DispatchQueue.main)
            .removeDuplicates()
            .filter { !$0.isEmpty }
            .flatMap { query in
                self.search(query: query)
            }
            .receive(on: DispatchQueue.main)
            .sink { [weak self] results in
                self?.results = results
            }
            .store(in: &cancellables)
    }
    
    private func search(query: String) -> AnyPublisher<[String], Never> {
        // 실제 검색 로직
        Just(["Result 1", "Result 2"])
            .delay(for: .milliseconds(500), scheduler: DispatchQueue.global())
            .eraseToAnyPublisher()
    }
}
```

### Backpressure

Publisher 가 Subscriber 보다 빠를 때 처리.

```swift
// buffer: 값을 버퍼에 저장
publisher
    .buffer(size: 10, prefetch: .byRequest, whenFull: .dropNewest)
    .sink { value in
        // 처리
    }

// throttle: 일정 간격으로만 방출
publisher
    .throttle(for: .seconds(1), scheduler: DispatchQueue.main, latest: true)
    .sink { value in
        print(value)
    }
```

### 커스텀 Publisher

```swift
struct RandomNumberPublisher: Publisher {
    typealias Output = Int
    typealias Failure = Never
    
    let count: Int
    
    func receive<S>(subscriber: S) where S : Subscriber, Never == S.Failure, Int == S.Input {
        let subscription = RandomNumberSubscription(subscriber: subscriber, count: count)
        subscriber.receive(subscription: subscription)
    }
}

class RandomNumberSubscription<S: Subscriber>: Subscription where S.Input == Int, S.Failure == Never {
    private var subscriber: S?
    private let count: Int
    private var current = 0
    
    init(subscriber: S, count: Int) {
        self.subscriber = subscriber
        self.count = count
    }
    
    func request(_ demand: Subscribers.Demand) {
        guard let subscriber = subscriber else { return }
        
        for _ in 0..<demand.max ?? 0 {
            if current >= count {
                subscriber.receive(completion: .finished)
                cancel()
                return
            }
            
            current += 1
            _ = subscriber.receive(Int.random(in: 1...100))
        }
    }
    
    func cancel() {
        subscriber = nil
    }
}

// 사용
RandomNumberPublisher(count: 5)
    .sink { value in
        print(value)
    }
```

### Combine vs async/await

```swift
// Combine
func fetchUserCombine(id: Int) -> AnyPublisher<User, Error> {
    URLSession.shared.dataTaskPublisher(for: url)
        .map(\.data)
        .decode(type: User.self, decoder: JSONDecoder())
        .eraseToAnyPublisher()
}

// async/await
func fetchUserAsync(id: Int) async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}
```

**언제 Combine 사용:**
- 여러 비동기 스트림 결합
- UI 바인딩 (@Published)
- 복잡한 변환/필터링 체인
- 취소 가능한 작업

**언제 async/await 사용:**
- 단순한 비동기 작업
- 순차적 흐름
- Swift Concurrency 와 통합

### 더 보기

[[apple-swiftui-deep-dive]], [[apple-swift-concurrency]], [[apple-urlsession-deep-dive]], [[apple-runtime-and-swift]]
