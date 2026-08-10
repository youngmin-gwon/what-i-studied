---
title: http-protocol
tags: [application, http, networking, protocol, web]
aliases: [HTTP, HTTP 상태코드, HyperText Transfer Protocol]
date modified: 2026-01-08 16:13:47 +09:00
date created: 2026-01-08 16:06:40 +09:00
---

## 🌐 개요 (Overview)

**HTTP (HyperText Transfer Protocol)** 는 웹 상에서 하이퍼텍스트 문서를 전송하기 위한 프로토콜입니다. **TCP 80 번** 포트를 사용합니다.

## 📋 HTTP 특징

| 특징 | 설명 |
|------|------|
| **Stateless** | 상태를 유지하지 않음 (쿠키/세션으로 보완) |
| **Request-Response** | 클라이언트 요청, 서버 응답 |
| **Text-based** | ASCII 텍스트 기반 프로토콜 |
| **Keep-Alive** | HTTP/1.1 부터 지속 연결 지원 |

---

## 📨 HTTP 요청 메서드 (Method)

| 메서드 | 설명 | 특징 |
|--------|------|------|
| **GET** | 리소스 조회 | 데이터가 URL 에 노출 |
| **POST** | 리소스 생성/데이터 전송 | 본문에 데이터 포함 |
| **PUT** | 리소스 수정 (전체) | 멱등성 보장 |
| **PATCH** | 리소스 수정 (일부) | |
| **DELETE** | 리소스 삭제 | |
| **HEAD** | 헤더 정보만 조회 | GET 과 동일하나 본문 없음 |
| **OPTIONS** | 지원 메서드 확인 | CORS preflight |
| **TRACE** | 경로 추적 | XST 공격에 취약 |
| **CONNECT** | 프록시 터널링 | HTTPS 프록시 |

### GET vs POST

GET과 POST 메서드의 상세한 기술 비교, 사용 사례, 실무 선택 기준은 별도 문서로 분리되어 있습니다.

- **[GET vs POST](get-vs-post.md)** - GET과 POST의 데이터 위치, 보안, 캐싱, 성능 비교

---

## 📊 HTTP 상태 코드 (Status Code)

### 1xx: 정보 (Informational)

| 코드 | 이름 | 설명 |
|:----:|------|------|
| 100 | Continue | 요청 계속 진행 |
| 101 | Switching Protocols | 프로토콜 전환 (WebSocket) |

### 2xx: 성공 (Success)

| 코드 | 이름 | 설명 |
|:----:|------|------|
| **200** | OK | 요청 성공 |
| 201 | Created | 리소스 생성 완료 |
| 204 | No Content | 성공, 본문 없음 |

### 3xx: 리다이렉션 (Redirection)

| 코드 | 이름 | 설명 |
|:----:|------|------|
| **301** | Moved Permanently | 영구 이동 |
| **302** | Found | 임시 이동 |
| 304 | Not Modified | 캐시 사용 |

### 4xx: 클라이언트 오류 (Client Error)

| 코드 | 이름 | 설명 |
|:----:|------|------|
| **400** | Bad Request | 잘못된 요청 문법 |
| **401** | Unauthorized | 인증 필요 |
| **403** | Forbidden | 접근 금지 (권한 없음) |
| **404** | Not Found | 리소스 없음 |
| 405 | Method Not Allowed | 메서드 미허용 |
| 413 | Payload Too Large | 요청 본문 너무 큼 |
| 429 | Too Many Requests | 요청 횟수 초과 |

### 5xx: 서버 오류 (Server Error)

| 코드 | 이름 | 설명 |
|:----:|------|------|
| **500** | Internal Server Error | 서버 내부 오류 |
| 502 | Bad Gateway | 게이트웨이 오류 |
| 503 | Service Unavailable | 서비스 이용 불가 |
| 504 | Gateway Timeout | 게이트웨이 타임아웃 |

---

## 📦 HTTP 메시지 구조

### 요청 (Request)

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: ko-KR
Connection: keep-alive

[Request Body - POST일 경우]
```

### 응답 (Response)

```http
HTTP/1.1 200 OK
Date: Wed, 08 Jan 2026 07:00:00 GMT
Server: Apache/2.4.41
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Connection: keep-alive

<!DOCTYPE html>
<html>
...
```

---

## 🔄 HTTP 버전 비교

HTTP/1.0, 1.1, 2, 3의 진화 과정과 각 버전별 성능, 특징, 실무 선택 기준은 별도 문서로 분리되어 있습니다.

- **[HTTP 버전 비교](http-1-vs-2-vs-3.md)** - HTTP/1.0부터 HTTP/3까지의 역사, 성능 비교, 적용 기준

---

## 🔒 HTTPS (HTTP Secure)

**TLS/SSL**로 암호화된 HTTP 입니다. **TCP 443 번** 포트 사용.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    
    C->>S: TCP 3-Way Handshake
    C->>S: TLS ClientHello
    S->>C: TLS ServerHello + Certificate
    C->>S: Key Exchange
    Note over C,S: 암호화된 통신 시작
    C->>S: HTTP Request (암호화)
    S->>C: HTTP Response (암호화)
```

---

## 💡 실무 명령어

```bash
# curl로 HTTP 요청
curl -v http://example.com

# GET 요청
curl http://example.com/api/users

# POST 요청
curl -X POST -d "name=test" http://example.com/api/users

# 헤더만 확인
curl -I http://example.com

# 응답 헤더 포함
curl -i http://example.com

# HTTP/2로 요청
curl --http2 https://example.com
```

## 🔗 연결 문서 (Related Documents)

- [GET vs POST](get-vs-post.md) - HTTP 요청 메서드 상세 비교
- [HTTP 버전 비교](http-1-vs-2-vs-3.md) - HTTP/1.0, 1.1, 2, 3의 진화와 성능 비교
- [osi-7-layer-model](osi-7-layer-model.md) - OSI 7 계층 (응용 계층)
- [network-security-protocols](../../security/protocols/network-security-protocols.md) - TLS/SSL
- [web-security](../../security/web-security.md) - 웹 보안 (XSS, CSRF)
- [ftp-protocol](ftp-protocol.md) - FTP 프로토콜
