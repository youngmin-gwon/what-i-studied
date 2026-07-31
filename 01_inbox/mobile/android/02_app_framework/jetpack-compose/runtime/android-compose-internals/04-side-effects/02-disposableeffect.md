# DisposableEffect

리소스 정리가 필요한 경우.

```kotlin
@Composable
fun LocationUpdates() {
    val context = LocalContext.current
    
    DisposableEffect(Unit) {
        val locationManager = context.getSystemService<LocationManager>()
        val listener = object : LocationListener {
            override fun onLocationChanged(location: Location) {
                // 처리
            }
        }
        
        locationManager?.requestLocationUpdates(
            LocationManager.GPS_PROVIDER,
            1000L,
            0f,
            listener
        )
        
        onDispose {
            // Composition 이 떠날 때 정리
            locationManager?.removeUpdates(listener)
        }
    }
}
```
