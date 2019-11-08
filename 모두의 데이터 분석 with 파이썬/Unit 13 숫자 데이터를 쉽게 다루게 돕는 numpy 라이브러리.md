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

- numpy의 random 서브 라이브러리에 rand()를 실행하면 0~1 사이에 있는 nro