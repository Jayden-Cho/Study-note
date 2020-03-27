# Unit 13 숫자 데이터를 쉽게 다루게 돕는 numpy 라이브러리

### matplotlib 홈페이지

데이터 시각화와 관련된 다양한 예시를 제공.

- 원하는 예시를 클릭하면 해당 그래프를 어떻게 그렸는지 알 수 있는 코드도 함께 제시.

<br>

https://www.matplotlib.org에 접속한 후 tutorials 메뉴 클릭 - 검색 창에 numpy tutorial - 스크롤 내려 Pyplot tutorial 선택.

- numpy 라이브러리를 사용한 경우가 훨씬 적은 수의 코드로 작성해 간결함.

<br>

### numpy 라이브러리 시작하기

**제곱근**

~~~python
import numpy as np
print(np.sqrt(2))
# result: 
# 1.4142135623730951
~~~

<br>

**파이, 삼각함수**

~~~python
print(np.pi) # 3.141592653589793
print(np.sin(0)) # 0.0
print(np.cos(np.pi)) # -1.0
~~~

<br>

**랜덤 함수**

- numpy의 random 서브 라이브러리에 rand()를 실행하면 0~1 사이에 있는 n개의 실수가 랜덤하게 생성됨.

~~~python
# import numpy as np는 생략.
a = np.random.rand(5) # 0~1 사이에 있는 5개의 실수가 랜덤하게 생성.
print(a) # [0.27719068 0.84839229 0.16870041 0.93395037 0.64014575]
print(type(a)) # <class 'numpy.ndarray'>
~~~

numpy.ndarray 타입의 데이터가 생성됨.

- N-Dimensional, 'N-차원'이라는 의미. randint() 함수의 실수 버전.

<br>

**choice() 함수**

~~~python
print(np.random.choice(6, 10))
# result: 
# [1 3 5 2 1 3 0 2 4 3]
~~~

0~5 사이의 숫자를 랜덤하게 10번 선택.

- 한 번 뽑은 숫자를 다시 뽑지 못하게 하고 싶다면 replace 속성을 False로.

~~~python
print(np.random.choice(10, 6, replace=False))
# result:
# [7 4 9 6 0 3]
~~~

확률을 지정할 수 있는 p 속성 추가.

- 각 경우의 수가 발생할 확률을 정할 수 있음. 합이 반드시 1이여야.

~~~python
print(np.random.choice(6, 10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1]))
# result:
# [2 3 1 2 0 3 3 2 3 0]
~~~

<br>

### numpy 라이브러리를 활용해 그래프 그리기

각 숫자가 출력되는 횟수를 쉽게 확인하는 방법 찾기.

- 히스토그램을 그려 각 숫자의 빈도가 한 눈에 들어오도록.
- numpy의 장점을 확인하기 위해 random 라이브러리와 리스트를 사용했던 코드와 비교.

**numpy를 사용한 모드**

~~~Python
import matplotlib.pyplot as plt
import numpy as np

dice = np.random.choice(6, 10)

plt.hist(dice, bins=6)
plt.show()
~~~

**random 라이브러리 활용한 코드**

~~~python
import matplotlib.pyplot as plt
import random

dice = []
for i in range(10):
	dice.append(random.randint(1, 6))

plt.hist(dice, bins=6)
plt.show()
~~~

![A](https://i.imgur.com/j1J5OTv.png)

10번 실행해서 속도가 비슷하지만 100만번으로 바꾸면 numpy 실행 코드가 확실히 빠름.

- p 속성으로 확률을 설정해 결과 확인.

~~~python
dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])

plt.hist(dice, bins=6)
plt.show()
~~~

![A](https://i.imgur.com/vjm6q0I.png)

설정한 확률에 따라 값들이 추출됨을 확인할 수 있음.

<br>

버블 차트를 numpy 라이브러리를 활용해 다시 코딩.

**numpy를 사용한 버블 차트**

~~~python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10, 100, 200) # 10부터 100사이 정수 200개가 랜덤하게 생성.
y = np.random.randint(10, 100, 200)
size = np.random.rand(100) * 100 # 0~100 사이 실수 생성.

plt.scatter(x, y, s=size, c=x, cmap'jet', alpha=0.7)
plt.colorbar()
plt.show()
~~~

> np.random.rand(n): 0~1 사이에 있는 n개의 실수 만드는 함수.
>
> np.random.randint(): a 이상 b 이하인 정수 n개 만드는 함수.

**random 라이브러리를 사용한 코드**

~~~python
import matplotlib.pyplot as plt
import random

x, y, size = [], [], []

for i in range(200):
  x.append(random.randint(10, 100))
  y.append(random.randint(10, 100))
  size.append(random.randint(10, 100))
  
plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/MhAYyPx.png)

> numpy 라이브러리의 다양한 함수를 알아보고 싶다면:
>
> https://docs.scipy.org/doc/numpy-1.13.0/reference/ 에서 Mathematical functions 선택.

<br>

### numpy array 생성하기

리스트와 같은 연속된 데이터는 다음과 같이 numpy array로 변환할 수 있음.

~~~python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a) # [1 2 3 4]
~~~

<br>

인덱싱과 슬라이싱도 가능.

~~~python
a = np.array([1, 2, 3, 4])
print(a[1], a[-1]) # 2 4
print(a[1:]) # [2 3 4]
~~~

<br>

하지만 리스트와는 달리 numpy array에는 한 가지 타입의 데이터만을 저장할 수 있음.

~~~python
a = np.array[1, 2, '3', 4]
print(a) # ['1', '2', '3', '4']
~~~

<br>

zeros(), ones(), eye() 같은 다양한 함수를 사용해 배열을 초기화 할 수 있음.

~~~python
a = np.zeros(10) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
a = np.ones(10) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
a = np.eye(3)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]
~~~

<br>

0과 1이 아닌 연속된 숫자로 데이터를 생성할 땐:

- arange() 함수는 값을 3개까지 입력 가능.

~~~python
# 값이 1개 입력될 경우, 0부터 해당 숫자보다 1만큼 작은 정수까지 저장된 배열 생성.
print(np.arange(3)) # [0 1 2]

# 값이 2개 입력될 경우, 첫 번째 숫자부터 두 번째 숫자보다 1만큼 작은 정수까지 저장된 배열이 생성.
print(np.arange(3, 7)) # [3 4 5 6]

# 값이 3개 입력될 경우, 첫 번째 숫자부터 두 번째 숫자보다 1맠므 작은 정수까지의 범위에서 세 번째 숫자만큼의 간격을 둔 숫자가 저장된 배열이 생성.
print(np.arange(3, 7, 2)) # [3 5]
~~~

<br>

linspace() 함수로도 숫자 생성 가능.

~~~python
a = np.arange(1, 2, 0.1) # 1이상 2미만 구간에서 0.1 간격으로 실수 생성.
b = np.linspace(1, 2, 11) # 1부터 2까지 11개 구간으로 나눈 실수 생성.
print(a)
print(b)
# result:
# [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
# [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ]
~~~

linspace() 함수는 구간의 개수를 지정하고, arange() 함수는 간격을 지정함.

- 쓰임에 차이가 있기에 사용하고자 하는 목적에 맞게 사용하기.
  - 특정 간격에 해당하는 값을 생성하고 싶을 땐 arange().
  - 특정 개수의 구간으로 나눈 값을 생성하고 싶을 땐 linspace().

~~~Python
a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20)
print(a)
print(b)
# result: 
# [-3.14159265 -2.82743339 -2.51327412 -2.19911486 ...  2.82743339]
# [-3.14159265 -2.81089869 -2.48020473 -2.14951076 ...  3.14159265]
~~~

<br>

### numpy array의 다양한 활용

왜 np.twos(), np.threes()는 없을까?

~~~python
import numpy as np
a = np.zeros(10) + 5
print(a)
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
~~~

<br>

함수를 적용할 수도 있음.

~~~python
a = np.linspace(1, 2, 11)
print(np.sqrt(a))
# [1.         1.04880885 1.09544512 1.14017543 ... 1.41421356]
~~~

연산이나 함수를 적용하면 배열의 모든 값이 한꺼번에 계산됨.

<br>

이런 특성을 활용하면 간단한 코드로 그래프를 나타낼 수 있음.

~~~python
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()
~~~

![A](https://i.imgur.com/AjeumnY.png)

<br>

배열 a에 저장된 값을 바탕으로 sin() 함수와 cos() 함수를 표현한 것.

- sin() 함수의 평행이동도 쉽게 구현할 수 있음.

~~~python
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()
~~~

![A](https://i.imgur.com/LzCAWHF.png)

<br>

**마스크 기능**

마스크는 어떤 조건에 부합하는 데이터만 선별적으로 저장하기 위한 기능.

- 마스크에 뚫린 부분과 막힌 부분이 있는 것을 생각하기.

~~~python
a = np.arange(-5, 5)
print(a)
# result: [-5 -4 -3 -2 -1  0  1  2  3  4]
~~~

<br>

numpy에서는 이런 상황을 배열 전체에 조건을 적용할 수 있음.

- 배열에서 조건에 부합하는 데이터는 True, 아니면 False인 마스크가 생성됨.

~~~python
print(a<0)
# result: [ True  True  True  True  True False False False False False]
~~~

<br>

이 마스크를 다시 배열에 적용하면 조건에 부합하는 데이터만 남음.

~~~python
print(a[a<0])
# result: [-5 -4 -3 -2 -1]
~~~

<br>

마스크를 변수에 넣어서 사용할 수도 있음.

~~~python
mask1 = abs(a) > 3 # 원소의 절대값이 3보다 더 크다
print(a[mask1])
# result: [-5 -4 4]
~~~

<br>

몇 개의 마스크를 연결해서 사용할 수도 있음.

~~~python
mask1 = abs(a) > 3
mask2 = abs(a) % 2 == 0
print(a[mask1+mask2]) # 둘 중 하나의 조건이라도 참일 경우
print(a[mask1*mask2]) # 두 가지 존이 모두 참일 경우
# result: 
# [-5 -4 -2  0  2  4]
# [-4  4]
~~~

<br>

**numpy 라이브러리를 사용하여 재미있는 버블차트 그리기**

~~~python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)
size = np.random.rand(100) * 100
mask1 = abs(x) > 50
mask2 = abs(y) > 50
x = x[mask1+mask2]
y = y[mask1+mask2]

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/votjdpe.png)

https://docs.scipy.org/doc/numpy/index.html 에서 자세한 내용 확인 가능.