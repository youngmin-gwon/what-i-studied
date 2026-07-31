# ⚡ 1. 핵심 성능 기능 활성화 (Core Speed-ups)

`gradle.properties` 에 다음 설정을 추가하여 기본 성능을 강화합니다.

```properties
# 병렬 프로젝트 실행
org.gradle.parallel=true

# 빌드 구성 캐싱 (매우 중요)
org.gradle.configuration-cache=true

# JVM 데몬 메모리 확장
org.gradle.jvmargs=-Xmx6g -XX:+UseParallelGC -Dfile.encoding=UTF-8

# 증분 빌드 활성화
org.gradle.caching=true
```

---
