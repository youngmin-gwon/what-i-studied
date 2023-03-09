## Node
- 다른 노드와 소통하기 위해 ROS를 사용하는 실행파일
- 구독/발행을 할 수 있음
## Message
- 구독/배포(subscribing/publishing)할 때 사용하는 ROS 자료형
## Topic
- 구독/배포(subscribing/publishing)할 때 사용하는 ROS 데이터
## Master
- ROS를 위한 Name Service?
- ROS node가 서로 찾을 수 있도록 도움
## rosout
- ROS의 stdout/stderr
## roscore
- Master + rosout + parameter server
## catkin
- build tool
- 이전에 사용하던 rosbuild와 다르게 CMake 표준규약에 가까워 어렵게 느껴질 수 있음
- CMake에 특정 기능이 추가된 툴