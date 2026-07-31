# 4 Conditional Delivery (조건부 배포)

| 항목           | 설명                            |
|--------------|-------------------------------|
| **동작**       | 설치 시 특정 조건을 만족하는 기기에만 자동 다운로드 |
| **조건 불만족 시** | 해당 모듈이 아예 설치되지 않음             |

```xml

<dist:delivery>
    <dist:install-time>
        <dist:conditions>
            <!-- API 레벨 조건 -->
            <dist:min-sdk dist:value="21" />

            <!-- 기기 기능 조건 -->
            <dist:device-feature dist:name="android.hardware.camera.ar" />

            <!-- 사용자 국가 조건 -->
            <dist:user-countries dist:exclude="false">
                <dist:country dist:code="KR" />
                <dist:country dist:code="US" />
            </dist:user-countries>
        </dist:conditions>
    </dist:install-time>
</dist:delivery>
```

**지원 조건 목록:**

| 조건               | 설명                  | 예시            |
|------------------|---------------------|---------------|
| `min-sdk`        | 최소 API 레벨           | API 21 이상만    |
| `device-feature` | 하드웨어/소프트웨어 기능       | AR 지원, NFC 탑재 |
| `user-countries` | 사용자 국가              | 한국, 미국만       |
| `device-model`   | 특정 기기 모델 (API 31+)  | 특정 제조사 기기     |
| `device-ram`     | 기기 RAM 용량 (API 31+) | 4GB 이상        |
| `system-feature` | 시스템 기능 (API 31+)    | 특정 SoC        |

**적합한 상황:**

- **AR 기능**: AR Core를 지원하는 기기에만 배포
- **국가별 기능**: 특정 국가의 규제나 서비스에 맞는 모듈
- **고사양 기능**: 충분한 RAM이 있는 기기에만 고해상도 리소스 배포
- **특정 하드웨어**: NFC, 지문인식 등 특정 센서가 있는 기기

---
