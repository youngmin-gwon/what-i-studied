---
title: apple-security-pq3
tags: [apple, apple/security, pq3, cryptography, quantum]
---

# [[mobile-security]] > [[apple-security-pq3]]

## PQ3: Post-Quantum Cryptography (iMessage)

2024년부터 iMessage에 도입된 **PQ3**는 양자 컴퓨터의 발전에 대비한 차세대 암호 프로토콜입니다. 기존의 타원 곡선 암호(ECC)를 넘어선 극도로 높은 보안 수준(Level 3)을 제공합니다.

---

### 🛡️ 배경: "Harvest Now, Decrypt Later" 공격 방어

현재의 암호화된 데이터는 미래의 강력한 양자 컴퓨터로 복호화될 위험이 있습니다.
- **Harvest Now**: 해커들이 현재의 데이터를 수집하여 보관합니다.
- **Decrypt Later**: 양자 컴퓨터가 실용화되었을 때 보관된 데이터를 복호화합니다.
- **PQ3의 목적**: 이러한 미래의 위협으로부터 현재의 대화를 보호하는 것입니다.

---

### ⚙️ 동작 메커니즘 (Level 3 Security)

1. **Kyber 기반 암호화**: NIST가 선정한 양자 내성 알고리즘인 **Kyber**를 사용하여 키 교환을 수행합니다.
2. **하이브리드 암호화**: 기존의 ECC 암호와 Kyber 양자 내성 암호를 결합하여 사용합니다. (둘 중 하나가 뚫려도 보안이 유지됨)
3. **지속적인 리키잉(Rekeying)**: 대화 중에 주기적으로 새로운 양자 내성 키를 생성하고 교환하여, 특정 시점의 키가 유출되더라도 과거와 미래의 대화를 보호합니다.

---

### 🚀 개발자 및 사용자에게 갖는 의미

- **투명성**: 사용자는 이를 인지하지 못하지만, 시스템 수준에서 이미 최고의 보안을 제공받습니다.
- **성능 최적화**: 메시지 크기 증가를 최소화하면서도 양자 공격에 대한 강력한 방어력을 갖추고 있습니다.

### 연관 문서
- [[cryptography-basics]] - 암호학 기초
- [[network-security-protocols]] - 네트워크 보안 프로토콜
- [[mobile-security]] - 모바일 보안 허브
