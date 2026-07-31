# Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다

Dynamic feature module은 필요할 때 설치되는 선택 feature unit이다. DI graph가 dynamic feature implementation을 base가 compile time에 직접 알아야만 동작한다면 dynamic delivery의 장점과 충돌한다.

Base module에는 feature entry contract, navigation route, dependency interface처럼 안정적으로 알아야 할 것만 둔다. Dynamic feature 내부 implementation과 binding은 설치 이후 entry boundary에서 연결한다.

관련 노트: [Dynamic feature module](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).
