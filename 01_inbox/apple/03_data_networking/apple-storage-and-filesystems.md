---
title: apple-storage-and-filesystems
tags: [apple, filesystem, storage, sandbox, filemanager, app-group]
aliases: []
date modified: 2025-12-17 21:00:00 +09:00
date created: 2025-12-16 16:09:38 +09:00
---

## Storage & Filesystems Deep Dive

iOS/macOS 앱은 **샌드박스(Sandbox)**라는 격리된 공간에 갇혀 있습니다.
"파일을 저장한다"는 행위조차, 내 앱만의 작은 방(Container) 안에서 질서 있게 이루어져야 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **앱 업데이트했더니 데이터가 날아갔어요**: "tmp" 폴더나 "Library/Caches"에 유저 데이터를 저장하면, OS가 공간 확보를 위해 언제든 지워버릴 수 있습니다.
- **절대 경로 저장 금지**: `user/123/Documents/image.png`라는 경로를 DB에 문자열로 저장하지 마세요. 앱이 업데이트되면 `user/456/Documents/`로 컨테이너 경로가 바뀝니다(UUID 변경). 항상 상대 경로(`Documents/image.png`)로 저장해야 합니다.
- **위젯과 데이터 공유**: 앱 위젯이 메인 앱의 데이터를 읽으려면 `App Group`이라는 특별한 공유 창고를 써야 합니다.

---

### 📂 앱 컨테이너 구조 (The Anatomy)

#### 1. Documents/
- **용도**: 사용자가 생성하거나 인지하는 중요한 데이터. (예: 작성한 문서, 다운로드한 오디오북)
- **특징**: iCloud 및 iTunes 백업에 포함됩니다.
- **주의**: 재생 가능한 콘텐츠(임시 다운로드 파일)를 여기 넣으면 앱 심사에서 거절될 수 있습니다. ("do not backup" 속성 필수)

#### 2. Library/
- **Application Support/**: 앱 동작에 필수적이지만 사용자에게 노출할 필요 없는 데이터. (예: Core Data DB 파일, 설정 파일)
- **Caches/**: 언제든지 다시 만들 수 있는 데이터. (예: 이미지 캐시, 서버 응답 캐시). OS가 공간 부족 시 *임의로 삭제*할 수 있습니다.
- **Preferences/**: `UserDefaults` 파일(.plist)이 저장되는 곳입니다. 직접 건드리지 마세요.

#### 3. tmp/
- **용도**: 지금 당장만 필요한 임시 파일. (예: Zip 압축 풀기 중간 단계)
- **특징**: 앱이 종료되면 시스템이 지울 수 있습니다. 개발자가 직접 비워주는 게 매너입니다.

---

### 🔐 보안 및 공유 (Security & Sharing)

#### 1. App Group (공유 컨테이너)
기본적으로 앱 A와 앱 B(혹은 위젯)는 서로의 파일을 볼 수 없습니다.
`App Group`을 설정하면 `/private/var/mobile/Containers/Shared/AppGroup/UUID/` 경로에 공유 폴더가 생깁니다.

```swift
let fileManager = FileManager.default
if let sharedURL = fileManager.containerURL(forSecurityApplicationGroupIdentifier: "group.com.myapp") {
    // 여기에 파일을 쓰면 위젯에서도 읽을 수 있음
}
```

#### 2. Data Protection (파일 잠금)
iOS는 기기가 잠겨있을 때(Lock Screen), 파일 시스템 전체를 암호화하여 잠급니다.
- **File Protection Complete**: 기기가 잠기면 파일 읽기/쓰기 불가. (백그라운드 작업 시 주의)
- **Complete Until First Unlock**: 부팅 후 한 번만 풀면 계속 접근 가능 (기본값).

---

### 🛠️ 실무 패턴 및 주의사항

#### 1. 절대 경로(Absolute Path)의 함정
앱이 업데이트되거나 재설치되면 컨테이너의 UUID 경로가 바뀝니다.

```swift
// ❌ Bad: 전체 경로를 DB에 저장
let fullPath = url.path // "/var/.../Application/UUID-1111/Documents/file.txt"
saveToDB(fullPath) 

// (앱 업데이트 후)
// ❌ 경로가 "/var/.../Application/UUID-2222/Documents/file.txt"로 바뀌어서 못 찾음

// ✅ Good: 상대 경로만 저장하고 런타임에 조합
let fileName = "file.txt"
saveToDB(fileName)

// 불러올 때
let docDir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
let fileURL = docDir.appendingPathComponent(fileName)
```

#### 2. 대용량 파일 처리
`Data(contentsOf: url)`로 1GB 파일을 읽으면 메모리가 터집니다.
- `FileHandle`이나 `InputStream`을 사용하여 청크(Chunk) 단위로 읽어야 합니다.
- `Memory Mapped File` (mmap)을 쓰면 가상 메모리를 활용해 큰 파일도 빠르게 읽을 수 있습니다(`Data(contentsOf: url, options: .mappedIfSafe)`).

### 더 보기
- [[apple-platform-differences]] - macOS 샌드박스와 iOS 차이
- [[apple-security-privacy]] - Keychain과 파일 보안 등급
