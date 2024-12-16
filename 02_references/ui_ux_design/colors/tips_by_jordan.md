---
title: tips_by_jordan
tags: []
aliases: []
date modified: 2024-12-16 17:24:05 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

## UI Color Palettes

### 색상 카테고리를 먼저 지정하자
#### 1. Brand colors
- 비즈니스에서 사용하는 색상
- UI 전반에서 사용하게 될 색상
- 사이트 전반의 느낌이 어떤지 결정하는 색상
- ex) Facebook's blue
- 사용처
	- button
	- link
	- navigation
	- icon
#### 2. Supporting colors
- 주의를 끌어야 하거나, 사용자에게 색깔로서 무언가를 전달해야하는중요한 UI 공간에 사용할 색상
- brand color 보다 적게 사용됨
	- error message 나 confirmation dialog, informational dialog 같은 부분에서 사용하게 됨
#### 3. Neutrals
- 대부분의 UI 요소를 구성하는 색상
- 사용처
	- text
	- background
	- border
	- secondary button
---
### Steps
#### 0. 디자인 프로그램이 HEX 아닌 HSB 시스템을 사용하게 변경하라
- Hue\[1, 365\] = 색상
- Saturation\[0,100\] = 색상의 강렬함
- Brightness\[0,100\] = 색상에 검은색이 추가된 정도
#### 1. 시작지점을 찾아라
- 모든 색상을 고를 필요 없이 하나의 색상만 선택한 이후, 구조적인 방법으로 색상 팔레트를 넓혀가라
- brand color 먼저 시작하라
	- 가장 중요하고, 가장 바뀔 확률이 적다
	- 좋은 middle color 를 선택하라
		- lighter color 와 darker color 를 선택하기 좋은 색상이어야 한다
		- (과학적 방법은 아니지만) 경험 법칙
			- color picker 에서 오른쪽 상단부에 해당하는 색상
		- 참고하기 좋은 사이트
			- [huemint](https://www.huemint.com)
			- [colorhunt](https://colorhunt.co)
#### 2. Supporting Color 를 지정하라
- 적어도 다음 4 개 색상 정도는 미리 지정하는 것을 추천
	- success message(positive) = green
	- warning message = yellow
	- dangerous message = red
	- neutral message = blue
- brand color 와 잘 어우러지는 것이 중요함
	- `tips`
		- brand color 의 saturation 와 supporting color 의 saturation 과 brightness 을 비슷하게 맞춰주자
			- 아니면 이상하게 보인다
			- 5~10 정도 차이는 괜찮다
#### 3. shades 를 지정하라
- 여태까지 지정한 색상이 UI 전반에 사용될 것이기 때문에 dark, medium, light 보다 더 많은 색상이 필요하다
	- 대략 5~10 개 정도의 shades 를 지정해주자
	- `tips`
		- 9 개의 블럭을 준비하고 각각 100~900 으로 이름 지정하라
		- 500 에 middle color(brand color, supporting color) 를 지정하라
		- color picker 를 열고 왼쪽 상단에서 오른쪽 상단으로 가는 선을 긋는데, 앞에서 지정한 base color 를 지나가는 선을 그어라
		- shade 의 각 색상을 위의 선이 지나가는 라인 위에서 선정하기 시작해라
		- darkest shade 는 saturation 약 \[90,100\], brightness 약 \[20,30\] 의 색상을 고르라
		- lightest shade 는 saturation 약 \[5,10\], brightness 약 \[95,100\] 의 색상을 고르라
		- 각 색상이 어디에 사용될지도 미리 생각하라
			- darkest shade 는 주로 글자에, lightest shade 는 주로 배경에 사용될 것
		- 100, 900 을 고른 이후, 300, 700 을 먼저 골라라
			- 그래프 상에서 base color 와 lightest shade 의 중간지점, base color 와 darkest shade 의 중간지점의 색상을 지정하라
		- 남은 색상 모두 300, 700 색상을 골랐던 것과 같은 방법으로 골라라
#### 4. neutrals 를 지정하라
- `tips`
	- 앞선 단계에서 했던 것처럼, color picker 왼쪽 상단, 오른쪽 하단으로 곡선을 그리는데 이번에는 반대 방향으로 볼록하게 그려라
	- 100~900 까지 똑같은 과정으로 선정하라
#### 5. 색상을 테스트하라
- `tips`
	- 모든 색상 스케일을 세워놓고 색상을 흐리게 한 이후 각각의 스케일이 같은 범위를 갖는지 확인하라
	- 안맞다면 일관성 있도록 shade 색상을 조정하라

### Reference

[Jordan's video](https://www.youtube.com/watch?v=yYwEnLYT55c)

https://github.com/PLAIF-dev/sw_drink_picker/issues/1#issue-1815011762

https://github.com/PLAIF-dev/sw_drink_picker/issues/2#issue-1815013122
