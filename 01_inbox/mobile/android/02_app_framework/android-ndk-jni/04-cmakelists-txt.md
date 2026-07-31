# CMakeLists.txt

상위 노트: [[android-ndk-jni]]

```cmake
cmake_minimum_required(VERSION 3.22.1)
project("myapp")

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 소스 파일
add_library(
    native-lib
    SHARED
    native-lib.cpp
    image_processor.cpp
    utils.cpp
)

# 헤더 파일 경로
target_include_directories(native-lib PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Android 라이브러리 찾기
find_library(log-lib log)
find_library(android-lib android)
find_library(jnigraphics-lib jnigraphics)

# 링크
target_link_libraries(
    native-lib
    ${log-lib}
    ${android-lib}
    ${jnigraphics-lib}
)

# 외부 라이브러리 (예: OpenCV)
add_library(opencv SHARED IMPORTED)
set_target_properties(opencv PROPERTIES IMPORTED_LOCATION
    ${CMAKE_SOURCE_DIR}/../jniLibs/${ANDROID_ABI}/libopencv_java4.so)
target_link_libraries(native-lib opencv)
```
