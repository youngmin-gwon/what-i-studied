# 07. 텍스트 처리 툴킷(grep/sed/awk/coreutils)

## 시험 포인트
- grep 기본/확장(-E)/Perl(-P) 정규식 차이, 빈출 옵션 `-n -H -r -i -v -o -m`
- sed 스트림 편집: 치환 `s///`, 삭제 `d`, 인플레이스 `-i`, 주소 지정 패턴
- awk 필드 처리: `-F`, `NR`, `NF`, `$0/$1`, BEGIN/END 블록, 내장 함수
- coreutils: `sort`, `uniq`, `cut`, `paste`, `tr`, `wc`, `join`, `comm`, `split`, `xargs`
- 인코딩/개행 주의: `dos2unix`, `LC_ALL=C`로 퍼포먼스/바이트 단위 처리

## grep 요약
- `grep PATTERN file` 기본은 Basic RE. `-E`로 ERE, `-P`는 PCRE(환경따라 미지원).
- 자주 쓰는 패턴: `-r` 재귀, `-n` 라인번호, `-H` 파일명 항상, `-i` 대소문자 무시, `-v` 부정, `-o` 매칭 부분만, `-m1` 첫 매치 후 종료.
- `-F`는 fixed string(패턴 해석 안 함)으로 빠름. `fgrep` 동일.
- 빈출 사례: `grep -R "^export" ~/.bashrc`, `grep -E 'foo|bar' file`, `grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}' log`

## sed 치트
- 구조: `sed -n '1,5p' file`(출력 억제 후 특정 범위만), `sed 's/foo/bar/g'`
- 주소: `1,3`, `$`, `/pattern/`, `,/pattern2/`
- 명령: `p` 출력, `d` 삭제, `s/old/new/g`, `i\ text` 삽입, `a\ text` 추가, `c\ text` 치환
- 인플레이스: `sed -i.bak 's/foo/bar/g' file`(백업 생성). macOS BSD sed는 `-i ''` 필요.
- 예시: 로그 레벨 필터 `sed -n '/ERROR/,$p'`, 주석 제거 `sed '/^#/d;/^$/d' file`

## awk 기본
```bash
awk -F: 'BEGIN { OFS=":" } { print $1, $3 } END { print "lines", NR }' /etc/passwd
```
- 필드 구분자 `-F`, 출력 구분자 `OFS`, 입력 구분자 `RS`(기본 개행)
- 변수: `NR`(행 번호), `NF`(필드 수), `$0` 전체 행
- 조건 {액션} 조합: `$3 > 1000 { print $1 }`, `/regex/ { ... }`
- 내장 함수: `length`, `substr`, `split`, `gsub`, `toupper`, `tolower`, `strftime`, `system`
- 매핑/합계: `sum[$1]+=$2; END{for(k in sum) print k, sum[k]}`

## coreutils 스냅샷
- `cut -d: -f1,3 /etc/passwd` 필드 추출. 탭이 디폴트.
- `sort` 옵션: `-n` 숫자, `-r` 역순, `-k2,2` 키 범위, `-t,` 구분자, `-u` 고유.
- `uniq -c` 카운트(연속 중복만). 중복 제거 전 정렬 필요.
- `tr -d '\r'` CR 제거, `tr '[:lower:]' '[:upper:]'` 대문자 변환.
- `paste -sd,` 한 줄로 합치기, `join` 키 기반 병합, `comm` 정렬된 두 파일 비교.
- `split -l 1000 big.txt part_` 줄 단위 분할, `xargs -0 -n1 cmd` NUL 안전 실행.

## 안전/성능 팁
- `LC_ALL=C`로 바이트 정렬/매칭 → 속도↑, locale 영향 제거
- 긴 파이프라인에서 `grep -F` `grep -E` 선택, 필요 시 `rg`/`ag` 사용
- 큰 파일 tail: `tail -n +1000 file` 1000행부터, `sed -n '1000,$p'` 대체
- `parallel`/`xargs -P`로 병렬 처리 가능 여부 검토

## 5분 실습
1. `/etc/passwd`로 `cut/sort/uniq`를 조합해 쉘 타입 카운트 구하기
2. `printf 'a\r\nb\r\n' | tr -d '\r'`와 `dos2unix` 비교
3. `awk '/ERROR/ {count[$2]++} END{for(k in count) print k, count[k]}' app.log` 실행
4. `find . -type f -print0 | xargs -0 -n1 basename`으로 NUL 안전 리스트 만들기

## 체크리스트
- [ ] OS별 sed -i 차이를 인지하고, 백업 확장자 사용
- [ ] 정규식 맛집: grep 기본/확장/PCRE 구분, `-F`로 성능 개선 가능 여부
- [ ] awk 사용 시 필드 구분자/출력 구분자 명시, NR/NF 활용
- [ ] 파일명 안전성을 위해 NUL-종단 처리 고려
- [ ] 로케일이 결과에 미치는 영향(정렬/대소문자) 점검

## 심화: 정규식/패턴 팁
- **줄 anchors**: `^` 줄 시작, `$` 줄 끝. `grep -x`는 전체 행 매칭.
- **역참조**: `grep -P '(\\w+) \\1'` → 같은 단어 반복 찾기. `-P` 미지원 시 `awk` 사용.
- **멀티라인**: `grep`은 기본 라인 단위. 여러 줄 매칭은 `perl -0777` 또는 `awk`/`sed` 스크립트 필요.
- **인코딩**: `LC_ALL=C`에서 `[:upper:]` 등 클래스는 ASCII 기준. UTF-8이 필요하면 로케일 설정 확인.

## sed 심층 예제
- 줄 번호 부여: `sed = file | sed 'N;s/\\n/ /'`
- n개 줄마다 빈 줄 추가: `sed '0~3G' file`(GNU), BSD는 별도 스크립트 필요.
- 여러 패턴 치환: `sed -e 's/foo/bar/g' -e 's/baz/qux/g'`
- 특정 구간 수정: `sed '/^START/,/^END/s/foo/bar/' file`
- 행 삭제 패턴: `sed '/^#/d;/^$/d'` → 주석+빈 줄 제거 스니펫

## awk 심층 예제
- CSV 안전 파싱은 `awk -F, 'BEGIN{OFS=\",\"} { $1=toupper($1); print }' file` 정도로 단순 처리만. 따옴표 포함 CSV는 전용 파서 필요.
- 그룹별 통계: `awk '{sum[$1]+=$2; cnt[$1]++} END{for(k in sum) printf \"%s %.2f\\n\", k, sum[k]/cnt[k]}' data` → 평균 계산.
- 조건부 필드 변경: `$3 ~ /error/ { $4=\"FAIL\" } {print}` → 패턴 매칭 후 수정.
- 외부 변수 주입: `awk -v threshold=10 '$2>threshold' file`

## coreutils 활용 패턴
- **중복 제거**: `sort file | uniq -c | sort -nr`로 빈도수 상위 추출.
- **컬럼 재조합**: `paste file1 file2 | awk '{print $1\",\"$3}'`
- **대량 치환**: `tr '[:upper:]' '[:lower:]' <file | sed 's/foo/bar/g'`
- **숫자 정렬**: `sort -t, -k2,2nr data.csv | head -n 5`
- **파일 병합**: `join -t, -1 1 -2 1 <(sort -t, -k1,1 a.csv) <(sort -t, -k1,1 b.csv)`

## 연습 문제
1. `grep -E '^[[:alnum:]_]+$'`가 매칭하는 문자열을 설명하라.  
2. macOS sed에서 `sed -i '' 's/a/b/' file`이 필요한 이유를 설명하라.  
3. `awk 'NR==1{next} {sum+=$2} END{print sum}' data`의 동작을 한 줄씩 해설하라.  
4. 공백/개행이 섞인 파일 목록을 안전하게 `xargs`로 넘기는 패턴을 작성하라.  
5. `LC_ALL=C sort`와 기본 locale sort의 차이를 예시와 함께 설명하라.
