---
title: Domain Driven Design
tags: [architecture, book, code-quality, ddd]
aliases: []
date modified: 2024-12-16 17:02:48 +09:00
date created: 2024-12-16 12:12:56 +09:00
author: Eric Evans
published at: 2003-08-20
type: book
---

## Structure

### Hexagonal perspective

(Center) Domain -> Application -> Infrastructure (Surface)

---
## Layers
### 1. Domain Layer
#### Value Object
- 도메인 정보 하나를 상징하는 간단한 데이터 형식
- immutable
- ex) color, size, address
#### Entity
- 현실의 복잡한 데이터를 상징하는 형식
- 고유 식별자 (id) 를 포함하여 시간의 흐름에 따라 추적이 가능해야함
- 다른 entity 와 관계를 가져 연결할 수 있음
- mutable
- ex) customer, order
#### Aggregate
- 논리적으로 서로 연관있는 entity 의 모임
- 하나의 root entity 를 가진다. root entity 는 aggregate 바깥에서 바로 접근할 수 있는 entity
- aggregate 에 대한 변경 사항은 항상 root entity 에 이루어지며, root entity 에 대한 변경 사항은 aggregate 의 다른 모든 entity 로 전파됨
- ex) customer order, product catalog, bank account
#### Service
- domain model 에 대한 접근을 제공하는 부분
- domain model 은 아니니 주의
- domain model 에 행위를 수행하기 위해 사용됨
- domain model 로 부터 데이터를 합치는데 사용하거나, 바깥으로 일관된 view 를 제공하기 위해 사용함
- ex) creating, reading, updating, deleting entity
- domain model 을 시스템의 다른 부분으로부터 분리할 수 있게 도와주는 역할 => domain model 을 테스트, 리팩토링 하기 쉬워짐
- 목적에 따라 domain, infrastructure, application 어디든 있을 수 있음. 처음에는 domain layer 에 놓고 추후 필요하다면 application/infrastructure layer 로 이동 시키는 것을 권장
	1. Domain Service: 단일 entity 또는 value object 에 자연스럽게 맞지 않는 복잡한 작업이나 행동을 모델링하는 객체. 일반적으로 비즈니스 논리와 도메인 지식을 캡슐화하고, 도메인 객체에 작동.
	 - 많은 usecase 에 걸쳐서 사용되는 경우
	  - ex) shipping cost 를 목적지와 패키지 무게에 따라 계산하는 서비스
	 - 다양한 entity 나 aggregate 사이의 협업이 필요한 서비스의 경우
	  - ex) inventory level, 배송 계획을 확인하여 주문을 완성하고 업데이트 하는 서비스는 많은 entity 간 협업이 필요함
	 - domain 개념과 연결되어 있고 domain model 과 infrastructure component 들과 상호작용해야하는 경우
	  - 확실히 관심사 분리 해주고, 외부 시스템과 통신할 수 있도록 만들어주기도 함
	2. Application Service: 도메인 객체와 Usecase 를 조합하여 기능을 구현하는 서비스. 요청을 처리하고, 입력을 검증하고, 도메인 서비스를 호출하고, 결과를 반환할 책임이 있음.
	 - 특정한 연산이나 usecase 에 구체적이고, domain model 과 넓은 관계를 가지지 않을 때
	  - ex) 주문을 했을 때 고객에게 주문 알람을 보내는 서비스
	 - usecase 와 관계있으나 infrastructure component 와 상호작용이 없는 경우
	  - ex) 사용자 입력을 처리하는 경우
	 - 다양한 usecase 에 사용되고 infrastructure component 와 상호작용이 필요한 경우에는 application layer 에 interface 를 만들고 이를 infrastructure layer 에서 implementation 해야함
	  - ex) 사용자 인증이나 데이터 캐싱
	3. Infrastructure Service
	 - 외부 시스템이나 infrastructure component 와 상호작용해야하는 경우
	  - ex) payment gateway 나 message broker 의 경우
	 - 다양한 usecase 에 사용되고 infrastructure component 와 상호작용이 필요한 경우에는 application layer 에 interface 를 만들고 이를 infrastructure layer 에서 implementation 해야함
	  - ex) 사용자 인증이나 데이터 캐싱
#### Domain Event
- domain model 로 부터 발생하는 event
- 도메인 모델의 변화를 시스템의 다른 부분으로 알리는 역할을 함
- event sourcing 을 구현하기 위해 사용되기도 함
	- event sourcing: domain model 의 변화기록을 저장하기 위한 패턴
- 도메인 모델을 일관되게 유지하는 데 도움이 될 수 있음
	- 도메인 모델이 변경되면, 도메인 이벤트가 발생하고, 이 이벤트는 변화에 관심이 있는 시스템의 다른 부분을 업데이트하는 데 사용함

##### Event Sourcing
- 객체 변화의 기록을 저장하는 패턴
- 더 유지 가능하고, 더 안전한 애플리케이션을 만들기 위해 DDD 에서 사용하는 패턴
- 객체에 대한 각 변경 사항은 이벤트로 표시됨
	- 이벤트는 연대순으로 저장되며, 언제든지 객체의 상태를 재구성하기 위해 재생할 수 있음
 - data loss 로 부터 회복하는 것이 쉬움
	 - database 가 망가지거나 없어진 경우, 저장된 event 를 사용하여 객체 상태를 다시 가져올 수 있음
  - 누가 언제 객체를 변경했는지 추적하기 위해 사용할 수 있음
  - 테스트 환경을 다시 불러올 수 있어서, 제대로 동작하는지 테스트를 하는 것이 더 쉬워짐

#### Repository
- 데이터 액세스 계층을 추상화하는 소프트웨어 디자인 패턴
- 애플리케이션을 기본 데이터 저장소와 독립적일 수 있게 만들어주고, 향후 데이터 저장소를 더 쉽게 변경하거나 교체할 수 있게 함
- 일반적으로 데이터를 생성, 읽기, 업데이트 및 삭제하는 method 제공
- 만약 Domain Layer 에 넣는다면 다음사항을 주의하라
	- repository 는 interface 형태로 넣고, implementation 은 안된다. domain layer 에 영향을 주지 않고 변경할 수 있는 방법이기 때문이다
	- domain layer 와 repository 를 철저히 분리해라. 그래야 테스트가 가능하다

#### Event Publisher
- "entity 에 포함 " 하는 방법과 "service 에 포함 " 하는 방법이 있음
- Entity publisher in entity
	- pros
		- 직관적이고 간단함
		- 적용하기 쉬움
		- service 만들 필요가 없음
	- cons
		- 애플리케이션의 다른 부분들은 필요하지 않음에도 event 가 발행될 수 있어 비효율적임
		- event 가 다른 곳에서 발행되기 때문에 테스트하기 어려울 수 있음
- Entity publisher in service
	- pros
		- event 는 애플리케이션의 다른 부분들이 필요할 때만 불리기 때문에 효율적임
		- event 가 오직 코드 한 곳에서만 발행되기 때문에 테스트하기 쉬움
	- cons
		- race condition 을 피하도록 service 를 디자인해야하기 때문에 적용이 어려울 수 있음
		- service 가 event 를 발행해야하는 모든 entity를 알고 있어야 하기 때문에 복잡함
### 2. Infrastructure layer

### 3. Application layer

### 4. Presentaiton layer

#### View or UI component
- screen, widget, dialog 같은 요소들
#### Presenter or ViewModel
- 화면에 보이는 데이터를 처리하는 business logic 넣는 부분
- domain 객체를 UI 에서 쉽게 사용할 수 있는 형태로 변환함
#### Adapter
- domain 계층이나 외부 시스템으로부터의 데이터를 presentation 계층에서 요구하는 형태로 변경하는 역할
#### Controller
- 사용자 상호 작용의 흐름을 관리하고 화면이나 구성 요소 간의 탐색을 처리
#### Validator
- 사용자 입력을 검증
- 올바른 형식이고, business logic 이나 제약 조건을 충족하는지 확인
---
### Advice from ChatGPT
- presentation layer 로 부터 바로 domain layer 의 repository 를
	- adapter layer 로 부터 repository 부르는것은 괜찮다
 - presentation layer 로 부터 바로 service 를 부르는 것 역시 권장되지 않는다
