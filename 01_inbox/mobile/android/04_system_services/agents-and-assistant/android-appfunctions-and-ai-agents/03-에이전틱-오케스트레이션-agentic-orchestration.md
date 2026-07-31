# 에이전틱 오케스트레이션 (Agentic Orchestration)

안드로이드의 에이전트(주로 Gemini Nano)는 사용자의 자연어 명령을 분석하여 필요한 AppFunctions 의 조합을 결정한다.

**예시 시나리오:**

1. **사용자 요청:** "우리 팀원들에게 오늘 오후 5 시에 강남역 근처 카페에서 미팅한다고 메시지 보내줘."
2. **에이전트 판단:**
    - `CalendarApp / find_free_slot` 호출하여 일정 확인.
    - `MapApp / search_poi` (강남역 카페) 호출하여 위치 정보 획득.
    - `MessengerApp / send_group_message` 호출하여 최종 발송.
