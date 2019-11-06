# Unit 10 우리 동네 인구 구조를 산점도로 나타내기

파이 차트로는 남녀 성별 비율을 알 수 있고, 항아리 그래프로는 연령별 인구 분포를 알 수 있지만, 정확하게 어떻게 다른지 한눈에 알아보기는 어렵다.

### 꺾은선 그래프로 표현하기

남녀 데이터를 서로 다른 색의 꺾은 선 그래프로 표현하면 연령대별 성별 비율을 쉽게 알 수 있음.

~~~python
import csv

f = open('gender.csv', encoding='cp949')
m, f = [], []
name = input('궁금한 동네를 입력해주세요 : ')

for row in data :
  if name in row[0] :
    for i in range(3, 104) :
      row[i] = row[i].replace(",", "")
      m.append(int(row[i]))
      row[i+103] = row[i+103].replace(",", "")
      f.append(int(row[i+103]))
    break
    
import matplotlib.pyplot as plt

plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()
~~~

![10-3](https://i.imgur.com/4h2lcYl.png)

> 현재 다운로드된 csv 파일에 999를 넘는 숫자를 보면 콤마(,)로 간격이 나눠져있기 때문에 replace() 함수가 필요.
>
> ~~~python
> i = i.replace(",", "")
> ~~~

<br>

중간 블록을 이렇게 표현할 수도 있음.

~~~python
for row in data :
  if name in row[0] :
    for i in range(101) :
      row[i+3] = row[i+3].replace(",", "")
      m.append(int(row[i+3])) # 3~104 구간
      row[i+106] = row[i+106].replace(",", "")
      f.append(int(row[i+106])) # 106~207 구간
    break
~~~

<br>

이렇게도 가능함. 방법은 많으니 다양하게 생각해보고 가장 효율적인 코딩을 할 수 있게 연습하자.

~~~python
for row in data:
  if name in row[0] :
    for i in row[3:104] :
      i = i.replace(",", "")
      m.append(int(i))
    for i in row[106:] :
      i = i.replace(",", "")
      f.append(int(i))
    break
~~~

<br>

### 막대그래프로 표현하기

연령대별 남성 인구에서 여성 인구를 뺀 값을 result라는 리스트에 추가.

~~~python
import csv
import matplotlib.pyplot

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  # 일일히 input() 입력하기 귀찮으니 직접 제주도 적었음.
  if '제주특별자치도' in row[0] :
    for i in range(3, 104):
      row[i] = row[i].replace(",", "")
      row[i+103] = row[i+103].replace(",", "")
      result.append(int(row[i]) - int(row[i+103]))
    break
      
plt.bar(range(101), result)
plt.show()
~~~

![10-4](https://i.imgur.com/AW4gMdy.png)

60대를 기준으로 그보다 나이가 적은 인구는 남성이 많지만, 60대 이상 인구는 여성이 많다는 것이 드러남.

- 같은 데이터라도 다양한 형태로 시각화하면 데이터에 숨겨진 사실을 발견할 수 있음.

<br>

### 산점도로 표현하기

가로축, 세로축을 기준으로 두 요소가 서로 어떤 관계를 맺고 있는지 파악하기 쉽게 나타낸 그래프.

![A](https://i.imgur.com/pUaDYOi.png)

점들은 연령대에 따른 인구를 뜻하고, 오른쪽 컬러바를 참고해 색깔로 나이대를 알 수 있음.

- 대각선으로 그려진 초록색 선은 남성과 여성이 동일한 비율일 때를 의미.
- 남녀 연령대별 인구수를 점의 크기로 나타내는 것도 가능.

'버블 차트'라고도 함.

- 점의 크기를 다르게 버블로 표현하고, 버블들을 겹쳐서 표현할 수도 있음.
- 하나의 그래프 안에 남녀 성비, 연령대별 인구수 등 다양한 정보를 담을 수 있음.

<br>

### scatter() 함수로 표현하기

bar() 함수와 비슷하게 x축, y축에 해당하는 데이터를 각각 넣으면 그에 해당하는 산점도가 그려짐.

~~~python
import matplotlib.pyplot as plt

plt.scatter([10, 20, 30, 40], [10, 30, 20, 40])
plt.show()
~~~

![A](https://i.imgur.com/c6mmZNk.png)

<br>

### 버블 차트로 표현하기

scatter() 함수는 버블 차트 그릴 때도 사용할 수 있음. 기존 코드에 size를 표현하는 s 속성을 추가하고 원하는 크기를 입력.

~~~python
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[100, 200, 250, 300])
plt.show()
~~~

![A](https://i.imgur.com/gyxmDsF.png)

<br>

c라는 속성을 추가하면 각 점의 색상도 정할 수 있음.

~~~python
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[30, 60, 90, 120], c=['red', 'blue', 'green', 'gold'])
plt.show()
~~~

![A](https://i.imgur.com/0nD6AAZ.png)

<br>

colorbar() 함수를 사용하면 그래프 옆에 컬러바 추가할 수 있음.

- scatter() 함수에 c 속성을 추가해 표현하고 싶은 색상의 개수를 설정하면 각 데이터에 해당하는 컬러바의 색으로 정해짐.

~~~python
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[30, 60, 90, 120], c=range(4))
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/sgk05a2.png)

<br>

cmap이라는 컬러맵 속성을 사용하면 컬러바에 사용될 색상의 종류를 정할 수 있음. 여기서는 무지개색과 비슷한 jet 컬러맵 사용.

- https://matplotlib.org/tutorials/colors/colormaps.html 에서 자세한 내용 확인 가능.

~~~python
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[30, 60, 90, 120], c=range(4), cmap='jet')
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/5nl4bw1.png)

<br>

랜덤 함수를 활용해 위치와 크기가 서로 다른 100개의 점들 만들기.

~~~python
import matplotlib.pyplot as plt
import random

x, y, size = [], [], []

for i in range(100) :
  x.append(random.randint(50, 100))
  y.append(random.randint(50, 100))
  size.append(random.randint(10, 100))

plt.scatter(x, y, s=size)
plt.show()
~~~

<br>

![A](https://i.imgur.com/QknZOqX.png)

<br>

컬러바를 넣기. c에 size 리스트를 사용하면 크기에 따라 다른 색을 표현할 수 있음.

~~~python
import matplotlib.pyplot as plt
(생략)

plt.scatter(x, y, s=size, c=size, cmap='jet')
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/6NhhokO.png)

<br>

투명성을 조절해 큰 점에 가려진 작은 점 표현하기.

- alpha 속성값의 범위는 0부터 1.

~~~python
import matplotlib.pyplot as plt
(생략)

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
~~~

![A](https://i.imgur.com/rK8yE7l.png)

> c 속성에 대해 
>
> c 속성은 표현하고 싶은 색상의 수를 의미. c 속성에 다양한 값을 넣어 각 값이 표현하는 그래프를 직접 확인해 적절한 색상 표현 연습하기.
>
> ~~~python
> plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
> ~~~

![A](https://i.imgur.com/RTYJXJm.png)

<br>

### 제주도의 연령대별 성별 비율을 산점도로 표현하기

~~~python
# 남녀 인구 꺾은선 그래프로 표현
import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []

for row in data:
  if '제주특별자치도' in row[0] :
    for i in range(3, 104) :
      row[i] = row[i].replace(",", "")
      m.append(int(row[i]))
      row[i+103] = row[i+103].replace(",", "")
      f.append(int(row[i+103]))
    break

import matplotlib.pyplot as plt
plt.scatter(m, f)
plt.show()
~~~

![A](https://i.imgur.com/wp8AyhN.png)

<br>

여기에 연령에 따른 컬러맵을 적용하고 남성 인구수 중 가장 큰 값으로 y=x 형태의 직선을 그려 어떤 성별의 인구가 더 많은지 한눈에 들어오도록 함.

~~~python
import matplotlib.pyplot as plt

plt.scatter(m, f, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g') # 추세선 추가
plt.show()
~~~

![ㄷ](https://i.imgur.com/51jYQQs.png)

<br>

마지막으로 연령별 남성과 여성 인구수를 합친 값을 size 리스트에 넣어 버블 크기를 표현하면 완성.

- math 라이브러리에 sqrt()를 사용.

<br>

**전체 코드**

~~~python
import csv
import math

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f, size = [], [], []
name = input('궁금한 동네를 입력해주세요 : ')

for row in data:
  if name in row[0]:
    for i in range(3, 104):
      row[i] = row[i].replace(",", "")
      m.append(int(row[i]))
      row[i+103] = row[i+103].replace(",", "")
      f.append(int(row[i+103]))
      size.append(math.sqrt(int(row[i]) + int(row[i+103])))
    break

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rc('font', family='AppleGothic')
plt.figure(figsize=(10, 5), dpi=300)
plt.scatter(m, f, s=size, c=range(101), cmap='jet', alpha=0.5)
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.title(name+' 지역의 성별 인구 그래프')
plt.ylabel('여성 인구수')
plt.xlabel('남성 인구수')
plt.show()
~~~

![A](https://i.imgur.com/pUaDYOi.png)

<br>

제곱근을 사용하지 않으면 이렇게 된다:

![A](https://i.imgur.com/TLkJAIm.png)