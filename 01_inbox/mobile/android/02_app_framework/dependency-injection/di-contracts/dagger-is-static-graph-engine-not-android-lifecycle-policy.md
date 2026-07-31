# Dagger는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다

Dagger는 compile time에 dependency graph를 생성하고 검증하는 정적 DI engine이다. Android에서 어떤 component가 Activity, Fragment, ViewModel, Worker와 어떻게 만나야 하는지는 별도의 integration policy가 필요하다.

Hilt는 이 Android integration을 표준화한다. 순수 Dagger를 쓰는 경우에는 component owner, subcomponent/factory, injection timing, test replacement를 프로젝트가 직접 설계해야 한다.

공식 문서: [Dagger basics](https://developer.android.com/training/dependency-injection/dagger-basics)
