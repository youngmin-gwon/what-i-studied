# ADB 명령어를 통한 로컬 수동 검증 및 컴파일 시뮬레이션
로컬 개발 단계에서 Benchmark 코드 외에 **실제 단말에 프로필이 주입되어 작동하는지 수동으로 확인**하고 싶다면, 다음의 `adb` 명령어를 통해 ART(Android Runtime) 컴파일 상태를 강제로 시뮬레이션할 수 있습니다. (※ 에뮬레이터 또는 루팅된 실기기 환경 권장)

#### 1) 기존 컴파일 상태 초기화
앱을 순수 설치 상태(최적화 없는 상태, `CompilationMode.None`에 해당)로 복구합니다.
```bash
adb shell cmd package compile --reset <앱_패키지_명>
```

#### 2) Baseline Profile 강제 컴파일 적용
앱 패키지에 동반된 `baseline-prof.txt`를 기반으로 부분 AOT 컴파일을 수행합니다. (`CompilationMode.Partial`에 해당)
```bash
adb shell cmd package compile -m speed-profile -f <앱_패키지_명>
```

#### 3) Full AOT 컴파일 적용 (대조군 테스트용)
가장 극대화된 컴파일러 최적화 성능 지표를 테스트해볼 때 사용합니다. (`CompilationMode.Full`에 해당)
```bash
adb shell cmd package compile -m speed -f <앱_패키지_명>
```

#### 4) 현재 최적화/컴파일 상태 확인
해당 패키지가 어떠한 모드(speed, speed-profile 등)로 최적화되어 동작 중인지 로그로 검증합니다.
```bash
adb shell dumpsys package dexopt | grep -A 1 <앱_패키지_명>
```
출력 결과 로그 중 `[status=speed-profile]` 또는 `[reason=install-with-dexmetadata]` 등의 구문을 보고 컴파일 지도가 정상 적용되었는지 직접 판별할 수 있습니다.

---
