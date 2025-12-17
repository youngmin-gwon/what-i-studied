---
title: apple-uikit-lifecycle
tags: [apple, uikit, ios, lifecycle]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## UIKit Lifecycle apple uikit ios lifecycle

UIKit 의 생명주기와 렌더링 시스템. 기본은 [[apple-app-lifecycle-and-ui]] 참고.

### UIViewController 생명주기

```swift
class MyViewController: UIViewController {
    
    // 1. 초기화
    override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        print("init")
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        print("init from storyboard")
    }
    
    // 2. View 로딩
    override func loadView() {
        super.loadView()
        print("loadView - View 계층 생성")
        // 커스텀 view 설정 시 super 호출 안 함
    }
    
    // 3. View 로드 완료
    override func viewDidLoad() {
        super.viewDidLoad()
        print("viewDidLoad - 한 번만 호출")
        // UI 초기 설정
        setupUI()
    }
    
    // 4. View 가 나타나기 직전
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("viewWillAppear")
        // 데이터 새로고침
    }
    
    // 5. View 가 나타남
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        print("viewDidAppear")
        // 애니메이션 시작
    }
    
    // 6. View 가 사라지기 직전
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        print("viewWillDisappear")
        // 키보드 숨기기
    }
    
    // 7. View 가 사라짐
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        print("viewDidDisappear")
        // 타이머 정지
    }
    
    // 8. 메모리 경고
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        print("didReceiveMemoryWarning")
        // 캐시 정리
    }
    
    // 9. 해제
    deinit {
        print("deinit")
    }
}
```

### View 렌더링 사이클

```swift
class CustomView: UIView {
    
    // 1. 레이아웃 필요 표시
    func setNeedsLayout() {
        // 다음 업데이트 사이클에 layoutSubviews 호출 예약
        super.setNeedsLayout()
    }
    
    // 2. 즉시 레이아웃
    func layoutIfNeeded() {
        // 즉시 layoutSubviews 호출
        super.layoutIfNeeded()
    }
    
    // 3. 레이아웃 수행
    override func layoutSubviews() {
        super.layoutSubviews()
        // 서브뷰 위치/크기 조정
        print("layoutSubviews - frame: \(frame)")
    }
    
    // 4. 그리기 필요 표시
    func setNeedsDisplay() {
        // 다음 업데이트 사이클에 draw 호출 예약
        super.setNeedsDisplay()
    }
    
    // 5. 그리기 수행
    override func draw(_ rect: CGRect) {
        super.draw(rect)
        // 커스텀 그리기
        guard let context = UIGraphicsGetCurrentContext() else { return }
        
        context.setFillColor(UIColor.blue.cgColor)
        context.fill(rect)
    }
}
```

### Auto Layout

#### Constraint 생성

```swift
// 1. NSLayoutConstraint
let label = UILabel()
label.translatesAutoresizingMaskIntoConstraints = false
view.addSubview(label)

NSLayoutConstraint.activate([
    label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
    label.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
    label.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16)
])

// 2. Visual Format Language
let views = ["label": label]
let constraints = NSLayoutConstraint.constraints(
    withVisualFormat: "H:|-16-[label]-16-|",
    options: [],
    metrics: nil,
    views: views
)
NSLayoutConstraint.activate(constraints)
```

#### Priority

```swift
let widthConstraint = label.widthAnchor.constraint(equalToConstant: 200)
widthConstraint.priority = .defaultHigh // 750
widthConstraint.isActive = true

// Priority 값:
// .required: 1000
// .defaultHigh: 750
// .defaultLow: 250
```

#### Content Hugging & Compression Resistance

```swift
// Content Hugging: 내용보다 커지지 않으려는 저항
label.setContentHuggingPriority(.defaultHigh, for: .horizontal)

// Compression Resistance: 내용보다 작아지지 않으려는 저항
label.setContentCompressionResistancePriority(.required, for: .horizontal)
```

### UITableView

#### 기본 구현

```swift
class TableViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    let tableView = UITableView()
    var items = ["Item 1", "Item 2", "Item 3"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        
        view.addSubview(tableView)
        tableView.frame = view.bounds
    }
    
    // MARK: - DataSource
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return items.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = items[indexPath.row]
        return cell
    }
    
    // MARK: - Delegate
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        print("Selected: \(items[indexPath.row])")
    }
}
```

#### 커스텀 셀

```swift
class CustomCell: UITableViewCell {
    let titleLabel = UILabel()
    let subtitleLabel = UILabel()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func setupUI() {
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        subtitleLabel.translatesAutoresizingMaskIntoConstraints = false
        
        contentView.addSubview(titleLabel)
        contentView.addSubview(subtitleLabel)
        
        NSLayoutConstraint.activate([
            titleLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 8),
            titleLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
            titleLabel.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
            
            subtitleLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 4),
            subtitleLabel.leadingAnchor.constraint(equalTo: titleLabel.leadingAnchor),
            subtitleLabel.trailingAnchor.constraint(equalTo: titleLabel.trailingAnchor),
            subtitleLabel.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -8)
        ])
    }
    
    func configure(title: String, subtitle: String) {
        titleLabel.text = title
        subtitleLabel.text = subtitle
    }
}
```

#### Diffable Data Source (iOS 13+)

```swift
class ModernTableViewController: UIViewController {
    enum Section {
        case main
    }
    
    struct Item: Hashable {
        let id: UUID
        let title: String
    }
    
    var dataSource: UITableViewDiffableDataSource<Section, Item>!
    let tableView = UITableView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        view.addSubview(tableView)
        tableView.frame = view.bounds
        
        configureDataSource()
        applySnapshot()
    }
    
    func configureDataSource() {
        dataSource = UITableViewDiffableDataSource<Section, Item>(tableView: tableView) { tableView, indexPath, item in
            let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
            cell.textLabel?.text = item.title
            return cell
        }
    }
    
    func applySnapshot() {
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
        snapshot.appendItems([
            Item(id: UUID(), title: "Item 1"),
            Item(id: UUID(), title: "Item 2"),
            Item(id: UUID(), title: "Item 3")
        ])
        dataSource.apply(snapshot, animatingDifferences: true)
    }
}
```

### UICollectionView

#### Flow Layout

```swift
class CollectionViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
    var collectionView: UICollectionView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let layout = UICollectionViewFlowLayout()
        layout.itemSize = CGSize(width: 100, height: 100)
        layout.minimumInteritemSpacing = 10
        layout.minimumLineSpacing = 10
        layout.sectionInset = UIEdgeInsets(top: 10, left: 10, bottom: 10, right: 10)
        
        collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: layout)
        collectionView.dataSource = self
        collectionView.delegate = self
        collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
        collectionView.backgroundColor = .white
        
        view.addSubview(collectionView)
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 20
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
        cell.backgroundColor = .blue
        return cell
    }
    
    // 동적 크기
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let width = (collectionView.bounds.width - 30) / 2
        return CGSize(width: width, height: width)
    }
}
```

#### Compositional Layout (iOS 13+)

```swift
func createLayout() -> UICollectionViewLayout {
    let itemSize = NSCollectionLayoutSize(
        widthDimension: .fractionalWidth(0.5),
        heightDimension: .fractionalHeight(1.0)
    )
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    item.contentInsets = NSDirectionalEdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5)
    
    let groupSize = NSCollectionLayoutSize(
        widthDimension: .fractionalWidth(1.0),
        heightDimension: .absolute(200)
    )
    let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize, subitems: [item])
    
    let section = NSCollectionLayoutSection(group: group)
    section.contentInsets = NSDirectionalEdgeInsets(top: 10, leading: 10, bottom: 10, trailing: 10)
    
    return UICollectionViewCompositionalLayout(section: section)
}
```

### 성능 최적화

#### 셀 재사용

```swift
// ✅ 올바른 재사용
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    
    // 셀 재설정
    cell.textLabel?.text = items[indexPath.row]
    cell.imageView?.image = nil // 이전 이미지 제거
    
    return cell
}

// ❌ 잘못된 사용
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = UITableViewCell() // 매번 새로 생성 (느림!)
    return cell
}
```

#### Prefetching

```swift
class PrefetchingTableViewController: UIViewController, UITableViewDataSourcePrefetching {
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.prefetchDataSource = self
    }
    
    func tableView(_ tableView: UITableView, prefetchRowsAt indexPaths: [IndexPath]) {
        // 미리 데이터 로드
        for indexPath in indexPaths {
            loadImage(for: indexPath.row)
        }
    }
    
    func tableView(_ tableView: UITableView, cancelPrefetchingForRowsAt indexPaths: [IndexPath]) {
        // 취소된 작업 정리
        for indexPath in indexPaths {
            cancelImageLoad(for: indexPath.row)
        }
    }
}
```

### 더 보기

[[apple-swiftui-deep-dive]], [[apple-app-lifecycle-and-ui]], [[apple-memory-management]], [[apple-performance-and-debug]]
