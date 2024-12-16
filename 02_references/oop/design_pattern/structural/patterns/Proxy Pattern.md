---
aliases: []
date created: 2024-12-12 15:53:12 +09:00
date modified: 2024-12-16 12:20:27 +09:00
tags: [design-pattern, gof, oop, structural-pattern]
title: Proxy Pattern
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2040.png)

![Untitled](../../../../../_assets/oop/Untitled%2041.png)

- 다른 객체에 대한 접근을 제어하기 위한 역할

## Case

### Situation

- 많은 시스템의 리소스를 사용하는 객체가 있으나 언제나 필요한건 아님
- Lazy Loading 으로 구현이 가능하지만, 필요 시점에만 객체를 생성하고, 후에 모든 클라이언트는 해당 객체를 초기화 하는 방법은 코드 중복이 너무 많이 발생하게 됨
- 해당 객체에 직접 주입하는 방법도 있지만, 3rd-party 라이브러리 라면 이 방법 역시 불가능

### Solution

- 프록시 패턴이 원본 서비스를 제공하는 객체와 동일한 인터페이스를 구현하는 새로운 프록시 클래스를 생성하여 이 문제를 해결함
- 클라이언트가 요청을 보내면, 프록시 클래스는 실제 서비스 객체를 만들고, 요청을 위임
- 이렇게 하면 좋은 점?
  - 원본 서비스 클래스의 변경없이 전처리나 후처리 기능을 제공할 수 있음
  - 원본 서비스 객체의 인터페이스를 동일하게 구현하기 때문에 클라이언트 입장에서는 원본 서비스를 사용하는 것과 다를바가 없음

## Examples

- 신용카드는 은행 계좌를 위한 프록시이며, 은행 계좌는 현금을 위한 프록시임
- 둘 다 결제행위를 할 수 있는 같은 인터페이스를 구현하고 있음
- 소비자는 돈을 직접 들고 다니지 않아도 되기 때문에 상당히 편리함
- 가게 주인 역시 보증금을 잃어버릴 위험요소를 감수하지 않아도 되기 때문에 편리함

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2042.png)

1. ServiceInterface
    - Service 와 Proxy 를 위한 인터페이스 정의
2. Service
    - 비즈니스 로직을 포함하고 있는 사용해야할 실제 객체 정의
3. Proxy
    - 실제 서비스와 동일한 인터페이스를 구현
    - 접근을 제어하는 service 객체를 가리키는 참조도 포함해야함
    - 실제 객체를 생성, 삭제 하는데 책임이 있을 수 있음
4. Client
    - 같은 인터페이스를 이용해 Service, Proxy 모두 소통함
    - service 객체를 요구하는 어떤 코드에 proxy 를 할당할 수 있음

## Type

1. Virtual Proxy (lazy initialization)
   - Lazy Loading 개념으로, 요청이 필요한 때만 고비용 객체를 생성함
   - 초기 비용이 많이 드는 연산이 포함된 객체의 경우 가상 프록시를 사용했을 때 효과를 볼 수 있음
2. Protection Proxy (access control)
   - 원격 객체에 대한 실제 접근을 제어함
   - 객체 별로 접근 권한이 다를 때 유용하게 사용 가능
3. Remote Proxy (local execution of remote service)
   - 서로 다른 주소공간에 존재하는 객체를 가리키는 대표 객체
   - 로컬 환경에 위치함
4. Logging Proxy (logging request)
   - 원본 서비스에 접근하는 요청에 대한 기록을 남길 수 있음
5. Caching Proxy (caching request results)
   - 캐시를 보관하는 프록시

## [[Decorator Pattern]] vs [[Proxy Pattern]]

### Commons

- (Proxy 패턴에서 원본에 해당하는) ConcreteComponent 는 (Proxy 패턴에서 프록시에 해당하는) 데코레이터를 통해 호출되는 몇 가지 동작을 구현
- 공통 기본 클래스 (common base class) 로부터 상속

### Differences

- 의도에서 차이가 남
  - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent 의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
  - 프록시는 세부적으로 정의된 하우스키핑 코드 (housekeeping code) 를 원본으로부터 분리하는 역할

## Adaptability

- 초기화 지연 (Lazy Initialization) 가 필요할 때 사용
- 접근 제한 (Access Control) 이 필요할 때 사용
- 원격 서비스 실행 (Remote Service Execution) 이 필요할 때 사용
- 요청 정보를 캐시에 보관 (Caching request result) 할 필요가 있을 때 사용
- 원본 서비스 접근 기록 (Logging Request) 이 필요할 때 사용
- 무거운 객체를 사용 하지 않을 때 자동으로 메모리에서 제거하는 스마트 레퍼런스를 위해 사용

## Pros

- 서비스 개체를 알고 있는 클라이언트 없이 서비스 개체를 제어할 수 있음
- 클라이언트가 신경 쓰지 않아도 서비스 개체의 수명 주기를 관리할 수 있음
- 서비스 개체가 준비되지 않았거나 사용할 수 없는 경우에도 사용할 수 있음
- 새로운 Proxy 를 기존 코드 수정 없이 추가할 수 있음 ⇒ [[../../../solid/OCP(Open Closed Principle)]]

## Cons

- 새로운 클래스를 생성해야 하므로 코드가 복잡해질 수 있음
- 서비스 객체로부터 응답이 늦을 수 있음

## Relationship with other patterns

### [[Adapter Pattern]], [[Decorator Pattern]]

- Adapter 는 감싸진 객체에 다른 인터페이스를 제공
- Proxy 는 감싸진 객체에 같은 인터페이스를 제공
- Decorator 는 감싸진 객체에 증강된 인터페이스를 제공

### [[Facade Pattern]]

- 둘 다 복잡한 엔티티를 버퍼링하고 자체적으로 초기화함
- Proxy 는 서비스 객체와 동일한 인터페이스를 가지고 있어 상호 교환이 가능함

### [[Decorator Pattern]]

#### 1. Commons

- 두 패턴 모두 한 개체가 일부 작업을 다른 개체에 위임해야 하는 구성 원칙을 기반으로 함
- (Proxy 패턴에서 원본에 해당하는) ConcreteComponent 는 (Proxy 패턴에서 Proxy 에 해당하는) Decorator 를 통해 호출되는 몇 가지 동작을 구현
- 공통 기본 클래스 (common base class) 로부터 상속

#### 2. Differences

- 의도에서 차이가 남
  - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent 의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
  - 프록시는 세부적으로 정의된 하우스키핑 코드 (housekeeping code) 를 원본으로부터 분리하는 역할
- Proxy 는 일반적으로 자체적으로 서비스 개체의 수명 주기를 관리
- Decorator 의 구성은 항상 클라이언트에 의해 제어됨
