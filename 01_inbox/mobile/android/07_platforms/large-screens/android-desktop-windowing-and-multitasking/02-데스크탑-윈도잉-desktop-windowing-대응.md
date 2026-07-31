# 데스크탑 윈도잉(Desktop Windowing) 대응

안드로이드 16 기기에서 사용자는 모든 앱을 창 모드로 전환할 수 있다. 이제 모든 앱은 **가변적인 화면 크기(Resizability)**를 완벽하게 지원해야 한다.

##### 매니페스트 설정 및 처리

```xml
<activity
    android:name=".MainActivity"
    android:resizeableActivity="true"
    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation">
    <!-- 창 크기 변화 시 Activity가 재시작되지 않도록 설정 -->
</activity>
```
