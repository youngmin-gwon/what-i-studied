# Bound Service 와 AIDL

[android-binder-and-ipc](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-binder-and-ipc.md) 를 통해 프로세스 간 통신이 가능하다.

```kotlin
// 같은 프로세스 내 Binder
class LocalService : Service() {
    private val binder = LocalBinder()
    
    inner class LocalBinder : Binder() {
        fun getService(): LocalService = this@LocalService
    }
    
    override fun onBind(intent: Intent): IBinder = binder
    
    fun getRandomNumber(): Int = Random.nextInt(100)
}

// Activity 에서 바인드
class MainActivity : AppCompatActivity() {
    private var service: LocalService? = null
    private var bound = false
    
    private val connection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, binder: IBinder?) {
            val localBinder = binder as LocalService.LocalBinder
            service = localBinder.getService()
            bound = true
        }
        
        override fun onServiceDisconnected(name: ComponentName?) {
            bound = false
        }
    }
    
    override fun onStart() {
        super.onStart()
        Intent(this, LocalService::class.java).also { intent ->
            bindService(intent, connection, Context.BIND_AUTO_CREATE)
        }
    }
    
    override fun onStop() {
        super.onStop()
        if (bound) {
            unbindService(connection)
            bound = false
        }
    }
}
```
