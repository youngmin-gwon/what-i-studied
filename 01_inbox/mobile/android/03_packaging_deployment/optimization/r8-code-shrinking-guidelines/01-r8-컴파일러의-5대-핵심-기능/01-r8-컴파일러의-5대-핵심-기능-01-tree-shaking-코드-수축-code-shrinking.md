# Tree Shaking (코드 수축, Code Shrinking)
* 앱의 진입점(예: `AndroidManifest.xml`에 등록된 Component)을 시작점으로 그래프를 탐색하여 **호출되지 않는 모든 코드, 클래스, 필드, 메서드를 추적해 바이너리에서 삭제**합니다.
* 사용하지 않는 라이브러리/SDK 내부의 불필요한 클래스들이 이때 대거 제거됩니다.
