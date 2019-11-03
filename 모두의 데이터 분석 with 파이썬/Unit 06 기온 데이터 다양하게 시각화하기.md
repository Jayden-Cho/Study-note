# Unit 06 기온 데이터 다양하게 시각화하기

> 데이터에 질문하기
>
> 히스토그램
>
> 기온 데이터를 히스토그램으로 표현하기
>
> 기온 데이터를 상자 그림으로 표현하기

<br>

같은 그림이라도 보는 관점에 따라 다르게 느껴질 수 있듯이, 데이터도 보는 관점에 따라 다르게 해석될 수 있다.

<br>

### 히스토그램

자료의 분포 상태를 직사각형 모양의 막대 그래프로 나타낸 것. 데이터의 빈도에 따라 높이가 결정됨.

- hist() 함수 사용해 히스토그램 그리기.

~~~python
import matplotlib.pyplot as plt
plt.hist([1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
plt.show()
~~~

![6-3](https://i.imgur.com/uGHQBIa.png)

<br>

**주사위 시뮬레이션**

주사위 굴리는 것을 시뮬레이션하기 위해 random 모듈의 randint() 함수 사용.

- randint(a, b)를 실행하면 a 이상 b 이하의 정수 중 하나의 숫자를 무작위로 선택.

~~~python
import random
print(random.randint(1, 6))
# result: 4
~~~

<br>

여러 번 굴리는 상황을 시뮬레이션하기 위해 for 반복문 사용.

~~~python
import random
dice = []
for i in range(5):
  dice.append(random.randint(1, 6))
print(dice)

# result: [2, 4, 6, 1, 6]
~~~

<br>

숫자들이 저장된 dice를 히스토그램으로 표현하기.

- bins 옵션은 가로축 구간 개수를 설정하는 속성.

~~~python
import matplotlib as plt
import random
dice = []
for i in range(5):
  dice.append(random.randint(1, 6))

plt.hist(dice, bins=6)
plt.show()
~~~

![6-5](https://i.imgur.com/tIGuxTc.png)

<br>bins 속성을 사용하지 않는다면 이렇게 출력된다:

![6-5-1](https://i.imgur.com/thC64JW.png)

<br>표본의 수가 적어 분포가 불규칙하다. 100번 굴린 결과를 시뮬레이션 하기.

~~~python
import matplotlib.pyplot as plt
import random
dice = []
for i in range(100):
  dice.append(random.randint(1, 6))
  
plt.hist(dice, bins=6)
plt.show()
~~~

![6-6](https://i.imgur.com/XxcAyNM.png)

<br>시뮬레이션 숫자를 100번으로 늘려도 분포가 불규칙하다. 100만번으로 늘려보자.

~~~python
import matplotlib.pyplot as plt
import random
dice = []
for i in range(1000000):
  dice.append(random.randint(1, 6))
 
plt.hist(dice, bins=6)
plt.show()
~~~

![6-7](https://i.imgur.com/XpgRpQf.png)

> 실험 또는 관찰에 의해 얻은 통계 비율을 '**통계적 확률**'이라하고, 각각의 사건이 일어날 가능성이 모두 같다고 가정해 얻은 통계 비율을 '**수학적 확률**'이라 한다.
>
> 주사위 던지는 횟수를 늘릴수록 특정 숫자가 나오는 횟수가 전체의 1/6에 가까워진다고 예상할 수 있음. 이러한 법칙을 '**큰 수의 법칙**'이라고 함.

<br>

### 기온 데이터를 히스토그램으로 표현하기

1907년부터 현재까지 수집된 서울의 기온 데이터를 히스토그램으로 표현하기.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data= csv.reader(f)
next(data)
result = []

for row in data:
  if row[-1] != '' :
  	result.append(float(row[-1]))
 
plt.hist(result, bins=100, color='r')
plt.show()
~~~

![6-8](https://i.imgur.com/KNEtmu5.png)

<br>

이번엔 8월 데이터만 뽑아서 히스토그램으로 그리기.

~~~python
import csv
import matplotlib.pyplt as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
aug = []

for row in data:
  if row[-1] = '' :
    month = row[0].split(".")[1]
    if month == '8' :
      aug.append(float(row[-1]))
      
plt.hist(aug, bins=100, color='r')
plt.show()
~~~

![6-9](https://i.imgur.com/gJnB1tt.png)

결괏값이 종 모양, 정규 분포표처럼 나타남.

- 역대 8월에는 최고 기온이 30도 정도였던 날이 가장 많고, 그 전후로 분포가 떨어짐.

<br>

**1월과 8월의 데이터를 히스토그램으로 시각화하기**

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data - csv.reader(f)
next(data)
jan, aug = [], []

for row in data:
  month = row[0].split(".")[1]
  if row[-1] != '' :
    if month == '1' :
      jan.append(float(row[-1]))
    elif month == '8' :
      aug.append(float(row[-1]))
      
plt.hist(jan, bins=100, color='b', label='Jan')
plt.hist(aug, bins=100, color='r', label='Aug')
plt.legend()
plt.show()
~~~

![6-10](https://i.imgur.com/tjZazUd.png)

빨간색으로 표현된 8월의 온도는 20~40도 범위에, 파란색으로 표현된 1월의 온도는 -10~10도 범위에 표현된 걸 알 수 있음.

- 같은 데이터에서 어떤 내용을 추출하여, 어떤 방법으로 시각화하느냐에 따라 새로운 정보를 발견할 수 있음.

<br>

### 기온 데이터를 상자 그림으로 표현하기

상자 그림은 가공하지 않은 자료를 그대로 이용하는 것이 아니라, 자료에서 얻어낸 최댓값, 최솟값, 상위 25%, 50%(중앙), 75%에 위치한 값을 보여주는 그래프.

- 데이터의 분포를 한눈에 보기 쉽다는 장점.

<br>

randint() 함수를 사용해 임의의 데이터를 만들고, 그 데이터를 상자 그림으로 나타내기.

~~~python
import matplotlib.pyplot as plt
import random
result = []
for i in range(13):
  result.append(random.randint(1, 1000))
print(sorted(result))

# result: [12, 205, 210, 255, 367, 396,398, 572, 595, 604, 714, 723, 1000]

plt.boplot(result)
plt.show()
~~~

![6-11](https://i.imgur.com/20V1Z6l.png)

> 다른 위치 값이 알고 싶다면:
>
> import numpy as np
>
> 25%값: np.percentile(result, 25)
>
> 50%값: np.percentile(result, 50)
>
> 75%: np.percentile(result, 75)

<br>

서울 최고 기온 데이터를 상자 그림으로 그리기.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
  if row[-1] != '' :
    result.append(float(row[-1]))
    
plt.boxplot(result)
plt.show()
~~~

![6-12](https://i.imgur.com/vLvFkjL.png)

<br>

1월과 8월 상자 그림을 함께 그리기.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
jan, aug = [], []

for row in data:
  month = row[0].split(".")[1]
  if row[-1] != '' :
    if month == '1' :
      jan.append(float(row[-1]))
    elif month == '8' :
      aug.append(float(row[-1]))
      
plt.boxplot(jan)
plt.boxplot(aug)
plt.show()
~~~

![6-13](https://i.imgur.com/qJMENBa.png)

- 그림 위, 아래에 그려진 동그라미는 이상치(outlier) 값을 표현한 것으로, 다른 수치에 비해 너무 크거나 작은 값을 자동으로 나타낸 것.

<br>

1월 최고 기온 데이터와 8월 최고 기온 데이터를 원소로 하는 리스트를 boxplot() 함수로 표현한다면?

~~~python
(생략)
plt.boxplot([aug, jan])
plt.show()
~~~

![6-14](https://i.imgur.com/gjDMX19.png)

<br>

최고 기온 데이터를 월별로 구분해 표현해보기.

~~~python
import matplotlib.pyplot as plt
import csv

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)

month = []
for i in range(12):
  month.append([])
  
for row in data:
  if row[-1] != '' :
    # 월과 같은 번호의 인덱스에 월별 데이터 저장(예: 1월 - month[0])
    # month안에 row[0]...-1으로 넣으면 그냥 month[0]가 아니라 row[0]의 '월'이 들어감.
    month[int(row[0].split(".")[1])-1].append(float(row[-1]))
    
plt.boxplot(month)
plt.show()
~~~

![6-15](https://i.imgur.com/wSyVJDE.png)

코드 분석:

1. 1~12월 데이터를 분류하기 위해 빈 리스트 12개 생성.
2. 날짜에서 추출한 월별 데이터를 정수로 변환한 1~12 사이 숫자에서 1을 뺀값에 월별 데이터를 저장.

<br>

**8월 일별 기온 데이터를 상자 그림으로 표현하기**

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)

day = []
for i in range(31):
  day.append([])
  
for row in data:
  if row[-1] != '' :
    if row[0].split(".")[1] == '8' :
 	   day[int(row[0].split(".")[2])-1].append(float(row[-1]))

plt.style.use('ggplot') # (1) 그래프 스타일 지정
plt.figure(figsize=(10, 5), dpi=300) # (2) 그래프 크기 수정
plt.boxplot(day, showfilers=False) # (3) 아웃라이어 값 생략

plt.show()
~~~

![6-15](https://i.imgur.com/iVICTvH.png)

(1) ***plt.style.use('ggplot')***: 그래프의 스타일을 지정하는 코드. ggplot이라는 스타일로 지정해 배경이 회색의 격자 무늬로 바뀌었고, 2/4 값을 의미하는 선의 색이 바뀜.

(2) ***plt.figure(figsize=(10, 5), dpi=300)***: 그래프의 크기를 (10, 5)로 지정해 박스 크기 수정.

(3) ***showfliers=False***: 이상치 값이 보이지 않게 설정하는 코드.

<br>

**활용: 2018.08월 온도 분석**

~~~python
import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)

day_high, day_low = [], []

for row in data:
    year = row[0].split(".")[0]
    month = row[0].split(".")[1]
    day = row[0].split(".")[2]
    if year == '2018' and month == '8' :
        day_high.append(float(row[-1]))
        day_low.append(float(row[-2]))

temp_change = []
for i in range(0, len(day_high)):
    temp_change.append(day_high[i] - day_low[i])

plt.figure(figsize=(10, 5))
plt.plot(day_high, label='highest temp')
plt.plot(day_low, label='lowest temp')
plt.plot(temp_change, color='y', label='temp change')
plt.title('temperature change on 2018.08 in Seoul')
plt.xlabel('day')
plt.xlim(1, 31)
plt.ylabel('temperature change')
plt.legend()
plt.show()
~~~

![app](https://i.imgur.com/G8a8ZAj.png)