# Structure

## Hexagonal perspective
(Center) Domain -> Application -> Infrastructure (Surface)

# Domain Layer
## Value Object
- 도메인 정보 하나를 상징하는 간단한 데이터 형식
- immutable
- ex) color, size, address
## Entity
- 현실의 복잡한 데이터를 상징하는 형식
- 고유 식별자(id)를 포함하여 시간의 흐름에 따라 추적이 가능해야함
- 다른 entity와 관계를 가져 연결할 수 있음
- mutable
- ex) customer, order
## Aggregate
- 논리적으로 서로 연관있는 entity의 모임
- 하나의 root entity를 가진다. root entity는 aggregate 바깥에서 바로 접근할 수 있는 entity
- aggregate 에 대한 변경 사항은 항상 root entity 에 이루어지며, root entity 에 대한 변경 사항은 aggregate 의 다른 모든 entity 로 전파됨
- ex) customer order, product catalog, bank account
## Service
- domain model에 대한 접근을 제공하는 부분
- domain model은 아니니 주의
- domain model에 행위를 수행하기 위해 사용됨
- domain model로 부터 데이터를 합치는데 사용하거나, 바깥으로 일관된 view를 제공하기 위해 사용함
- ex) creating, reading, updating, deleting entity
- domain model 을 시스템의 다른 부분으로부터 분리할 수 있게 도와주는 역할 => domain model을 테스트, 리팩토링 하기 쉬워짐
- 목적에 따라 domain, infrastructure, applcation 어디든 있을 수 있음. 처음에는 domain layer에 놓고 추후 필요하다면 application/infrastructure layer로 이동 시키는 것을 권장
	1. Domain Service: 단일 entity 또는 value object에 자연스럽게 맞지 않는 복잡한 작업이나 행동을 모델링하는 객체. 일반적으로 비즈니스 논리와 도메인 지식을 캡슐화하고, 도메인 객체에 작동.
	2. Application/Infrastructure Service: 도메인 객체와 Usecase를 조합하여 기능을 구현하는 서비스. 요청을 처리하고, 입력을 검증하고, 도메인 서비스를 호출하고, 결과를 반환할 책임이 있음.
## Domain Event
- domain model로 부터 발생하는 event
- 도메인 모델의 변화를 시스템의 다른 부분으로 알리는 역할을 함
- event sourcing 을 구현하기 위해 사용되기도 함
	- event sourcing: domain model의 변화기록을 저장하기 위한 패턴
- 도메인 모델을 일관되게 유지하는 데 도움이 될 수 있음
	- 도메인 모델이 변경되면, 도메인 이벤트가 발생하고, 이 이벤트는 변화에 관심이 있는 시스템의 다른 부분을 업데이트하는 데 사용함

### Event Sourcing
- 객체 변화의 기록을 저장하는 패턴
- 더 유지 가능하고, 더 안전한 애플리케이션을 만들기 위해 DDD에서 사용하는 패턴
- 객체에 대한 각 변경 사항은 이벤트로 표시됨
	- 이벤트는 연대순으로 저장되며, 언제든지 객체의 상태를 재구성하기 위해 재생할 수 있음
 - data loss로 부터 회복하는 것이 쉬움
	 - database가 망가지거나 없어진 경우, 저장된 event를 사용하여 객체 상태를 다시 가져올 수 있음
  - 누가 언제 객체를 변경했는지 추적하기 위해 사용할 수 있음
  - 테스트 환경을 다시 불러올 수 있어서, 제대로 동작하는지 테스트를 하는 것이 더 쉬워짐

## Repository
- 데이터 액세스 계층을 추상화하는 소프트웨어 디자인 패턴
- 애플리케이션을 기본 데이터 저장소와 독립적일 수 있게 만들어주고, 향후 데이터 저장소를 더 쉽게 변경하거나 교체할 수 있게 함
- 일반적으로 데이터를 생성, 읽기, 업데이트 및 삭제하는 method 제공
- 만약 Domain Layer에 넣는다면 다음사항을 주의하라
	- repository는 interface형태로 넣고, implementation은 안된다. domain layer에 영향을 주지 않고 변경할 수 있는 방법이기 때문이다
	- domain layer와 repository를 철저히 분리해라. 그래야 테스트가 가능하다

## Event Publisher
- "entity에 포함" 하는 방법과 "service에 포함" 하는 방법이 있음
- Entity publisher in entity
	- pros
		- 직관적이고 간단함
		- 적용하기 쉬움
		- service 만들 필요가 없음
	- cons
		- 애플리케이션의 다른 부분들은 필요하지 않음에도 event가 발행될 수 있어 비효율적임
		- event가 다른 곳에서 발행되기 때문에 테스트하기 어려울 수 있음
- Entity publisher in service
	- pros
		- event는 애플리케이션의 다른 부분들이 필요할 때만 불리기 때문에 효율적임
		- event가 오직 코드 한 곳에서만 발행되기 때문에 테스트하기 쉬움
	- cons
		- race condition을 피하도록 service를 디자인해야하기 때문에 적용이 어려울 수 있음
		- service가 event를 발행해야하는 모든 entity를 알고 있어야 하기 때문에 복잡함
  # Infrastructure layer
  - 
  # Application layer
  -