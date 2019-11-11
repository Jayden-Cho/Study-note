# Unit 14 numpy를 활용한 나만의 프로젝트 만들기



우리 동네 인구 구조와 가장 비슷한 곳을 찾는 간단한 프로젝트 만들기.

<br>

### 관심 있는 데이터 찾기

공공데이터포털(www.data.go.kr/)을 이용하거나, 인터넷 검색을 통해 데이터 찾기.

- 데이터에 다양한 질문을 던지면서 여러 가지 재미있는 프로젝트 진행.

<br>

### 데이터 살펴보며 질문하기

데이터를 살펴볼 때는 엑셀과 같은 프로그램을 활용해 데이터를 구석구석 살펴보는게 좋음.

- 어떤 내용을 담고 있는지, 또 어떤 내용은 담고 있지 않은지 , 기록된 기간은 언제인지 등 질문을 던지다 보면 재미있는 질문들을 찾을 수 있음.

<br>

### 질문을 명확한 문제로 정의하기

문제를 명확히 정의하면, 현재 갖고있는 데이터로 문제를 해결할 수 있는지를 판단할 수 있고, 문제를 해결하기 위한 알고리즘 설계도 훨씬 수월해짐.

- 질문을 선택할 때는 가장 궁금하면서도 **현재 지식과 능력으로 해결 가능한 것**을 선택.
- 이번 질문의 경우: '우리 동네 인구 구조와 가장 비슷한 지역은 어디일까'에서 '전국에서 신도림동의 연령별 인구 구조와 가장 형태가 비슷한 지역은 어디일까' 라고 다듬었다.

<br>

### 알고리즘 설계하기

알고리즘 설계에 앞서 우리가 해결하려는 문제가 현재 가진 데이터로 해결할 수 있는지 먼저 확인.

문제를 해결하기 위한 절차:

1. 데이터 읽어오기.
2. 궁금한 지역의 이름을 입력.
3. 궁금한 지역의 인구 구조를 저장.
4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾기.
5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화.

> 코드를 구체화하는 과정에서 많은 시행착오가 있을 수 있다. 시행착오를 지속적으로 개선하는 과정도 살펴본다면 데이터 프로젝트를 진행할 때 도움이 될 수 있음.

<br>

### 알고리즘을 코드로 표현하기

각 단계를 코드로 표현하기.

**1. 데이터 읽어오기**

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

for row in data:
  print(row)
~~~

<br>

**2. 궁금한 지역의 이름을 입력**

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')

for row in data:
  print(row)
~~~

<br>

**3. 궁금한 지역의 인구 구조를 저장**

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')
home = []

for row in data:
  if name in row[0]:
    for i in row[3:]:
      home.append(int(i))
      
print(home)
~~~

<br>

Unit 13에서 numpy 배웠으니 사용해보자.

~~~python
import numpy as np
import csv
 
f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')

for row in data:
  if name in row[0]:
    home = np.array(row[3:], dtype=int)
    
print(home)
~~~

<br>

여기까지 잘 작성되었는지 그래프로 표현.

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
plt.title(name+' 지역의 인구 구조')
plt.plot(home)
plt.show()
~~~

![A](https://i.imgur.com/Kt8BHmn.png)

<br>

**4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기**

알고리즘으로 표현하기

1. 전국의 모든 지역 중 한 곳(B)을 선택.
2. 궁금한 지역 A의 0세 인구수에서 B의 0세 인구수를 빼기.
3. 100세 이상 인구수에 해당하는 값까지 반복한 후 각각의 차이를 모두 더함.
4. 전국의 모든 지역에 대해 반복해 그 차이가 가장 작은 지역을 찾기.

![A](https://i.imgur.com/VBd56Dv.png)

신도림동과 강원도 홍천군 화촌면의 연령별 인구를 그래프로 표현한 것.

- 인구수가 다른 지역에서는 연령별 인구수 차이를 구하는 형태로 비교가 어렵다.
- (2)의 알고리즘을 비율로 비교하는 것으로 수정.
  - 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 뺀다.

<br>

아래와 같이 코드를 수정.

~~~python
home = np.array(row[3:], dtype=int) / int(row[2])
~~~

<br>

int(row[2])만 입력하게 된다면 에러가 발생함.

- 3열부터의 모든 값에 콤마(,)를 제외해야 한다.

~~~python
for i in range(2, 104):
  row[i] = row[i].replace(",", "")
home = np.array(row[3:], dtype=int)/int(row[2])
~~~

![A](https://i.imgur.com/4OOyqRS.png)

똑같아 보이지만 y축을 보면 비율로 변해있는걸 알 수 있음.

- 이렇게 비율을 적용해 신도림과 화촌면을 비교해 그래프 그리기.

![A](https://i.imgur.com/vSPym9i.png)

<br>

이제 궁금한 지역과 다른 지역의 연령별 인구 비율을 뺄 차례.

~~~python
import matplotlib.pyplot as plt
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f) # (1)
next(data)

name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')

for row in data: # (2)
  if name in row[0]:
    for i in range(2, 104):
      row[i] = row[i].replace(",", "")
    home = np.array(row[3:], dtype=int) / int(row[2]) # (3)
for row in data: # (4)
  print(row) # (5)
~~~

**아무 것도 출력되지 않음. ????**

- (1) 에서 읽어온 데이터는 (2)를 거쳐 마지막 줄까지 이미 읽혔다.
- 따라서 (3)의 for loop에 들어갈 데이터는 없음.
- 그런데 (4)와 (5)에서 데이터를 읽으려 하니 아무것도 출력되지 않는 것.

데이터를 리스트에 저장해 문제를 해결하기.

~~~python
...
next(data)
data = list(data)
(생략)
~~~

> 이런 알고리즘을 생각할 땐 사소한 문제들이 계속 생김.
>
> 이러한 문제들이 생겼을 때 스스로 고민하는 것도 중요하지만, 구글링을 적절히 활용하는 것도 중요.

<br>

**4-1. 전국의 모든 지역 중 한 곳(B)을 선택 후 A의 0세 인구 비율에서 B의 0세 인구 비율을 빼기**

~~~python
import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)

name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')

for row in data:
  if name in row[0]:
    for i in range(2, 104):
      row[i] = row[i].replace(",", "")
    home = np.array(row[3:], dtype=int) / int(row[2])
for row in data:
  for i in range(2, 104):
    row[i] = row[i].replace(",", "")
    away = np.array(row[3:], dtype=int) / int(row[2])
    print(home-away)
    
# result:
# [ 3.24750299e-03  2.86230589e-03  4.15806641e-03  ... (생략)]
~~~

<br>

**4-2. 100세 이상 인구수에 해당하는 값까지 반복한 후 각가의 차이를 모두 더하기**

간단하게 `np.sum()` 사용.

~~~python
print(np.sum(home-away))

# result: 
# 5.9631119486702744e-18
# 1.2793585635328952e-17
# 1.2576745200831851e-17... (생략)
~~~

<br>

**4-3. 전국의 모든 지역에 대해 반복하여 그 차이가 가장 작은 지역 찾기**

최솟값을 찾는 패턴.

~~~python
import numpy as np
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)

mn = 1
result_name = ''
result = 0
name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요 : ')

for row in data:
  if name in row[0]:
    for i in range(2, 104):
      home = np.array(row[3:], dtype=int)/int(row[2])
for row in data:
  for i in range(2, 104):
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum(home-away)
    if s < mn:
      mn = s
      result_name = row[0]
      result = away
      
~~~

<br>

**5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화하기**

두 개의 그래프를 비교할 목적이므로 가장 기본 그래프인 꺾은선 그래프로 표현.

~~~python
import matplotlib.pyplot as plt

plt.plot(home)
plt.plot(result)
plt.show()
~~~

![A](https://i.imgur.com/m20erZ5.png)

**??????**

두 그래프 전혀 비슷해 보이지 않음. 그래도 어떤 지역인지 출력해보자.

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
plt.title(name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()
~~~

![A](https://i.imgur.com/9vjsw9s.png)

제대로 출력되는 것을 보니 코드의 문제는 아님. 알고리즘의 문제.

- 기존의 알고리즘은 두 지역의 차이가 0에 가장 가까운 지역을 찾은 것.
  - **알고리즘에 음수(-) 값이 선택되어 이상한 결과가 출력됨.**
  - np.sum에 제곱을 해 모두 양수로 전환.

~~~Python
np.sum((home-away)**2)
~~~

![A](https://i.imgur.com/6g6q62K.png)

**...**

자신을 제외하고 찾기.

~~~python
if s < mn and name not in row[0]:
# 전국에 인구 구조가 완전히 똑같은 지역은 없을것이라 가정하면 if 0 < s < mn:이라 작성해도 됨.
~~~

드디어 신도림동과 가장 비슷한 곳을 찾을 수 있다.

![A](https://i.imgur.com/eUOPcfR.png)

<br>

**전체 코드**

~~~python
import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)

mn = 1
result_name = ''
result = 0
name = 

for row in data:
  if name in row[0]:
    for i in range(2, 104):
      home = np.array(row[3:], dtype=int) / int(row[2])
      
for row in data:
  for i in range(2, 104):
    away = np.array(row[3:], dtype=int) / int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0]:
      mn = s
      result_name = row[0]
      result = away
      
plt.rc('font', family='AppleGothic')
plt.figure(figsize=(10, 5))
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.title(name+' 지역과 인구 구조가 가장 비슷한 지역')
plt.legend()
plt.show()
~~~



https://i.imgur.com/OsxzUcA.png