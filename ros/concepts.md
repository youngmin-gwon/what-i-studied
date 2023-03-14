## ROS
- Robot Operating System
- OS 아니고 미들웨어에 가까움
- 로봇 개발을 위한 라이브러리
	- 어떤 불편함을 해소해주는가?
	- 제어, 센서, 인식, 메시지 파킹, 개발환경, 패키지관리 등 다양한 라이브 러리와 개발 및 디버깅 도구를 제공하며 소프트웨어 플랫폼이면서 하드웨어에서 사용가능한 운영체제의 기능을 수행
- ROS 구조
![[ros_structure.png]]
- ROS는 Node 라고 하는 작은 프로그램의 집합이며, 각각의 노드끼리 서로 Message를 주고 받고 할 수 있는 구조
- 자체적으로 프로그램 스케쥴링, 자원 관리해줌
- ROS를 사용할 경우 그렇지 않은 경우에 비하여 프로그램 안정성, 스케쥴링, 확장성 등 많은 분야에서 훨씬 편해짐
#### Example: Car Robot
```
① 여러개의 센서로부터 데이터를 수신받는다  
② 받은 데이터를 가공해서 주변 환경과 자차상태을 인지한다  
③ 주변 환경과 자차상태로부터 어떤 행동을 취해야 할지 판단한다  
④ 판단한 내용을 실행(주행)한다
```
#### Example: Car Robot without ROS
```python
def listenSensor(port):
	# Code for listening sensor
	return sensorData
    
def hanleSensorData(sensorData):
	# Code for handle sensor data
	return envData
    
def makeDrivingAlgorithm(carState, envData):
	# Code for determine action
    return controlCmd
    
def controlCar(controlCmd):
	# Code for control car
	return carState
    

if __name__ == "__main__":
	th = thread.Threading(target=listenSensor)
	th.start()

	while True:
    	logic = makeDrivingAlgorithm(carState, envData)
        carState = controlCar(logic)
```
- 문제점
	- 예외 처리 신중하지 않으면 프로그램 전체 멈출 수 있음
	- 싱글 코어를 이용한 연산이기 때문에 스케쥴링 문제 생김
#### Example: Car Robot with ROS
![[ros_structure_with_car_example.png]]
참고링크: [ROS란 무엇인가](https://velog.io/@7cmdehdrb/whatIsROS)
## Master
- ROS를 위한 Name Service?
	- ROS Node 사이 연결, 메시지 통신을 위한 네임 서버
	- 통신 지원
- 마스터가 없으면 ROS Node 간 메시지, 토픽등을 통신할 수 없음
```bash
roscore 
```
## Node
- 실행되는 최소 단위의 프로세스
	- 하나의 프로그램
	- ROS 에서는 하나의 목적에 하나의 노드를 개발 하는 것을 추천함
- 다른 노드와 소통하기 위해 ROS를 사용하는 실행파일
- 노드들은 생성되며 Publisher, Subscriber, Service Server, Service Client에서 사용하는 Topic 및 서비스 이름, 메시지 형태, URI 주소와 포트를 등록하고 이 정보를 기반으로 각 노드는 노드끼리 토픽과 서비스를 이용하여 통신이 가능.
- 노드들이 생성되면 정보를 마스터에 전달하고 이를 통해 통신할 수 있음
## Package
- ROS를 구성하는 기본 단위
	- ROS는 패키지 단위로 개발
- 최소 하나 이상의 노드를 포함하거나 다른 패키지의 노드를 실행하기 위한 설정파일들을 포함
## Message
- 구독/배포(subscribing/publishing)할 때 사용하는 ROS 자료형
## Topic
- 메시지의 이름, 주제
- 노드에서 어떤 메시지를 송신하고 싶으면 토픽으로 마스터에 등록하고 해당 토픽으로 메시지를 보냄
- 수신을 원하는 구독 노드는 마스터에 등록된 토픽의 이름에 해당하는 퍼블리셔 노드의 정보를 받는다
## Publish
- 토픽의 내용에 해당하는 메시지 형태의 데이터를 송신 하는 것. send
## Publisher
- 발행을 수행하기 위해 토픽을 포함한 자신의 정보를 마스터에 등록하고 구독 노드에 메시지를 보냄
- 하나의 노드에서 복수로 선언할 수 있음
- Publisher 생성시 가지는 파라미터(bold는 필수로 들어가야하는 파라미터)
	1. _**name**_ : Publisher가 발행하는 topic 이름
	2. _**data_class**_ : Publisher가 발행할 메시지 타입(클래스)
	3. subscriber_listener
	4. tcp_nodelay
	5. latch
	6. headers
	7. _**queue_size**_ : 큐 자료형 사이즈
 
 기본 제공하는 data class(std_msgs 모듈에서 제공)
 ![[ros_pub_data_class.png]]
 - publisher 선언을 하는 부분은 advertise()를 이용
	 - 마스터가 해당 topic의 메시지를 구독하는 노드에 그 topic으로 발행하는 노드가 있음을 전달
	 - 이후 publisher와 subscriber가 직접 연결
	 - 이후 advertise()는 해당 topic으로 Publisher 클래스를 반환하여 그 객체의 publish()를 이용해 원하는 메시지를 발행
## Subscribe
- 토픽의 내용에 해당하는 메시지 형태의 데이터를 수신하는 것. recv
## Subscriber
- 같은 ROS 네트워크 상에 존재하는 특정 토픽명을 가진 메시지가 발행되는 것을 주시하고, 그 메시지가 발행될 경우 이벤트 리스너를 실행
- 구독을 수행하기 위해 토픽을 포함한 자신의 정보를 마스터에 등록하고, 구독하고자 하는 토픽을 발행하는 퍼블리셔 노드의 정보를 마스터로부터 받음
- 하나의 노드에 복수로 선언할 수 있음
- Subscriber 생성시 가지는 파라미터(bold는 필수로 들어가야하는 파라미터)
	1. _**name**_ : 구독할 topic 이름
	2. _**data_class**_ : 해당 topic의 데이터 타입 
	3. _callback_ : topic이 발행되는 이벤트가 발생하였을 때, 작동할 이벤트 리스너 함수를 콜백 함수 형태로 선언
	4. callback_args
	5. tcp_nodelay
	6. buff_size
	7. _**queue_size**_ : 큐 자료형 사이즈
 
## Service
- ROS에서는 서비스라는 이름으로 메시지 동기 방식을 제공
	- Publisher와 Subscriber의 통신은 비동기 방식으로 이루어짐
	- 잘 동작되지만, 경우에 따라서는 요청과 응답이 동시에 이루어져야하는 동기 방식이 필요할 때도 있음
 - API 부르기 위해 API Specification이라고 이해함
## Action
- 서비스처럼 양방향을 요구하나 요청 처리 후 응답까지 오랜 시간이 걸리고 중간 결과값이 필요한 경우 사용
## rosout
- ROS의 stdout/stderr
## roscore
- Master + rosout + parameter server
- ROS 마스터 구동하는 명령어
## catkin
- build tool
- 이전에 사용하던 rosbuild와 다르게 CMake 표준규약에 가까워 어렵게 느껴질 수 있음
- CMake에 특정 기능이 추가된 툴
## rosrun
- ROS의 기본 실행 명령어
## roslaunch
- rosrun이 하나의 노드를 실행하는 명령어라면 roslaunch는 여러 노드를 실행하는 개념
