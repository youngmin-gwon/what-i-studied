---
title: apple-uikit-lifecycle
tags: [apple, uikit, ios, lifecycle, internals, optimization]
aliases: []
date modified: 2025-12-17 14:00:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## UIKit Lifecycle & Internals

UIKit의 생명주기와 렌더링 시스템 상세 분석. 기본 개념은 [[apple-app-lifecycle-and-ui]] 참고.

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 (Official Docs)
- [UIViewController - Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller)
- [View Controller Programming Guide](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/)
- [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/)
- [UIView - Apple Developer](https://developer.apple.com/documentation/uikit/uiview)

#### 🎥 WWDC 세션
- [WWDC 2023: What's new in UIKit](https://developer.apple.com/videos/play/wwdc2023/10055/)
- [WWDC 2019: Modernizing Your UI for iOS 13](https://developer.apple.com/videos/play/wwdc2019/224/)
- [WWDC 2018: UIKit: Apps for Every Size and Shape](https://developer.apple.com/videos/play/wwdc2018/235/)
- [WWDC 2015: Mysteries of Auto Layout, Part 1](https://developer.apple.com/videos/play/wwdc2015/218/)

#### 💻 오픈소스 및 심화 학습
- [UIKit Headers (via Runtime)](https://github.com/nst/iOS-Runtime-Headers)
- [Cassowary Constraint Solving Algorithm](https://constraints.cs.washington.edu/cassowary/) - Auto Layout의 기반 알고리즘

---

### UIViewController 생명주기 심화

단순한 메서드 순서를 넘어, 각 단계에서 시스템이 실제로 수행하는 작업과 주의할 점을 다룹니다.

```swift
class MyViewController: UIViewController {
    
    // 1. 초기화 (Initialization)
    // 스토리보드/NIB 사용 시 init(coder:)가 호출됩니다. 
    // 이때는 아직 View가 생성되지 않았으므로 View 접근 시도 시 무한 루프나 nil 참조가 발생할 수 있습니다.
    override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        print("init")
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        print("init from storyboard")
    }
    
    // 2. View 로딩 (Loading)
    // view 프로퍼티가 nil일 때 접근하면 호출됩니다.
    // 커스텀 View 계층을 코드로 "처음부터" 만들 때만 override 합니다.
    // super.loadView()는 호출하지 않습니다 (빈 뷰를 생성함).
    override func loadView() {
        // self.view = MyCustomView() 
        super.loadView() 
        print("loadView - View 계층 생성")
    }
    
    // 3. View 로드 완료 (View Loaded)
    // View 계층이 메모리에 올라온 직후입니다.
    // 하지만 아직 Window에 추가되지 않았고, 정확한 Frame 크기가 결정되지 않았을 수 있습니다 (Autolayout 이전).
    override func viewDidLoad() {
        super.viewDidLoad()
        print("viewDidLoad - 한 번만 호출")
        setupUI()
        setupConstraints() // 제약조건 설정은 여기서
    }
    
    // 4. View 나타나기 직전 (Appearance Transition Start)
    // 뷰 계층에 추가되기 직전입니다.
    // 네비게이션 바 숨김 처리나, 애니메이션 준비 등을 수행합니다.
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("viewWillAppear")
        // 데이터 리프레시 트리거
    }
    
    // 5. Layout 결정 (Layout Pass)
    // 뷰의 Bounds가 변경될 때마다 호출됩니다 (회전, 크기 조정 등).
    // Subview들의 Frame을 수동으로 조정해야 한다면 이곳이 마지막 기회입니다.
    override func viewWillLayoutSubviews() {
        super.viewWillLayoutSubviews()
        print("viewWillLayoutSubviews")
    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        print("viewDidLayoutSubviews - Frame 확정됨")
        // 그라데이션 레이어 크기 업데이트 등 Frame 의존 로직
    }

    // 🆕 iOS 17+: viewIsAppearing
    // viewWillAppear와 viewDidAppear 사이.
    // View가 계층에 추가되었고 Layout도 완료된 상태.
    // Frame에 의존적인 UI 업데이트를 하기에 가장 적절한 시점 (viewDidAppear보다 빠름).
    /* 
    override func viewIsAppearing(_ animated: Bool) {
        super.viewIsAppearing(animated)
        // Update UI based on final geometry
    } 
    */
    
    // 6. View 나타남 완료 (Appearance Transition End)
    // 화면에 완전히 표시된 후입니다.
    // 애니메이션 시작, 비디오 재생, 로그 수집 등을 수행합니다.
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        print("viewDidAppear")
    }
    
    // ... Disappear 메서드들은 대칭적으로 동작합니다.
}
```

---

### 🔍 내부 동작 원리 (Deep Dive)

#### 1. NIB/Storyboard 로딩 메커니즘
`viewDidLoad`가 호출되기 전, 시스템은 어떻게 NIB 파일을 로드할까요?
1. **Bundle Lookup**: `Bundle.main.path(forResource:...)`를 통해 NIB 바이너리를 찾습니다.
2. **Unarchiving**: NIB는 `NSKeyedArchiver`로 직렬화된 객체 그래프입니다. `NSCoder`를 통해 객체들이 메모리로 역직렬화(Deserialize)됩니다.
3. **Initialization**: 각 객체의 `init(coder:)`가 호출됩니다.
4. **Connections**: Outlet과 Action (`@IBOutlet`, `@IBAction`) 연결이 `setValue(_:forKey:)` (KVC)를 통해 수행됩니다.
5. **Awake**: 모든 연결이 완료되면 `awakeFromNib()`이 호출됩니다.

#### 2. Auto Layout 엔진 (Cassowary Algorithm)
Auto Layout은 단순한 박스 모델이 아니라, **선형 방정식 해결 시스템**입니다.
- **Constraint Solving**: `y = mx + b` 형태의 부등식/등식 집합을 풉니다.
- **Simplex Algorithm**: 내부적으로 최적화 문제를 푸는 Simplex 알고리즘의 변형을 사용합니다.
- **Cost**: 제약 조건이 n개일 때 최악의 경우 O(n^3)까지 갈 수 있으나, 일반적으로는 선형에 가깝게 최적화되어 있습니다. 하지만 뷰 계층이 깊고 제약 조건이 복잡하면 메인 스레드 병목의 원인이 됩니다.

---

### View 렌더링 사이클 (The Render Loop)

iOS는 `Run Loop`의 한 사이클마다 **Layout -> Display -> Commit** 단계를 거칩니다.

1.  **Constraints Check**: 제약 조건 변경 사항 확인 (`setNeedsUpdateConstraints`) -> `updateConstraints()`
2.  **Layout Pass**: 프레임 계산 (`setNeedsLayout`) -> `layoutSubviews()`
3.  **Display Pass**: 실제 그리기 (`setNeedsDisplay`) -> `draw(_:)` (CPU 드로잉 시)
4.  **Commit**: 렌더링 트리(Render Tree)를 렌더 서버(Render Server)로 전송 (GPU 합성)

```swift
class CustomView: UIView {
    
    // 1. 레이아웃 필요 표시
    // "다음 런루프 때 레이아웃 좀 다시 해줘" 라고 예약하는 것. 매우 가벼운 연산.
    func setNeedsLayout() {
        super.setNeedsLayout()
    }
    
    // 2. 즉시 레이아웃
    // 예약된 레이아웃 작업이 있다면 "지금 당장" 실행.
    // 애니메이션 블록 안에서 변경된 constraint를 즉시 프레임에 반영할 때 필수적.
    func layoutIfNeeded() {
        super.layoutIfNeeded()
    }
    
    // 3. 레이아웃 수행 (Override Point)
    // 여기서 frame을 직접 수정하면 다음 런루프에 다시 layoutSubviews가 호출되어 무한루프 가능성 있음. 주의!
    override func layoutSubviews() {
        super.layoutSubviews()
        // 서브뷰 위치/크기 조정
        print("layoutSubviews - frame: \(frame)")
    }
}
```

---

### 🛡️ 실무 패턴 및 최적화 (Advanced Patterns)

#### 1. View Controller Containment (컨테이너 패턴)
비대한 ViewController(Fat VC)를 막기 위해 화면을 레고 블록처럼 쪼개 관리합니다.

**올바른 자식 VC 추가 순서:**
```swift
func add(childVC: UIViewController) {
    // 1. 부모-자식 관계 수립
    addChild(childVC) 
    
    // 2. View 계층 추가
    view.addSubview(childVC.view)
    
    // 3. Layout 설정
    childVC.view.translatesAutoresizingMaskIntoConstraints = false
    NSLayoutConstraint.activate([
        // ... Constraints
    ])
    
    // 4. 완료 알림
    childVC.didMove(toParent: self)
}

func remove(childVC: UIViewController) {
    // 1. 제거 시작 알림
    childVC.willMove(toParent: nil)
    
    // 2. View 제거
    childVC.view.removeFromSuperview()
    
    // 3. 관계 해제
    childVC.removeFromParent()
}
```

#### 2. 메모리 효율적인 이미지 로딩 (Optimized Image Loading)
`UIImage(named:)`는 캐싱을 하지만, 대용량 이미지를 그대로 로드하면 메모리 스파이크가 발생합니다. `ImageIO`를 사용해 필요한 크기만큼만 다운샘플링하는 것이 좋습니다.

```swift
func loadDownsampledImage(at url: URL, for size: CGSize, scale: CGFloat = UIScreen.main.scale) -> UIImage? {
    let imageSourceOptions = [kCGImageSourceShouldCache: false] as CFDictionary
    guard let imageSource = CGImageSourceCreateWithURL(url as CFURL, imageSourceOptions) else { return nil }
    
    let maxDimensionInPixels = max(size.width, size.height) * scale
    
    let downsampleOptions = [
        kCGImageSourceCreateThumbnailFromImageAlways: true,
        kCGImageSourceShouldCacheImmediately: true, // 디코딩을 백그라운드에서 수행
        kCGImageSourceCreateThumbnailWithTransform: true,
        kCGImageSourceThumbnailMaxPixelSize: maxDimensionInPixels
    ] as CFDictionary
    
    guard let downsampledImage = CGImageSourceCreateThumbnailAtIndex(imageSource, 0, downsampleOptions) else { return nil }
    
    return UIImage(cgImage: downsampledImage)
}
```

#### 3. Diffable Data Source (Modern CollectionView)
`reloadData()`의 성능 저하와 애니메이션 부재를 해결합니다.

```swift
// SnapshotApplying
var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
snapshot.appendSections([.main])
snapshot.appendItems(items)

// apply 메서드는 백그라운드 스레드에서 호출해도 안전합니다 (iOS 15+).
// UI 업데이트는 자동으로 메인 스레드에서 처리됩니다.
dataSource.apply(snapshot, animatingDifferences: true)
```

---

### Troubleshooting (문제 해결)

#### ❌ "Main Thread Checker: UI API called on a background thread"
- **현상**: 앱 크래시나 보라색 경고.
- **원인**: `UILabel.text` 업데이트 등을 비동기 클로저(네트워크 응답) 내부에서 직접 호출.
- **해결**:
  ```swift
  // Old
  DispatchQueue.main.async {
      self.label.text = "Hello"
  }
  
  // Modern
  Task { @MainActor in
      self.label.text = "Hello"
  }
  ```

#### ❌ "Unsatisfiable Constraints"
- **현상**: 콘솔에 긴 로그가 찍히며 레이아웃이 깨짐.
- **해결**:
  1. 로그에서 충돌하는 Constraint ID 확인.
  2. `translatesAutoresizingMaskIntoConstraints = false`가 설정되어 있는지 확인 (코드로 UI 짤 때 필수).
  3. Constraint Priority 조절 (Required(1000)끼리 충돌하지 않게 하나를 999로 낮춤).

### 더 보기
- [[apple-swiftui-deep-dive]] - 선언형 UI의 생명주기
- [[apple-memory-management]] - ARC와 메모리 관리
- [[apple-performance-and-debug]] - 성능 측정 도구 사용법
