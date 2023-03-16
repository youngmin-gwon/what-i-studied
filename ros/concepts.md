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
## ROS Filesystem
1. Stack: 높은 수준의 라이브러리를 구성하는 패키지의 집합
2. Stack Manifest: 보통 매니페스트 와 동일하지만, 스택을 위한 것
3. Package: ROS 소프트웨어 구성의 가장 기초가 되는 구성. 1) 라이브러리, 2) 도구, 3) 실행파일 등을 포함
4. Manifest: 패키지의 의존 구성을 설명. 패키지 간의 의존 관계를 설명

: Stack 은 Package를 포함
- Stack은 stack.xml 파일 하나 존재
- Package은 manifest.xml 파일 하나 존재

## Master
- ROS를 위한 Name Service
	- 각 노드들을 검색하도록 도움
	- ROS Node 사이 연결, 메시지 통신을 위한 네임 서버
	- 통신 지원
- 마스터가 없으면 ROS Node 간 메시지, 토픽등을 통신할 수 없음
```bash
roscore 
```
## Node
- ROS 패키지의 실행파일
- 실행되는 최소 단위의 프로세스
	- 하나의 프로그램
	- ROS 에서는 하나의 목적에 하나의 노드를 개발 하는 것을 추천함
- 다른 노드와 소통하기 위해 ROS를 사용하는 실행파일
- 노드들은 생성되며 Publisher, Subscriber, Service Server, Service Client에서 사용하는 Topic 및 서비스 이름, 메시지 형태, URI 주소와 포트를 등록하고 이 정보를 기반으로 각 노드는 노드끼리 토픽과 서비스를 이용하여 통신이 가능.
- 노드들이 생성되면 정보를 마스터에 전달하고 이를 통해 통신할 수 있음
## Package
- ROS를 구성하는 기본 단위
	- ROS는 패키지 단위로 개발
- 하나 이상의 노드, 노드 실행을 위한 정보 등을 묶어 놓은 것
## Message
- 노드간 데이터 주고 받을 때 사용하는 것
- 구독/배포(subscribing/publishing)할 때 사용하는 ROS 자료형식
- integer, floating point, boolean와 같은 변수형태
	- list, nested json 가능
 - ROS에서 가장 기본이 되는 기술적 포인트: __노드간 메시지 통신__
 - 메시지 방식 여러가지
	 1. Topic: 단방향, 연속성 데이터 통신
	 2. Service: 양방향, 일회성 데이터 통신
	 3. Action: 양방향, 연속성 데이터 통신
## Topic
- 단방향, 연속성을 갖는 데이터(메시지) 통신 방법 중 하나
- 1:1, 1:N, N:1, N:M 단방향 통신 가능
- 대부분의 경우 통신 방법
- ex) Sensor Data
- 구성: Topic, Publisher, Subscriber
- 계속 프로세스를 처리하기 때문에 네트워크, 자원점유가 높지만 간단하기 때문에 끊기 쉬움
- Topic 통신 프로세스
	1. master 구동: XMLRPC(XML-Remote Procedure Call)
	 - 실행되는 노드 정보 관리
	```bash
	 roscore
	```
	2. subscribe node 구동
	- 실행되자마자 master에게 정보 전달
	 <blockquote>
	/subscribe_node_name<br>
	/topic_name<br>
	message_type<br>
	http://ROS_HOSTNAME:1234<br>
	 </blockquote>
	```bash
	rosrun 패키지이름 노드이름
	```
	3. publish node 구동
	- 실행되자마자 master에게 정보 전달
	 <blockquote>
	/publish_node_name<br>
	/topic_name<br>
	message_type<br>
	http://ROS_HOSTNAME:5678<br>
	 </blockquote>
	```bash
	rosrun 패키지이름 노드이름
	```
	![[ros_topic_1.png]]
	4. publisher 정보 알림
	- master는 subscriber node에게 publisher 정보 알림
	![[ros_topic_2.png]]
	5. publisher node에 접속 요청
	- master로부터 받은 publisher 정보를 이용하여 TCPROS 접속 요청
	![[ros_topic_3.png]]
	6. subscriber node에 접속 응답
	- 접속 응답에 해당되는 자신의 TCP URI 주소와 포트번호를 전송
	![[ros_topic_4.png]]
	7. TCP 접속
	- TCPROS를 이용하여 publisher node와 직접 연결
	- 이전까지 아주 간단한 server-client 모델인 XMLRPC 모델에서 TCPROS 모델로 변경됨
	![[ros_topic_5.png]]
	8. 메시지 전송
	- publisher node는 subscriber node에게 메시지 전송
	![[ros_topic_6.png]]
## Service
- 양방향, 일회성 데이터 통신 방법
- 요청 보내고 응답 받는 방식
	- Publisher와 Subscriber의 통신은 비동기 방식으로 이루어짐
	- 잘 동작되지만, 경우에 따라서는 요청과 응답이 동시에 이루어져야하는 동기 방식이 필요할 때도 있음
 - 구성: Service, Service server, Service client
 - Service 통신 프로세스
	1~7까지 모두 동일
	8. 서비스 요청 및 응답
	 - topic과 달리 1회 한해 접속하고 요청 및 응답 수행한 후에는 서로간의 접속을 끊는다 (1회성)
  
  type:std_msgs/Int16
	![[ros_service_1.png]]
	
## Action
- 양방향, 연속성을 갖는 데이터 통신 방법
	- 중간값을 받을 수 있음
	- 복잡한 일 같이 응답까지 오랜 시간이 걸리고 중간 결과값이 필요한 경우 사용
 - 구성: Action, Action server, Action client
## Parameter
- ROS parameter 서버의 데이터를 저장하거나 조종하는 것을 허용
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
{"op":"advertise","topic":"/interface_manager/topic_name","type":"interface_manager/MsgType", args:{}}