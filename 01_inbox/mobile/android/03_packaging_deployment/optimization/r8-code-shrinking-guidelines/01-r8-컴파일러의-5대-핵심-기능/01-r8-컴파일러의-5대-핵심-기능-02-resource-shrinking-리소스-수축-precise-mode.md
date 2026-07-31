# Resource Shrinking (리소스 수축 & Precise Mode)
* `isShrinkResources = true` 옵션과 연동하여, 코드에서 참조되지 않는 `res/` 폴더 내의 미사용 이미지, XML, 레이아웃 리소스를 제거하거나 0바이트 껍데기로 대체합니다.
* 문자열 식별자(`resources.getIdentifier()`)로 동적 참조되는 리소스도 정적 코드 파싱을 거쳐 정밀하게 도려냅니다.
