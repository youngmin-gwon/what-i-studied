---
title: "SELinux는 Linux 사용자 권한을 넘어 mandatory policy를 강제한다"
tags: ["android", "android/security-privacy"]
---

# SELinux는 Linux 사용자 권한을 넘어 mandatory policy를 강제한다

Android의 SELinux는 Linux UID 기반 권한 위에 mandatory access control을 추가한다. 프로세스는 domain을, 파일과 socket 같은 객체는 type을 가지며, 정책이 허용하지 않는 접근은 root 권한으로도 통과할 수 없다.

이 계층은 sandbox가 깨졌을 때 피해 범위를 줄인다. 앱 프로세스가 더 높은 권한을 얻거나 취약한 native 경로를 타더라도 SELinux domain과 neverallow 정책이 시스템 파티션, device node, service 접근을 제한한다.

앱 개발자는 SELinux 정책을 직접 작성하지 않는 경우가 많지만, permission denied, binder access, vendor device 접근 문제를 볼 때 Linux file permission만으로 판단하면 안 된다.

## 판단 기준

Platform security 노트는 앱 권한보다 낮은 계층에서 device integrity와 mandatory policy가 어떻게 강제되는지 판단하는 기준으로 읽는다.

## 경계

client-side check를 authorization으로 오해하지 않고 server verification, boot trust, sandbox boundary를 분리한다.
