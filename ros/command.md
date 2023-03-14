## rospack
- 패키지 정보 제공하는 도구
```bash
rospack find roscpp
```

## roscd
- rosbash 도구 일부
- 패키지 찾아 폴더 이동
```bash
roscd roscpp
```

```bash
# ROS log 파일 저장 경로로 이동하는 명령
roscd log
```

## rosls
- rosbash 도구 일부
- 패키지 찾아 경로 정보 보여주기
```bash
rosls roscpp_tutorials
```

## catkin_init_workspace
- 작업장소 초기화
- CMakeLists.txt 생성
```bash
catkin_init_workspace
```
## catkin_make
- 패키지 빌드
```bash
catkin_init_workspace
```

## roscore
- ros를 사용할때 가장 먼저 해야하는 일
- ros master를 구동하는 명령어
```
roscore
```

## rosrun
- ROS의 기본 실행 명령어

## roslaunch
- rosrun이 하나의 노드를 실행하는 명령어라면 roslaunch는 여러 노드를 실행하는 개념