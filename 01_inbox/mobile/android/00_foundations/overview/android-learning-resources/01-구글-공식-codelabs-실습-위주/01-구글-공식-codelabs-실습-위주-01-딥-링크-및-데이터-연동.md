# 딥 링크 및 데이터 연동

| 코드랩 | 매니페스트 관점에서 배우는 내용 |
|:---|:---|
| **앱 링크 및 딥 링크 구현** ([검색: "Android App Links"](https://codelabs.developers.google.com/?product=android)) | `<action>`, `<category>`, `<data>` 태그의 실무 배치, `android:autoVerify` 검증 |
| **웹 - 앱 인증 공유** ([Seamless Credential Sharing](https://codelabs.developers.google.com/seamless-credential-sharing)) | Digital Asset Links(DAL) 설정, 패스키(Passkey) 웹 - 앱 교차 사용 |

##### 🔍 Credential Sharing 코드랩 핵심 요약

이 코드랩은 **"같은 회사의 여러 웹사이트(shopping.com, pay.com)와 Android 앱이 비밀번호/패스키를 공유하도록 묶어주는 기술"**을 다룹니다.

개발자가 세팅해야 하는 것:

1. **웹사이트**: `/.well-known/assetlinks.json` 에 앱과의 공유 선언 JSON 업로드
2. **앱**: `AndroidManifest.xml` 에 웹사이트와의 공유 선언
3. **구글 플레이 콘솔**: Credential Sharing 토글 활성화

>[!IMPORTANT]
>비밀번호 없는 시대(Passwordless)의 핵심 기술인 **패스키(Passkey)**는 기술 표준상 생성 시 지정된 도메인이 아니면 암호학적으로 작동 자체가 불가능합니다. 이 설정 없이는 웹에서 만든 패스키를 앱에서 사용할 수 없습니다.
