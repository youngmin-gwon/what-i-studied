# GitUI: 터미널 기반 고성능 Git UI 가이드

**GitUI**는 Rust로 작성된 매우 빠르고 효율적인 터미널 기반 Git 인터페이스입니다. 키보드 중심의 조작을 통해 Git CLI의 복잡한 문법을 외우지 않고도 강력한 Git 기능을 활용할 수 있게 해줍니다.

---

## 1. 개요 (Overview)
- **속도와 성능**: Rust 라이브러리(`git2-rs`)를 사용하여 대규모 리포지토리에서도 지연 없는 성능을 제공합니다.
- **키보드 중심**: 마우스 없이도 거의 모든 작업을 수행할 수 있도록 설계되었습니다.
- **안정성**: Rust의 메모리 안전성을 바탕으로 충돌 없는 사용자 경험을 제공합니다.

---

## 2. 설치 방법 (Installation)

### MacOS (Homebrew)
```bash
brew install gitui
```

### Rust/Cargo (Universal)
```bash
cargo install gitui
```

---

## 3. 기본 조작법 (Basic Usage)

### 실행
터미널에서 Git 저장소 위치로 이동한 후 다음을 입력합니다:
```bash
gitui
```

### 탐색 및 제어
- **창 이동**: `Tab` (다음 창), `Shift + Tab` (이전 창)
- **탭 전환**: 숫자키 `1`~`5` 사용 (Status, Logs, Files, Stashing, Stashes 순서)
- **도움말**: `?` 키를 누르면 현재 화면에서 사용 가능한 모든 단축키를 확인할 수 있습니다.
- **종료**: `q` 또는 `Esc`

---

## 4. 주요 탭별 기능 (Tab Features)

### [1] Status: 변경 사항 관리
현재 작업 디렉토리의 변경 사항을 확인하고 커밋하는 메인 탭입니다.
- **스테이징**: 파일 선택 후 `Enter` (또는 `Space`)를 눌러 Stage/Unstage 전환.
- **변경 사항 확인**: 오른쪽 패널에서 Diff를 실시간으로 확인.
- **커밋**: `c` 키를 눌러 커밋 메시지 입력 (완료 후 `Enter`).
- **커밋 수정**: `A` (Shift + a) 키로 직전 커밋을 수정(Amend).
- **Push/Pull**: `p` (Push), `f` (Fetch), `u` (Pull).

### [2] Logs: 커밋 히스토리
저장소의 커밋 내역을 탐색하고 관리합니다.
- **세부 정보**: 커밋 선택 후 `Enter`를 눌러 변경된 파일 목록 확인.
- **해시 복사**: `y` 키를 눌러 선택한 커밋의 Hash 값을 클립보드에 복사.
- **파일 목록**: `Shift + f`를 눌러 해당 커밋에 포함된 전체 파일 조회.
- **브랜치/태그 관리**: `b` 키로 브랜치 목록을 보고 전환하거나 관리할 수 있습니다.

### [3] Files: 리포지토리 파일 브라우저
현재 버전의 모든 파일을 탐색합니다. `.gitignore`에 등록된 파일은 제외됩니다.
- **검색**: `f` 키로 파일명 기반 퍼지 검색 수행.
- **편집**: `e` 키를 눌러 기본 에디터(`$EDITOR`)로 해당 파일 열기.
- **Blame**: `b` 키로 해당 라인의 수정 기록 확인.

### [4] Stashing & Stashes: 임시 저장
작업 중인 내용을 잠시 보관하거나 꺼내올 때 사용합니다.
- **Stashing**: 현재 변경 사항을 스태시에 저장.
- **Stashes**: 저장된 스태시 목록을 보고 다시 적용(Apply)하거나 삭제.

---

## 5. 고급 설정 및 팁

### Vim 키바인딩 설정 (hjkl 지원)
기본적으로 방향키를 사용하지만, 설정을 통해 Vim 스타일(`hjkl`)로 바꿀 수 있습니다.

1. `gitui` 설정 폴더로 이동 (MacOS: `~/Library/Application Support/gitui`)
2. `key_config.ron` 파일을 생성하거나 수정하여 Vim 설정을 추가합니다.
   - [공식 Vim 키 설정 샘플](https://github.com/extrawurst/gitui/blob/master/vim_style_key_config.ron)을 참고하세요.

### 외부 에디터 연동
커밋 메시지 작성이나 파일 편집 시 사용하는 에디터는 환경 변수를 따릅니다.
```bash
# .zshrc 또는 .bashrc에 추가
export EDITOR='nvim' # 또는 'code', 'vim' 등
```

---

## 6. 참고 링크
- [공식 GitHub 리포지토리](https://github.com/extrawurst/gitui)
- [GitUI 공식 블로그 가이드 (zolmok.org)](https://zolmok.org/gitui/)
