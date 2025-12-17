# Git 커밋 메시지 작성법

## 좋은 커밋 메시지의 중요성
- 나중에 코드 변경 이유를 쉽게 찾을 수 있음
- 팀원들이 변경사항을 빠르게 이해 가능
- 자동화 도구가 버전 관리와 릴리스 노트 생성에 활용

## 기본 구조

### 표준 형식
```
<타입>: <제목>

<본문>

<꼬리말>
```

### 간단한 예시
```
feat: 사용자 로그인 기능 추가

로그인 페이지와 인증 로직을 구현했습니다.
- 이메일/패스워드 로그인 지원
- JWT 토큰 기반 인증
- 로그인 실패 시 에러 메시지 표시

Closes #123
```

## 커밋 타입 (Type)

### 주요 타입들
- **feat**: 새로운 기능 추가
- **fix**: 버그 수정
- **docs**: 문서 변경
- **style**: 코드 포맷팅, 세미콜론 누락 등
- **refactor**: 기능 변경 없는 코드 리팩토링
- **test**: 테스트 코드 추가/수정
- **chore**: 빌드 프로세스, 라이브러리 업데이트 등

### 예시
```bash
feat: 결제 모듈 추가
fix: 로그인 버튼 클릭 안되는 문제 해결
docs: API 문서 업데이트
style: 코드 들여쓰기 수정
refactor: 사용자 데이터 처리 로직 개선
test: 사용자 등록 테스트 케이스 추가
chore: webpack 설정 업데이트
```

## 제목 (Subject) 작성법

### 규칙
1. **50자 이내로 작성**
2. **명령형으로 작성** ("추가했다" ❌, "추가" ⭕)
3. **첫 글자는 대문자**
4. **마침표 사용 안함**
5. **무엇을 했는지 명확히 표현**

### 좋은 제목 예시
```
feat: 사용자 프로필 편집 기능 추가
fix: 이메일 유효성 검사 오류 수정
refactor: 데이터베이스 연결 로직 개선
docs: 설치 가이드 업데이트
```

### 나쁜 제목 예시
```
fix: 버그 수정됨 (무엇을 수정했는지 불명확)
feat: 새로운 기능을 추가했습니다 (과거형, 너무 김)
update: stuff (불명확)
asdf (의미 없음)
```

## 본문 (Body) 작성법

### 언제 본문을 작성할까?
- 변경 이유가 복잡할 때
- 여러 파일을 수정했을 때
- 중요한 기술적 결정이 있을 때

### 작성 규칙
1. **72자마다 줄바꿈**
2. **무엇을 바꿨는지보다 왜 바꿨는지 설명**
3. **어떻게 문제를 해결했는지 설명**

### 예시
```
fix: 사용자 로그아웃 시 세션이 완전히 삭제되지 않는 문제 해결

기존에는 클라이언트의 토큰만 삭제하고 서버의 세션은
그대로 남아있어서 보안상 문제가 있었습니다.

이제 로그아웃 시 다음과 같이 처리합니다:
- 클라이언트의 JWT 토큰 삭제
- 서버의 세션 정보 완전 삭제
- 관련 캐시 데이터 정리

이로 인해 로그아웃 후 이전 토큰으로 접근할 수 없게 되었습니다.
```

## 꼬리말 (Footer)

### 이슈 참조
```
Closes #123
Fixes #456
Resolves #789
Related to #012
```

### Breaking Changes (중요한 변경사항)
```
BREAKING CHANGE: API 응답 형식이 변경되었습니다.

기존: { data: { user: {...} } }
새로운: { user: {...} }
```

## 실제 예시들

### 기능 추가
```
feat: 다중 파일 업로드 기능 구현

사용자가 한 번에 여러 파일을 업로드할 수 있도록 했습니다.

주요 변경사항:
- 드래그앤드롭 인터페이스 추가
- 파일 타입 및 크기 검증
- 업로드 진행률 표시
- 실패한 파일에 대한 에러 메시지

최대 10개 파일, 각각 5MB까지 업로드 가능합니다.

Closes #234
```

### 버그 수정
```
fix: Safari에서 날짜 입력 필드가 동작하지 않는 문제 해결

Safari는 input[type="date"]의 기본값 형식을
다르게 해석해서 발생한 문제였습니다.

ISO 8601 형식(YYYY-MM-DD)으로 통일하고
브라우저별 호환성 검사를 추가했습니다.

Fixes #567
```

### 리팩토링
```
refactor: 사용자 인증 로직을 별도 모듈로 분리

기존 코드가 여러 파일에 분산되어 있어 유지보수가
어려웠습니다.

변경사항:
- 인증 관련 함수들을 auth.js로 통합
- 중복 코드 제거
- 단위 테스트 추가로 안정성 향상

외부 API는 변경되지 않았습니다.
```

## 팀별 컨벤션 예시

### Conventional Commits 스타일
```
feat(auth): 소셜 로그인 기능 추가
fix(ui): 모바일에서 버튼이 잘리는 문제 수정
docs(api): 사용자 API 엔드포인트 문서화
test(auth): 로그인 실패 케이스 테스트 추가
```

### Angular 스타일
```
feat(scope): 기능 설명

fix(scope): 문제 해결

docs: 문서 업데이트
```

### 한국어 스타일
```
기능: 사용자 알림 설정 페이지 추가
수정: 이메일 전송 실패 문제 해결
문서: README 파일 업데이트
```

## 자동화 도구

### Commitizen 사용
```bash
npm install -g commitizen
npm install -g cz-conventional-changelog

# 설정
echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc

# 사용
git cz
```

### Git 훅 설정
```bash
# .gitmessage 템플릿 파일 생성
git config --global commit.template ~/.gitmessage

# ~/.gitmessage 내용:
# <타입>: <제목>
#
# <본문>
#
# <꼬리말>
```

### Commitlint 사용
```bash
npm install -g @commitlint/cli @commitlint/config-conventional

# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

# 훅 설정
echo 'npx commitlint --edit $1' > .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

## 자주하는 실수들

### 피해야 할 것들
```bash
# 너무 모호함
git commit -m "fix"
git commit -m "update"

# 너무 길고 구체적
git commit -m "사용자가 로그인 페이지에서 이메일을 입력하고 비밀번호를 입력한 다음 로그인 버튼을 클릭했을 때 서버에서 인증을 처리하고 성공하면 대시보드로 리다이렉트하는 기능 추가"

# 과거형 사용
git commit -m "feat: 로그인 기능을 추가했다"

# 개발자 중심적
git commit -m "fix: console.log 제거"
```

### 올바른 방법
```bash
# 명확하고 간결
git commit -m "feat: 사용자 로그인 기능 추가"
git commit -m "fix: 이메일 유효성 검사 오류 수정"
git commit -m "refactor: 데이터베이스 연결 로직 개선"
```

## 커밋 단위

### 좋은 커밋
- 논리적으로 관련된 변경사항만 포함
- 빌드가 깨지지 않는 상태
- 하나의 목적을 가짐

### 나쁜 커밋
- 여러 기능이 섞여 있음
- 관련 없는 파일들이 포함됨
- 빌드가 실패하는 상태

## 관련 문서
- [[Git 기본 개념]]
- [[Git 명령어 비교]]
- [[Git 브랜치 전략]]
- [[Git 고급 워크플로우]]