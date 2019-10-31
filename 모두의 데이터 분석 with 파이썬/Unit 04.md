# Unit 04 기본 그래프 그리기 

### matplotlib 라이브러리?

파이썬에서 데이터를 시각화하는데 matplotlib이 주로 많이 사용됨.

- 2D 형태의 그래프, 이미지 등을 그릴 때 사용.



Matplotlib 불러오기

~~~python
import matplotlib.pyplot as plt
~~~

<br>

### 기본 그래프 그리기

**간단한 그래프**

plot() 함수는 직선 또는 꺾은선 형태의 그래프를 그릴 때 사용할 수 있는 명령어.

~~~python
import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40])
plt.show()
~~~

![figure 4-2](https://i.imgur.com/wuckZbv.png)

- plot()에 입력된 리스트의 값이 하나라면 y축 값으로 입력되며, x축 값은 자동으로 0부터 1씩 증가하는 정수로 입력됨.
  - x축 값을 생략할 경우, range(y 축 데이터 개수)로 표현할 수도 있음.



plot()에 리스트가 두 개 들어간다면:

~~~python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
plt.show()
~~~

![figure 4-3](https://i.imgur.com/w5Isy5N.png)

- 첫 번째 리스트가 x축, 두 번째 리스트가 y축.
- x, y축 데이터 개수가 맞지 않는다면:
  - ValueError: x and y must have same first dimension, but have shapes (), and ().

> 별도의 창이 아니라 주피터 노트북 화면 안에서 그래프를 보고 싶다면 다음과 같이 입력.
>
> 일반적으로 위의 코드를 입력하지 않아도 주피터 노트북 안에서 그려짐.
>
> ~~~python
> %matplotlib inline
> ~~~



### 그래프에 옵션 추가하기

제목, 레이블과 같은 기본적인 옵션 추가하기



**그래프에 제목 넣기**

title() 함수로 제목 입력 가능.

~~~python
import matplotlib.pyplot as plt
plt.title('plotting')
plt.plot([10, 20, 30, 40])
plt.show()
~~~

![graph](https://i.imgur.com/oqPRFWk.png)

> 제목은 영어로 넣기. 한글을 지원하는 폰트 설정이 이루어지지 않아 제목에 한글을 넣으면 글자가 깨짐.



**그래프에 범례(legend) 넣기**

보통 두 개 이상의 데이터를 표시할 때 범례 사용.

- 범례를 넣기 위해 plot() 함수에 label을 입력하고, 그래프 그리기 전에 legend() 함수를 실행.

~~~python
import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10, 20, 30, 40], label='asc')
plt.plot([40, 30, 20, 10], label='dec')
plt.legend()
plt.show()
~~~

![graph](https://i.imgur.com/QUiHLnZ.png)

> 범례 위치 직접 지정 가능.
>
> ~~~python
> plt.legend(loc=5)
> ~~~
>
> loc에 들어갈 숫자는 원하는 위치에 따라 0~10까지 넣을 수 있음.
>
> | 2     | 9      | 1        |
> | ----- | ------ | -------- |
> | **6** | **10** | **5, 7** |
> | **3** | **8**  | **4**    |



**그래프 색상 바꾸기**

원하는 색상으로 바꾸려면 color 속성을 추가하면 됨. 속성 선택을 생략하면 자동으로 색상이 설정됨.

~~~python
import matplotlib.pyplot as plt
plt.title('color')
plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
plt.plot([40, 30, 20, 10], color='pink', label='pink')
plt.legend()
plt.show()
~~~

![graph](https://i.imgur.com/ImZlWxw.png)

> 색상을 표현할 때 기본적인 색은 다음과 같은 약자로 표기할 수 있음.
>
> red = r, green = g, blue = b, black = k, yellow = y 



**그래프 선 모양 바꾸기**

그래프의 선 모양(line style)을 바꾸고 싶을 땐 lifestyle 속성에 원하는 선 모양을 지정.

- linestyle 대신 ls라고 작성해도 됨.

~~~python
import matplotlib.pyplot as plt
plt.title('linestyle')
plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
plt.plot([40, 30, 20, 10], color='g', linestyle=':', label='dotted')
plt.legend()
plt.show()
~~~

![graph](https://i.imgur.com/kxLiVDM.png)

> 색과 선 모양을 '<색상><선모양>'을 동시에 적는 형태로 코드를 작성할 수 있음.
>
> ~~~python
> plt.plot([1, 2, 3, 4], 'r--')
> ~~~



**마커 모양 바꾸기**

plot() 함수에 marker 속성을 설정하면 점 형태로 그래프를 그릴 수 있음.

- 색상과 마커 모양을 한번에 설정할 수도 있음.

~~~python
import matplotlib.pyplot as plt
plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.', label='circle')
plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
plt.legend()
plt.show()
~~~

![graph](https://i.imgur.com/udx1oAR.png)

> 색상, 선 모양과 마커 모양을 동시에 설정하고 싶을 땐 '<색상><마커모양><선모양>' 순으로 코드 작성.
>
> ~~~python
> plt.plot([1, 2, 3, 4], 'r.--')
> ~~~

