
---

mindmap-plugin: basic

---

# 11. API 리팩터링<br/>Refactoring APIs

## 11.1 질의 함수와 변경 함수 분리하기<br/>Seperate Query from Modifier
- Background
   - 질의 함수와 변경 함수를 분리한다면, 질의 함수가 어떠한 side effect 를 내지 않고 결과를 내주기만 한다면 문제를 일으킬 걱정을 하지 않아도된다.
   - 즉 신경쓰지 않아도 된다. 그러므로 질의 함수는 부수 효과가 없어야 한다.
   - 나는 값을 반환하면서 부수효과가 있는 함수를 발견하면 이를 분리시키려고 한다.
   - 물론 나는 이 규칙을 절대적으로는 신뢰하지 않지만 되도록 따르려고 노력은 하고 있고 그 효과를 잘봤다.
   - __(나는 이 말을 잘못 오해헀는데 질의만 해야한다. 변경만 해야한다. 이런 뜻이 아니라 한 함수에서 질의와 변경이 섞여있다면 이것들을 분리하는게 맞다 라는 뜻이다. 즉 큰 하나의 함수에서는 질의와 변경이 각각의 함수 호출로 있겠지.)__
- Procedure
   - 대상 함수를 복제하고 질의 목적에 충실한 이름을 짓는다. (함수가 어떠한 결과를 반환하는지를 살펴보면 이름을 짓는데 충분한 단초를 줄 수 있다.)
   - 새 질의 함수에서 부수 효과를 모두 지운다.
   - 정적 검사를 수행한다.
   - 기존 함수를 호출하는 곳을 모두 찾아내서 새 함수를 호출하도록 변경한다. 그 다음 변경 함수를 새 함수 호출 밑에다가 추가한다.
   - 기존 함수에서 질의 관련 코드를 모두 제거한다.
   - 테스트한다.

## 11.2 함수 매개변수화 하기
- Background
   - 두 함수의 로직이 유사하고 리터럴 값만 다르다면 그 리터럴 값만 매개변수로 해서 코드의 중복을 제거할 수 있다.
   - 이렇게하면 매개변수의 값만 바꿔서 여러 곳에 적용할 수 있으니 더욱 유용하다.
- Procedure
   - 비슷한 함수 중 하나를 선택한다.
   - 함수 선언 바꾸기 (6.5 절) 로 리터럴들을 매개변수로 추가한다.
   - 이 함수를 호출하는 곳 모두에 적절한 리터럴 값을 추가한다.
   - 테스트한다.
   - 매개변수로 받은 값을 사용하도록 함수 본문을 수정한다.
   - 하나 수정할 때마다 테스트한다.
   - 비슷한 다른 함수를 호출하는 곳을 찾아 매개변수화된 함수를 호출하도록 하나씩 수정하고 수정할 때마다 테스트한다.

## 11.3 플래그 인수 제거하기
- Background
   - 플래그 인수란 (Flag Argument) 호출하는 함수가 호출되는 함수의 로직을 결정하기 위해 전달하는 매개변수다.
   - 플래그 인수는 이렇게 boolean 타입일수도, enum 일수도, String 일수도 있다. 다양하다.
   - 주요 포인트는 함수의 실행을 결정해주는 매개변수라는 점이다.
   - 함수를 이해하기 어렵다.
- Procedure
   - 플래그 인수로 실행될 수 있는 흐름들에 대한 함수를 명시적으로 만든다.
      - 플래그 인수를 기반으로 깔끔하게 분기되어있다면 조건문 분해하기 (10.1 절) 을 이용해서 명시적인 함수들을 생성하면 좋다.
      - 그렇지 않다면 래핑 함수 (Wrapping Function) 형태로 만들면 된다.
   - 원래 함수를 호출하는 코드들을 찾아서 명시적인 함수 호출로 바꾸자.

## 11.4 객체 통째로 넘기기
- Background
   - 하나의 레코드에서 값 두어개를 가져와서 인수로 넘기는 코드를 보면 그냥 객체를 통째로 넘기는게 낫지 않은가 라는 고민을 한다.
   - 객체 자체를 통째로 넘기면 대응하기 쉽다.
   - 객체에서 값을 뽑아서 다른 곳을 던진다는 것 자체가 의미없는 코드를 양산하는 것과 같다. (명확성을 떨어뜨린다.)
   - 그리고 매개변수 목록도 짧아지므로 함수를 이해하기가 더 쉽기도하다.
   - 하지만 함수가 객체 자체에 의존하면 안되는 경우라면, 서로 다른 모듈에 있는 관계라면 이 리팩토링의 기법을 사용하지는 않는다.
   - 이 리팩토링은 객체로부터 값 몇개를 꺼내서 함수에 전달하고 함수가 그 값들을 이용해서 무언가를 하는 행위를 한다면 이는 객체로 넘기는게 좋다.
   - 추상화면에서도 코드의 의도를 나타내는 면에서도 그런 편이 더 좋기 때문이다.
   - 한편 객체의 일부를 기반으로 같은 동작을 반복하는 코드가 있다면 그 일부가 클래스가 되어야 한다는 뜻이기도 하다. 그래서 따로 묶어서 클래스 추출하기 (7.5 절) 을 적용하자.
   - 마지막으로 많은 사람이 놓치는 예제가 있는데 객체가 다른 객체의 메소드를 호출하는 과정에서 자신이 가지고 있는 메소드 여러개를 전달하는 경우라면 그 객체 자체를 넘기는 경우, 즉 this 를 통해 넘기는 경우가 더 나을 수 있다. 이런 기법도 있다.
- Procedure
   - 매개변수를 원하는 형태로 빈 함수를 만든다. (이후 이름을 변경할 것이다.)
   - 새 함수의 본문에서는 원래 함수를 호출하도록 만든다. 매핑하도록 하면 된다.
   - 정적 검사를 수행한다.
   - 모든 호출자가 새 함수를 호출하도록 만든다.
   - 호출자를 모두 수정했다면 원래 함수를 인라인 (6.2 절) 한다.
   - 새 함수의 이름을 적절히 수정하고 모든 호출자에 반영한다.

## 11.5 매개변수를 질의 함수로 바꾸기
- Background
   - 매개변수 목록은 함수의 동작에 영향을 줄 수 있는 요소들이다.
   - 매개변수의 목록은 중복이 없는게 좋고 짧을수록 좋다.
   - 피호출 함수가 스스로 매개변수의 값을 알고있고 구할 수 있는 경우라면 매개변수는 없는게 더 코드를 이해하기가 쉽다.
   - 이 경우에 해당 매개변수는 의미없는 코드일 뿐이기 때문이다.
   - 매개변수가 있다면 호출자가 이런 의존성을 연결시켜주는 작업을 해야하고 매개변수가 없다면 피호출자가 주체가 되서 의존성 문제를 해결해야한다.
   - 나는 습관적으로 피호출자가 주체가 되도록 하는데 그러면 함수의 사용이 훨씬 쉬워지기 때문이다.
   - 피호출자가 주체가 될 때 고려해야하는 사항은 피호출자 함수에 의도치 않은 의존성이 생기는지의 여부다.
   - 피호출자가 쉽게, 또는 다른 매개변수를 통해서 알 수 있는 경우라면 의존성이 생기지 않겠지만 다른 모듈에 있는 객체를 매개변수로 받지않고 스스로 알아낼려고 하면 불필요한 의존성이 생긴다.
   - 즉 해당 함수가 알면 안되는 변수는 매개변수를 삭제하면 안된다.
   - 그리고 주의사항으로 매개변수를 없애는 대신 전역변수 같은 걸 이용할려고는 하지말자. 함수는 참조 투명 (referential transparency) 해야한다.
   - 함수에 똑같은 매개변수의 전달은 같은 결과를 반영해야 한다. 이를 기억하자.
- Procedure
   - 필요하다면 대상 매개변수를 계산하는 코드를 별도의 함수로 추출하자.
   - 함수 본문에서 대상 매개변수로의 참조를 새로 추출한 함수 호출로 바꾸자.
   - 함수 선언 바꾸기 (6.5 절) 로 대상 매개변수를 없애자.

## 11.6 질의 함수 매개변수로 바꾸기
- Background
   - 코드를 읽다 보면 함수 안에 있기에는 적합하지 않은 참조들이 있다.
   - 이 경우에는 해당 참조를 매개변수로 바꿈으로써 해결할 수 있다.
   - 이로인해 함수를 호출하는 호출자에게 책임을 옮겨진다.
   - 이런 상황 대부분은 코드안에서 의존관계를 바꾸려고 할 때 일어난다.
   - 함수가 특정 대상에 대한 의존을 가지지 않기 위해 매개변수로 바꾸고 호출하는 쪽이 해당 의존성을 가지게 된다.
   - 즉 어느 쪽에 의존성을 둘 것인지에 대한 문제로 여기에는 정답은 없다.
   - 따라서 프로그램을 더 잘 이해하게 되서 적합한 쪽으로 의존성을 옮기면 된다.
   - 이렇게 언제든지 리팩토링이 일어날 수 있게 기존의 코드를 바꾸기 쉽게 설계해두는 것이 중요하다.
   - 그리고 함수를 설계할 땐 참조 투명성이 중요하다. 왜냐하면 참조 투명성이 있는 함수는 똑같은 매개변수에선 똑같은 동작을 하기 때문에 예측하기 쉽기 때문이다.
   - 함수가 어떤 대상의 값에 의존하고 있고 이 값이 바뀔 여지가 많다면 참조 투명성을 가지는 함수로, 매개변수로 전달받도록 하면 함수를 다루기 쉽다.
   - 이 리팩토링을 수행하면 함수를 호출하는 쪽에 책임을 전가하게 된다. 그래서 호출하는 쪽의 코드가 더 어려워지고 결합도가 높아진다는 특징이 있다.
   - 그치만 그로인해 얻을 수 있는 혜택은 피호출자 함수가 담긴 클래스는 의존성을 없앨 수 있다. 필요하지 않는 의존성을 없앨 수 있어서 때로는 불변의 특성을 갖기도 한다.
- Procedure
   - 변수 추출하기 (6.3 절) 로 질의 코드를 함수 본문의 코드와 분리한다.
   - 함수 본문 중 해당 질의를 호출하지 않는 코드들을 별도의 함수로 추출 한다.
   - 방금 만든 변수를 인라인해서 제거한다.
   - 원래 함수도 인라인 한다.
   - 새 함수 이름을 원래 함수의 이름으로 변경한다.

## 11.7 세터 제거하기
- Background
   - 세터 메소드가 있는 것은 객체가 변경될 여지가 있다는 의미를 나타낸다.
   - 객체 생성 후에 변경되지 않을 것이라고 설계한 불변 객체라면 세터 메소드를 없애도록 하는게 맞다.
   - 즉 수정하지 않겠다 라는 의도를 드러내는 것이다.
   - 세터 제거하기 위한 상황은 크게 두 가지인데 첫 번째는 생성자에서만 세터를 호출하는 경우다.
   - 이런 세터는 필요하지 않으므로 그냥 세터를 없애고 생성자에서 필드 값을 설정하도록 하고 불변의 의도를 드러내는게 조핟.
   - 두 번째는 객체 생성 코드에서 세터를 통해 객체를 완성하는 경우다.
   - 이런 경우에도 세터를 제거하고 생성자를 이용하는게 더 좋다.
- Procedure
   - 설정해야 할 값을 생성자에서 받지 않는다면 그 값을 생성자에서 매개변수로 받도록 한다.
   - 세터 메소드를 인라인 한다.
   - Sub title
      - 특정 객체를 여러 객체에서 공유하고자 한다면
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
      - Sub title
   - 테스트한다.

## 11.8 생성자를 팩토리 함수로 바꾸기
- Background
   - 많은 객체 지향 언어에서는 생성자를 사용한다.
   - 객체를 초기화하는 용도로 사용하지만 자바를 기준으로 생성자는 기능 제공에서 한계를 제공하기도 한다.
   - 가령 생성자는 그 객체의 인스턴스를 반환한다는 점. 서브 클래스나 프록시를 반환하지는 못한다는 점이 있고
   - 생성자 메소드의 이름보다 더 적절한 이름이 있다고 판단되더라도 그 이름을 사용할 수 없다.
   - 또 생성자를 호출하려면 특별한 연산자 new 키워드 (일반적인 프로그래밍 언어에서) 를 사용해야해서 일반적인 함수를 기대하는 자리에서는 사용할 수 없다.
   - 팩토리 함수는 이런 제약이 없는데 팩토리 함수에선 생성자를 써도되고 다른 함수로 대체해도 되기 때문이다.
- Procedure
   - 팩토리 함수를 만든다. 그리고 팩토리 함수의 본문에서는 생성자를 호출하도록 한다.
   - 생성자를 호출하던 코드를 팩토리 함수로 대체한다.
   - 하나씩 수정할 때마다 테스트한다.
   - 생성자의 가시 범위를 최소화한다.

## 11.9 함수를 명령으로 바꾸기
- Background
   - 함수는 프로그래밍의 가장 기본적인 빌딩 요소다.
   - 그런데 함수는 그 함수만을 위한 객체로 캡슐화 되면 종종 유용해지는 상황이 생긴다 __(이 유용성에 대해서 알아야 겠다.)__
   - 이런 객체를 가리켜서 명령 객체, 함수를 명령 함수라고 한다. __(디자인 패턴의 Command Pattern 과도 같으며 명령이란 말은 객체의 상태를 변경하는 메소드다.)__
   - 명령 객체 대부분은 메소드 하나로 구성되고 이 메소드를 요청해서 실행하는 것이 이 객체의 목적이다.
   - 명령은 평범한 함수 매커니즘 보다 훨씬 유연함을 제공해줄 수 있다. 가령 Undo 연산을 제공해줄 수 있다던지. 라이프 사이클을 좀 더 세밀하게 제어가 가능하다라는 점.
   - 그리고 메소드와 필드를 이용해서 복잡한 함수를 쪼갤 수 있다 라는 점.
- Procedure
   - 대상 함수의 기능을 옮길 빈 클래스를 만든다. 클래스 이름은 함수 이름에 기초한다.
   - 방금 생성한 빈 클래스로 함수를 옮긴다. (리팩토링이 끝날 때 까지는 함수를 클래스에서 함수 호출로 바꾸자, 함수 이름은 규칙이 따로 없다면 execute 나 call 로 짓는다.)
   - 함수의 인수들 중 필드로 가질 것들을 생성자로 옮긴다.

## 11.10 명령을 함수로 바꾸기
- Background
   - 명령 객체의 장점은 복잡한 연산을 수행하도록 객체 안에서 캡슐화를 할 수 있다는 점이다.
   - 복잡한 함수 자체가 객체가 가진 필드들로 인해서 쪼개질 수 있다라는 점이 가장 크다.
   - 하지만 함수 자체가 복잡하지 않다라고 한다면 명령 객체를 사용한다는 점 자체가 더 복잡할 수 있다.
- Procedure
   - 명령을 생성하는 코드와 명령 실행 함수를 하나의 함수로 추출한다.
   - 명령의 보조 함수들을 각각 인라인 한다.
   - 함수 선언 바꾸기를 통해서 생성자의 매개변수들을 모두 명령의 파라미터로 바꾼다.
   - 명령 실행 메소드에서 필드를 사용하는 부분에서 파라미터를 사용하는 부분으로 바꾼다.
   - 생성자 호출과 명령의 실행 메소드 호출을 대체 함수 안으로 인라인 한다.
   - 테스트 한다.
   - 죽은 코드를 제거한다.

## 11.11 수정된 값 반환하기
- Background
   - 데이터가 어떻게 수정되는지 코드에서 추적하는 일은 어렵다.
   - 그것을 도와주는 방법 중 하나로 함수가 객체의 한 상태만을 변경시킨다면, 값 한 개만 변경시킨다면 그 값을 리터하도록 해서, 외부로 드러나도록 해서 어떻게 수정되는지 추적하기 쉽게 하는 방법이 있다.
   - (이 방법은 __질의 함수와 변경 함수 분리하기 (11.1 절)__ 과 대비된다고 생각들기도 하는데 본질적인 목적인 데이터 변경 추적이 가능해지는지에 주목하면 되지 않을까.)
   - 이 리팩토링의 방법은 값 여러 개를 변경시키는 경우에는 하지 말자.
- Procedure
   - 함수가 수정된 값을 반환하게 하고 호출자가 그 값을 변수로 담도록 한다.
   - 테스트한다.
   - 피호출함수 안에 반환할 값을 가리키는 새로운 변수를 선언한다.
   - 테스트한다.
   - 계산이 선언과 동시에 이뤄지도록 통함한다.
   - 테스트한다.
   - 피호출 함수의 변수 이름을 새 역할에 어울리도록 바꾼다.
   - 테스트한다.

## 11.12 오류 코드를 예외로 바꾸기
- Background
   - 오류 코드를 사용한다면 오류 코드를 일일히 검사해서 처리해줘야 한다.
   - 예외는 예외를 던지면 적절한 예외 핸들러를 찾을 때까지 콜스택을 타고 위로 전판된다.
   - 그래서 프로그램에서 적절한 지점에서 예외를 처리하도록 해놨다면 프로그램은 예외가 생기는 것에 대해서 신경쓰지 않아도 된다. __(다만 예외 처리는 정교해야한다. 자신이 처리할 수 있는 것이고 처리하는게 맞다면 처리하고 그렇지 않다면 다시 던지느 구조. )__
   - 예외를 사용할 땐 예외가 나서 프로그램이 종료되더라도 프로그램이 정상적으로 동작할 것인지에 대한 물음을 해보면 된다.
   - 그렇다면 예외를 사용해서 처리하면 되고 그렇지 않다면 오류를 잡아서 검출해야 한다는 뜻이다.
- Procedure
   - 콜스택 상위에어서 예외를 처리할 예외 핸들러를 만든다.
   - 테스트한다.
   - 정적 검사를 수행한다.
   - catch 절에서 직접 처리할 수 있는 예외는 적절히 대처하고 그렇지 않다면 던진다.
   - 테스트한다.
   - 오류 코드를 반환하는 곳에서 예외를 던지도록 한다.
   - 모두 수정했다면 오류 코드를 콜스택 위로 던지는 코드를 모두 제거한다.

## 11.13 예외를 사전확인으로 바꾸기
- Background
- 예외를 던지기 전에 호출자가 예외가 일어날 상황을 미리 감지하고 사전에 대처할 수 있다면 그렇게 하는게 좀 더 직관적일 것이다.
- __(예외를 던지고 뒤늦게 catch 문에서 수숩하는 코드보다 적절한지 확인하고 그렇지 않다면 문제를 해결하고 다음 곳으로 가는 코드.)__
- Procedure
- 예외를 유발하는 코드를 검사하는 조건문을 추가한다. (catch 블록의 코드를 조건문에 옮긴다.)
- catch 문에 어서션을 추가하고 테스트한다.
- try 문과 catch 문을 제거한다.
- 테스트한다.

## 한 변수를 여러가지 목적으로 사용하면 코드를 이해하는데 혼란을 줄 수 있고 추후에 버그를 낼 가능성이 높다.