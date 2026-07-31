# DAC 의 한계

전통적인 Unix 권한 (UID/GID/permission bits) 은 **DAC(Discretionary Access Control)**다. 파일 소유자가 권한을 결정한다.

문제:

- 루트 권한을 얻으면 모든 제약이 사라진다.
- setuid 바이너리 (예: `su`, `passwd`) 가 뚫리면 공격자도 루트 권한을 얻는다.
