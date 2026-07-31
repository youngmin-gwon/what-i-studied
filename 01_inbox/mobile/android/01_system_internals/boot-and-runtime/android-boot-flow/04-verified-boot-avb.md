# Verified Boot (AVB)

### 서명 체인

```
OEM Key (eFuse) 
  → vbmeta.img 검증
    → boot.img 검증
    → system.img 검증 (dm-verity)
```

**dm-verity**:

- 블록별 해시 트리
- 읽기 시 실시간 검증
- 변조 감지 시 부팅 차단 or 경고

### Verified Boot States

| State | 설명 |
|-------|------|
| **Green** | 완전 검증됨 (OEM key) |
| **Yellow** | 검증됨 (사용자 key, 커스텀 ROM) |
| **Orange** | Bootloader unlocked (경고 표시) |
| **Red** | 검증 실패 (부팅 차단) |

---
