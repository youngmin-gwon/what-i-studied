# visionOS Design Patterns #apple #visionos #design

비전OS에서 자주 쓰는 설계 패턴을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 공간 배치 패턴
- 정보 패널: 창(Window)에 텍스트/리스트/버튼을 배치, 주변에 볼륨/3D 미니뷰를 둔다.
- 워크스테이션: 여러 창/볼륨을 사용자 앞/옆에 배치해 멀티태스킹. 거리/각도를 일정하게 유지.
- 몰입 허브: 풀 스페이스에서 사용자 주위를 감싸는 HUD/데이터, 하지만 시야를 가리지 않도록 투명/곡면 활용.

## 상호작용 패턴
- 시선 + 핀치: 기본 선택. 핀치 제스처를 짧게, 타겟을 크게.
- 공중 슬라이더/노브: 손 제스처/시선을 조합해 값 조정. 실물과 유사한 피드백.
- 공간 드래그: 3D 오브젝트를 집어 다른 위치에 놓기. 중력/마찰 등 물리 규칙을 적절히 줄 수 있다.

## 정보 레이어
- 근거리/중거리/원거리 레이어를 나눠 가독성 확보. 텍스트는 너무 멀리 두지 않는다.
- 반투명 카드로 배경과 분리, 그림자/깊이 힌트 제공.
- 알림/토스트는 시야를 가리지 않는 위치에 짧게 표시.

## 이동/전환
- 강제 카메라 이동은 피하고, 순간이동/페이드/확대 축소로 전환.
- 2D→3D 전환 시 사용자가 주의를 잃지 않도록 안내 텍스트/애니메이션 제공.

## 협업/공유
- Shared Space: 여러 사용자가 같은 장면을 볼 때, 아바타/포인터/하이라이트로 위치를 표시.
- 콘텐츠 동기화: 지연을 줄이고, 충돌 정책을 명시.

## 접근성/편안함
- 시선 민감도/손 제스처 민감도 조정 옵션 제공.
- 장시간 사용을 고려해 휴식/자세 가이드를 제안.
- 색상 대비/자막/오디오 설명을 지원.

## 성능/품질
- 오브젝트 수/폴리곤/머티리얼을 제한. 중요하지 않은 오브젝트는 LOD/컬링.
- Foveated 렌더링/멀티레이어로 GPU 예산 관리.
- 패스스루 밝기/명암 대비를 과하게 바꾸지 않는다(눈 피로 방지).

## 테스트 체크
- 다양한 방 크기/조명/배경/착용 자세.
- 시선/손 입력이 잘 인식되지 않는 상황(안경/조명)에 대한 대응.
- 프레임/열/배터리/메모리 모니터링.

## 링크
[apple-visionos-immersion-guide](apple-visionos-immersion-guide.md), [apple-visionos-spatial](../../02_ui_frameworks/apple-visionos-spatial.md), [apple-ui-performance-guide](../../../../../../../apple-ui-performance-guide.md), [apple-accessibility-and-internationalization](../../02_ui_frameworks/apple-accessibility-and-internationalization.md).
