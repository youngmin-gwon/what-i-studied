# Component Scopes

| Component | Scope | 생명주기 |
|-----------|-------|---------|
| SingletonComponent | @Singleton | Application |
| ActivityRetainedComponent | @ActivityRetainedScoped | Activity (설정 변경 유지) |
| ViewModelComponent | @ViewModelScoped | ViewModel |
| ActivityComponent | @ActivityScoped | Activity |
| FragmentComponent | @FragmentScoped | Fragment |
| ViewComponent | @ViewScoped | View |
| ServiceComponent | @ServiceScoped | Service |

```kotlin
@Module
@InstallIn(ViewModelComponent::class)
object ViewModelModule {
    
    @Provides
    @ViewModelScoped
    fun provideAnalytics(): Analytics {
        return Analytics() // ViewModel 생명주기
    }
}
```
