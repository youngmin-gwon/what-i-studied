# RemoteViews (레거시/내부 동작 방식)

안드로이드 위젯은 다른 프로세스(시스템 홈 화면)에서 그려지기 때문에 통상적인 뷰 계층 구조를 가질 수 없다. `RemoteViews` 는 이 제약을 극복하기 위해 "특정 뷰를 이렇게 그려라"는 명령의 집합이다.

>[!CAUTION] **Devil's Advocate : RemoteViews 직접 만지는 것은 위험**
>`RemoteViews` 를 직접 코딩하면 레이아웃 XML 과 소스 코드가 분리되어 가독성이 떨어지며, `PendingIntent` 관리가 매우 번잡해진다. 신규 위젯은 무조건 Glance 를 사용하라.
