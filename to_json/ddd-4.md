[
  {
    "title": "Map 1",
    "topic": {
      "title": "4. 도메인의 격리",
      "topics": [
        {
          "title": "도메인은 대게 전체 소프트웨어 시스템의 극히 작은 부분을 구성한다"
        },
        {
          "title": "계층화",
          "topics": [
            {
              "title": "응집력 있는 설계가 가능해지고, 깔끔한 분리로 인해 설계를 훨씬 쉽게 이해할 수 있게 됨"
            },
            {
              "title": "Layered Architecture",
              "topics": [
                {
                  "title": "Presentation",
                  "topics": [
                    {
                      "title": "사용자에게 정보를 보여주고 사용자의 명령을 해석함"
                    }
                  ]
                },
                {
                  "title": "Application",
                  "topics": [
                    {
                      "title": "소프트웨어가 수행할 작업을 정의"
                    },
                    {
                      "title": "표현력 있는 도메인 객체가 문제를 해결하게 함"
                    },
                    {
                      "title": "이 계층은 얇게 유지됨:\n\n업무 규칙이나 지식을 포함하지 않고, 오직 작업을 조정하고 아래에 위치한 계층에 포함된 도메인 객체의 협력자에게 작업을 위임"
                    }
                  ]
                },
                {
                  "title": "Domain",
                  "topics": [
                    {
                      "title": "모델과 설계 요소에 직접적으로 관계돼 있는 모든것들을 명시한 것"
                    },
                    {
                      "title": "업무 개념과 업무 상황에 관한 정보, 업무 규칙을 표현하는 일을 책임짐"
                    }
                  ]
                },
                {
                  "title": "Infrastructure",
                  "topics": [
                    {
                      "title": "상위 계층을 지원하는 일반화된 기술적 기능 제공"
                    },
                    {
                      "title": "메시지 전송, 도메인 영속화, UI 위젯 그리기"
                    },
                    {
                      "title": "도메인의 구체적인 지식을 가져서는 안된다 -> Service로 제공함"
                    }
                  ]
                }
              ]
            },
            {
              "title": "오직 아래에 있는 계층에만 의존하는 설계를 만들어라",
              "topics": [
                {
                  "title": "하위 수준 객체가 상위 수준 객체와 소통해야 할 경우:\n\ncallback, or observer pattern 이용"
                }
              ]
            },
            {
              "title": "표준 아키텍처 패턴에 따라 상위 계층과의 결합을 느슨하게 유지하라"
            }
          ]
        },
        {
          "title": "도메인 주도 설계의 전제조건: 도메인 격리"
        }
      ]
    },
    "structure": "org.xmind.ui.map.clockwise"
  }
]