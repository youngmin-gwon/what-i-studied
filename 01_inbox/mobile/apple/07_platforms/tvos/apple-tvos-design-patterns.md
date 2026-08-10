---
title: apple-tvos-design-patterns
tags: [apple, design, tvos]
aliases: []
date modified: 2026-08-10 16:00:00 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## tvOS Design Patterns

거실 환경에 맞는 tvOS UI/UX 패턴을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

### 💡 왜 이것을 알아야 하나요?

tvOS는 **거실의 대형 TV 화면에서 원거리(1~3m)에서 리모컨으로 조작**합니다. 스마트폰과 달리 터치 피드백이 없고, 포커스가 매우 중요하며, 사용자 경험이 전혀 다릅니다. 잘못된 디자인은 사용성 문제와 높은 이탈률로 이어집니다.

---

### 포커스 중심 내비게이션

#### 포커스 엔진이 핵심. 포커스 이동 경로 단순화, 포커스된 항목 명확한 피드백

**왜 필요한가**: tvOS는 터치가 없으므로 **포커스(Focus)라는 시각적 하이라이트**가 사용자가 현재 어디에 있는지 알려주는 유일한 방법입니다. 포커스가 명확하지 않으면 사용자는 길을 잃습니다.

- **포커스 이동**: Siri Remote의 방향 패드로 상하좌우 이동. 포커스 엔진이 자동으로 가장 가까운 요소로 이동.
- **포커스 표현**: 크기 증대, 밝기 증가, 그림자 추가, 약간의 스케일 애니메이션.
- **포커스 경로 설계**: 사용자가 예측 가능하게 이동하도록 레이아웃 구성. 포커스가 갑자기 점프하거나 사라지는 일 없도록.
- **초기 포커스**: 화면 로드 시 가장 중요한 요소(예: 재생 버튼)에 포커스 설정.

```swift
import UIKit
import TVUIKit

// 포커스 중심 UI
class FocusableCollectionViewController: UICollectionViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // tvOS 포커스 스타일 설정
        if #available(tvOS 11.0, *) {
            collectionView?.remembersLastFocusedIndexPath = true
        }
    }
    
    override func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("포커스된 항목: \(indexPath)")
    }
}

// 커스텀 포커스 처리
class FocusableButton: UIButton {
    override func didUpdateFocus(in context: UIFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator) {
        coordinator.addCoordinatedAnimations({
            // 포커스 시: 크기 증대
            if self.isFocused {
                self.transform = CGAffineTransform(scaleX: 1.1, y: 1.1)
                self.layer.shadowOpacity = 1.0
            } else {
                self.transform = CGAffineTransform.identity
                self.layer.shadowOpacity = 0.3
            }
        })
    }
}

// 초기 포커스 설정
class HomeViewController: UIViewController {
    @IBOutlet weak var playButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 초기 포커스를 재생 버튼으로 설정
        setNeedsFocusUpdate()
        updateFocusIfNeeded()
    }
    
    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        return [playButton]
    }
}

// 포커스 엔진 커스터마이징
class CustomFocusGuide: UIView {
    func setupFocusGuides() {
        let focusGuide = UIFocusGuide()
        addLayoutGuide(focusGuide)
        
        // 포커스가 어느 방향으로든 화면 끝에 도달하면 다른 요소로 이동하도록 설정
        focusGuide.preferredFocus = UIView() // 이동할 대상
        
        // 제약 조건 설정 (포커스 가이드 위치)
        focusGuide.topAnchor.constraint(equalTo: topAnchor).isActive = true
        focusGuide.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
    }
}
```

---

### tvOS 레이아웃 및 타이포그래피

#### 큰 화면, 원거리 시청. 큰 카드, 큰 텍스트, 적절한 여백 및 라인 수

**왜 필요한가**: TV는 가까운 스마트폰(30cm)과 달리 1~3m 떨어진 거리에서 시청되므로, 텍스트와 터치 타깃이 충분히 커야 합니다.

- **카드 크기**: 최소 480x270pt 이상. 제목은 44pt 이상의 큰 폰트.
- **여백**: 최소 60pt 마진으로 화면 가장자리에 콘텐츠가 닿지 않도록 (안전 영역).
- **라인 수**: 텍스트는 최대 3줄 정도로 간결하게.
- **히어로 영역 + 그리드 조합**: 상단에 큰 이미지/비디오 프리뷰, 하단에 그리드 형식의 항목.

```swift
import UIKit

// tvOS 안전 영역(Safe Insets) 고려
class SafeAreaLayout: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let safeArea = view.safeAreaLayoutGuide
        
        // 콘텐츠는 안전 영역 내에서만 배치
        let contentView = UIView()
        view.addSubview(contentView)
        
        contentView.topAnchor.constraint(equalTo: safeArea.topAnchor, constant: 60).isActive = true
        contentView.leftAnchor.constraint(equalTo: safeArea.leftAnchor, constant: 60).isActive = true
        contentView.rightAnchor.constraint(equalTo: safeArea.rightAnchor, constant: -60).isActive = true
        contentView.bottomAnchor.constraint(equalTo: safeArea.bottomAnchor, constant: -60).isActive = true
    }
}

// tvOS CollectionView: 카드 레이아웃
class CardCell: UICollectionViewCell {
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var imageView: UIImageView!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        
        // 큰 폰트 설정
        titleLabel.font = UIFont.systemFont(ofSize: 44, weight: .bold)
        titleLabel.numberOfLines = 2
        
        // 코너 라운드
        contentView.layer.cornerRadius = 12
        contentView.layer.masksToBounds = true
    }
}

// 히어로 영역 + 그리드 레이아웃
class HomeViewController: UIViewController, UICollectionViewDataSource {
    var collectionView: UICollectionView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let layout = UICollectionViewFlowLayout()
        layout.itemSize = CGSize(width: 480, height: 270) // tvOS 최소 카드 크기
        layout.minimumInteritemSpacing = 40
        layout.minimumLineSpacing = 40
        layout.sectionInset = UIEdgeInsets(top: 60, left: 60, bottom: 60, right: 60)
        
        collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: layout)
        collectionView?.dataSource = self
        view.addSubview(collectionView!)
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 12 // 그리드 항목 개수
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "CardCell", for: indexPath)
        // 셀 구성
        return cell
    }
}
```

---

### 검색 및 입력

#### Siri 음성 검색 우선, 텍스트 입력은 리모컨 제스처/음성/iPhone 키보드

**왜 필요한가**: tvOS 사용자는 리모컨의 작은 키보드로 텍스트를 입력하기 싫어합니다. **음성 검색(Siri)과 자동 완성**이 필수입니다.

- **Siri 음성 검색**: UISearchController + `UISearchResultsUpdating` 프로토콜.
- **텍스트 입력**: 리모컨 스와이프 조합, 또는 iPhone에서 텍스트 입력 후 전송.
- **추천/최근 검색**: 검색창 아래에 추천 키워드와 최근 검색 결과 표시.

```swift
import UIKit

// Siri 음성 검색 지원
class SearchViewController: UIViewController, UISearchResultsUpdating {
    lazy var searchController = UISearchController(searchResultsController: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 검색 컨트롤러 설정
        searchController.searchResultsUpdater = self
        searchController.obscuresBackgroundDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        
        // Siri 음성 입력 지원 (tvOS 자동)
        navigationItem.searchController = searchController
    }
    
    func updateSearchResults(for searchController: UISearchController) {
        let searchText = searchController.searchBar.text ?? ""
        print("검색: \(searchText)")
        
        // 실시간 검색 결과 업데이트
        performSearch(with: searchText)
    }
    
    func performSearch(with query: String) {
        // 서버에 검색 쿼리 전송
    }
}

// 추천 검색어 표시
class SearchSuggestionsViewController: UITableViewController {
    let suggestions = ["최신 영화", "인기 시리즈", "다큐멘터리"]
    let recentSearches = ["액션", "코미디"]
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 2
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return section == 0 ? suggestions.count : recentSearches.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "SuggestionCell", for: indexPath)
        
        if indexPath.section == 0 {
            cell.textLabel?.text = suggestions[indexPath.row]
        } else {
            cell.textLabel?.text = recentSearches[indexPath.row]
        }
        
        cell.textLabel?.font = UIFont.systemFont(ofSize: 36)
        return cell
    }
}

// iPhone 원격 키보드 통합
class RemoteKeyboardInput {
    func setupRemoteKeyboardInput() {
        // tvOS는 iPhone의 원격 키보드를 자동으로 지원
        // 사용자가 Siri Remote를 위아래로 스와이프하면 iPhone 키보드 자동 활성화
    }
}
```

---

### 미디어 발견 및 콘텐츠 큐레이션

#### 카테고리/추천/큐레이션으로 빠른 탐색. 자동 재생 토글, 데이터 사용 최소화

**왜 필요한가**: tvOS 사용자는 콘텐츠가 많으면 길을 잃기 쉬우므로, **카테고리와 추천**으로 빠르게 찾을 수 있도록 도와야 합니다.

- **카테고리/추천**: 영화, 시리즈, 새로운 콘텐츠, 내 목록 등.
- **미리보기 자동 재생**: 선택적으로 제공 (설정에서 토글).
- **이미지 품질**: 인터넷 속도에 따라 자동 조정. 4K vs HD 선택.

```swift
import UIKit

// 콘텐츠 카테고리별 섹션
class ContentBrowserViewController: UICollectionViewController {
    let categories = [
        ("추천", ["콘텐츠 1", "콘텐츠 2"]),
        ("영화", ["영화 1", "영화 2"]),
        ("시리즈", ["시리즈 1", "시리즈 2"]),
        ("내 목록", ["즐겨찾기 1", "즐겨찾기 2"])
    ]
    
    override func numberOfSections(in collectionView: UICollectionView) -> Int {
        return categories.count
    }
    
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return categories[section].1.count
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "ContentCell", for: indexPath)
        // 셀 구성
        return cell
    }
}

// 자동 재생 설정 및 토글
class PlaybackSettingsViewController: UITableViewController {
    @IBOutlet weak var autoPlayToggle: UISwitch!
    @IBOutlet weak var dataQualitySegmentedControl: UISegmentedControl!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 저장된 설정 로드
        let autoPlayEnabled = UserDefaults.standard.bool(forKey: "autoPlayEnabled")
        autoPlayToggle.isOn = autoPlayEnabled
        
        let quality = UserDefaults.standard.integer(forKey: "videoQuality")
        dataQualitySegmentedControl.selectedSegmentIndex = quality
    }
    
    @IBAction func autoPlayToggled(_ sender: UISwitch) {
        UserDefaults.standard.set(sender.isOn, forKey: "autoPlayEnabled")
        // 미디어 플레이어에 설정 전달
    }
    
    @IBAction func qualityChanged(_ sender: UISegmentedControl) {
        UserDefaults.standard.set(sender.selectedSegmentIndex, forKey: "videoQuality")
        // 스트리밍 품질 변경
    }
}

// 예상 미디어 프리로드 (적응형 비트레이트)
class AdaptiveStreamingManager {
    func determineStreamQuality(for bandwidth: Int) -> String {
        switch bandwidth {
        case 0..<5_000_000:
            return "SD" // 540p
        case 5_000_000..<15_000_000:
            return "HD" // 720p
        case 15_000_000...:
            return "4K" // 2160p
        default:
            return "HD"
        }
    }
}
```

---

### 애니메이션 및 피드백

#### 부드러운 포커스 전환 애니메이션, 패럴랙스 효과, 사운드 피드백 (햅틱 대신)

**왜 필요한가**: tvOS에는 햅틱(진동) 피드백이 없으므로, 시각적 애니메이션과 사운드가 사용자 피드백의 전부입니다.

- **포커스 애니메이션**: 부드러운 스케일/크기 변화 (0.2초 정도). 갑작스러운 변화 피하기.
- **패럴랙스**: 포커스된 요소가 약간 튀어나와 보이는 3D 효과 (UIMotionEffect).
- **사운드 피드백**: 선택, 취소, 오류 음성 재생.

```swift
import UIKit
import AVFoundation

// 포커스 애니메이션
class AnimatedFocusButton: UIButton {
    override func didUpdateFocus(in context: UIFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator) {
        coordinator.addCoordinatedAnimations({
            if self.isFocused {
                // 부드러운 스케일 애니메이션
                UIView.animate(withDuration: 0.3, delay: 0, options: .curveEaseOut, animations: {
                    self.transform = CGAffineTransform(scaleX: 1.1, y: 1.1)
                    self.layer.shadowOpacity = 0.8
                })
            } else {
                UIView.animate(withDuration: 0.2, delay: 0, options: .curveEaseIn, animations: {
                    self.transform = CGAffineTransform.identity
                    self.layer.shadowOpacity = 0.2
                })
            }
        })
    }
}

// 패럴랙스 효과 (3D 깊이감)
class ParallaxCardCell: UICollectionViewCell {
    let motionEffect = UIMotionEffectGroup()
    
    override func awakeFromNib() {
        super.awakeFromNib()
        
        // X축 패럴랙스
        let xMotion = UIInterpolatingMotionEffect(keyPath: "layer.transform.translation.x", type: .tiltAlongHorizontalAxis)
        xMotion.minimumRelativeValue = -20
        xMotion.maximumRelativeValue = 20
        
        // Y축 패럴랙스
        let yMotion = UIInterpolatingMotionEffect(keyPath: "layer.transform.translation.y", type: .tiltAlongVerticalAxis)
        yMotion.minimumRelativeValue = -20
        yMotion.maximumRelativeValue = 20
        
        motionEffect.motionEffects = [xMotion, yMotion]
        addMotionEffect(motionEffect)
    }
}

// 사운드 피드백
class SoundFeedbackManager {
    static let shared = SoundFeedbackManager()
    
    private var audioPlayer: AVAudioPlayer?
    
    func playSelectionSound() {
        playSound(named: "selection_sound")
    }
    
    func playCancelSound() {
        playSound(named: "cancel_sound")
    }
    
    func playErrorSound() {
        playSound(named: "error_sound")
    }
    
    private func playSound(named soundName: String) {
        guard let url = Bundle.main.url(forResource: soundName, withExtension: "mp3") else {
            return
        }
        
        do {
            audioPlayer = try AVAudioPlayer(contentsOf: url)
            audioPlayer?.play()
        } catch {
            print("사운드 재생 실패: \(error)")
        }
    }
}
```

---

### 다중 사용자 프로필

#### 빠른 프로필 전환, 사용자별 추천/시청 기록 분리

**왜 필요한가**: 가정의 여러 가족 구성원이 같은 TV를 사용하므로, 프로필 전환이 쉬워야 하고, 각 사용자의 데이터가 분리되어야 합니다.

```swift
import UIKit

// 사용자 프로필 관리
class UserProfile: Codable {
    let id: String
    let name: String
    let avatar: UIImage?
    var watchHistory: [String] = []
    var recommendations: [String] = []
}

class ProfileSwitchViewController: UIViewController {
    var profiles: [UserProfile] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 저장된 프로필 로드
        loadProfiles()
    }
    
    func loadProfiles() {
        if let data = UserDefaults.standard.data(forKey: "userProfiles"),
           let decoded = try? JSONDecoder().decode([UserProfile].self, from: data) {
            profiles = decoded
        }
    }
    
    func switchToProfile(_ profile: UserProfile) {
        UserDefaults.standard.set(profile.id, forKey: "activeProfileId")
        
        // 추천과 시청 기록 새로 로드
        loadProfileContent(for: profile)
    }
    
    func loadProfileContent(for profile: UserProfile) {
        // 해당 프로필의 추천 콘텐츠 로드
        print("프로필 전환: \(profile.name)")
    }
}
```

---

### 접근성

#### 자막, 오디오 설명, 색 대비, VoiceOver, 방향키 입력

**체크리스트**:
```
시각 접근성:
- [ ] 자막 지원 (오프 옵션 포함)
- [ ] 오디오 설명 (영화/콘텐츠)
- [ ] 높은 색 대비 (WCAG AA 이상)
- [ ] VoiceOver 지원
- [ ] Zoom 기능 호환

운동 접근성:
- [ ] Reduce Motion 지원 (애니메이션 최소화)
- [ ] 방향키 입력 (리모컨 제스처 대체)
- [ ] 포커스 가이드 명확성

청각 접근성:
- [ ] 음성 설명 설정
- [ ] 시각적 알림 (음성 대신)
```

---

### 성능 및 네트워크

#### 이미지/비디오 프리로드, 적응형 비트레이트, 버퍼링 상태 표시, On-Demand Resources

**왜 필요한가**: tvOS 사용자는 인터넷 속도가 불안정할 수 있으므로 (5GHz WiFi, 셀룰러 미지원), 버퍼링 상태를 명확히 표시해야 합니다.

```swift
import AVFoundation

// 비디오 스트리밍: 적응형 비트레이트
class AdaptiveVideoPlayer: UIViewController {
    var player: AVPlayer?
    
    func setupAdaptiveStreaming() {
        let url = URL(string: "https://example.com/video.m3u8")! // HLS 스트림
        let asset = AVAsset(url: url)
        let playerItem = AVPlayerItem(asset: asset)
        
        // 적응형 비트레이트 자동 설정
        player = AVPlayer(playerItem: playerItem)
        player?.currentItem?.preferredPeakBitrate = 5_000_000 // 5Mbps 제한
    }
    
    // 버퍼링 상태 모니터링
    func observeBufferingState() {
        NotificationCenter.default.addObserver(
            forName: .AVPlayerItemPlaybackStalled,
            object: nil,
            queue: .main
        ) { _ in
            print("버퍼링 중...")
        }
    }
}

// On-Demand Resources: 초기 앱 크기 줄이기
class OnDemandResourceManager {
    func downloadContentBundle(for contentId: String) {
        // NSBundleResourceRequest로 필요한 리소스만 다운로드
        let tags = Set(["content_\(contentId)"])
        let request = NSBundleResourceRequest(tags: tags)
        
        request.beginAccessingResources { error in
            if let error = error {
                print("리소스 다운로드 실패: \(error)")
            } else {
                print("리소스 다운로드 완료")
            }
        }
    }
}
```

---

### 관련 링크

[apple-tvos-media](apple-tvos-media.md), [apple-animation-and-motion](../../02_ui_frameworks/apple-animation-and-motion.md), [apple-networking-and-cloud](../../03_data_networking/apple-networking-and-cloud.md), [apple-accessibility-and-internationalization](../../02_ui_frameworks/apple-accessibility-and-internationalization.md).
