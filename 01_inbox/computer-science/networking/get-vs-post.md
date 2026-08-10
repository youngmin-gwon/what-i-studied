---
title: get-vs-post
tags: [http, get, post, method, protocol, networking]
aliases: [GET vs POST, GET과 POST 비교]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## GET vs POST

---

### 초보자를 위한 쉽게 이해하는 비유

* **GET (우편함에서 편지를 꺼내기)**:
  - 우편함 번호(URL)만 말해서 그 우편함의 편지 내용을 조회하는 것. 모두가 볼 수 있습니다.

* **POST (봉투에 편지를 넣어서 보내기)**:
  - 비밀 봉투에 편지(데이터)를 넣어서 우체부(서버)에 건네주는 것. 봉투 안의 내용은 남이 볼 수 없습니다.

---

## GET vs POST 핵심 기술 비교표

| 특성 | GET | POST |
|------|-----|------|
| **데이터 위치** | URL (Query String) | 요청 본문 (Body) |
| **데이터 길이** | 제한 있음 (~2KB) | 제한 없음 |
| **캐시** | 가능 (브라우저, 프록시) | 불가능 |
| **보안** | URL에 노출 (상대적 안전하지 않음) | 본문에 숨김 (상대적 안전) |
| **북마크** | 가능 | 불가능 |
| **용도** | 데이터 조회 | 리소스 생성/수정 |
| **멱등성** | 멱등성 보장 (Side Effect 없음) | 비멱등성 (호출할 때마다 상태 변경) |
| **HTTP 상태** | 안전한 메서드 | 안전하지 않은 메서드 |

---

## 상세 특성 비교

### 데이터 위치와 보안

**GET**: URL 쿼리 스트링에 데이터 노출
```
GET /search?q=password&user=john HTTP/1.1
```
- 브라우저 히스토리에 저장됨
- 로그 파일에 노출됨
- 캐시에 저장될 수 있음

**POST**: 요청 본문에 데이터 포함
```
POST /users HTTP/1.1
Content-Type: application/x-www-form-urlencoded

name=john&password=secret123
```
- 히스토리에 저장되지 않음
- 상대적으로 더 안전함

### 데이터 길이 제한

**GET**: 브라우저와 서버의 URL 길이 제한 (일반적으로 2KB)
```bash
# 대량 데이터 전송 불가
GET /api/search?ids=1,2,3,4,5,...1000  # ❌ 너무 길어서 실패 가능
```

**POST**: 제한 없음 (서버 설정에 따라 조정 가능)
```bash
# 대용량 파일 업로드 가능
POST /upload
# 100MB+ 파일 전송 가능
```

### 캐싱

**GET**: 브라우저와 프록시에 자동 캐시됨
```bash
# 같은 쿼리 반복 시 캐시에서 응답
GET /api/user/123
GET /api/user/123  # 캐시된 결과 반환
```

**POST**: 캐시되지 않음 (매번 서버 실행)
```bash
# 매번 새로 실행
POST /users
POST /users  # 같은 데이터라도 매번 실행
```

### 실제 사용 예시

```bash
# GET - 조회
curl -G https://api.example.com/users -d "page=1&limit=10"
# GET /users?page=1&limit=10 HTTP/1.1

# POST - 데이터 전송/생성
curl -X POST https://api.example.com/users \
  -d "name=John&email=john@example.com"
# POST /users HTTP/1.1
# name=John&email=john@example.com
```

---

## 실무 선택 기준

| 상황 | 추천 메서드 | 이유 |
|------|---------|------|
| 데이터 조회 | GET | 캐싱 가능, 북마크 가능, 안전 |
| 리소스 생성 | POST | 부작용 발생, 캐시 불가 |
| 민감한 데이터 전송 | POST | URL 노출 방지 |
| 대량 데이터 전송 | POST | 길이 제한 없음 |
| RESTful API | 용도에 맞는 메서드 | GET (조회), POST (생성), PUT/PATCH (수정), DELETE (삭제) |

---

## 연결 문서 (Related Documents)

- [HTTP Protocol](http-protocol.md) - HTTP 개요 및 요청 메서드 전체
- [HTTP 버전 비교](http-1-vs-2-vs-3.md) - HTTP/1.0, 1.1, 2, 3의 진화 과정
