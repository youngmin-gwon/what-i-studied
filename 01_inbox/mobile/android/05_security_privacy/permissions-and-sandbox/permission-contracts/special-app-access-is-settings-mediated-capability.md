# Special app access는 일반 runtime permission이 아니라 설정 기반 capability다

Special app access는 일반 runtime permission dialog로 얻는 권한이 아니다. 다른 앱 위에 그리기, 시스템 설정 변경, 모든 파일 접근처럼 위험도가 큰 capability는 별도 설정 화면, 정책 검토, 사용자 확인을 통해 관리된다.

이 권한들은 "요청하면 허용될 수 있는 기능"이 아니라 앱의 제품 요구사항이 정말 해당 capability를 필요로 하는지 먼저 증명해야 하는 영역이다. Play 정책 검토 대상이 될 수 있고, 사용자가 설정에서 언제든 끌 수 있다.

따라서 구현은 fallback을 포함해야 한다. capability가 거부되거나 회수되어도 앱은 핵심 기능을 설명하고 제한된 대안으로 동작해야 한다.
