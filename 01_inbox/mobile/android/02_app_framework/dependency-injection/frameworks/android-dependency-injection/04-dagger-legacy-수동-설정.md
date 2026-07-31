# Dagger (Legacy - 수동 설정)

상위 노트: [android-dependency-injection](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection.md)

>[!CAUTION] **Devil's Advocate : 순수 Dagger 2 의 악몽**
>과거 안드로이드 진영의 DI 를 지배하던 Dagger 2 는 어마어마한 보일러플레이트(`Component`, `SubComponent`, `Module` 등)와 높은 러닝 커브로 프로젝트를 무겁게 만들었습니다.
>현재는 구글이 직접 **Hilt**를 만들어 이 모든 설정을 어노테이션 하나(`@HiltAndroidApp`)로 압축했습니다. 아직도 순수 Dagger 를 써서 아키텍처를 자랑하는 코드는 유지보수가 불가능한 기술 부채입니다. 무조건 Hilt 나 Koin 으로 넘어가야 합니다.

```kotlin
// Component
@Singleton
@Component(modules = [AppModule::class, NetworkModule::class])
interface AppComponent {
    fun inject(activity: MainActivity)
    
    @Component.Factory
    interface Factory {
        fun create(@BindsInstance application: Application): AppComponent
    }
}

// Module
@Module
class AppModule {
    
    @Provides
    @Singleton
    fun provideContext(application: Application): Context {
        return application.applicationContext
    }
}

// Application
class MyApplication : Application() {
    val appComponent: AppComponent by lazy {
        DaggerAppComponent.factory().create(this)
    }
}

// Activity
class MainActivity : AppCompatActivity() {
    
    @Inject
    lateinit var analytics: Analytics
    
    override fun onCreate(savedInstanceState: Bundle?) {
        (application as MyApplication).appComponent.inject(this)
        super.onCreate(savedInstanceState)
    }
}

// Subcomponent (Activity Scope)
@ActivityScope
@Subcomponent(modules = [ActivityModule::class])
interface ActivityComponent {
    fun inject(activity: MainActivity)
    
    @Subcomponent.Factory
    interface Factory {
        fun create(): ActivityComponent
    }
}

@Module(subcomponents = [ActivityComponent::class])
object SubcomponentModule
```
