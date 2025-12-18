# macOS System Extensions & DriverKit #apple #macos #driverkit #systemextensions

macOS에서 시스템 확장/드라이버를 만들 때 알아야 할 내용을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 왜 바뀌었나?
- 커널 확장(kext)은 안정성/보안 위험이 커서, 사용자 공간으로 옮긴 [[apple-glossary#Kext/DriverKit|DriverKit]]/시스템 확장이 권장된다.
- Hardened Runtime/SIP/노타리제이션으로 서명/검증이 강화되었다.

## 시스템 확장 종류
- Network Extension: VPN/프록시/콘텐츠 필터/패킷 터널. Entitlement 필요, App Store 정책 엄격.
- Endpoint Security: 파일/프로세스/exec 이벤트 관찰/차단. 기업/보안 제품에서 사용, 사용자 동의 필요.
- DriverKit: USB/PCI/새 장치 드라이버. IOKit 대신 사용자 공간 API.
- System Extension: 위 확장을 담는 컨테이너. 설치/업데이트/제거는 시스템 대화상자 승인이 필요.

## 배포/설치 흐름
1) 앱 번들에 시스템 확장 포함(.systemextension).
2) 사용자가 설치 승인(시스템 프롬프트). 일부는 재부팅 필요.
3) 승인 후 launchctl/systemextensionsctl이 로드/관리.
4) 제거 시 승인 후 언로드.

## 권한/보안
- 적절한 Entitlement/프로비저닝/서명이 없으면 로드되지 않는다.
- Endpoint Security는 Team ID/특수 권한이 필요하고, 사용자 동의가 필수.
- 설치/업데이트 시 macOS 버전/SIP 상태/하드웨어 호환 확인.

## 개발/디버깅
- systemextensionsctl list/log로 상태 확인.
- Console/Unified Logging에서 subsystem별 로그 보기.
- `kmutil`은 기존 kext 관리 도구, DriverKit에도 일부 사용.
- 가상 머신/시뮬레이터에서는 일부 하드웨어 테스트가 불가.

## 사용자 경험
- 설치/제거/권한 프롬프트를 명확히 안내. 왜 필요한지, 어떤 기능을 제공하는지 설명.
- 실패/거부 시 대체 경로/기능 축소를 제공.

## 업데이트/호환성
- OS 업데이트마다 보안 정책이 달라질 수 있으니 최신 가이드 확인.
- Intel/Apple Silicon 모두 지원하는지, Rosetta에서도 동작하는지 테스트.

## 링크
[apple-macos-advanced](apple-macos-advanced.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md), [apple-distribution-and-policies](../../05_security_privacy/apple-distribution-and-policies.md), [apple-network-basics](../../../../../../../apple-network-basics.md).
