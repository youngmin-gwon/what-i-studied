# Binder 와의 통합

Binder 호출도 SELinux 로 제어된다:

```
allow untrusted_app activity_service:service_manager find;
allow untrusted_app system_server:binder call;
```

이 정책이 없으면, 앱이 `ActivityManager` 를 찾을 수 없다.
