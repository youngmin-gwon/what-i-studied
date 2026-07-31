# DataBinding (Legacy)

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

>[!CAUTION] **Devil's Advocate : 최악의 디버깅 경험, DataBinding**
>XML 파일 내부에 로직과 표현식을 섞어 쓰는 DataBinding 은 컴파일 타임을 심각하게 저하시키고, 난해한 바인딩 에러 메시지로 인해 **악명 높은 생산성 저하 원인**입니다.
>Compose 도입이 불가능한 레거시 프로젝트라도 ViewBinding 까지만 허용해야 하며, DataBinding 은 절대 피해야 할 안티패턴으로 여겨지고 있습니다.

XML 에서 직접 데이터 바인딩. (Compose 도입 이전 과도기 기술)

```xml
<!-- layout.xml -->
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable
            name="viewModel"
            type="com.example.UserViewModel" />
    </data>
    
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{viewModel.userName}" />
        
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="@{() -> viewModel.loadUser()}"
            android:text="Load" />
    </LinearLayout>
</layout>
```

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val viewModel: UserViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.viewModel = viewModel
        binding.lifecycleOwner = this
    }
}
```
