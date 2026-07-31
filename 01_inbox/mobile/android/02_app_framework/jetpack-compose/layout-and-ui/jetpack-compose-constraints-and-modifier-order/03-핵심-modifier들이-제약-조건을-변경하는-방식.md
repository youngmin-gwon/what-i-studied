# 핵심 Modifier들이 제약 조건을 변경하는 방식

### 3-1. `Modifier.padding`
* **제약 조건 영향**: 다음 체인으로 전달하는 `Max Width`와 `Max Height` 값을 패딩 크기만큼 줄여서 전달합니다.
* **크기 보고 영향**: 안쪽 요소가 보고한 크기에 자신이 적용한 패딩 크기를 더해 상위 노드로 보고합니다.

### 3-2. `Modifier.size` & `Modifier.fillMaxSize` (크기 제약 조건의 상속과 강제)

이들 크기 수정자는 다음 체인으로 전달하는 `Min/Max Width`와 `Min/Max Height`를 특정 범위 혹은 고정 크기로 강제 변환합니다.

> [!IMPORTANT]
> **크기 강제 변환(Coercion) 규칙**: 
> 모든 크기 관련 수정자는 입력받은 Constraints 범위 내에서 작동하도록 강제(`coerceIn`)됩니다.
> * 예: `width = targetWidth.coerceIn(constraints.minWidth, constraints.maxWidth)`

이 규칙으로 인해 **상위(바깥쪽) 크기 수정자가 하위(안쪽) 크기 수정자의 범위를 강제로 제어**하게 됩니다.

#### 1) `Modifier.fillMaxSize()` 아래에 `Modifier.size(50.dp)`가 오는 경우
1. **`fillMaxSize()`** 는 부모로부터 넘어온 최대 제약 조건(예: `width: 0dp ~ 300dp`)을 받아서 `minWidth = maxWidth = 300dp`로 고정하여 전달합니다. 즉, 최소 크기와 최대 크기를 강제로 일치시킵니다.
2. 그 아래에 있는 **`size(50.dp)`** 는 `50.dp`를 요구하지만, 이미 상위에서 넘어온 제약 조건의 최솟값이 `300.dp`이기 때문에 강제 변환 수식(`50.dp.coerceIn(300.dp, 300.dp)`)에 의해 결국 **`300.dp`** 가 됩니다.
3. **결과**: 안쪽의 `size(50.dp)`는 완전히 무시되고 상위의 `fillMaxSize()` 크기를 따라갑니다.

#### 2) `Modifier.size(100.dp)` 아래에 `Modifier.size(50.dp)`가 오는 경우
1. **`size(100.dp)`** 가 다음 체인으로 넘겨주는 제약 조건은 `min = max = 100.dp`로 고정됩니다.
2. 아래에 있는 **`size(50.dp)`** 는 자신의 크기를 설정하려 하지만, 입력 제약 조건의 최소/최대가 `100.dp`이므로 `50.dp.coerceIn(100.dp, 100.dp)`에 의해 **`100.dp`** 로 결정됩니다.
3. **결과**: 이 경우 역시 하위의 작은 크기가 무시되고 상위의 큰 크기(`100.dp`)를 그대로 유지하게 됩니다.

### 3-3. `Modifier.requiredSize` (강제적 크기 해제)
* **제약 조건 영향**: `size`와 달리 부모가 강제한 Constraints 경계 조건(`min`, `max`)을 완전히 무시하고 지정한 크기를 강제로 밀어붙입니다.
* **사용 용도**: 상위 `size` 또는 `fillMaxSize` 체인을 무시하고 자식 고유의 크기를 확보하고 싶을 때 사용합니다.

### 3-4. `Modifier.wrapContentSize` (제약 조건 최소 범위 초기화)
상위 수정자로부터 물려받은 Constraints의 **최소 너비와 높이를 `0`으로 재설정(초기화)** 하여, 안쪽 컴포저블이 상위 고정 크기보다 작아질 수 있도록 허용합니다.

> [!NOTE]
> * **Constraints 변화**: `minWidth = 0`, `minHeight = 0`으로 변경하고, `maxWidth`와 `maxHeight`는 상위에서 넘어온 값을 그대로 전달합니다.
> * **Layout 변화**: 자식이 자신보다 더 작게 측정되는 것을 허용한 뒤, 남는 여분의 공간(상위 최대 크기 공간) 내에서 지정된 Alignment(기본값은 Center)에 따라 자식의 위치를 배치합니다.

#### 💡 [핵심 예시] `fillMaxSize()` $\rightarrow$ `wrapContentSize()` $\rightarrow$ `size(50.dp)` 순서로 체이닝된 경우
1. **`fillMaxSize()`**: 제약 조건을 `minWidth = maxWidth = 300dp`로 고정하여 전달합니다.
2. **`wrapContentSize()`**: 들어온 제약조건(`300dp ~ 300dp`)에서 최소 제약 조건을 초기화하여 **`minWidth = 0dp`, `maxWidth = 300dp`**로 변경하여 다음 체인에 보냅니다.
3. **`size(50.dp)`**: 입력된 범위 `[0dp, 300dp]` 내에 `50.dp`가 정상적으로 포함되므로, 다음 체인에 **`minWidth = maxWidth = 50dp`**의 제약 조건을 안전하게 전달합니다.
4. **결과**: 최종 컴포저블은 `50.dp` 크기로 정상 측정되며, `wrapContentSize()`의 정렬 동작 덕분에 전체 `300.dp` 크기의 상위 영역 한가운데(Center)에 `50.dp` 크기의 자식이 예쁘게 자리잡게 됩니다.



---
