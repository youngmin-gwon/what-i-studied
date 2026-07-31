# Database Debugging

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

##### Database Inspector

```
View → Tool Windows → App Inspection → Database Inspector
```

**기능:**

- 실시간 데이터 확인
- 쿼리 실행
- 데이터 수정

##### 수동 확인

```bash
# SQLite DB 가져오기
adb pull /data/data/com.example.app/databases/app.db

# SQLite 열기
sqlite3 app.db

# 테이블 확인
.tables

# 쿼리
SELECT * FROM users;
```
