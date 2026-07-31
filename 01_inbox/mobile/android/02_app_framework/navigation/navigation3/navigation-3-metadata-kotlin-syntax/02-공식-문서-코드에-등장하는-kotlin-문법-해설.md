# 공식 문서 코드에 등장하는 Kotlin 문법 해설

## 원자 노트

### 2-1. `Map<String, Any>` — 제네릭(Generics)과 Any 타입
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-01-map-제네릭-generics-과-any-타입](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-01-map-%EC%A0%9C%EB%84%A4%EB%A6%AD-generics-%EA%B3%BC-any-%ED%83%80%EC%9E%85.md)

### 2-2. `object` 선언 — 싱글톤 객체
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-02-object-선언-싱글톤-객체](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-02-object-%EC%84%A0%EC%96%B8-%EC%8B%B1%EA%B8%80%ED%86%A4-%EA%B0%9D%EC%B2%B4.md)

### 2-3. `data object` vs `object`
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-03-data-object-vs-object](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-03-data-object-vs-object.md)

### 2-4. 인터페이스 상속 — `: NavMetadataKey<String>`
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-04-인터페이스-상속-navmetadatakey](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-04-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-%EC%83%81%EC%86%8D-navmetadatakey.md)

### 2-5. 후행 람다(Trailing Lambda) — DSL의 핵심
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-05-후행-람다-trailing-lambda-dsl의-핵심](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-05-%ED%9B%84%ED%96%89-%EB%9E%8C%EB%8B%A4-trailing-lambda-dsl%EC%9D%98-%ED%95%B5%EC%8B%AC.md)

### 2-6. 중위 함수(Infix Function) — `togetherWith`
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-06-중위-함수-infix-function-togetherwith](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-06-%EC%A4%91%EC%9C%84-%ED%95%A8%EC%88%98-infix-function-togetherwith.md)

### 2-7. `when` 표현식과 `is` 패턴 매칭
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-07-when-표현식과-is-패턴-매칭](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-07-when-%ED%91%9C%ED%98%84%EC%8B%9D%EA%B3%BC-is-%ED%8C%A8%ED%84%B4-%EB%A7%A4%EC%B9%AD.md)

### 2-8. 연산자 오버로딩 — `contains`와 `get`
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-08-연산자-오버로딩-contains와-get](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-08-%EC%97%B0%EC%82%B0%EC%9E%90-%EC%98%A4%EB%B2%84%EB%A1%9C%EB%94%A9-contains%EC%99%80-get.md)

### 2-9. 중첩 `object`를 키로 쓰는 이유
- [02-공식-문서-코드에-등장하는-kotlin-문법-해설-09-중첩-object를-키로-쓰는-이유](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4/02-%EA%B3%B5%EC%8B%9D-%EB%AC%B8%EC%84%9C-%EC%BD%94%EB%93%9C%EC%97%90-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-kotlin-%EB%AC%B8%EB%B2%95-%ED%95%B4%EC%84%A4-09-%EC%A4%91%EC%B2%A9-object%EB%A5%BC-%ED%82%A4%EB%A1%9C-%EC%93%B0%EB%8A%94-%EC%9D%B4%EC%9C%A0.md)
