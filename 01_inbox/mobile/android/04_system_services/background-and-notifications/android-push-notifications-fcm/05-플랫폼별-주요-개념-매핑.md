# 📊 플랫폼별 주요 개념 매핑

| 특징 | Android (FCM) | iOS (APNs) |
| :--- | :--- | :--- |
| **기기 식별** | FCM Token | Device Token |
| **백그라운드 갱신** | Data-only (High Priority) | Silent Push (`content-available`) |
| **커스텀 UI** | RemoteViews | Content Extension |
| **알림 그룹화** | Group Key | Thread ID |
