# The Art of Readable Code 정리

## Prolog. 코드는 이해하기 쉬워야 한다

무엇이 코드를 좋게 만드는가?

- 판단하기 쉽지 않음 ⇒ 이를 판단하기 쉽게 하기 위해 **가독성의 기본 정리** 를 사용

The Fundamental Theorem of Readability

- 평범한 사람(코드 작성자 포함)이 코드를 읽고 이해하는 데 걸리는 시간을 최소화하는 코드

적은 분량으로 코드를 작성하는 것이 좋은 목표이긴 하지만, 언제나 이해를 위한 시간을 최소화 하는 것으로 해야함

## Part 1. 표면적 수준에서의 개선

좋은 이름 짓기, 좋은 설명 달기, 코드를 보기 좋게 정렬하는 것 ⇒ 프로그램이 동작하는 방식을 바꾸지 않고 그 자리에서 곧바로 만들 수 있음

### 이름에 정보 담기

`size` 혹은 `get` 처럼 그럴 듯 해보이는 이름조차 많은 정보를 담아내지 못하는 경우가 있으므로 다음 원칙을 주의해서 이름을 선택하라

#### 1. 특정 단어 고르기

함수명을 정의할 때 `get`과 같은 키워드는 너무 보편적이기 때문에 구체적인 단어를 선택하여 무의미한 단어를 피하자

```dart
// before
void getPage(String url){
...
}
```

```dart
// after
void fetchPage(String url){
}

// or

void downloadPage(String url){
}
```

```dart
// before
class Thread{

    void stop(){
        ...
    }

}
```

```dart
// after
class Thread{

    void kill(){
        ...
    }

// or
    void pause(){
        ...
    }

}
```

상황에 적합할 수 있는 '화려한' 단어를 골라라 (항상 좋은것은 아님)

```markdown
// thesaurus 참고
send => deliver, dispatch, announce, distribute, route
find => search, extract, locate, recover
start => launch, create, begin, open
make => create, set up, build, generate, compose, add, new
```

```dart
// bad case

// ?
explode();

// !
split();
```

#### 2. tmp 나 retval 같은 보편적인 이름 지향하기

변수의 목적이나 담고 있는 값을 설명하는 기능을 하게 됨

```dart
// before
var euclidean_norm = Function<void> (v) {
    var retval = 0.0;
    for (var i=0; i<v.length; i++){
        retval = v[i]*v[i];
    }
    return retval;
}

// ```````````````

// after
var euclidean_norm = Function<void> (v) {
    var sum_squares = 0.0;
    for (var i=0; i<v.length; i++){
        sum_squares = v[i]*v[i];
    }
    return sum_squares;
}
```

```dart
// i, j, k 문제 : 인덱스를 잘못 지칭해도 문제를 찾기 어려움
// before
for (int i=0;i<clubs.size;i++){
    for (int j=0;j<clubs[i].members.size;j++){
        for (int k=0;k<users.size;k++){
            if (clubs[i].members[k] == users[j]){
                // do something
            }
        }
    }
}

// ```````````````
// after

for (int ci=0;ci<clubs.size;ci++){
    for (int mj=0;mj<clubs[ci].members.size;mj++){
        for (int uk=0;uk<users.size;uk++){
            if (clubs[ci].members[mj] == users[uk]){
                // do something
            }
        }
    }
}

```

오히려 보편적인 이름이 필요한 의미를 전달해주는 경우도 있으므로 주의

```dart
// 변수 목적이 코드 몇줄에서만 사용되는 임시 저장소 역할을 하기 때문에 tmp라는 이름이 오히려 완벽
if (right < left) {
    var tmp = right;
    right = left;
    left = tmp;
}
```

tmp, it, retval 같은 보편적인 이름을 사용하려면, 꼭 그렇게 해야하는 이유가 있어야 함

정말 떠오르지 않는다면 foo 같은 무의미한 이름을 사용하며 앞으로 진전할 수 있지만, 몇 초라도 좋은 이름을 생각하려고 고민하는 습관을 들여 '작명을 위한 내공'을 키우려 노력해야 함

#### 3. 추상적이지 않은, 대상을 자세하게 묘사하는 구체적인 이름을 선호하라

예제로 확인

```markdown
DISALLOW_EVIL_CONSTRUCTOR => DISALLOW_COPY_AND_ASSIGN

--run_locally => --extra_logging --use_local_database
```

#### 4. 변수명에 중요한 세부 정보를 덧붙여라

모든 변수에 추가적인 정보를 담을 필요는 없지만, 보안과 관련된 버그처럼 심각한 결과를 낳을 가능성이 있을 때 중요 세부 정보를 추가해야함

```markdown
// 리턴되는 시간범위가 milliseconds인 경우
var start => var start_ms
var elapsed => var elapsed_ms

// 그 밖
Start(int delay) => Start(int delay_secs)
CreateCache(int size) => CreateCache(int size_mb)
ThrottleDownload(float limit) => ThrottleDownload(float max_kbps)
Rotate(float angle) => Rotate(float degree_cw)

password => plaintext_password
comment => unescaped_comment
html => html_utf8
data => data_url_enc
```

#### 5. 사용 범위가 넓으면 긴 이름을 사용하라

기능을 잘 설명하면서 일반적 통용보다 긴 이름은 괜찮음
좁은 범위에서는 짧은 이름이 괜찮음
eval, doc. str 등 흔한 축약형 혹은 약어는 프로그래머 사이에서 많이 통용되므로 사용해도 무관하나, 자체적으로 만든 축약어는 지향해야함(BEDeveloper ⇒ BackEndDeveloper)
불필요한 단어는 생략(ConvertToString ⇒ ToString)

#### 6. 대문자나 밑줄 등을 의미 있는 방식의 포맷팅을 활용하라

클래스 멤버변수는 \_(underscore)을 사용하여 로컬변수와 구분하라

### 오해할 수 없는 이름들

지은 이름을 "다른 사람들이 다른 의미로 해석할 수 있을까?"라는 질문을 던져보며 철저히 확인해야 함

```dart
final results = Database.all_objects.filter("year <= 2011");

// 가능성
// 1) year <= 2011인 객체
// 2) year <= 2011이 아닌 객체
// 의미가 모호함

// 1)의 경우 : select()
// 2)의 경우 : extract()
// 가 더 적합함
```

```dart
String clip(String text, int length) {
    ...
}

// 가능성
// 1) 문단의 끝에서부터 거꾸로 length만큼 제거
// 2) 문단을 처음부터 length만큼 잘라냄

// better way
String truncate(String text, int maxChars) {
    ...
}
```

#### 1. 경계를 포함하는 한계값을 다룰 때는 min과 max를 사용

예시

```dart
// before
const static int CART_TOO_BIG_LIMIT = 10;

if (shopping_cart.num_items() >= CART_TOO_BIG_LIMIT){
    Error("Too many items in cart");
}

// LIMIT을 포함하는지 알 수 없음

// after
const static int MAX_ITEMS_IN_CART = 10;

if (shopping_cart.num_items() >= MAX_ITEMS_IN_CART){
    Error("Too many items in cart");
}
```

#### 2. 경계를 포함하는 범위에는 first 와 last 를 사용

예시

```dart
// before
print(integerRange(start=2,stop=4));
// [2,3] 인지 [2,3,4] 인지 알 수 없음

// after
print(integerRange(first=2,last=4));
```

#### 3. 경계를 포함하고/배제하는 범위에는 begin과 end를 사용

예시

```dart
printEventsInRange(begin:"2021-02-01 00:00:00",  end:"2021-02-02 00:00:00");
```

#### 4. boolean 변수에 이름 붙이기

`is`, `has`, `can`, `should`와 같은 단어를 더하여 불리언 값의 의미를 더 명확하게 만들어야 함

```dart
// before
bool read_password = true;

// after
bool isAuthenticated = true;
```

부정하는 의미를 피하는 것이 좋음

```dart
// before
bool disable_ssl = false;

// after
bool useSsl = false;
```

#### 5. 사용자의 기대에 부응하기

#### 6. 이름을 짓기 위해 복수의 후보를 평가하기

---

### 미학

'눈을 편하게' 만드는 코드가 좋은 코드라는 사실을 자각하며 다음 원리를 이용하라

```plaintext
1. 코드를 읽는 사람이 이미 친숙한, 일관성 있는 레이아웃을 사용하라
2. 비슷한 코드는 서로 비슷해 보이게 만들어라
3. 서로 연관된 코드는 하나의 블록으로 묶어라
```

#### 1. 미학적으로 보기 좋은 코드가 사용하기 더 편리하다

코드를 훑어보는 데 걸리는 시간이 적을수록, 사람들은 코드를 더 쉽게 사용할 수 있음

```cpp
// before
class StatsKeeper {
public:
    // 일련의 더블 변수값을 저장하는 클래스
    void Add(double d); // 그리고 그런 값들에 대한 간단한 통계를 계산하는 메소드
    private: int count; /* 지금까지 몇 개가 저장 되었는가
    */ public:
                double Average();
private: double minimum;
list<double>
    past_items
            ; double maximum;

}

// after
class StatsKeeper {
    public:
        void Add(double d);
        double Average();

    private:
        list<double> past_items;
        int count;

        double minimum;
        double maximum;
}
```

#### 2. 일관성과 간결성을 위해서 줄 바꿈을 재정렬하기

여러 블록에 담긴 코드가 모두 비슷한 일을 수행하면, 실루엣이 동일해 보이게 만들어라

#### 3. 메소드를 활용하여 불규칙성을 정리하라

#### 4. 도움이 된다면 코드의 열을 맞춰라

#### 5. 의미 있는 순서를 선택하고 일관성 있게 사용하라

#### 6. 선언문을 블록으로 구성하라

#### 7. 코드를 '문단'으로 쪼개라

#### 8. 개인적 스타일 vs 일관성

개인 스타일을 추구한다고 가독성에 실질적 영향을 주진 않지만, 여러 가지 스타일을 섞어쓰면 가독성에 영향을 줌

```dart
// 어느 스타일을 사용해도 상관없으나 한가지 스타일만 전체 코드 베이스에서 사용하자
// 1.
class Logger{
    ...
}

// 2.
class Logger
{
    ...
}
```

### 주석에 담아야 하는 대상

주석의 목적은 코드를 읽는 사람이 코드를 작성한 사람만큼 코드를 잘 이해하게 돕는 데 있다는 것을 명심하자
머릿속에 있는 정보 중 어떤 정보를 언제 적어야 하는지 초점을 맞춤

#### 1. 설명하지 말아야 할 것

코드에서 빠르게 유추할 수 있는 내용은 주석으로 달지 말라
설명 자체를 위한 설명을 달지 말라

> 😱 의미없는 주석 : 코드를 읽는 사람이 코드를 더 잘 이해하도록 도와주지 않음

```dart
// 클래스 Account를 위한 정의
class Account {
    // 생성자
    const Account();

    // profit에 새로운 값 설정
    void setProfit(double profit);
}
```

> 😱  의미없는 주석 : 코드를 읽으면 무슨 일이 수행 되는지 알 수 있음

```python
# 두 번째 '*' 뒤에 오는 내용을 모두 제거
name = '*'.join(line.split('*')[:2])
```

> 😱  의미없는 주석 → ☺️ 의미있는 주석

```go
// ``` bad ```
// 주어진 이름과 깊이를 이용해서 서브 트리[h1]에 있는 노드 찾기
func FindNodeInSubtree(subtree *Node, name string, depth int) (*Node)

// ``` better ```
// 주어진 'name' 으로 노드를 찾거나 아니면 null을 반환
// 만약 depth <= 0 이면 'subtree'만 검색됨
// 만약 depth == N 이면 N 레벨과 그 아래만 검색됨
func FindNodeInSubtree(subtree *Node, name string, depth int) (*Node)
```

나쁜 이름에 주석을 달지 마라 - 대신 이름을 고쳐라

- 좋은 이름은 '스스로 설명'하므로 좋은 주석보다 낫다
- "좋은 코드 > 나쁜코드 + 좋은 주석" 의 원칙을 기억하자

```dart
// ``` bad ```
// 반환되는 항목의 수나 전체 바이트 수와 같이
// Request가 정하는 대로 Reply에 일정한 한계를 적용
void cleanReply(Request request, Reply reply);

// ``` better ```
// 'reply' 가 count/byte/등과 같이 'request'가 정하는 조건을 만족시키도록 한다
void enforceLimitsFromRequest(Request request, Reply reply);
```

```dart
// ``` bad ```
// 해당 키를 위한 핸들을 놓아준다. 이 함수는 실제 레지스트리를 수정하지 않는다
void deleteRegistry(RegistryKey key);

// ``` better ```
void releaseRegistryHandle(RegistryKey key);
```

#### 2. 코딩을 수행하면서 머릿속에 있는 정보를 기록하기

`감독의 설명`을 포함하라

- 영화에 대한 통찰, 영화가 만들어진 과정을 잘 이해하게 도와주는 '감독의 설명'을 추가하여 중요한 통찰을 전달

```dart
// 놀랍게도, 이 데이터에서 이진트리는 해시테이블보다 40% 정도 빠르다
// 해시를 계산하는 비용이 좌/우 비교를 능가한다
```

코드를 읽는 사람이 코드를 최적화 하느라 시간을 허비하지 않게 도와줌

```dart
// 이 주먹구구식 논리는 몇 가지 단어를 생략할 수 있다. 상관없다. 100% 해결은 쉽지 않다.
```

코드가 훌륭하지 않은지도 설명할 수 있음

```dart
// 이 클래스는 점점 엉망이 되어가고 있다. 어쩌면 'ResourceNode' 하위클래스를
// 만들어서 정리해야 할지도 모르겠다.
```

코드에 있는 결함을 설명하라

- 코드가 계속적으로 진화하며 버그를 갖게 될 수 밖에 없으므로, 결함을 설명하는 것을 부끄러워하지 말라

```dart
// TODO: 더 빠른 알고리즘을 사용하자
```

개선 아이디어를 설명하는 것도 좋다

```dart
// TODO(더스틴) : JPEG말고 다른 이미지 포맷도 처리할 수 있어야 한다.
```

| 표기   | 의미                            |
| ------ | ------------------------------- |
| TODO:  | 아직하지 않은 일                |
| FIXME: | 오작동을 일으킨다고 알려진 코드 |
| HACK:  | 아름답지 않은 해결책            |
| XXX:   | 위험! 여기 큰 문제가 있다       |

상수에 대한 설명

- 상수가 생성된 '사연'이 존재 하기 때문에 이 사연을 알고 있는 작성자가 설명하라

```python
NUM_THREADS = 8 # 이 상수값이 2 * num_processors보다 크거나 같으면 된다
```

- 상수가 아무런 의미를 갖고 있지 않을 때, 혹은 변경하지 않는게 더 좋은 경우, 이러한 사실을 알려주는 주석도 유용함

```python
# 합리적 한계를 설정하라 - 그렇게 많이 읽을 수 있는 사람은 어차피 없다
MAX_RSS_SUBSRIPTIONS = 8

IMAGE_QTY = 0.72 # 사용자들은 0.72가 크기/해상도 대비 최선이라고 생각한다
```

- 상수에 대한 주석을 작성하며 상수를 설정할 때 무슨 생각을 하고 있었는지를 밝힐 수 있음

#### 3. 코드를 읽는 사람의 입장에서 필요한 정보가 무엇인지 유추하기

나올 것 같은 질문 예측하기

- 다른 누군가가 읽을 때 '이게 뭐하는 코드야?' 라는 생각이 들 만한 부분에 주석 달기

사람들이 쉽게 빠질 것 같은 함정 경고하기

- 앞질러 생각했을 때 다른 사람들이 코드를 사용하다 만날지 모르는 문제를 미리 예측하여 주석 달기

```dart
// before
void sendEmail(String to, String subject, String body);

// 이 함수를 구현하려면 외부 이메일 서비스에 접속해야 하는데,
// 이 작업이 1초 이상 걸릴 수 있음
// 웹 애플리케이션을 작성하는 다른 사람이 이런 사실을 모른 채
// HTTP 질의를 처리하는 과정에서 이 함수를 사용할 수 있음

// after

/// 외부 서비스를 호출하여 이메일 서비스를 호출한다(1분 이후 타임아웃 됨)
void sendEmail(String to, String subject, String body);
```

`큰 그림` 에 대한 주석

- 팀에 새로운 사람이 합류 했다 상상하고, 그 사람이 팀의 코드베이스에 익숙해 질 수 있도록 파일이나 클래스 단위의 상위 수준(high-level) 주석달기
- file-level comment

```dart
// 파일 시스템에 편리한 인터페이스를 제공하는 헬퍼 함수들을 담고 있다
// 파일의 퍼미션과 다른 자세한 세부 사항을 처리한다
```

요약 주석

- 함수 내부에서 큰 그림을 설명하는 방식을 추가하는 것 역시 좋음
- low-level comment

```dart
// 고객이 자신을 위해 구입한 항목을 모두 찾는다
for (final customerId in allCustomers) {
    for (final sale in allSales[customerId].sales){
        if (sale.recipient == customerId) {
            ...
        }
    }
}
// 주석 없이 읽는 것은 미스터리물을 읽는 행위나 다름없음
```

몇몇 커다란 '덩어리'로 구성된 긴 함수에 특히 유용함

```dart
void generateUserReport(){
    // 이 사용자를 위한 lock을 얻음
    ...
    // 데이터베이스에서 사용자의 정보를 읽음
    ...
    // 정보를 파일에 작성
    ...
    // 사용자를 위한 lock을 되돌려 넣음
    ...
}
```

글 쓰는 두려움 떨쳐내기

- 많은 프로그래머가 주석 달기를 달가워 하지 않음 ← 좋은 주석을 창작하기 위해 시간들이는 것을 아깝다고 생각하기 때문
- 다듬어 지지 않은 생각이라도 일단 쓰기 시작하라(아무것도 없는 것 보다는 낫다) → 그 이후 다듬으면 된다
- 주석 작성하는 과정
    1. 마음에 떠오르는 생각을 무조건 적어본다
    2. 주석을 읽고 무엇이 개선되어야 하는지(그런 부분이 있다면) 확인한다
    3. 개선한다

```dart
// before
// 이런 제길, 이 리스트 안에 중복된 항목이 있으면 이건 복잡해지잖아

// after
/// 주의: 이 코드는 리스트 안에 있는 중복된 항목을 다루지 않는다.
/// 그렇게 하는 것이 더 어렵기 때문이다.
```

### 명확하고 간결한 주석 달기

주석은 높은 '정보 대 공간' 비율을 갖춰야 함

#### 1. 주석을 간결하게 하라

주석은 꼭 필요한 경우가 아니면 최소한으로 작성하자
예시

```dart
// before
// int는 CategoryType이다
// 내부 페어의 첫 번째 float는 'score'다
// 두 번째는 'weight'다
typedef Map<int, Pair<double,double>> scoreMap;

// after
// CategoryType -> (score,weight)
typedef Map<int, Pair<double,double>> scoreMap;
```

#### 2. 모호한 대명사는 피하라

예시

```dart
// before
// 데이터를 캐시에 넣어라. 하지만 그것이 너무 큰지 먼저 확인하라

// after
// 데이터를 캐시에 넣어라. 하지만 데이터가 너무 큰지 먼저 확인하라

// or
// 데이터가 충분히 작으면, 이를 캐시에 넣어라
```

#### 3. 엉터리 문장을 다듬어라

예시

```dart
// before
// 이 URL을 전에 이미 방문했는지에 따라서 다른 우선순위를 부여

// after
// 전에 방문하지 않은 URL에 높은 우선순위를 부여하라
```

#### 4. 함수의 동작을 명확하게 설명하라

- 예시

```dart
// before
// 이 파일에 담긴 줄 수를 반환한다
int countLines(String fileName){}

// after
// 파일 안에 새 줄을 나타내는 바이트('\n')이 몇개인지 센다
int countLines(String fileName){}
```

#### 5. 코너케이스를 설명해주는 입/출력 예를 사용하라

주석을 작성하는데 신중하게 선택된 입/출력 예제는 천 마디 말보다 위력적이다

```dart
// before
/// 입력된 'src'의 'chars'라는 접두사와 접미사를 제거한다
String strip(String src, String chars){ ... }

/// 다음과 같은 질문에 답하지 않으므로 명확하지 않다
/// 1. chars가 제거되어야 하는 정확한 부분 문자열을 의미하는가
///    아니면 특정한 순서가 정해지지 않은 문자의 집합을 의미하는가
/// 2. src의 끝에 chars가 여러번 있으면 어떻게 되는가

// after
/// ex) strip("abba/a/ba", "ab")은 "/a/"를 반환한다
String strip(String src, String chars){ ... }
```

```dart
// before
/// pivot보다 작은 요소가 pivot과 크거나 같은 요소들보다 앞에 오도록 'v'를 재배열한다
/// 그 다음 v[i] < pivot을 만족시키는 것 중에서 가장 큰 'i'를 (혹은 pivot보다 작은 것이
/// 없으면 -1을) 반환한다

int partition(Vector v, int pivot);

// to wordy !

// after
/// ex) partition([8,5,9,8,2],8) 은 [5 2 | 8 9 8] 을 만들고 1를 반환할 것이다
int partition(Vector v, int pivot);

// 짚고 넘어갈 부분
/// 벡터 안에 존재하는 값을 pivot으로 사용하여 경계가 분할되는 것을 보임
/// 벡터가 중복된 값을 허용한다는 사실을 보여주기 위해 중복된 값 8을 보임
/// 중복된 값 8을 포함시켜 벡터가 중복된 값을 허용한다는 사실을 보임
/// 결과값을 담은 벡터를 일부러 정렬하지 않았음. 정렬하면 혼동을 초래할 것임.
/// 반환된 값이 1이므로, 벡터에 1이 포함되지 않게 했음. 1이 포함되면 혼동을 초래할 것임.
```

#### 6. 코드의 의도를 명시 하라

너무 자세한 내용이 아니라 높은 수준에서 개괄적으로 설명하는 것이 좋음
코드를 작성하면서 생각했던 바를 나중에 코드를 읽는 사람에게 전달하기 위해 주석을 작성하지만 대다수의 주석은 새로운 정보 없이 그냥 코드가 수행하는 동작을 문자 그대로 설명하는데 그침

```dart
// before
/// 리스트를 역순으로 반복한다

// after
/// 각 가격을 높은 값에서 낮은 값 순으로 나타낸다

/// 오류가 있더라도 후자로 작성하는 것이 중요함. => 읽는 사람이 작성자 의도를
/// 단번에 파악하고 수정할 수 있기 때문

/// = 주석이 중복검사의 역할을 수행하게 됨
```

#### 7. 이름을 가진 함수 파라미터(Named Function Parameter) 주석

해당 언어에서 Named Function Parameter 을 지원하지 않는 경우, 무슨 의미인지 파악할 수 있게 주석을 작성하라

```dart
// 주석을 가진 파라미터를 이용하여 함수를 호출한다
connect(/* timeout_ms = */ 10, /* use_encryption = */ false);
```

#### 8. 정보 축약형 단어를 사용하라

프로그래밍 에서 반복되는 문제 패턴, 관용구를 묘사하기 위한 특정한 어휘나 문구를 사용하여 문장을 간단하게 표현하라

```dart
// before
/// 이 클래스는 데이터베이스와 동일한 정보를 담는 멤버를 가지고 있는데, 이는
/// 속도를 향상시키는 데 사용된다. 나중에 이 클래스가 읽히면, 멤버들이 어떤 값을
/// 가졌는지 확인하고, 만약 값이 있으면 그 값이 반환된다. 값이 없으면
/// 데이터베이스에서 값이 읽혀져서 나중에 이용될 수 있게 멤버에 저장된다.

// after
/// 이 클래스는 데이터베이스에 대한 캐시 계층으로 기능한다

// -----------------------------------------------------------

// before
/// 주사값에서 불필요한 빈칸을 제거한다. 그리고 "Avenue"를 "Ave."로 바꾸는 것과
/// 같은 정리 작업을 수행한다. 이러한 과정으로 사실상 같지만 다르게 입력된
/// 주소는 동일한 방식으로 정리된 값을 갖게 되어 동일한주소를 가지는지를
/// 값들을 서로 비교해서 확인할 수 있다.

// after
/// 주소값을 표준화한다(불필요한 빈칸을 제거하고, "Avenue" -> "Ave." 등의 정리작업 수행)
```

프로그래밍에 전형적인 상황을 묘사하는 표현이 있는지 확인한 후 주석 작성을 하면 유용함. (경험적인 `heuristic`, 주먹구구식 `brute-force`, 순진한 해법 `naive solution`)

## Part 2. 루프와 논리를 단순화 하기

흐름제어, 논리식, 변수에서의 단순화

읽는 사람의 ‘정신적 짐’을 부과하는 요소들을 최소화 하는 것이 핵심

- 정신적 짐: 복잡한 루프, 거대한 표현, 많은 변수들로 인해, 코드 읽는 것을 고민하게 하고 불편하게 만드는 것.

### 읽기 쉽게 흐름제어 만들기

- 핵심: 흐름을 제어하는 조건과 루프 그리고 여타 요소를 최대한 ‘자연스럽게’ 만들도록 노력하라. 코드를 읽다가 다시 되돌아가서 코드를 읽지 않아도 되게끔 만들어야 한다.

#### 1. 조건문에서 인수의 순서

다음 두 코드 중 읽기 편한것은 어떤 것이고 그 이유는 무엇일까?

```dart
// 1.
if (length >= 10)

// 2.
if (10 <= length)

// 많은 사람이 1번이 더 읽기 편하다고 생각할 것이다
```

```dart
// 1.
while(bytes_received < bytes_expected)

// 2.
while(bytes_expected > bytes_received)

// 많은 사람이 역시 1번이 더 읽기 편하다고 생각할 것이다
```

- 한 쪽이 읽기 편하다고 느끼는 이유는 다음 규칙을 통해 설명될 수 있다

| 왼쪽                                | 오른쪽                                     |
| ----------------------------------- | ------------------------------------------ |
| 값이 더 유동적인 ‘질문을 받는’ 표현 | 더 고정적인 값, 비교대상으로 사용되는 표현 |

영어 어순과 일치함

```plaintext
1. 당신이 적어도 18세라면
2. 18년이 당신의 나이보다 작거나 같다면
```

둘 중 첫 번째가 자연스럽다

#### 2. if/else 블록의 순서

다음 두 가지 중 어떤 코드 블럭을 선택하여 작성해야하는가

```dart
if (a == b) {
    // 첫 번째 경우
} else {
    // 두 번째 경우
}
```

```dart
if (a != b) {
    // 첫 번째 경우
} else {
    // 두 번째 경우
}
```

다음과 같은 규칙을 참고하라

```plaintext
1. 부정이 아닌 긍정을 다루어라. 즉, if(!debug) 보다 if(debug)를 선호하자
2. 간단한 것을 먼저 처리하라. 이렇게 하면 동시에 같은 화면에 if와 else 구문을 나타낼 수도 있다
3. 더 흥미롭고, 확실한 것을 먼저 다루어라
```

때때로 이러한 규칙이 서로 충돌을 일으켜 판단해야할 경우의 예시

```dart
// before
/// URL이 expand_all 이라는 질의 파라미터 포함 여부에 따라 response를 만드는 웹서버 기능
if (!url.hasQueryParameter("expand_all")) {
    response.render(items);
} else {
    for (var i=0; i<items.size; i++) {
        items[i].expand();
    }
}

/// 코드를 읽는 대부분이 expand_all 이 무엇인지 궁금할 것이다
/// => "분홍색 코끼리를 생각하지 마세요"라고 말하는 것과 유사함
/// "분홍색 코끼리"가 흥미로운 부분이기 때문에 먼저 처리해준다

// after
if (url.hasQueryParameter("expand_all")) {
    for (var i=0; i<items.size; i++) {
        items[i].expand();
    }
} else {
    response.render(items);
}
```

```python
# 부정해야 더 단순하고 흥미로우면서 동시에 위험해지는 경우
if not file:
    # 에러를 기록
else:
    # ...

# 이런 경우 상세 내용을 따지고 난 이후 판단을 내려야 함
```

#### 3. (삼항 연산자로 알려진)?:를 이용하는 조건문 표현

줄 수를 최소화 하는 일보다 다른 사람이 코드를 읽고 이해하는데 걸리는 시간을 최소화 하는 일이 더 중요함

간단하지 않은 코드를 삼항연산자로 바꾸는 것은 모든 것을 한줄에 쓰기 ‘모든 것을 한줄에 쓰기’ 그 이상 아무것도 아니다

기본적으로 if/else 를 사용하라. ?: 를 이용하는 삼항 연산은 매우 간단한 경우에만 사용해야 한다

예시

```dart
// 삼항 연산자가 적합한 경우
time_str += (hour >= 12) ? "pm":"am";

// 이런경우는 매우 삼가하라
// return exponent >= 0 ? mantissa * (1 << exponent) : mantissa / (1 << exponent);
```

#### 4. do/while 루프를 피하라

do while문 문법은 조건이 먼저 눈에 띄지 않기 때문에 에러와 혼동의 원인이 되는 경우가 많다

```dart
// do while 문의 문제점
/// 과연 다음 문장은 몇번 반복되는 것인가?
do {
    continue;
} while(false);

/// 1번

/// 이런식으로 do while 문은 혼란을 가중 시킨다
```

```dart
// before
/// node 부터 리스트를 검색하여 주어진 'name'을 찾는다
/// 'max_length' 이상의 노드는 고려하지 않는다
bool listHasNode(Node node, String name, int max_length) {
    do {
        if (node.name.equals(name)){
            return true;
        }
        node = node.next();
    } while (node != null && --max_length > 0);

    return false;
}
/// 아래에 있는 조건에 따라서 다시 실행될 수도 있다.
/// 일반적으로 논리적 조건은 그것을 감싸는 것 위에 놓이는 것이 자연스럽다.
/// 코드를 두번 읽어야 하기 때문이다.

// after
bool listHasNode(Node node, String name, int max_length) {
    while (node != null && max_length-- > 0) {
        if (node.name.equals(name)){
            return true;
        }
        node = node.next();
    }
    return false;
}
```

#### 5. 함수 중간에서 반환하기

어떤 프로그래머는 한 함수에서 반환하는 곳이 여러 곳이면 안된다고 주장함

- 함수 끝부분에서 실행되는 cleanup 코드의 호출을 보장하려는 의도
- 현대 언어는 cleanup 코드를 실행시키는 더 정교한 방법을 제공

| 언어         | 클린업 코드를 위한 관용적 구조 |
| ------------ | ------------------------------ |
| C++          | destructors                    |
| Java, Python | try finally                    |
| Python       | with                           |
| C#           | using                          |

순수한 C 언어는 함수를 반환할 때 특정한 코드를 실행시키는 방법을 제공. 따라서 함수가 기다란 코드의 중간부분에서 반환될 수 있도록 작성되어 있으면, 반환되는 지점 다음에 위치한 클린업 코드는 실행되지 않는다는 문제가 있음

- 이러한 경우는 함수를 리팩토링하거나 goto cleanup 같은 명령을 신중하게 사용하는 등의 별도의 방법을 취해야함

이 책에서는 함수 중간에 반환하는 것이 완전히 허용되어야 한다고 함 ⇒ ‘보호장치’ 역할을 하기 때문

예시

```dart
bool contains(String str, String substr) {
    if (str == null || substr == null) return false;
    if (substr == "") return true;
    ...
}
```

#### 6. 악명높은 goto

C 를 제외한 다른 언어에는 `goto`를 사용하는 것 보다 더 좋은 방법이 있으므로 쓸 필요가 없음
C 프로젝트는 여전히 `goto` 를 발견할 수 있음(특히, 리눅스 커널)

- `goto` 를 사용하는 것을 용서할 수 없는 신성모독으로 간주하기 전에, `goto` 를 사용하면 어째서 더 나은지 살펴봐야함
- `goto` 를 사용하는 유일한 상황이라면 심각한 문제가 아니지만, 이동할 수 있는 장소가 여러 곳이 교차된다면 스파게티 코드가 양산됨

goto 문은 피할수 있으면 피하는 것이 낫다

#### 7. 중첩을 최소화 하기

코드의 중첩이 심할수록 이해하기 힘듬(중첩이 일어날때 마다 코드를 읽는 사람의 마음 속에 존재하는 ‘정신적 스택’ 에 추가적인 조건이 입력됨)
예시

```dart
// 바람직하지 않은 예
// 다음 코드에서 정신적 스택이 추가되는 과정을 보라

if (user_result == "SUCCESS"){
    if (permission_result != "SUCCESS") {
        reply.writeErrors("error reading permissions");
        reply.done();
        return;
    }
    // 코드를 읽는 사람이 여기서 여러가지 것을 기억해야함
    // 1. permission_result == "SUCCESS" 인 부분이구나
    // 2. user_result == "SUCCESS" 조건에 아직 있구나
    // => user_result == "SUCCESS" && permission_result == "SUCCESS"

    reply.writeErrors("");
} else {
    reply.writeErrors(user_result);
}
reply.done();
```

```dart
// 원래 코드
if (user_result == "SUCCESS"){
    reply.writeErrors("");
} else {
    reply.writeErrors(user_result);
}
reply.done();

// 원래 이렇게 단순 했음
```

```dart
// 두번째 동작을 추가 => 일리가 있지만 복잡해짐
if (user_result == "SUCCESS"){
    if (permission_result != "SUCCESS") {
        reply.writeErrors("error reading permissions");
        reply.done();
        return;
    }
    reply.writeErrors("");
}
/// 누군가 다른 사람이 나중에 이 코드를 읽으면, 앞에서 살펴본 종류의 문맥은 모두 사라지게 됨.
```

수정해야 하는 상황이라면 작성한 코드를 새로운 관점에서 바라보아야 함. 뒤로 한걸음 물러서서 코드 전체를 보라.

##### (1) 함수 중간에서 반환하여 중첩을 제거하라

‘실패한 경우’들을 최대한 빠르게 처리하고 함수에서 반환하여 제거할 수 있다

앞의 코드 수정

```dart
if (user_result != "SUCCESS"){
    reply.writeErrors(user_result);
    reply.done();
    return;
}

if (permission_result != "SUCCESS") {
    reply.writeErrors(permission_result);
    reply.done();
    return;
}

reply.writeErrors("");
reply.done();
```

##### (2) 루프 내부에 있는 중첩 제거하기

루프 내부에 중첩된 코드가 있을 때는 반환할 수 없음

다음과 같은 방법으로 처리

```dart
// before
for (int i=0; i < results.size; i++) {
    if (results[i] != null) {
        non_null_count++;
        if (results[i].name != "") {
            ...
        }
    }
}

// after
for (int i=0; i < results.size; i++) {
    if (results[i] == null) continue;
    non_null_count++;

    if (results[i].name == "") continue;
    ...
}
```

#### 8. 실행 흐름을 따라올 수 있는가?

프로그램 하위 수준의 흐름제어(ex. 루프, 조건문)이 아닌 프로그램 상위수준에서 잘 따라갈 수 있게 만들어라

| 프로그래밍 구조         | 상위수준의 프로그램 흐름이 혼란스러워지는 방식                                            |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| 스레딩                  | 어느 코드가 언제 실행되는지 불분명 하다                                                   |
| 시그널/인터럽트 핸들러  | 어떤 코드가 어ㄸ너 시점에 실행될지 모른다                                                 |
| 예외                    | 예외처리가 여러 함수 호출을 거치면서 실행될 수 있다                                       |
| 함수 포인터 & 익명 함수 | 실행할 함수가 런타임에 결정되기 때문에 컴파일 과정에서는 어떤 코드가 실행될지 알기 어렵다 |
| 가상 메소드             | object.virtualMethod()는 알려지지 않은 하위클래스의 코드를 호출할 지도 모른다             |

위의 예시 중 일부는 매우 유용함 ⇒ 코드를 더 읽기 편하고 덜 중복되게 함
하지만 나중에 코드를 읽는 사람이 버그 추적을 하기 어렵게 만드는 경우가 있으므로 이러한 구조를 사용하는 비율을 너무 높지 않게 해야함

### 거대한 표현을 잘게 쪼개기

> 핵심: 거대한 표현을 더 소화하기 쉬운 여러 조각으로 나눈다

우리는 보통 한번에 서너 개 일만 생각할 수 있으므로, 코드의 표현을 줄여 이해하기 쉽도록 한다

#### 1. 설명변수

거대한 표현을 잘게 쪼개는 가장 쉬운 방법: 작은 하위표현을 담을 “추가변수 extra variable”을 만들어라

```python
# before
if line.split(":")[0].strip() == "root":

# after
username = line.split(":")[0].strip()
if username == "root":
```

#### 2. 요약변수

커다란 코드 덩어리를 짧은 이름으로 대체하여 더 쉽게 관리하고 파악하는 목적을 가진 변수

의미를 쉽게 파악할 수 있어 설명을 요구하지 않는 표현이라 해도, 새로운 변수로 담아두는 방법은 여전히 유용함

예시

```dart
// before
if (request.user.id == document.owner_id) {
    // 사용자가 이 문서를 수정할 수 있다
}

if (request.user.id != document.owner_id) {
    // 문서는 읽기 전용이다
}

// after
/// 코드의 핵심 개념 "사용자가 이 문서를 소유하는가" 를 더 명확하게 표현할 수 있음

final bool user_owns_document = request.user.id == document.owner_id;
if (user_owns_document) {
    // 사용자가 이 문서를 수정할 수 있다
}
if (!user_owns_document) {
    // 문서는 읽기 전용이다
}

/// 코드를 읽는 사람에게 이 함수에서 생각해야 하는 주된 개념을 짚어주는 역할을 함
```

#### 3. 드모르간의 법칙 사용하기

> 드모르간의 법칙(De Morgan’s Laws)

```plaintext
1. not (a or b or c) == (not a) and (not b) and (not c)
2. not(a and b and c) == (not a) or (not b) or (not c)
```

위의 법칙을 이용하여 불리언 표현을 간단하게 만들 수 있음

```jsx
// before
if (!(file_exists && !is_protected))

// after
if (!file_exists || is_protected)
```

#### 4. 쇼트 서킷 논리(Short-Circuit Logic) 오용 말기

> 쇼트서킷 논리: if (a || b) 에서 a가 참이면 b는 평가하지 않는 것

매우 편리하지만 때로는 복잡한 연산을 수행할 때 오용될 수 있음

예시

```jsx
// before
assert((!(bucket = FindBucket(key))) || !bucket->IsOccupied());
/// 이 키를 위한 바구니를 구하라. 바구니가 null이 아니면,
/// 그것을 누군가가 차지하고 있지 않은지 확인하라

/// 손을 멈추고 잠시 생각해야 무슨 의미인지 이해할 수 있다

// after
/// 거대한 코드를 쪼게 2줄로 늘어낫지만 훨씬 이해하기 쉬워졌다
bucket = FindBucket(key);
if (bucket != null) assert(!bucket->IsOccupied());
```

‘영리하게’ 작성된 코드에 유의하라. 나중에 다른 사람이 읽으면 그런 코드가 종종 혼란을 초래한다.

물론 이러한 깔끔한 경우에 쇼트 서킷 연산을 사용하는 것에는 무리가 없다

```jsx
if (object && object-> method()) ...

x = a || b || c
```

#### 5. 복잡한 논리와 씨름하기

반대로 생각해보는 것으로 더욱 우아한 접근 방법을 찾을 수 있다

```go
// before
struct Range {
    int begin
    int end // end는 경계를 포함하지 않음. (이전 챕터 참고)
    // 예컨대 [0,5)은 [3,8) 와 부분적으로 겹친다
    bool OverlapsWith(Range other)
}

func (r *Range) OverlapsWith(Range other) bool {
    // begin이나 end가 other에 속하는지 검사한다
    return (r.begin >= other.begin && r.begin <= other.end) ||
            (r.end >= other.begin && r.end <= other.end);
}

// 버그가 있음. end에서 겹치는 것을 제외하지 않음
// =>
func (r *Range) OverlapsWith(Range other) bool {
    // begin이나 end가 other에 속하는지 검사한다
    return (r.begin >= other.begin && r.begin < other.end) ||
            (r.end > other.begin && r.end <= other.end);
}

// 또 다른 버그가 있음. begin/end가 other를 완전히 포함하는 경우를 무시하고 있음
func (r *Range) OverlapsWith(Range other) bool {
    // begin이나 end가 other에 속하는지 검사한다
    return (r.begin >= other.begin && r.begin < other.end) ||
            (r.end > other.begin && r.end <= other.end) ||
            (r.begin <= other.begin &&  r.end >= other.end);
}

/// 코드가 매우 복잡해졌다

// after
/// 창의성이 필요하다.
/// 반대의 경우를 생각해보자 => 겹치지 않는 경우
/// 1. 다른 범위가 이 범위 시작보다 전에 끝난다
/// 2. 다른 범위가 이 범위가 끝난 후에 시작한다
func (r *Range) OverlapsWith(Range other) bool {
    // begin이나 end가 other에 속하는지 검사한다
    if (other.end <= r.begin) return false;
    if (other.begin >= r.end) return false;

    return true;
}

```

#### 6. 거대한 구문 나누기

개별적인 표현 뿐만 아니라, 거대한 구문도 동일한 테크닉으로 나눌 수 있다

```jsx
// before
var update_highlight = function (message_num) {
    if ($("#vote_value" + message_num).html() === "Up"){
        $("#thumbs_up" + message_num).addClass("highlighted");
        $("#thumbs_down" + message_num).removeClass("highlighted");
    } else if ($("#vote_value" + message_num).html() === "Down"){
        $("#thumbs_up" + message_num).removeClass("highlighted");
        $("#thumbs_down" + message_num).addClass("highlighted");
    } else {
        $("#thumbs_up" + message_num).removeClass("highlighted");
        $("#thumbs_down" + message_num).removeClass("highlighted");
    }
}
/// 개별 표현은 그렇게 크지 않지만, 모두 한곳에 있어서 코드를 읽는 사람의
/// 머리를 강타하는 거대한 구문을 형성한다

// after
/// DRY 원리의 예
var update_highlight = function (message_num) {
    var thumbs_up = $("#thumbs_up" + message_num);
    var thumbs_down = $("#thumbs_down" + message_num);
    var vote_value = $("#vote_value" + message_num).html();
    var hi = "highlighted";

    if (vote_value === "Up"){
        thumbs_up.addClass(hi);
        thumbs_down.removeClass(hi);
    } else if (vote_value === "Down"){
        thumbs_up.removeClass(hi);
        thumbs_down.addClass(hi);
    } else {
        thumbs_up.removeClass(hi);
        thumbs_down.removeClass(hi);
    }
}
```

#### 7. 표현을 단순화하는 다른 창의적인 방법들

매크로 사용을 권장하는 것은 아니지만 때에 따라선 매크로가 간단한 사용과 코드 가독성에 도움을 주기도 함

비슷한 예시

```dart
/// C++ 매크로 관련 예시여 비슷하게 적용할 수 있을만한 사례
// before
void AddStats(String stat){
    final void Function(String) onTap;
    final String Function(String) onPassed;
}

// after
typedef onProcessed<T> = T Function(String);
```

### 변수와 가독성

변수를 엉터리로 사용하면?

```plaintext
변수가 많을수록 기억하고 다루기 어려워짐
변수의 범위가 넓어질수록 기억하고 다루는 시간이 더 길어짐
변수값이 자주 바뀔수록 현재값을 기억하고 다루기가 더 어려워짐
```

이러한 문제는 다음 방법으로 다루어볼 수 있다

#### 1. 변수 제거하기

가독성에 도움이 되지 않는 변수들을 제거하라

    1. 불필요한 임시 변수들
        
        ```python
        # before
        now = datetime.datetime.now()
        root_message.last_view_time = now
        ## 변수가 필요하지 않다
        ### 1. 복잡한 표현을 잘게 나누지 않는다
        ### 2. 명확성에 도움이 되지 않는다(datetime.datetime.now()은 그자체로 명확)
        ### 3. 한번만 중복되어 중복된 코드를 압축하지 않는다
        
        # after
        root_message.last_view_time = datetime.datetime.now()
        ```
        
    2. 중간결과 삭제하기
        - 예시
            
            ```jsx
            // before
            var remove_one = function(array, value_to_remove) {
            	var index_to_remove = null;
            	for (var i = 0; i < array.lengthl i +=1){
            		if (array[i] == value_to_remove){
            			index_to_remove = i;
            			break;
            		}
            	}
            	if (index_to_remove != null){
            		array.splice(index_to_remove,1);
            	}
            }
            /// index_to_remove 는 단지 중간결과를 저장할 뿐임
            /// 변수 결과를 얻자마자 바로 제거
            
            // after
            var remove_one = function(array, value_to_remove) {
            	for (var i = 0; i < array.lengthl i +=1){
            		if (array[i] == value_to_remove){
            			array.splice(index_to_remove,1);
            			break;
            		}
            	}
            	
            }
            
            ```
            
            ```jsx
            // before
            var remove_one = function(array, value_to_remove) {
            	var index_to_remove = null;
            	for (var i = 0; i < array.length; i +=1){
            		if (array[i] == value_to_remove){
            			index_to_remove = i;
            			break;
            		}
            	}
            	if (index_to_remove != null){
            		array.splice(index_to_remove,1);
            	}
            }
            /// index_to_remove 는 단지 중간결과를 저장할 뿐임
            /// 변수 결과를 얻자마자 바로 제거
            
            // after
            var remove_one = function(array, value_to_remove) {
            	for (var i = 0; i < array.length; i +=1){
            		if (array[i] == value_to_remove){
            			array.splice(i,1);
            			break;
            		}
            	}
            }
            
            ```
            
    3. 흐름 제어 변수 제거하기
        - 예시
            
            ```dart
            // before
            bool done = false;
            
            while (/*조건*/ && !done){
            	...
            
            	if(...){
            		done = true;
            		continue;
            	}
            }
            
            // after
            while (/*조건*/){
            	...
            
            	if(...){
            		break;
            	}
            }
            
            /// 이 예제는 간단하지만, 중첩된 여러 루프 때문에 추가로 break가 필요한 경우
            /// - 루프 안에서 반복되는 코드를 새로운 함수로 만들면 됨
            ```

#### 2. 변수의 범위를 좁혀라

각 변수의 위치를 옮겨서 변수가 나타나는 줄의 수를 최소화 하라. 눈에 보이지 않으면 마음에서도 멀어지는 법이다.

#### 3. 값을 한 번만 할당하는 변수를 선호하라

한번만 할당되는 `const`, `final` 등 불변의 변수가 훨씬 이해하기 쉽다.
한번만 할당할 수 없다면, 최대한 적은 횟수로 변하게 하는 것이 도움이 된다.

## Part 3. 코드 재작성하기

코드를 전체적으로 함수 수준에서 변경하는 방법에 대한 논의

```plaintext
1. 프로그램의 주된 목적과 상관없는 하위문제를 추출하라
2. 코드를 재배열하여 한 번에 한 가지 일만 수행하게 하라
3. 코드를 우선 단어로 묘사하고, 이 묘사를 이용하여 깔끔한 해결책을 발견하도록 하라
```

### 상관없는 하위문제 추출하기

- 엔지니어링은 커다란 문제를 작은 문제들로 쪼갠 다음, 각각의 문제에 대한 해결책을 구하고, 다시 하나의 해결책으로 맞추는 일련의 작업 ⇒ 이러한 원리를 코드에 적용하면 코드가 더 튼튼해지며 가독성도 좋아짐
    1. ‘상위 수준에서 본 이 코드의 목적은 무엇인가?’ 를 질문하라
    2. 코드의 모든 줄에 질문을 던져라. 예를 들어 ‘이 코드는 직접적으로 목적을 위해서 존재하는가? 혹은 목적을 위해서 필요하긴 하지만 목적 자체와 직접적으로 연관없는 하위문제를 해결하는가’
    3. 만약 상당히 원래의 목적과 직접적으로 관련되지 않은 하위 문제를 해결하는 코드 분량이 많으면, 이를 추출해서 별도의 함수로 만든다
- 예시
    
    ```jsx
    // 다음 코드를 어떻게 바꿀 수 있을까?
    
    // 상위수준 목적: 주어진 점과 가장 가까운 장소를 찾는것
    var findClosestLocation() = function (lat, lng, array) {
    	var closest;
    	var closest_dist = Number.MAX_VALUE;
    
    	for (var i=0; array.length; i+=1) {
    		// 복잡한 기하학 문제이므로 자세하게 알 필요 없다고 책에서 설명함
    		// 두 점 모두를 라디언으로 변환한다
    		var lat_rad = radians(lat);
    		var lng_rad = radians(lng);
    		var lat2_rad = radians(array[i].latitude);
    		var lng2_rad = radians(array[i].longitude);
    
    		// '코사인의 특별법칙' 공식을 사용
    		var dist = Math.acos(Math.sin(lat_rad) * Math.sin(lat2_rad) + 
    												 Math.cos(lat_rad) * Math.cos(lat2_rad) *
    												 Math.cos(lng2_rad - lng_rad)
    		);
    
    		if (dist < closest_dist) {
    			closest = array[i];
    			closest_dist = dist;
    		}
    	}
    	return closest;
    };
    
    // 문제
    /// 1. 루프의 내부에 있는 코드는 대부분 주요 목적과 직접 상관없는 하위문제를 다룬다
    ///   - 구 위에 있는 두 개의 위도/경도 점 사이의 거리를 계산하는데, 이 내용의 분량이 꽤 많으니
    ///     별도의 함수로 추출하는 편이 좋다
    var spherical_distance = function (lat1, lng1, lat2, lng2) {
    	var lat1_rad = radians(lat1);
    	var lng1_rad = radians(lng1);
    	var lat2_rad = radians(lat2);
    	var lng2_rad = radians(lng2);
    
    	// '코사인의 특별법칙' 공식을 사용
    	return Math.acos(Math.sin(lat1_rad) * Math.sin(lat2_rad) + 
    											 Math.cos(lat1_rad) * Math.cos(lat2_rad) *
    											 Math.cos(lng2_rad - lng1_rad)
    	);
    }
    /// - 코드를 읽는 사람은 밀도 높은 기하 공식에 방해받지 않고 상위수준의 목적에 집중할 수 있으니
    ///   전반적으로 코드의 가독성이 높아짐
    /// - spherical_distance()라는 별도의 메소드로 독립하면서 독립적인 테스트도 더 용이하게 됨
    ///   (의도치 않은 추가적 이점)
    ```
    
1. 순수한 유틸리티 코드
    - 유틸리티 코드: 문자열 변경, 해시테이블 사용, 파일 읽기/쓰기와 같이 프로그램이 수행하는 일에 매우 기본적인 작업을 포괄하는 핵심적 집합
    - 일반적으로 해당 프로그래밍 언어에 내장된 라이브러리에 있음
    - 없다면 직접 만들어라 → 대신, 그럴듯한 유틸리티 코드 모음으로 만들어라
2. 일반적인 목적의 코드
    - 예시
        
        ```jsx
        // 자바스크립트를 디버깅할 때 사용하는 alert()에 관련된 예시
        /// ajax를 이용하여 데이터를 서버에 제출하고, 서버가 반환한 데이터 딕셔너리를 화면에 나타냄
        
        // before
        ajax_post({
        	url: "http://example.com/submit",
        	data: data,
        	on_success: function (response_data){
        		// 다음 내용은 직접 상관없는 하위문제, 즉 딕셔너리에 담긴 내용을 예쁘게 출력하는 일
        		// 이러한 코드는 따로 추출하는 편이 낫다
        		var str =  "{\n";
        		for (var key in response_data){
        			str += " " + key + " = " + respones_data[key] + "\n"; 
        		}
        		alert(str + "}");
        
        		// 계속해서 "response_data"를 처리
        
        	}
        });
        
        // after
        ajax_post({
        	url: "http://example.com/submit",
        	data: data,
        	on_success: alert(format_pretty(response_data)),
        });
        
        var format_pretty = function (obj) {
        	var str =  "{\n";
        	for (var key in response_data){
        		str += " " + key + " = " + respones_data[key] + "\n"; 
        	}
        	return str + "}";
        }
        /// 추출하면 뜻하지 않은 장점이 많아짐
        /// 1. 호출하는 코드를 간단하게 만듬
        /// 2. format_pretty()를 다룬 곳에서도 간편하게 사용할 수 있는 함수로 만듬
        /// 3. 필요할 때 format_pretty() 함수를 손쉽게 개선할 수 있음
        ///    (별도로 분리된 작은 함수를 다룰 때는 기능을 더하고, 가독성을 개선하고, 
        ///     코너 케이스를 다루는 일이 상대적으로 쉽게 느껴지기 때문)
        
        /// 추출함으로서 쉽게 볼 수 있는 문제점
        /// 1. obj를 객체라고 간주한다. 문자열 혹은 undefined이면 예외가 발생
        /// 2. obj의 값이 간단한 값이라고 생각한다. 중첩된 객체면 현재 코드는 [object Object]
        ///    라는 코드를 출력함(심지어 예쁘지도 않음).
        
        /// 개선판
        var format_pretty = function (obj,indent) {
        	// null이 되거나 정의되지 않은 문자열, 그리고 객체가 아닌 경우를 처리
        	if (obj === null) return "null";
        	if (obj === undefined) return "undefined";
        	if (typeof obj === "string") return '"' + obj + '"';
        	if (typeof obj !== "object") return String(obj);
        
        	if (indent == undefined) indent = "";
        
        	// (null이 아닌) 객체를 처리
        	var str =  "{\n";
        	for (var key in response_data){
        		str += " " + key + " = " + respones_data[key] + "\n"; 
        	}
        	return str + "}";
        }
        
        ```
        
3. 일반적인 목적을 가진 코드를 많이 만들어라
    - 앞서 만든 format_pretty()는 상관없는 하위문제를 다루는 대표적 함수 ⇒ 매우 기본적이고 폭넓게 적용할 수 있는 일을 수행하므로 다른 프로젝트에서도 사용할 수 있음
    - 코드베이스는 이와 같은 코드를 담아두는 디렉터리를 따로 두고 있으므로 쉽게 공유할 수 있음
    - 일반적인 목적을 가진 코드는 프로젝트의 나머지 부분에서 완전히 분리 되므로 좋다.
    - 이러한 코드는 개발, 테스트, 이해가 쉽다.
        - 많은 사람들이 사용하는 강력한 라이브러리의 내부는 염려할 필요 없음
            - 코드베이스가 완전히 분리되어 있기 때문
4. 특정한 프로젝트를 위한 기능
    - 추출한 하위 문제는 사용하는 프로젝트를 전혀 몰라야 하는 것이 이상적이지만, 그렇지 않고 단순히 분리하는 것만으로도 큰 도움이 된다
    - 예시
        
        ```python
        # before
        business = Business()
        business.name = request.POST("name")
        
        url_path_name = business.name.lower()
        url_path_name = re.sub(r"['\.]", "", url_path_name)
        url_path_name = re.sub(r"[^a-z0-9]+", "-", url_path_name)
        url_path_name = "/biz/" + url_path_name
        
        business.date_created = datetime.datetime.utcnow()
        business.save_to_database()
        ## 전체 목적과 직접 상관없는 하위문제는 name을 유효한 url로 변환하는 일을 함
        ## 추출하는 것이 바람직함
        
        # after
        CHARS_TO_REMOVE = re.compile(r"['\.]+")
        CHARS_TO_DASH = re.compile(r"[^a-z0-9]+")
        
        def make_url_friendly(text):
        	text = text.lower()
        	text = CHARS_TO_REMOVE.sub("",text)
        	text = CHARS_TO_DASH.sub("-",text)
        	return text.strip("-")
        
        business = Business()
        business.name = "/biz/" + make_url_friendly(business_name)
        business.date_created = datetime.datetime.utcnow()
        business.save_to_database()
        ## 훨씬 더 정규적인 패턴을 갖게 됨
        ## 정규표현식이나 복잡한 문자열 처리를 신경 쓰지 않아도 되므로 코드의 가독성이 더 좋아짐
        
        ## 함수는 util/ 혹은 현재 위치 중 어느 곳에 놔두는 것이 좋을까?
        ## => 어느 곳에 두어도 상관없음. 필요하면 위치를 언제든지 옮길 수 있음
        ## - 추출되었다는 사실이 더 중요함
        ```
        
5. 기존 인터페이스를 단순화 하기
    - 적은 인수를 받으며, 별다른 설정을 요구하지 않고, 사용하기 편한 인터페이스를 맞추는데 초점을 둬라
        - 누구나 좋아함
        - 이러한 인터페이스는 코드를 우아하게 만듬
        - 간단하고 강력하게 만듬
    - 예시
        
        ```jsx
        // before
        var max_results;
        var cookies = document.cookie.split(";");
        for (var i=0; i < cookies.length; i++){
        	var c = cookies[i];
        	c = c.replace(/^[ ]+/, ""); // 앞에 있는 빈칸을 제거
        	if (c.indexOf("max_results") === 0) {
        		max_results = Number(c.substring(12, c.length));
        	}
        }
        /// 매우 지저분함
        /// cookie를 따로 찾는 함수를 만들어야 할 것으로 보임
        
        // after
        /// 인터페이스 형태 참고
        var max_results = Number(get_cookie("max_results"));
        
        // 쿠기 값을 생성하거나 변경하는 작업
        document.cookie = "max_results=50; expires=Wed, 1 Jan 2020 20:53:47 UTC; path=/";
        /// 수정
        set_cookie(name, vaue, days_to_expire);
        /// 쿠키를 제거하는 작업도 직관에 어긋남 => 쿠기가 만료된 것처럼 억지로 설정해야하기 때문
        /// 다음이 더 나은 인터페이스
        delete_cookie(name);
        
        // * 이상적이지 않은 인터페이스를 그냥 받아들일 이유는 없다는 것 기억하기
        //  - 이런 인터페이스는 언제나 이를 둘러싸는 함수를 작성하여 지저분한 내부를 감출 수 있음
        ```
        
6. 자신의 필요에 맞춰서 인터페이스의 형태를 바꾸기
    - 다른 코드를 지원하려고 존재하는 “접착(glue) 코드”는 프로그램의 실제 논리와 별로 직접적 연관이 없는데, 필요에 따라 따로 분리하여 독자적인 함수를 만들만하다
    - 예시
        
        ```python
        # 상황
        ## 민감한 사용자 정보를 담는 dictionary를 Cipher 클래스로 암호화하여 URL로 구성하려함
        # 문제
        ## Cipher는 딕셔너리가 아니라 바이트로 이루어진 문자열이 입력되길 바란다
        ## 또, Cipher는 바이트로 이루어진 문자열을 반환하지만, URL로 이용할 수 있는 문자열을 필요로 함
        
        # before
        user_info = {"username":"...", "password":"..."}
        user_str = json.dumps(user_info)
        cipher = Cipher("aes_128_abc", key=PRIVATE_KEY, init_vector=INIT_VECTOR,
        								op=ENCODE)
        encrypted_bytes = cipher.update(user_str)
        encrypted_bytes += cipher.final() # 현재의 128 비트 블록을 읽어 들인다
        url = "http://example.com/?user_info=" 
        			+ base64.urlsafe_b64encode(encrypted_bytes)
        
        # after
        def url_safe_encrypt(obj):
        	obj_str = json.dumps(obj)
        	cipher = Cipher("aes_128_abc", key=PRIVATE_KEY, init_vector=INIT_VECTOR,
        									op=ENCODE)
        	encrypted_bytes = cipher.update(obj_str)
        	encrypted_bytes += cipher.final() # 현재의 128 비트 블록을 읽어 들인다
        	return base64.urlsafe_b64encode(encrypted_bytes)
        
        user_info = {"username":"...", "password":"..."}
        url = "http://example.com/?user_info=" + url_safe_encrypt(user_info)
        ```
        
7. 지나치게 추출하기
    - 상관없는 하위문제를 적극적으로 발견하고 추출하는 것을 잊지말자
    - 하지만 너무 흥분해서 지나친 수준으로 나아가는 일도 있으니 조심하자
    - 예시
        
        ```python
        ## 앞의 코드를 다음과 같이 너무 잘게 쪼개면 가독성을 해침
        
        user_info = {"username":"...", "password":"..."}
        url = "http://example.com/?user_info=" + url_safe_encrypt(user_info)
        
        def url_safe_encrypt(obj):
        	obj_str = json.dumps(obj)
        	return url_safe_encrypt_str(obj_str)
        
        def url_safe_encrypt_str(data):
        	encrypted_bytes = encrypt(data)
        	return base64.urlsafe_b64encode(encrypted_bytes)
        
        def encrypt(data):
        	cipher = make_cipher()
        	encrypted_bytes = cipher.update(user_str)
        	encrypted_bytes += cipher.final() # 현재의 128 비트 블록을 읽어 들인다
        	return encrypted_bytes
        	
        def make_cipher():
        	return Cipher("aes_128_abc", key=PRIVATE_KEY, 
        								init_vector=INIT_VECTOR, op=ENCODE)	
        
        ```
        

### 한번에 하나씩

- 한 번에 하나의 작업만 수행하게 코드를 구성해야 이해하기 쉽다
- 이 장에서는 코드를 “탈파편화(defragmenting)”하는 방법을 다룸
- 함수 수준에서 머무르는 것이 아니라, 커다란 함수 안에 있는 코드를 재조직하여 그 안에 여러 개의 독자적인 논리적 영역이 있는 것처럼 만들어야 한다
- 한가지 일만 수행하게 하는 절차
    1. 코드가 수행하는 모든 ‘작업’을 나열한다. 이 ‘작업’ 이라는 단어는 매우 유연하게 사용된다. 이는 “객체가 정상적으로 존재하는지 확인하라”처럼 작은 일일 수도 있고, “트리 안에 있는 모든 노드를 방문하라”처럼 모호한 일일 수도 있다
    2. 이러한 작업을 분리하여 서로 다른 함수로 혹은 적어도 논리적으로 구분되는 영역에 놓을 수 있는 코드로 만들어라
1. 작업은 작을 수 있다
    - 예시
        
        ```jsx
        // 댓글에 추천 반대 의사표시를 할 수 있는 투표 도구 예시
        
        // before
        var vote_changed = function(old_vote, new_vote){ 
        	// 각 투표는 '추천', '반대' 혹은 '' 이다
        	var score = get_score();
        
        	if (new_vote !== old_vote) {
        		if (new_vote === "Up") {
        			score += (old_vote === "Down" ? 2 : 1);			
        		} else if (new_vote === "Down") {
        			score -= (old_vote === "Up" ? 2 : 1);			
        		} else if (new_vote === "") {
        			score += (old_vote === "Up" ? -1 : 1);
        		}
        	}
        	set_score(score);
        };
        /// 코드 길이는 짧지만 많은 일을 수행하기 때문에 미세한 에러, 오자,
        /// 혹은 다른 버그가 숨어있는지 확인하기 어려움
        
        /// 코드는 한가지 일만 수행하는 것 같지만 실제로 한번에 두가지 일을 수행함
        /// 1. old_vote와 new_vote가 수치값으로 '해석' 된다
        /// 2. 점수가 변경된다
        
        // after
        var vote_value = function(vote) {
        	if (vote === "Up") {
        		return 1;
        	}
        	if (vote === "Down") {
        		return -1;
        	}
        	return 0;
        }
        
        var vote_changed = function(old_vote, new_vote) {
        	var score = get_score();
        
        	score -= vote_value(old_vote); // 이전값 제거
        	score += vote_value(new_vote); // 새 값을 더함
        
        	set_score(score);
        }
        ```
        
2. 객체에서 값 추출하기
    - 예시
        
        ```jsx
        // location_info라는 dictionary를 이용하여 "Santa Monica, USA", "Paris, France"
        // 와 같은 포맷을 만드는 함수
        
        // 허나 dictionary 안에 일부 혹은 전체 값이 없는 경우 어떻게 처리해야할까?
        
        // before
        var place = location_info["LocalityName"]; // ex. "Santa Monica"
        if (!place) {
        	place = location_info["SubAdministrativeAreaName"]; // ex. Los Angeles
        }
        if (!place) {
        	place = location_info["AdministrativeAreaName"]; // ex. "California"
        }
        if (!place) {
        	place = "Middle-of-Nowhere"
        }
        
        if (!location_info["CountryName"]) {
        	place += ", " + location_info["CountryName"]; // ex. "USA"
        } else {
        	place += ", Planet Earth";
        }
        
        return place;
        /// 지저분하지만 잘 동작한다
        /// 개선하고 싶은 상황이 있을때는?
        ///   - country 대신 state를 표기하고 싶을 때는?
        ///   => 이러한 기능을 추가하면 더욱 지저분해지게 된다
        /// -------------------------------------------------------
        
        // after
        // ------------------------------------------------------------------
        /// 1.
        /// 사용하기 간편한 변수로 요약
        var town = location_info["LocalityName"]; // ex. "Santa Monica"
        var city = location_info["SubAdministrativeAreaName"]; // ex. Los Angeles
        var state = location_info["AdministrativeAreaName"]; // ex. "California"
        var country = location_info["CountryName"]; // ex. "USA"
        
        /// 반환되는 값의 '두 번째 절반' 이 무엇인지 알아내기
        /// - 기본값에서 부터 시작하라. 그리고 가장 구체적인 값으로 계속 덮어써라
        var second_half = "Planet Earth";
        if (country) {
        	second_half = country;
        }
        if (state && country === "USA") {
        	second_half = state;
        }
        
        /// 이와 비슷한 방법으로 '첫번째 절반 알아내기'
        var first_half = "Middle-of-Nowhere";
        if (state && country !== "USA") {
        	first_half = state;
        }
        if (city) {
        	first_half = city;
        }
        if (town) {
        	first_half = town;
        }
        
        return first_half + ", " + second_half;
        /// 다음의 순서로 탈파편화 된 것을 확인하라
        /// 1. location_info 값 읽기
        /// 2. 도시의 값을 계산하기
        /// 3. 나라의 값을 계산하기
        /// 4. 장소 값을 변경하기
        
        // ---------------------------------------------------------------------
        // 2.
        /// 사실 일부 코드에서는 두가지 작업이 동시에 일어나고 있다
        /// - 변수의 리스트를 하나씩 읽어서, 존재하는 값 중 가장 선호되는 값을 선택
        /// - 나라가 "USA" 인지 아닌지에 따라서 다른 리스트르를 사용함
        
        /// if USA 논리가 곳곳에 섞여있음
        /// a || b || c 문법: 첫번째 참값 리턴
        var first_half, second_half;
        
        if (country === "USA") {
        	first_half = town || citiy || "Middle-of-Nowhere";
        	second_half = state || "USA";
        } else {
        	first_half = town || citiy || state || "Middle-of-Nowhere";
        	second_half = country || "Planet Earth";	
        }
        return first_half + ", " + second_half;
        // ---------------------------------------------------------------------
        ```
        
        ```dart
        // 상황
        // - 웹크롤링 시스템에서 각각의 웹페이지가 내려받아지면 
        //   UpdateCounts()라는 함수가 호출됨
        
        // 우리가 바라는 코드의 모습
        void UpdateCounts(HttpDownload hd) {
        	counts["Exit State"][hd.exit_state()]++;        // ex. "SUCCESS" or "FAILURE"
        	counts["Http Response"][hd.http_response()]++;  // ex. "404 NOT FOUND"
        	counts["Content-Type"][hd.content_type()]++;    // ex. "text/html"
        }
        
        // before
        
        // 실제 로직
        void UpdateCounts(HttpDownload hd) {
        	// 값이 있으면 Exit State 값을 찾는다
        	if (!hd.has_event_log() || !hd.event_log().has_exit_state()) {
        		counts["Exit State"]["unknown"]++;	
        	} else {
        		String state_str = ExitStateTypeName(hd.event_log().exit_state());
        		counts["Exit State"][state_str]++;			
        	}
        
        	// 만약 HTTP 헤더가 아예 없으면, 나머지 요소들읠 위해서 "unknown"을 이용
        	if (!hd.has_http_headers()) {
        		counts["Http Response"]["unknown"]++;
        		counts["Content-Type"]["unknown"]++;
        		return;
        	}
        
        	HttpHeaders headers = hd.http_headers();
        
        	// 값이 있으면 HTTP 응답을 기록하고, 아니면 "unknown"을 기록한다.
        	if (!headers.has_response_code()) {
        		counts["HTTP Response"]["unknown"]++;
        	} else {
        		String code = StringPrintf("%d", headers.response_code());
        		counts["HTTP Response"][code]++;
        	}
        	
        
        	// 값이 있으면 Content-Type 값을 기록하고, 아니면 "unknown"을 기록한다.
        	if (!headers.has_content_type()) {
        		counts["Content-Type"]["unknown"]++;
        	} else {
        		String content_type = ContentTypeMime(headers.content_type());
        		counts["Content-Type"][content_type]++;
        	}
        }
        
        // after
        // 1.
        void UpdateCounts(HttpDownload hd) {
        	// 작업: 읽고자 하는 각각의 값을 위한 기본값을 정의
        	String exit_state = "unknown";
        	String http_response = "unknown";
        	String content_type = "unknown";
        
        	// 작업: HttpDownload에서 각각의 값을 하나씩 읽는다
        	if (hd.has_event_log() && hd.event_log().has_exit_state()) {
        		exit_state = ExitStateTypeName(hd.event_log().exit_state());
        	}
        	if (hd.has_http_headers() && hd.http_headers().has_response_code()) {
        		http_response = StringPrintf("%d", headers.response_code());
        	} 
        	if (hd.has_http_headers() && hd.http_headers().has_content_type()) {
        		content_type = ContentTypeMime(headers.content_type());
        	} 
        
        	// 작업: count[]를 갱신한다
        	counts["Exit State"][exit_state]++;
        	counts["HttpResponse"][http_response]++;
        	counts["Content-Type"][content_type]++;
        }
        
        // 2.
        void UpdateCounts(HttpDownload hd) {
        	counts["Exit State"][ExitState(hd)]++;        // ex. "SUCCESS" or "FAILURE"
        	counts["Http Response"][HttpResponse(hd)]++;  // ex. "404 NOT FOUND"
        	counts["Content-Type"][ContentType(hd)]++;    // ex. "text/html"
        }
        
        String ExitState(HttpDownload hd) {
        	if (hd.has_event_log() && hd.event_log().has_exit_state()) {
        		return ExitStateTypeName(hd.event_log().exit_state());
        	} else {
        		return "unknown";
        	}
        }
        ```
        

### 생각을 코드로 만들기

- “할머니에게 설명할 수 없다면 당신은 제대로 이해한 것이 아닙니다” - Albert Einstein
- 설명할 내용을 걸러서 요지만 뽑아내서 설명한다면, 듣는 사람이 내용을 잘 이해하게 도와줄 뿐만 아니라 설명하는 사람 자신도 그 내용을 다시 한 번 명확하게 이해하게 도와준다 ⇒ 코드 역시 “쉬운 말” 로 작성해야 함
    - 간단하게 만드는 과정
        1. 코드가 할 일을 옆의 동료에게 말하듯이 평범한 영어로 묘사 하라
        2. 이 설명에 들어가는 핵심적인 단어와 문구를 포착 하라
        3. 설명과 부합하는 코드를 작성 하라
1. 논리를 명확하게 설명하기
    - 예시
        
        ```php
        // 보안 페이지 맨윗 부분: 사용자가 페이지를 볼 수 있는지 허가 여부를 확인하고, 
        // 만약 허가되어 있지 않으면 그러한 사실을 설명하는 페이지 반환
        
        $is_admin = is_admin_request();
        if ($document) {
        	if (!is_admin && ($document['username']!=$_SESSION['username'])) {
        		return not_authorized();
        	}
        } else {
        	if (!$is_admin) {
        			return not_authorized();
        	}
        }
        // 계속해서 페이지 렌더링
        ```
        
        - 위의 코드는 상당한 논리가 있어 이해하기 어렵다
        - 논리를 쉬운 말로 묘사하는 것부터 시작해야한다
            - 사용이 허가되는 방법은 두가지 경우
                1. 관리자이다
                2. 만약 문서가 있다면 현재 문서를 소유하고 있다
        - 이를 이용해 단순하게 만들어보자
        
        ```php
        if (is_admin_request()) {
        	// 허가
        } elseif ($document && ($document['username'] == $_SESSION['username'])) {
        	// 허가
        } else {
        	return not_authorized();
        }
        
        // 계속해서 페이지 렌더링 한다
        ```
        
        - 비어 있는 본문 두 개를 포함하므로 조금 이상해 보이지만, 코드 분량이 더 적고, 부정문이 없어 논리도 간단해짐
2. 라이브러리를 알면 도움이 된다
    - 라이브러리를 사용하면 간단하게 만들 수 있으면 사용해도 무방하다
3. 논리를 쉬운 말로 표현하는 방법을 더 큰 문제에 적용하기
    - 큰 문제에 적용해서 코드를 잘게 쪼갤수도 있다
        
        주식 구매 현황을 기록하는 시스템이 있다고 해보자. 이는 주식 목록, 가격, 거래주의 양을 각각 테이블에 따로 저장한다
        
        이를 SQL JOIN 연산처럼 결합하는 프로그램
        
        ```python
        # 조건에 일치하는 행을 찾는 코드
        def PrintStockTransaction():
        	stock_iter = db_read("SELECT time, ticker_symbol FROM ...")
        	price_iter = ...
        	num_shares_iter = ...
        
        	# 3 테이블의 모든 행을 동시에 순차적으로 반복한다
        	while stock_iter and price_iter and number_shares_iter:
        		stock_time = stock_iter.time
        		price_time = price_iter.time
        		number_shares_time = number_shares_iter.time
        		
        		# 만약 세 개의 행이 같은 time을 갖지 않으면 가장 오래된 행은 건너뛴다
        		# 주의: 아래에 있는 '<='은 가장 오래된 행이 2개 있으면 '<'이 될 수 없다
        		if stock_time != price_time or stock_time != num_shares_time:
        			if stock_time <= price_time and stock_time <= num_shares_time:
        			elif price_time <= stock_time and num_shares_time <= price_time:
        			elif num_shares_time <= stock_time and num_shares_time <= price_time:
        			else:
        				continue
        
        		assert stock_time == price_time == num_shares_time
        
        	# 일치된 행 출력
        	print "0", stock_time,
        	print stock_iter.ticker_symbol,
        	print price_iter.price,
        	print num_shares_iter.number_of_shares
        
        	stock_iter.NextRow()
        	price_iter.NextRow()
        	num_shares_iter.NextRow()
        ```
        
        - 코드는 정상적으로 작동하지만 일치하지 않는 행을 건너뛰려고 루프 안에서 많은 일이 일어난다
        - 읽기 쉬운 코드로 바꿔보자
        1. 해결책을 영어로 묘사하기
            - 원래 하려던 일을 쉬운 말로 묘사하는 것부터 시작하자
        
        ```python
        # 세 개 반복자를 병렬적을 동시에 읽는다
        # 어느 행의 time이 일치하지 않으면 하나 더 나아가서 일치하게 한다
        # 일치된 행을 출력하고, 다시 앞으로 나아간다
        # 일치되는 행이 더 이상 없을 때까지 이를 반복한다 << 가장 지저분한 부분
        
        # 지저분 한 부분을 깔끔하게 만들기 위해 새로운 함수로 분리할 수 있다
        def PrintStockTransaction():
        	stock_iter = ...
        	price_iter = ...
        	num_shares_iter = ...
        
        	while True:
        		time = AdvanceToMatchingTime(stock_iter,price_iter,num_shares_iter)
        		if time is None:
        			return
        
        	# 일치된 행 출력
        	print "0", stock_time,
        	print stock_iter.ticker_symbol,
        	print price_iter.price,
        	print num_shares_iter.number_of_shares
        
        	stock_iter.NextRow()
        	price_iter.NextRow()
        	num_shares_iter.NextRow()
        ```
        
        1. 이 방법을 재귀적으로 적용하기
        
        ```python
        # 원래 코드에 있던 지저분한 코드 블록과 같음
        def AdvanceToMatchingTime(stock_iter,price_iter,num_shares_iter):
        	stock_time = stock_iter.time
        	price_time = price_iter.time
        	number_shares_time = number_shares_iter.time
        	
        	# 만약 세 개의 행이 같은 time을 갖지 않으면 가장 오래된 행은 건너뛴다
        	# 주의: 아래에 있는 '<='은 가장 오래된 행이 2개 있으면 '<'이 될 수 없다
        	if stock_time != price_time or stock_time != num_shares_time:
        		if stock_time <= price_time and stock_time <= num_shares_time:
        		elif price_time <= stock_time and num_shares_time <= price_time:
        		elif num_shares_time <= stock_time and num_shares_time <= price_time:
        		else:
        			assert False # 불가능하다
        		continue
        	
        	assert stock_time == price_time == num_shares_time
        	return stock_time
        
        # 각 테이블의 현재 행에서 time을 확인한다. 값이 모두 같으면 작업이 완료된 것이다.
        # 그렇지 않으면 값이 '뒤처진' 행을 한 칸 전진시킨다.
        # 행이 모두 동일한 time을 가질 때까지 혹은 반복자 중의 하나가 끝에 이를 때까지 작업을 반복한다.
        
        ```
        
- 자신의 문제를 설명할 수 없다면, 해당 문제는 무언가 빠져있거나 아니면 제대로 정의되지 않은 것이다

### 코드 분량 줄이기

- 프로그래머가 배워야하는 가장 중요한 기술
    - 언제 코딩을 해야하는지 아는 것
        
        ⇒ 가장 읽기 쉬운 코드는 아무것도 없는 코드이다
        
- 프로그래머는 정말로 필요한 기능이 얼마나 있는지 과대평가하는 경향이 있음
    - YAGNI(You ain’t gonna need it) 철학을 기억하자
- 반대로 필요한 노력을 과소평가 해서도 안된다
    - 장차 코드를 유지보수하고, 문서를 만들고, 코드베이스에 새로운 ‘무게’를 더하는 시간까지 항상 고려하자
- 요구사항에 질문을 던지고 질문을 잘게 나누어 분석하라
    - 디스크에서 객체를 자주 접근해서 불러오는 경우 캐시를 적용할 필요가 있다
    - 이런 경우 LRU(Least Recently Used) 캐시를 적용하여 해결하는 대신, 단순하게 1개 항목만 저장하는 캐시를 구현해도 효과적임
    - “**요구사항 제거하기**” 와 “**더 간단한 문제 해결하기**”가 제공하는 이점을 항상 기억하라
- 코드베이스를 작게 유지하라
    - 코드베이스가 커지면 항상 수정은 어렵고 부담스러운 일이 된다
    - 코드베이스를 최대한 작고 가볍게 유지하는 것을 최선으로 생각하라
    - 해야할 일
        - 일반적인 ‘유틸리티’를 많이 생성하여 중복된 코드를 제거(10장 ‘상관없는 하위문제 추출하기’ 확인)
        - 사용하지 않는 코드 혹은 필요없는 기능 제거
        - 프로젝트가 서로 분절된 하위프로젝트로 구성되게 하라
        - 코드베이스의 ‘무게’를 의식하여 항상 가볍고 날렵하게 유지하라
- 자기 주변에 있는 라이브러리에 친숙해져라
    - 표준 라이브러리로 문제를 풀 수 있는 상황이 매우 많음
    - 한 줄, 한 줄 모두 상당한 분량의 설계, 디버깅, 재작성, 문서화, 최적화, 테스트를 거쳤기 때문에 사용해야 시간도 절약하고, 코드량도 줄일 수 있음
    - **매일 15분씩 표준 라이브러리에 있는 모든 함수/모듈/형들의 이름을 읽어라**
        - 외우는 것이 아니라 안에 무엇이 들어있는지 감을 잡으라는 의미
        - 코드를 직접 작성하는 대신 우선적으로 이미 존재하는 라이브러리를 사용하는 습관을 갖게 하기 때문

## Part 4. 선택된 주제들

### 테스트와 가독성

- 읽거나 유지보수가 쉽게 만들어라
    - 실제 코드와 마찬가지로 테스트 코드는 읽기 쉬워야함
    - 때때로 프로그래머들은 테스트코드가 실제코드가 어떻게 동작해야하는지에 대한 비공식적인 문서라고 생각하기 때문에 동작을 쉽게 이해할 수 있어야 함
    - 왜 테스트 코드가 실패하는지 쉽게 진단 가능해야하고, 새로운 테스트도 쉽게 덧붙일수 있어야 함
- 어떤 점이 잘못되었는가
    - 테스트를 더 쉽게 만들기
    - 덜 중요한 세부사항은 사용자가 볼 필요 없게 숨겨서 더 중요한 내용이 눈에 잘 띄게 해야함
- 목적에 맞는 미니-랭귀지 구현하기
- 읽기 편한 메세지 만들기
- 좋은 테스트 입력값의 선택
- 테스트 함수에 이름 붙이기
- 어떤 점이 잘못되었는가
- 테스트에 친숙한 개발
- 지나친 테스트

### '분/시간 카운터'를 설계하고 구현하기

클래스 인터페이스 정의하기
    - 이름을 개선하기
    - 주석을 개선하기

시도1: 순진한 해결책
시도2:  컨베이어 벨트 설계
시도3: 시간-바구니 설계
3가지 해결책 비교
