# Activity Result API는 lifecycle-aware 결과 반환 계약이다

Activity Result API는 다른 Activity나 system UI를 실행하고 typed result를 받는 계약이다. `registerForActivityResult()`는 callback과 `ActivityResultContract`를 등록하고, 반환된 launcher가 실제 실행을 담당한다.

Callback은 process/activity recreation 뒤에도 결과를 받을 수 있어야 하므로 매번 같은 순서로 조건 없이 등록한다. `launch()`는 lifecycle이 `CREATED` 이상일 때 호출하고, 결과 처리에 필요한 추가 상태는 이 API와 별도로 저장/복원해야 한다.

권한 요청, Photo Picker, SAF, 카메라 촬영은 모두 같은 Activity Result boundary를 통과하지만 각각의 permission/storage 의미는 별도 정본에서 판단한다.

공식 문서: [Get a result from an activity](https://developer.android.com/training/basics/intents/result)
