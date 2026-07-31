# 프로덕션 정밀 profiling을 위한 profileable 태그
Android Studio의 Profiler 및 Macrobenchmark를 통한 성능 분석 시, 디버그 빌드(`debuggable=true`)는 컴파일 최적화가 꺼져 있어 지표가 왜곡됩니다.

릴리즈 빌드 수준의 정밀한 성능/메모리 Profile 수치를 수집하려면 매니페스트 `<application>` 태그 내에 **`<profileable>`** 태그를 지정해야 합니다:

```xml
<application ...>
    <!-- Android Studio Profiler 및 Perfetto가 Release 빌드에서도 정밀 프로파일링을 수행하도록 허용 -->
    <profileable android:shell="true" />
    
    <activity android:name=".MainActivity" android:exported="true">
        ...
    </activity>
</application>
```

> [!TIP]
> **Profileable 설정의 장점**:
> 1. `debuggable=false` 상태(릴리즈용 R8 및 컴파일러 최적화 활성화)를 유지하면서도 Android Studio Profiler 및 Perfetto 툴링으로 메모리, 프레임, CPU 지표를 정밀 측정 가능합니다.
> 2. 일반 유저에게는 보안상 앱 내부 메모리 조작을 막으면서, 개발 쉘(`adb shell`) 접근만 프로파일링에 허용합니다.
