# 컬러 명명법의 규칙 (Suffixes & Modifiers)

M3에서는 일관된 대비 보장을 위해 컬러 이름 끝에 다음과 같은 접미사/변형 규칙을 적용합니다.

| 이름 형태                   | 설명                                                 | 사용 예시                                |
|:------------------------|:---------------------------------------------------|:-------------------------------------|
| **`{Base}`**            | 컴포넌트의 가장 기본이 되는 핵심 배경/칠(Fill) 색상                   | `Primary`, `Secondary`, `Error`      |
| **`On{Base}`**          | Base 색상 위에 얹어지는 **글자(Text), 아이콘(Icon)** 전용 색상      | `OnPrimary`, `OnSecondary`           |
| **`{Base}Container`**   | Base보다 톤이 낮고 채도가 부드러운 **넓은 면적의 용기(Container)** 배경색 | `PrimaryContainer`, `ErrorContainer` |
| **`On{Base}Container`** | Container 색상 위에 얹어지는 글자 및 아이콘 전용 색상                | `OnPrimaryContainer`                 |

> [!IMPORTANT]
> **접근성(Accessibility) 대비 규칙**
> * `{Base}`와 `On{Base}` 쌍은 스크린 리더 없이 일반 사용자가 글씨를 명확히 읽을 수 있도록 상호간에 **충분한 대비(최소 4.5:1 이상)** 가 나도록
    설계되어 있습니다.
> * `{Base}Container`와 `On{Base}Container` 역시 상호간에 **최소 3:1 이상의 대비**를 만족합니다.

---
