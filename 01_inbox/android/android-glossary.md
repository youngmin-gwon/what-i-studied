---
title: android-glossary
tags: [android, android/glossary]
aliases: []
date modified: 2025-12-16 16:00:06 +09:00
date created: 2025-12-16 15:56:51 +09:00
---

## Android Glossary (쉬운 설명) android android/glossary

- **[[android-glossary#리눅스 커널]] 리눅스 커널**: 안드로이드의 땅바닥. 프로세스, 메모리, 전원 같은 기초를 맡는다.
- **[[android-glossary#hal]] HAL**: 하드웨어와 안드로이드가 손을 잡도록 돕는 통역사. 카메라, 센서 등 기기별 코드를 여기에 둔다.
- **[[android-glossary#binder]] Binder**: 앱과 시스템이 서로 말을 주고받는 우체부 같은 통로.
- **[[android-glossary#zygote]] Zygote**: 앱을 낳는 공장. 미리 준비한 상태를 복사해 새 앱을 빠르게 만든다.
- **[[android-glossary#art]] ART**: 앱 코드를 실행하는 엔진. 필요하면 미리 (또는 그때그때) 코드를 빠르게 바꾼다.
- **[[android-glossary#system-server]] system_server**: 주요 시스템 서비스가 모여 있는 큰 집. Activity, Window, Package 등이 여기 있다.
- **[[android-glossary#ams]] AMS/ATMS**: 화면 전환과 앱 생명주기를 관리하는 두 서비스.
- **[[android-glossary#selinux]] SELinux**: 누가 무엇을 만질 수 있는지 규칙을 지키게 하는 보안 울타리.
- **[[android-glossary#uid]] UID**: 앱마다 부여되는 번호표. 이 번호로 파일과 권한을 구분한다.
- **[[android-glossary#permission]] 권한**: 민감한 기능을 쓰기 위해 사용자에게 받는 허락장.
- **[[android-glossary#appops]] AppOps**: 권한보다 더 세밀하게, 언제 어떻게 썼는지 기록하고 제한하는 조정 장치.
- **[[android-glossary#scoped-storage]] Scoped Storage**: 앱마다 외부 저장소를 나눠 쓰게 하는 규칙.
- **[[android-glossary#boot]] Boot/부팅**: 기기가 켜져서 준비되는 과정. 부트로더→커널→init→zygote 순서로 이어진다.
- **[[android-glossary#ota]] OTA**: 무선 업데이트. 기기 전체 또는 일부를 교체한다.
- **[[android-glossary#apex]] APEX/Mainline**: OS 일부를 앱처럼 따로 업데이트할 수 있게 만든 꾸러미.
- **[[android-glossary#adb]] ADB**: PC 에서 기기에 명령을 보내고 로그를 보는 줄.
- **[[android-glossary#fastboot]] Fastboot**: 부트로더 단계에서 이미지를 굽거나 정보를 읽는 도구.
- **[[android-glossary#boot-image]] Boot Image**: 커널과 초기 램디스크를 묶은 파일. 기기 켤 때 사용.
- **[[android-glossary#zygote#preload]] Preload**: 자주 쓰는 클래스를 미리 읽어둬서 새 앱이 빨리 뜨도록 하는 동작.
- **[[android-glossary#binder#parcelable]] Parcelable**: Binder 로 보낼 때 객체를 납작하게 눕히는 (직렬화) 방법.
- **[[android-glossary#anr]] ANR**: 앱이 너무 오래 멈춰 있을 때 뜨는 경고.
- **[[android-glossary#lmkd]] LMKD**: 메모리가 부족하면 덜 중요한 앱을 닫아주는 관리인.
- **[[android-glossary#wakelock]] Wakelock**: 기기가 잠들지 않도록 잠깐 깨우는 열쇠.
- **[[android-glossary#workmanager]] WorkManager/JobScheduler**: 조건에 맞춰 백그라운드 일을 예약하는 스케줄러.
- **[[android-glossary#zygote#fork]] fork**: 이미 뜬 프로세스를 복사해 새 프로세스를 만드는 동작.
- **[[android-glossary#apk]] APK/AAB**: 앱 꾸러미 형식. APK 는 하나, AAB 는 조각으로 나뉘어 배포될 수 있다.
- **[[android-glossary#dex]] DEX/oat**: 안드로이드가 이해하는 바이트코드와 그 변환본.
- **[[android-glossary#hidden-api]] Hidden API**: 호환성 때문에 일반 앱이 직접 쓰지 못하게 막아둔 내부 API.
- **[[android-glossary#rro]] RRO/Overlay**: 설정을 바꾸지 않고 리소스만 덮어씌워 UI 나 기능을 조정하는 방법.
- **[[android-glossary#fbe]] FBE**: 사용자 잠금에 따라 열리는 파일 암호화 방식.
- **[[android-glossary#verified-boot]] Verified Boot/AVB**: 부팅 파일이 변조되지 않았는지 확인하는 절차.
- **[[android-glossary#binder#death]] Death Recipient**: 통신 상대가 죽었는지 알 수 있는 알림 장치.
- **[[android-glossary#perfetto]] Perfetto**: 시스템 전체를 시간 순서로 기록해 병목을 찾는 도구.
- **[[android-glossary#bugreport]] Bugreport**: 기기 상태를 압축해 담은 큰 로그 묶음.
- **[[android-glossary#apm]] App Standby/Doze**: 배터리를 아끼기 위해 앱의 활동을 쉬게 하는 모드.
