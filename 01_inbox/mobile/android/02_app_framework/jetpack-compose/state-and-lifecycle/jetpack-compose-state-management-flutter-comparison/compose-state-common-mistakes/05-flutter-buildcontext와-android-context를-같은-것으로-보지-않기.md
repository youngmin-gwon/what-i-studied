# Flutter BuildContext와 Android Context를 같은 것으로 보지 않기

Flutter의 `BuildContext`는 widget tree 안의 위치에 가깝고, Android의 `Context`는 앱/컴포넌트가 OS 리소스와 시스템 서비스에 접근하는
환경 핸들입니다.

Compose에서 Android `Context`가 필요하면 `LocalContext.current`를 사용하지만, Repository나 ViewModel에 오래 보관할 객체로
넘기는 것은 피하는 편이 좋습니다. 자세한
내용은 [[android-context]]를
참조하세요.

---
