---
title: apple-ipados-productivity-deep
tags: [apple, apple/platforms, apple/platforms/ipados, ipados, productivity]
aliases: ["iPadOS Productivity", "아이패드 생산성"]
date modified: 2026-08-10 16:00:00 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## iPadOS Productivity Deep Dive

iPadOS 의 큰 화면과 멀티태스킹을 살려 생산성 앱을 만들기 위한 가이드. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

### 💡 왜 이것을 알아야 하나요?

iPad는 iPhone과 달리 **큰 화면(9.7" ~ 12.9")에서 여러 개 창을 동시에 띄우고, 마우스/키보드/Apple Pencil을 사용**합니다. 생산성 앱이라면 이 장점을 최대한 활용하지 않으면 사용자 불만족으로 이어집니다.

---

### 큰 화면 레이아웃 전략

#### 사이드바/3-Pane 레이아웃, 포인터 호버, 펜슬 입력 모두 고려

**왜 필요한가**: iPad의 넓은 화면은 탐색(Navigation), 리스트(Master), 상세(Detail) 정보를 동시에 보여줄 수 있으므로, 단순한 모바일 레이아웃이 아닌 데스크톱 수준의 정보 아키텍처가 필요합니다.

- **사이드바/3-Pane 레이아웃**: 탐색(좌) / 리스트(중) / 상세(우) 구조로 최대한 많은 정보를 한 화면에 보여줌.
- **포인터(Cursor)**: 마우스/트랙패드 입력. Hover 상태에 따른 시각적 피드백, 커스텀 포인터 모양 지원.
- **Apple Pencil**: 텍스트 입력(Scribble), 필기 인식, 샘플링/압력(Pressure)/기울기(Tilt) 데이터.
- **외장 디스플레이(Stage Manager, iPad Pro 7세대 이상)**: 별도 해상도/색역. 어느 디스플레이에 어느 창을 띄울지 설계.

```swift
import SwiftUI

// 사이드바 레이아웃 (NavigationSplitView)
struct ProductivityApp: View {
    @State var selectedCategory: Category? = .all
    @State var selectedItem: Item? = nil
    
    var body: some View {
        NavigationSplitView {
            // 좌측: 카테고리 탐색
            List(Category.allCases, id: \.self, selection: $selectedCategory) { category in
                NavigationLink(value: category) {
                    Label(category.name, systemImage: category.icon)
                }
            }
            .navigationSplitViewColumnWidth(min: 100, ideal: 200, max: 300)
        } content: {
            // 중앙: 리스트
            if let category = selectedCategory {
                List(category.items, id: \.self, selection: $selectedItem) { item in
                    NavigationLink(value: item) {
                        VStack(alignment: .leading) {
                            Text(item.title).font(.headline)
                            Text(item.subtitle).font(.caption).foregroundColor(.gray)
                        }
                    }
                }
                .navigationSplitViewColumnWidth(min: 150, ideal: 250)
            }
        } detail: {
            // 우측: 상세 정보
            if let item = selectedItem {
                DetailView(item: item)
            } else {
                Text("아이템을 선택하세요")
                    .foregroundColor(.gray)
            }
        }
        .navigationSplitViewStyle(.balanced)
    }
}

// 포인터 호버 효과
struct HoverEffectView: View {
    @State var isHovered = false
    
    var body: some View {
        VStack(spacing: 12) {
            RoundedRectangle(cornerRadius: 8)
                .fill(isHovered ? Color.blue : Color.gray)
                .frame(height: 60)
                .overlay(Text("포인터를 올려보세요"))
                .onContinuousHover { phase in
                    switch phase {
                    case .active:
                        isHovered = true
                    case .inactive:
                        isHovered = false
                    }
                }
            
            Text(isHovered ? "포인터 감지됨" : "포인터 없음")
                .font(.caption)
                .foregroundColor(.gray)
        }
        .padding()
    }
}

// Apple Pencil 입력 감지
class PencilInteractionHandler: NSObject, UIPointerInteractionDelegate {
    func pointerInteraction(_ interaction: UIPointerInteraction, regionFor request: UIPointerRegionRequest, defaultRegion: UIPointerRegion) -> UIPointerRegion? {
        // 커스텀 포인터 모양 설정 (예: 펜 아이콘)
        let preview = UITargetedPreview(view: request.view ?? UIView())
        let pointerShape = UIPointerShape.circle(radius: 12)
        let pointerRegion = UIPointerRegion(rect: request.view?.bounds ?? .zero, identifier: "pencil", content: { _ in
            UIPointerStyle(shape: pointerShape)
        })
        return pointerRegion
    }
}

// Pencil 필기 감지 (UIToolbar + UIKeyInput)
class PencilDrawingView: UIView {
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            // Pencil 입력: 압력, 기울기 데이터
            if touch.type == .pencil {
                let force = touch.force // 0.0 ~ 1.0
                let altitude = touch.altitudeAngle // 0 ~ π/2 (기울기)
                let azimuth = touch.azimuthAngle(in: self) // 0 ~ 2π (방향)
                
                print("Pencil 압력: \(force), 기울기: \(altitude), 방향: \(azimuth)")
            }
        }
    }
}
```

---

### 멀티 윈도우 및 스테이지 매니저 지원

#### UIScene/SwiftUI WindowGroup으로 여러 창. Stage Manager에서 창 크기 조절 가능하게 설계

**왜 필요한가**: iPad는 Split View(화면 분할), Slide Over(오버레이), Stage Manager(윈도우 겹침) 등 여러 멀티태스킹 모드를 지원하므로, 각 모드에서 최소/최대 크기를 설정하고 유연한 레이아웃을 제공해야 합니다.

- **UIScene/WindowGroup**: 여러 개의 독립적인 윈도우 생성.
- **Stage Manager** (iPad Pro 7세대 이상, iPadOS 16+): 창을 겹치고, 자유롭게 크기 조절 가능. 최소 크기(~320pt) 지원 필수.
- **Split View**: 좌우 화면 분할. 각 영역이 최소 320pt 너비 지원.
- **Slide Over**: 창을 오버레이로 띄우기. 너비 제한(~400pt).

```swift
import SwiftUI

// SwiftUI: 멀티 윈도우 앱
@main
struct MultiWindowApp: App {
    var body: some Scene {
        // 메인 윈도우
        WindowGroup {
            ContentView()
        }
        
        // 추가 윈도우 (예: 설정, 상세보기)
        Window("Details", id: "details") {
            DetailsWindow()
        }
        
        // 설정 윈도우
        WindowGroup(id: "settings") {
            SettingsView()
        }
    }
}

// UIKit: 멀티 윈도우 지원
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }
        
        let window = UIWindow(windowScene: windowScene)
        
        // Scene configuration ID에 따라 다른 ViewController 로드
        let vc: UIViewController
        if session.configuration.name == "DetailsScene" {
            vc = DetailsViewController()
        } else {
            vc = MainViewController()
        }
        
        window.rootViewController = UINavigationController(rootViewController: vc)
        window.makeKeyAndVisible()
        self.window = window
    }
}

// Stage Manager 대응: 최소/최대 창 크기 설정
struct StageManagerAwareView: View {
    @Environment(\.horizontalSizeClass) var sizeClass
    @Environment(\.verticalSizeClass) var vSizeClass
    
    var body: some View {
        VStack {
            // Compact 크기: 최소 크기 지원
            if sizeClass == .compact {
                CompactLayout()
            } else {
                RegularLayout()
            }
        }
        .frame(minWidth: 320) // Stage Manager에서 최소 320pt 너비
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

// Split View / Slide Over 대응: 유연한 레이아웃
struct AdaptiveLayoutView: View {
    @Environment(\.horizontalSizeClass) var hSizeClass
    @Environment(\.verticalSizeClass) var vSizeClass
    
    var body: some View {
        if hSizeClass == .regular && vSizeClass == .regular {
            // 풀 사이즈: 3-Pane
            HStack {
                Sidebar()
                    .frame(minWidth: 200, maxWidth: 300)
                
                Divider()
                
                MainContent()
                    .frame(minWidth: 150)
            }
        } else if hSizeClass == .compact {
            // 세로 모드 또는 좁은 화면: 스택 레이아웃
            VStack {
                Sidebar()
                Divider()
                MainContent()
            }
        } else {
            // Slide Over 등: 단일 뷰
            MainContent()
        }
    }
}
```

---

### 입력 방식 통합: 포인터, 펜슬, 터치, 키보드

#### 포인터 커스텀화, Scribble 텍스트 입력, Drag & Drop with UTType

**왜 필요한가**: iPad는 **동시에 여러 입력 방식**(포인터, 펜슬, 터치, 키보드)을 지원하므로, 각 입력에 맞는 인터랙션을 제공해야 합니다. 특히 Drag & Drop은 파일 시스템과의 연동이므로 UTType(Uniform Type Identifier)과 보안 북마크 처리가 필수입니다.

- **포인터**: Hover 상태 피드백, 커스텀 포인터 모양.
- **Pencil/Scribble**: 손글씨 텍스트 입력 자동 인식.
- **Drag & Drop**: 파일/텍스트/이미지 다른 앱으로 이동. 임시 파일과 보안 북마크 관리.
- **Context Menu**: UIContextMenuInteraction으로 마우스 우클릭, 길게 누르기 지원.

```swift
import UIKit
import UniformTypeIdentifiers

// 포인터 커스텀화
class PointerCustomizationView: UIView {
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesMoved(touches, with: event)
        
        // 커스텀 포인터 모양 설정
        if let interaction = self.interactions.first(where: { $0 is UIPointerInteraction }) as? UIPointerInteraction {
            interaction.invalidate()
        }
    }
}

// Scribble 텍스트 입력
class ScribbleTextField: UITextField {
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupScribble()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupScribble()
    }
    
    func setupScribble() {
        // Scribble 지원 (기본적으로 UITextField는 자동 지원, iOS 14+)
        // 손글씨 입력 -> 텍스트로 자동 변환
        self.placeholder = "여기에 쓰세요 (손글씨 또는 타이핑)"
    }
}

// Drag & Drop 구현
class DragDropView: UIView, UIDropInteractionDelegate, UIDragInteractionDelegate {
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupDragDrop()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupDragDrop()
    }
    
    func setupDragDrop() {
        // Drop 상호작용 추가
        let dropInteraction = UIDropInteraction(delegate: self)
        addInteraction(dropInteraction)
        
        // Drag 상호작용 추가
        let dragInteraction = UIDragInteraction(delegate: self)
        addInteraction(dragInteraction)
    }
    
    // Drop 수락
    func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
        // 파일, 텍스트, 이미지 모두 수락
        return session.hasItemsConforming(toTypeIdentifiers: [
            UTType.fileURL.identifier,
            UTType.plainText.identifier,
            UTType.image.identifier
        ])
    }
    
    func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: UIDropSession) -> UIDropProposal {
        let dropLocation = session.location(in: self)
        
        // Drop 위치에 따른 시각적 피드백
        return UIDropProposal(operation: .copy)
    }
    
    func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
        for item in session.items {
            let itemProvider = item.itemProvider
            
            // 파일 처리
            if itemProvider.hasItemConforming(toTypeIdentifier: UTType.fileURL.identifier) {
                itemProvider.loadFileRepresentation(forTypeIdentifier: UTType.fileURL.identifier) { url, error in
                    if let url = url {
                        print("파일 드롭됨: \(url.lastPathComponent)")
                        // 보안 북마크 생성
                        self.createSecurityBookmark(for: url)
                    }
                }
            }
            
            // 텍스트 처리
            if itemProvider.hasItemConforming(toTypeIdentifier: UTType.plainText.identifier) {
                itemProvider.loadItem(forTypeIdentifier: UTType.plainText.identifier, options: nil) { text, error in
                    if let text = text as? String {
                        print("텍스트 드롭됨: \(text)")
                    }
                }
            }
        }
    }
    
    // Drag 시작
    func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: UIDragSession) -> [UIDragItem] {
        let itemProvider = NSItemProvider(object: "Dragged Text" as NSString)
        let dragItem = UIDragItem(itemProvider: itemProvider)
        return [dragItem]
    }
    
    // 보안 북마크 생성 (App Sandbox 권한)
    func createSecurityBookmark(for url: URL) {
        do {
            let bookmarkData = try url.bookmarkData(options: .withSecurityScope, includingResourceValuesForKeys: nil, relativeTo: nil)
            // bookmarkData를 저장하여 나중에 접근
            UserDefaults.standard.set(bookmarkData, forKey: url.lastPathComponent)
        } catch {
            print("보안 북마크 생성 실패: \(error)")
        }
    }
}

// Context Menu (마우스 우클릭, 길게 누르기)
class ContextMenuView: UIView {
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupContextMenu()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupContextMenu()
    }
    
    func setupContextMenu() {
        let interaction = UIContextMenuInteraction(delegate: self)
        addInteraction(interaction)
    }
}

extension ContextMenuView: UIContextMenuInteractionDelegate {
    func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
        return UIContextMenuConfiguration(actionProvider: { suggestedActions in
            let delete = UIAction(title: "삭제", image: UIImage(systemName: "trash"), attributes: .destructive) { _ in
                print("삭제 선택됨")
            }
            let edit = UIAction(title: "편집", image: UIImage(systemName: "pencil")) { _ in
                print("편집 선택됨")
            }
            
            return UIMenu(children: [edit, delete])
        })
    }
}
```

---

### 파일 및 스토리지 관리

#### Files 앱 통합(UIDocumentPicker), 보안 북마크, App Groups, 외장 드라이브 지원

**왜 필요한가**: iPad는 Files 앱과 iCloud Drive를 통해 파일을 관리하고, 외장 드라이브(USB-C)와 네트워크 드라이브(NAS)를 지원합니다. 생산성 앱이라면 이 기능을 지원해야 유용성이 높습니다.

- **UIDocumentPicker**: 사용자가 Files 앱에서 파일/폴더 선택.
- **보안 북마크**: 선택한 파일/폴더에 지속적으로 접근할 권한.
- **App Groups**: 여러 앱/Extension 간 데이터 공유.
- **외장 드라이브/NAS**: File Coordination으로 동시 접근 안전성 보장.

```swift
import UIKit
import UniformTypeIdentifiers

class DocumentPickerViewController: UIViewController, UIDocumentPickerDelegate {
    func openDocumentPicker() {
        let types: [UTType] = [.plainText, .pdf, .spreadsheet, .folder]
        let picker = UIDocumentPickerViewController(forOpeningContentTypes: types)
        picker.delegate = self
        picker.allowsMultipleSelection = true
        present(picker, animated: true)
    }
    
    func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
        for url in urls {
            print("선택된 파일: \(url.lastPathComponent)")
            
            // 보안 북마크 생성 (지속적 접근)
            createSecurityBookmark(url)
        }
    }
    
    func createSecurityBookmark(_ url: URL) {
        do {
            let bookmarkData = try url.bookmarkData(options: .withSecurityScope, includingResourceValuesForKeys: nil, relativeTo: nil)
            
            // UserDefaults 또는 파일에 저장
            let fileName = url.lastPathComponent
            let bookmarkURL = FileManager.default
                .urls(for: .documentDirectory, in: .userDomainMask)[0]
                .appendingPathComponent("bookmarks")
                .appendingPathComponent("\(fileName).bookmark")
            
            try bookmarkData.write(to: bookmarkURL)
        } catch {
            print("북마크 생성 실패: \(error)")
        }
    }
    
    func accessBookmarkedFile(_ bookmarkURL: URL) throws -> URL? {
        guard let bookmarkData = try? Data(contentsOf: bookmarkURL) else { return nil }
        
        var isStale = false
        let url = try URL(resolvingBookmarkData: bookmarkData, options: .withSecurityScope, relativeTo: nil, bookmarkDataIsStale: &isStale)
        
        if isStale {
            // 북마크 업데이트 필요
            print("북마크가 오래됨, 업데이트 필요")
        }
        
        // 보안 범위 활성화
        guard url.startAccessingSecurityScopedResource() else { return nil }
        defer { url.stopAccessingSecurityScopedResource() }
        
        return url
    }
}

// App Groups: 앱과 Extension 간 데이터 공유
class AppGroupsStorage {
    static let groupIdentifier = "group.com.example.myapp"
    
    func saveSharedData(_ data: [String: Any]) {
        if let userDefaults = UserDefaults(suiteName: groupIdentifier) {
            userDefaults.set(data, forKey: "sharedData")
        }
    }
    
    func loadSharedData() -> [String: Any]? {
        if let userDefaults = UserDefaults(suiteName: groupIdentifier) {
            return userDefaults.dictionary(forKey: "sharedData")
        }
        return nil
    }
}

// 파일 조정 (File Coordination): 동시 접근 안전성
import FileProvider

class FileCoordinationManager {
    func readFileWithCoordination(_ url: URL) throws -> String {
        var content = ""
        let coordinator = NSFileCoordinator()
        var error: NSError?
        
        coordinator.coordinate(readingItemAt: url, options: [], error: &error) { readURL in
            content = (try? String(contentsOf: readURL, encoding: .utf8)) ?? ""
        }
        
        if let error = error {
            throw error
        }
        
        return content
    }
    
    func writeFileWithCoordination(_ url: URL, content: String) throws {
        let coordinator = NSFileCoordinator()
        var error: NSError?
        
        coordinator.coordinate(writingItemAt: url, options: [], error: &error) { writeURL in
            try? content.write(to: writeURL, atomically: true, encoding: .utf8)
        }
        
        if let error = error {
            throw error
        }
    }
}
```

---

### 생산성 기능 구현

#### 키보드 단축키, 커맨드 메뉴, 검색/Spotlight, 멀티 셀렉션

**왜 필요한가**: 생산성 앱 사용자는 마우스/키보드를 많이 사용하므로, 단축키와 커맨드 메뉴를 통한 빠른 접근이 필수입니다.

- **키보드 단축키**: Command/Option/Control 조합.
- **커맨드 메뉴**: UIMenu로 앱의 주요 액션을 빠르게 접근.
- **Spotlight 통합**: Core Spotlight으로 앱 콘텐츠 검색 가능.
- **멀티 셀렉션**: 여러 항목 선택 후 일괄 편집/삭제.

```swift
import SwiftUI
import CoreSpotlight

// 키보드 단축키
class ProductivityViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        setupKeyboardShortcuts()
    }
    
    func setupKeyboardShortcuts() {
        // Command+S: 저장
        let saveCommand = UIKeyCommand(input: "s", modifierFlags: .command, action: #selector(saveDocument))
        saveCommand.title = "저장"
        
        // Command+Z: 실행 취소
        let undoCommand = UIKeyCommand(input: "z", modifierFlags: .command, action: #selector(undo))
        undoCommand.title = "실행 취소"
        
        // Command+A: 모두 선택
        let selectAllCommand = UIKeyCommand(input: "a", modifierFlags: .command, action: #selector(selectAll))
        selectAllCommand.title = "모두 선택"
        
        addKeyCommand(saveCommand)
        addKeyCommand(undoCommand)
        addKeyCommand(selectAllCommand)
    }
    
    @objc func saveDocument() {
        print("저장됨 (Command+S)")
    }
    
    @objc func undo() {
        print("실행 취소 (Command+Z)")
    }
    
    @objc func selectAll() {
        print("모두 선택 (Command+A)")
    }
}

// 커맨드 메뉴
class CommandMenuViewController: UIViewController {
    override var canBecomeFirstResponder: Bool {
        return true
    }
    
    override var keyCommands: [UIKeyCommand]? {
        return [
            UIKeyCommand(input: "n", modifierFlags: .command, action: #selector(newDocument)),
            UIKeyCommand(input: "o", modifierFlags: .command, action: #selector(openDocument)),
        ]
    }
    
    func setupCommandMenu() {
        let newAction = UIAction(title: "새 문서", image: UIImage(systemName: "doc.badge.plus")) { _ in
            self.newDocument()
        }
        
        let openAction = UIAction(title: "열기", image: UIImage(systemName: "folder")) { _ in
            self.openDocument()
        }
        
        let menu = UIMenu(title: "", children: [newAction, openAction])
        self.navigationItem.rightBarButtonItem = UIBarButtonItem(title: nil, image: UIImage(systemName: "ellipsis.circle"), menu: menu)
    }
    
    @objc func newDocument() {
        print("새 문서")
    }
    
    @objc func openDocument() {
        print("열기")
    }
}

// Core Spotlight: 콘텐츠 검색 인덱싱
class SpotlightIndexing {
    static func indexDocument(id: String, title: String, content: String) {
        let item = CSSearchableItem(
            uniqueIdentifier: id,
            domainIdentifier: "documents",
            attributeSet: CSSearchableItemAttributeSet(itemContentType: .plainText)
        )
        
        item.attributeSet?.title = title
        item.attributeSet?.contentDescription = content
        item.attributeSet?.keywords = ["document", "productivity"]
        
        CSSearchableIndex.default().indexSearchableItems([item]) { error in
            if let error = error {
                print("Spotlight 인덱싱 실패: \(error)")
            } else {
                print("Spotlight 인덱싱 완료")
            }
        }
    }
    
    static func removeFromSpotlight(id: String) {
        CSSearchableIndex.default().deleteSearchableItems(withIdentifiers: [id]) { error in
            if let error = error {
                print("삭제 실패: \(error)")
            }
        }
    }
}

// 멀티 셀렉션
struct MultiSelectionView: View {
    @State var selectedItems = Set<String>()
    let items = ["항목 1", "항목 2", "항목 3", "항목 4"]
    
    var body: some View {
        VStack {
            List(items, id: \.self, selection: $selectedItems) { item in
                Text(item)
            }
            .environment(\.editMode, .constant(.active)) // 편집 모드
            
            if !selectedItems.isEmpty {
                HStack(spacing: 12) {
                    Button(action: { deleteSelected() }) {
                        Label("삭제", systemImage: "trash")
                    }
                    .tint(.red)
                    
                    Button(action: { editSelected() }) {
                        Label("편집", systemImage: "pencil")
                    }
                }
                .padding()
            }
        }
    }
    
    func deleteSelected() {
        print("선택된 항목 삭제: \(selectedItems)")
    }
    
    func editSelected() {
        print("선택된 항목 편집: \(selectedItems)")
    }
}
```

---

### 협업 및 실시간 동기화

#### Share Extension, SharePlay, CloudKit, 충돌 해결 전략

**왜 필요한가**: 생산성 앱에서 여러 사용자가 동시에 편집할 때 데이터 충돌이 발생할 수 있으므로, 충돌 감지와 병합(Merge) 전략이 필수입니다.

- **Share Extension**: 앱에서 다른 앱으로 문서/파일 공유.
- **SharePlay** (iOS/iPadOS 15.1+): FaceTime 중 실시간 협업.
- **CloudKit**: iCloud 기반 동기화.
- **충돌 해결**: Last-Write-Wins, Operational Transformation (OT), CRDT 등.

```swift
import CloudKit
import GroupActivities

// CloudKit 동기화
class CloudKitSync {
    let database = CKContainer.default().privateCloudDatabase
    
    func syncDocument(_ doc: Document) async throws {
        let record = CKRecord(recordType: "Document")
        record["title"] = doc.title
        record["content"] = doc.content
        record["lastModified"] = Date()
        
        let savedRecord = try await database.save(record)
        print("CloudKit에 저장됨: \(savedRecord.recordID)")
    }
    
    func fetchLatestDocument() async throws -> Document? {
        let query = CKQuery(recordType: "Document", predicate: NSPredicate(value: true))
        let (records, _) = try await database.records(matching: query)
        
        if let record = records.first {
            return Document(
                title: record["title"] as? String ?? "",
                content: record["content"] as? String ?? "",
                lastModified: record["lastModified"] as? Date ?? Date()
            )
        }
        return nil
    }
    
    // 충돌 감지 및 해결
    func resolveConflict(_ local: Document, _ remote: Document) -> Document {
        // Last-Write-Wins 전략
        if remote.lastModified > local.lastModified {
            return remote
        } else {
            return local
        }
    }
}

// Share Extension
import Social

class ShareViewController: UIViewController {
    func shareDocument(_ doc: Document) {
        let activityViewController = UIActivityViewController(
            activityItems: [doc.title, doc.content],
            applicationActivities: nil
        )
        
        present(activityViewController, animated: true)
    }
}

// SharePlay: FaceTime 중 실시간 협업
@available(iOS 15.1, *)
struct SharePlayView: View {
    @State var groupActivity: GroupActivity?
    
    var body: some View {
        VStack {
            Text("문서 공동 작성 중...")
            
            Button("FaceTime 공유 시작") {
                Task {
                    try await groupActivity?.activate()
                }
            }
        }
    }
}

struct Document {
    var title: String
    var content: String
    var lastModified: Date
}
```

---

### 성능 최적화 및 메모리 관리

#### 멀티 윈도우 메모리 관리, 이미지/데이터 캐시, 비동기 작업

**왜 필요한가**: iPad에서 여러 창을 띄우면 각 창이 뷰 계층 구조와 메모리를 사용하므로, 메모리 누수를 방지하고 캐시를 효율적으로 관리해야 합니다.

- 여러 창이 있어도 백그라운드 제한은 iOS와 비슷.
- 이미지/데이터 캐시 크기 제한.
- 비동기 작업 분할로 메인 스레드 블로킹 방지.

```swift
import UIKit

class CacheManager {
    static let shared = CacheManager()
    private let cache = NSCache<NSString, UIImage>()
    
    func setImage(_ image: UIImage, forKey key: String) {
        cache.setObject(image, forKey: key as NSString)
    }
    
    func getImage(forKey key: String) -> UIImage? {
        return cache.object(forKey: key as NSString)
    }
    
    func configureCache() {
        cache.totalCostLimit = 100 * 1024 * 1024 // 100MB 제한
    }
}

// 비동기 데이터 로딩
func loadLargeDataAsync(completion: @escaping ([String]) -> Void) {
    DispatchQueue.global(qos: .userInitiated).async {
        var result: [String] = []
        for i in 0..<10000 {
            result.append("Item \(i)")
        }
        
        DispatchQueue.main.async {
            completion(result)
        }
    }
}
```

---

### 접근성 및 국제화

#### Dynamic Type, RTL, VoiceOver, 멀티 윈도우에서 포커스 관리

**왜 필요한가**: iPad 사용자도 접근성 기능(Dynamic Type 확대, VoiceOver, 스위치 제어)을 활용하며, 멀티 윈도우 환경에서 포커스 이동이 제대로 되지 않으면 큰 문제가 됩니다.

- **Dynamic Type**: 사용자 설정 텍스트 크기에 따른 자동 조정.
- **RTL(오른쪽-왼쪽)**: 아랍어, 히브리어 등. 마진과 정렬 반전.
- **VoiceOver**: 스크린 리더. 큰 화면에서 여러 영역이 있으므로 명확한 Label 설정.
- **멀티 윈도우 포커스**: 각 윈도우에서 VoiceOver 포커스가 올바르게 이동하는지 확인.

```swift
import SwiftUI
import Accessibility

// Dynamic Type
struct AccessibleView: View {
    @Environment(\.sizeCategory) var sizeCategory
    
    var body: some View {
        VStack(spacing: 12) {
            Text("제목")
                .font(.system(.title, design: .default))
                .dynamicTypeSize(...DynamicTypeSize.xxxLarge)
            
            Text("이 텍스트는 사용자가 설정한 크기에 맞춥니다.")
                .font(.body)
                .lineLimit(nil) // 줄바꿈 제한 없음
        }
        .padding()
    }
}

// RTL 대응
struct RTLAwareView: View {
    @Environment(\.layoutDirection) var layoutDirection
    
    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: "checkmark.circle.fill")
                .flipsForRightToLeftLayoutDirection(false) // 반전 방지
            
            Text("완료됨")
        }
    }
}

// VoiceOver 레이블 설정
struct AccessibleButton: View {
    var body: some View {
        Button(action: { print("액션") }) {
            Image(systemName: "pencil")
        }
        .accessibilityLabel("편집")
        .accessibilityHint("현재 문서를 편집합니다")
    }
}

// 커스텀 접근성 요소
class AccessibleCustomView: UIView {
    override var accessibilityLabel: String? {
        get { "커스텀 뷰" }
        set { }
    }
    
    override var accessibilityHint: String? {
        get { "이것은 커스텀 인터랙티브 요소입니다" }
        set { }
    }
    
    override var accessibilityCustomActions: [UIAccessibilityCustomAction]? {
        return [
            UIAccessibilityCustomAction(name: "활성화", target: self, selector: #selector(activate))
        ]
    }
    
    @objc func activate() {
        print("활성화됨")
    }
}
```

---

### 테스트 시나리오 체크리스트

```
다양한 멀티태스킹 모드에서 레이아웃 확인:
- [ ] Split View (1/2, 1/3 분할)
- [ ] Slide Over (오버레이)
- [ ] Stage Manager (윈도우 겹침, iPad Pro 7세대+)
- [ ] 외장 디스플레이 연결 시 동작

입력 방식 혼합 테스트:
- [ ] 포인터(마우스) + 키보드
- [ ] Apple Pencil (필기, 호버)
- [ ] 터치 + 펜슬
- [ ] Drag & Drop

파일 작업 흐름:
- [ ] Files 앱에서 파일 선택
- [ ] 보안 북마크로 지속적 접근
- [ ] 다른 앱과의 Drag & Drop
- [ ] 외장 드라이브 파일 작업

협업 기능:
- [ ] 클라우드 동기화 (CloudKit)
- [ ] 충돌 감지 및 해결
- [ ] SharePlay (FaceTime)

성능:
- [ ] 메모리 누수 모니터링 (Instruments)
- [ ] 여러 창 열었을 때 프레임 유지
- [ ] 배터리 소비

접근성:
- [ ] VoiceOver + 멀티 윈도우
- [ ] Dynamic Type 최대 크기
- [ ] RTL 언어 (테스트 언어 설정)
```

---

### 관련 링크

[apple-ipados-multitasking](../../04_system_services/apple-ipados-multitasking.md), [apple-app-lifecycle-and-ui](../../02_ui_frameworks/apple-app-lifecycle-and-ui.md), [apple-storage-and-filesystems](../../03_data_networking/apple-storage-and-filesystems.md), [apple-networking-and-cloud](../../03_data_networking/apple-networking-and-cloud.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md).
