# 💡 Context: 백그라운드 처리의 진화

안드로이드 OS 는 버전이 올라갈수록 백그라운드 작업에 대해 엄격한 제한을 가하고 있습니다. 현대적인 개발에서는 **WorkManager**가 사실상의 표준이며, 즉각적인 반응이 필요한 특수한 경우에만 **Foreground Service**를 사용해야 합니다.

>[!NOTE] **상호 참조**
>iOS 의 백그라운드 처리 방식은 [[apple-background-tasks]] 를 참고하세요.

---
