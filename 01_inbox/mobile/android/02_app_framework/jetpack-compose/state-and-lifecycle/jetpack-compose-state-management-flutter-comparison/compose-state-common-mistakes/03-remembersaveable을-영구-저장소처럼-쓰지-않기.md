# `rememberSaveable`을 영구 저장소처럼 쓰지 않기

`rememberSaveable`은 UI 복원 장치입니다. sessionKey, auth token, 운동 기록, 측정 이력 같은 데이터는 DataStore나 Room에 저장해야
합니다.
