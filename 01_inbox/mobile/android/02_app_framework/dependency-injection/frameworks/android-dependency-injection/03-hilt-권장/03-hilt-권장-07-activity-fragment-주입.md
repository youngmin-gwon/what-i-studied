# Activity/Fragment 주입

```kotlin
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    
    @Inject
    lateinit var analytics: Analytics
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        analytics.logEvent("MainActivity_Created")
    }
}

@AndroidEntryPoint
class UserFragment : Fragment() {
    
    @Inject
    lateinit var userRepository: UserRepository
    
    private val viewModel: UserViewModel by viewModels()
}
```
