
---

mindmap-plugin: basic

---

    
# 0. 도메인 주도 설계
## 주요 컨텐츠
- 의사결정을 내리는 데 기반이 되는 틀
- 도메인 설계에 대해 논의할 때 사용되는 기술적인 어휘
- 설계 실천법, 기법, 원칙
## 도메인 주도 개발을 진행 하기 위해서는 도메인 모델 설계 기법, 또한 애자일 프로세스를 상호보완하여 사용해야한다
- 개발은 반복주기를 토대로 진행돼야 한다
- 개발자와 도메인 전문가는 밀접하게 협업하여 모델 설계 해야한다
## 저자가 찾은 성공한 프로젝트의 특징
- 반복적 설계를  거쳐 발전
- 풍부한 도메인 모델
## 모델 기반 객체 설계를 따름
- 장점
  - 팀원들이 도메인에 대한 새로운 통찰력을 얻으면서 모델의 깊이를 얻어감
  - 개발자-개발자, 개발자-도메인전문가 간의 의사소통 품질 향상
  - 설계가 변경이나 확장이 쉬운 구조로 바뀌어감
## 책의 전제
- 대부분의 소프트웨어 프로젝트에서는 가장 먼저 도메인과 도메인 로직에 집중해야 한다
- 복잡한 도메인 설계는 모델을 기반으로 해야한다
## 소프트웨어 복잡성을 해결하기 위한 방법
- 복잡성
  - != 기술적인 부분
  - == 사용자 활동이나 업무에 해당하는 도메인 자체
## 도메인 모델링
- 도메인?
  - 소프트웨어를 사용하는 사용자의 활동이나 관심사
- 모델?
  - 소프트웨어 프로젝트를 위한 공통 언어의 핵심
  - 도메인에 대한 통찰력을 반영하는 용어와 관계로 표현
  - 충분히 정확한 동시에 도메인에 맞게 조정된 언어의 의미체계 제공
  - 문제를 해결하는 것과 관련된 측면을 추상화하고, 그 밖에 중요하지 않은 세부사항에는 주의를 기울이지 않음
- 원칙
  - 모델과 핵심 설계는 서로 영향을 주면서 구체화 된다
    - 모델과 설계를 긴밀하게 연결하여 유지보수와 기능개선에 도움
  - 모델은 모든 팀 구성원이 사용하는 언어의 중추다
  - 모델은 지식의 정수만을 뽑아낸 것이다
    - 모델에는 도메인을 정리하면서 갖게된 우리의 사고방식이 담겨있다