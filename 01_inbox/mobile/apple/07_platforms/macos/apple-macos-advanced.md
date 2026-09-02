---
title: apple-macos-advanced
tags: [apple, apple/platforms, apple/platforms/macos, desktop, macos]
aliases: ["macOS Advanced", "macOS 심화"]
date modified: 2026-08-10 16:00:00 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## macOS Advanced

macOS 데스크탑 앱을 더 깊게 만들 때 필요한 내용을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

### 💡 왜 이것을 알아야 하나요?

macOS는 iOS와 달리 **권한 체계가 다양하고(TCC, Entitlement), 배포 경로도 여러 개**(Mac App Store, 직배포, 오픈소스)입니다. 잘못된 권한 설정이나 노타리제이션 누락은 Gatekeeper 차단과 사용자 신뢰 상실로 이어집니다.

---

### 샌드박스 vs 비샌드박스 배포 모델

#### Mac App Store (샌드박스) vs 직배포 (비샌드박스). 각각 권한과 배포 절차 상이

**왜 필요한가**: Mac App Store 앱은 샌드박스 격리로 보안이 높지만 기능 제약이 있고, 직배포는 자유도가 높지만 사용자 신뢰를 얻기 위해 서명과 노타리제이션이 필수입니다.

- **Mac App Store (샌드박스)**: 파일 접근 제한, Security-scoped bookmark 사용. 배포는 빠르지만 기능 제약.
- **직배포 (비샌드박스)**: 더 많은 권한(시스템 서비스 접근, 기기 드라이버 등)이 있지만, **코드 서명**(Code Sign)과 **노타리제이션**(Notarization)이 필수. Apple의 Gatekeeper가 검사.
- **시스템 확장/드라이버/네트워크 확장**: 별도 Entitlement와 Apple 승인 절차 필요.

```swift
import Foundation
import Security

// 코드 서명 확인
func verifyCodeSignature() {
    let bundleURL = Bundle.main.bundleURL
    var secStatic: SecStaticCode?
    
    let status = SecStaticCodeCreateWithPath(bundleURL as CFURL, [], &secStatic)
    if status == errSecSuccess {
        print("코드 서명됨")
    } else {
        print("코드 서명 없음 또는 유효하지 않음")
    }
}

// Entitlement 확인
func checkEntitlements() {
    guard let bundleURL = Bundle.main.bundleURL as CFURL? else { return }
    
    var secStatic: SecStaticCode?
    SecStaticCodeCreateWithPath(bundleURL, [], &secStatic)
    
    if let secStatic = secStatic {
        var requirement: SecRequirement?
        SecRequirementCreateWithString("anchor apple generic" as CFString, [], &requirement)
        
        let checkStatus = SecStaticCodeCheckValidity(secStatic, [], requirement)
        if checkStatus == errSecSuccess {
            print("Entitlement 유효함")
        }
    }
}

// Gatekeeper 정책 우회 시도 방지
class GatekeeperHelper {
    static func showGatekeeperGuide() {
        let alert = NSAlert()
        alert.messageText = "App이 블로킹되었습니다"
        alert.informativeText = "시스템 설정 > 개인정보 보호 및 보안에서 '어쨌든 열기'를 클릭하세요."
        alert.runModal()
    }
}
```

---

### 파일 접근 및 권한 관리

#### NSOpenPanel/NSSavePanel로 사용자 선택 경로만 접근. Full Disk Access, TCC 권한 명시

**왜 필요한가**: macOS는 iOS처럼 **TCC (Transparency, Consent, Control)** 권한을 강제하므로, 파일 접근, 캘린더, 마이크, 카메라 등은 모두 사용자 동의를 거쳐야 합니다.

- **NSOpenPanel/NSSavePanel**: 사용자가 직접 선택한 경로만 앱이 접근할 수 있음.
- **Security-scoped Bookmark**: 선택한 파일/폴더에 이후 접근하기 위한 북마크. 앱 재시작 후에도 유효.
- **Full Disk Access**: Entitlement 요청 후 사용자가 시스템 설정에서 명시적으로 허용해야 함.
- **TCC 권한**: 캘린더, 연락처, 사진, 마이크, 카메라, 스크린 녹화 등.

```swift
import Cocoa

class FileAccessManager {
    // 파일 선택 대화
    func openFile() {
        let openPanel = NSOpenPanel()
        openPanel.allowsMultipleSelection = false
        openPanel.canChooseDirectories = true
        openPanel.canChooseFiles = true
        
        openPanel.begin { result in
            if result == .OK, let url = openPanel.url {
                print("선택된 파일: \(url.lastPathComponent)")
                
                // 보안 북마크 생성
                self.createSecurityBookmark(url)
            }
        }
    }
    
    // 파일 저장 대화
    func saveFile() {
        let savePanel = NSSavePanel()
        savePanel.title = "파일 저장"
        savePanel.message = "저장할 위치와 이름을 지정하세요"
        
        savePanel.begin { result in
            if result == .OK, let url = savePanel.url {
                print("저장 경로: \(url.path)")
                
                // 파일 쓰기 수행
                do {
                    let content = "샘플 데이터"
                    try content.write(to: url, atomically: true, encoding: .utf8)
                } catch {
                    print("저장 실패: \(error)")
                }
                
                // 보안 북마크 생성
                self.createSecurityBookmark(url)
            }
        }
    }
    
    // 보안 북마크 생성 (지속적 접근)
    func createSecurityBookmark(_ url: URL) {
        do {
            let bookmarkData = try url.bookmarkData(
                options: .withSecurityScope,
                includingResourceValuesForKeys: nil,
                relativeTo: nil
            )
            
            // UserDefaults에 저장
            UserDefaults.standard.set(bookmarkData, forKey: url.lastPathComponent)
            print("보안 북마크 생성됨")
        } catch {
            print("북마크 생성 실패: \(error)")
        }
    }
    
    // 저장된 북마크로 파일 접근
    func accessBookmarkedFile(key: String) -> URL? {
        guard let bookmarkData = UserDefaults.standard.data(forKey: key) else {
            return nil
        }
        
        var isStale = false
        do {
            let url = try URL(
                resolvingBookmarkData: bookmarkData,
                options: .withSecurityScope,
                relativeTo: nil,
                bookmarkDataIsStale: &isStale
            )
            
            if isStale {
                // 북마크 업데이트
                self.createSecurityBookmark(url)
            }
            
            // 보안 범위 활성화
            guard url.startAccessingSecurityScopedResource() else {
                return nil
            }
            defer { url.stopAccessingSecurityScopedResource() }
            
            return url
        } catch {
            print("북마크 해석 실패: \(error)")
            return nil
        }
    }
}
```

---

### macOS UI/UX 설계 원칙

#### 메뉴바, 단축키, Dock, Menubar Extra, 멀티 윈도우/탭/풀스크린/스페이스 지원

**왜 필요한가**: macOS 사용자는 메뉴바와 키보드 단축키를 자주 사용하고, 여러 창과 데스크톱(스페이스)을 관리하므로, 이런 기능을 제대로 지원해야 생산성 앱으로 평가받을 수 있습니다.

- **메뉴바**: 파일, 편집, 보기, 윈도우, 도움말 메뉴는 필수.
- **키보드 단축키**: Command 조합 활용 (예: Command+S 저장, Command+Z 실행 취소).
- **Menubar Extra** (상단 우측 아이콘): 빠른 접근점. 상태 표시.
- **Dock**: 앱 아이콘, Badge 표시(업데이트, 알림 수).
- **윈도우 관리**: 탭, 풀스크린, 스페이스, 다중 모니터 지원.

```swift
import Cocoa

// NSDocument 기반 앱 (파일 중심)
class MyDocument: NSDocument {
    var content: String = ""
    
    override func data(ofType typeName: String) throws -> Data {
        guard let data = content.data(using: .utf8) else {
            throw NSError(domain: "Data conversion failed", code: -1)
        }
        return data
    }
    
    override func read(from data: Data, ofType typeName: String) throws {
        content = String(data: data, encoding: .utf8) ?? ""
    }
}

// 메뉴 구성 (AppDelegate)
class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        setupMainMenu()
    }
    
    func setupMainMenu() {
        let mainMenu = NSMenu()
        
        // 파일 메뉴
        let fileMenu = NSMenu(title: "파일")
        fileMenu.addItem(NSMenuItem(title: "새로 만들기", action: #selector(newDocument), keyEquivalent: "n"))
        fileMenu.addItem(NSMenuItem(title: "열기", action: #selector(openDocument), keyEquivalent: "o"))
        fileMenu.addItem(NSMenuItem.separator())
        fileMenu.addItem(NSMenuItem(title: "저장", action: #selector(saveDocument), keyEquivalent: "s"))
        fileMenu.addItem(NSMenuItem(title: "다른 이름으로 저장", action: #selector(saveAsDocument), keyEquivalent: "S"))
        fileMenu.addItem(NSMenuItem.separator())
        fileMenu.addItem(NSMenuItem(title: "종료", action: #selector(NSApplication.terminate), keyEquivalent: "q"))
        
        // 편집 메뉴
        let editMenu = NSMenu(title: "편집")
        editMenu.addItem(NSMenuItem(title: "실행 취소", action: #selector(undo), keyEquivalent: "z"))
        editMenu.addItem(NSMenuItem(title: "다시 실행", action: #selector(redo), keyEquivalent: "Z"))
        
        // 메뉴바에 추가
        mainMenu.addItem(NSMenuItem(title: "파일", action: nil, keyEquivalent: "").submenu = fileMenu)
        mainMenu.addItem(NSMenuItem(title: "편집", action: nil, keyEquivalent: "").submenu = editMenu)
        
        NSApp.mainMenu = mainMenu
    }
    
    @objc func newDocument() { print("새로 만들기") }
    @objc func openDocument() { print("열기") }
    @objc func saveDocument() { print("저장") }
    @objc func saveAsDocument() { print("다른 이름으로 저장") }
    @objc func undo() { print("실행 취소") }
    @objc func redo() { print("다시 실행") }
}

// Menubar Extra (상단 우측 아이콘)
class StatusBarManager {
    var statusBar: NSStatusBar?
    var statusItem: NSStatusBarItem?
    
    func setupStatusBar() {
        statusBar = NSStatusBar.system
        statusItem = statusBar?.statusItem(withLength: NSStatusBarItem.variableLength)
        
        if let button = statusItem?.button {
            button.image = NSImage(systemSymbolName: "star.fill", accessibilityDescription: "상태")
            button.action = #selector(statusBarClicked)
            button.target = self
        }
        
        // 컨텍스트 메뉴 추가
        let menu = NSMenu()
        menu.addItem(NSMenuItem(title: "설정", action: #selector(openPreferences), keyEquivalent: ""))
        menu.addItem(NSMenuItem(title: "종료", action: #selector(quitApp), keyEquivalent: ""))
        
        statusItem?.menu = menu
    }
    
    @objc func statusBarClicked() {
        print("상태바 클릭됨")
    }
    
    @objc func openPreferences() {
        print("설정 열기")
    }
    
    @objc func quitApp() {
        NSApplication.shared.terminate(nil)
    }
}

// Dock Badge (앱 아이콘의 배지)
func updateDockBadge(count: Int) {
    if count > 0 {
        NSApp.dockTile.badgeLabel = "\(count)"
    } else {
        NSApp.dockTile.badgeLabel = ""
    }
}

// 윈도우 탭 지원
class MyWindowController: NSWindowController {
    override func windowDidLoad() {
        super.windowDidLoad()
        
        if let window = window {
            // 풀스크린 버튼 표시
            window.collectionBehavior = .fullScreenPrimary
        }
    }
}
```

---

### 성능 최적화 및 전력 관리

#### GCD QoS, App Nap, Instruments로 성능 진단. 노트북 배터리 관리

**왜 필요한가**: macOS는 iOS보다 성능 요구가 높지만, 노트북은 배터리를 관리해야 하고, 발열/팬 소음도 사용자 경험에 영향을 미칩니다.

- **GCD QoS**: 백그라운드 작업(`.background`)과 사용자 상호작용(`.userInitiated`) 구분.
- **App Nap**: 앱이 숨겨지면 자동으로 절전 상태로 전환. 명시적으로 비활성화 가능.
- **Instruments**: Time Profiler, System Trace, Energy Log로 진단.

```swift
import Foundation

// GCD QoS 활용
class BackgroundTaskManager {
    func performHeavyWork() {
        // 백그라운드 작업: 우선순위 낮음
        DispatchQueue.global(qos: .background).async {
            let result = self.complexCalculation()
            
            // UI 업데이트는 메인 스레드
            DispatchQueue.main.async {
                self.updateUI(with: result)
            }
        }
    }
    
    func performUserInitiatedWork() {
        // 사용자가 명시적으로 요청한 작업
        DispatchQueue.global(qos: .userInitiated).async {
            let result = self.quickCalculation()
            
            DispatchQueue.main.async {
                self.updateUI(with: result)
            }
        }
    }
    
    func complexCalculation() -> Int {
        return (0...10_000_000).reduce(0) { $0 + $1 }
    }
    
    func quickCalculation() -> Int {
        return (0...1_000).reduce(0) { $0 + $1 }
    }
    
    func updateUI(with result: Int) {
        print("결과: \(result)")
    }
}

// App Nap 비활성화 (필요시)
class AppNapManager {
    func disableAppNap() {
        // 실시간 처리 필요한 앱에서만 사용
        ProcessInfo.processInfo.beginActivity(options: .userInitiatedAllowingIdleSleep, reason: "실시간 처리")
    }
}

// 에너지 영향 점검
class EnergyImpactMonitor {
    func checkEnergyImpact() {
        let processInfo = ProcessInfo.processInfo
        
        // 활성 프로세서 수
        let activeProcessors = processInfo.activeProcessorCount
        print("활성 프로세서: \(activeProcessors)")
        
        // 물리 메모리
        let physicalMemory = processInfo.physicalMemory / (1024 * 1024)
        print("물리 메모리: \(physicalMemory)MB")
    }
}
```

---

### 노타리제이션 및 배포

#### Notarytool로 Apple 검증. Code Sign & Staple. Gatekeeper 대응

**왜 필요한가**: macOS 10.15+에서는 모든 다운로드 앱이 Apple의 노타리제이션을 거쳐야 Gatekeeper가 차단하지 않습니다.

- **코드 서명**: `codesign` 명령으로 서명.
- **노타리제이션**: `notarytool` 또는 `xcrun notarize-app`으로 Apple에 제출. 검증 후 "staple" 처리.
- **Gatekeeper**: 사용자가 설정에서 예외 허용 가능. 우회 시도는 금지.

```bash
# 코드 서명
codesign --deep --force --verify --verbose --sign "Developer ID Application: Your Name" MyApp.app

# 노타리제이션 준비: ZIP 생성
ditto -c -k --keepParent MyApp.app MyApp.zip

# Apple에 노타리제이션 요청 (최신 방식)
notarytool submit MyApp.zip --apple-id "your-email@icloud.com" --team-id "ABCDEFGH" --password "@keychain:AC_PASSWORD"

# Staple (노타리제이션 결과 앱에 첨부)
xcrun stapler staple MyApp.app
```

```swift
// 노타리제이션 상태 확인
import Foundation

func checkNotarizationStatus() {
    let task = Process()
    task.executableURL = URL(fileURLWithPath: "/usr/bin/xcrun")
    task.arguments = ["notarytool", "history", "--keychain-profile", "AC_PASSWORD"]
    
    let pipe = Pipe()
    task.standardOutput = pipe
    
    try? task.run()
    task.waitUntilExit()
    
    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    if let output = String(data: data, encoding: .utf8) {
        print("노타리제이션 히스토리:\n\(output)")
    }
}
```

---

### 자동화 및 스크립트 통합

#### AppleScript, Shortcuts, LaunchAgent/LaunchDaemon으로 작업 자동화

**왜 필요한가**: macOS는 AppleScript와 Automator를 통해 반복 작업을 자동화할 수 있고, LaunchAgent/Daemon으로 백그라운드 작업을 예약할 수 있습니다.

- **AppleScript**: 앱 간 통신 (Apple Event).
- **Shortcuts**: Automator 대체. 더 직관적인 UI.
- **LaunchAgent**: 사용자 로그인 후 실행.
- **LaunchDaemon**: 시스템 부팅 후 실행 (관리자 권한 필요).

```swift
import Cocoa

// AppleScript 실행
class AppleScriptExecutor {
    func executeAppleScript(_ source: String) {
        if let script = NSAppleScript(source: source) {
            var error: NSDictionary?
            script.executeAndReturnError(&error)
            
            if let error = error {
                print("AppleScript 실행 오류: \(error)")
            } else {
                print("AppleScript 실행 성공")
            }
        }
    }
}

// 예시: Finder에서 데스크톱 파일 개수 구하기
func countDesktopFiles() {
    let script = """
    tell application "Finder"
        set desktopItems to (count files of (path to desktop))
        return desktopItems
    end tell
    """
    
    let executor = AppleScriptExecutor()
    executor.executeAppleScript(script)
}
```

---

### 개발 및 테스트 시나리오

#### 다양한 해상도/스케일/모니터. 샌드박스/비샌드박스, 인텔/Apple Silicon 테스트

**체크리스트**:
```
UI 렌더링:
- [ ] 1x/2x Retina 스케일
- [ ] 다양한 해상도 (1440x900, 1920x1080, 3440x1440 울트라와이드)
- [ ] 외부 모니터 연결 시 색역/DPI 차이
- [ ] 다크 모드/라이트 모드

보안/권한:
- [ ] 샌드박스 앱 권한 처리
- [ ] Full Disk Access 요청 플로우
- [ ] TCC 권한 거부 시나리오
- [ ] 코드 서명 및 노타리제이션

아키텍처:
- [ ] Apple Silicon (ARM64)
- [ ] Intel (x86_64)

입력 장치:
- [ ] Magic Mouse/트랙패드
- [ ] 외부 마우스/키보드

백그라운드:
- [ ] LaunchAgent 자동 시작
- [ ] App Nap 상태에서 복구
- [ ] 메모리 누수 모니터링
```

---

### 관련 링크

[apple-macos-system](../apple-macos-system.md), [apple-build-and-distribution](../../08_packaging_deployment/apple-build-and-distribution.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md).
