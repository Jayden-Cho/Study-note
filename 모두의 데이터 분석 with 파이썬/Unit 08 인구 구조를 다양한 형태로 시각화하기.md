# Unit 08 인구 구조를 다양한 형태로 시각화하기

>우리 동네 인구 구조 항아리 모양 그래프로 그리기

Unit 07에서 살펴보았던 인구 데이터를 다양한 형태로 시각화하기.

<br>

**원하는 지역의 인구 구조 출력**

~~~python
import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ') # (1)

for row in data:
  if name in row[0]: # (2)
    for i in row[3:] :
      result.append(int(i))
      
plt.style.use('ggplot') # (3)
plt.rc('font', family='AppleGothic') # (4)
plt.title(name+'지역의 인구 구조') 
plt.plot(result)
plt.show()
~~~

![8-1](https://i.imgur.com/aE4PNAk.png)

코드 분석

1. 인구 구조가 궁금한 지역의 이름을 input() 함수로 입력받음.
2. 입력받은 내용이 포함된 값을 찾기.
3. 그래프 스타일 설정.
4. 한글 제목을 넣기 위해 폰트를 애플고딕으로 설정.

<br>

### 막대그래프 그리기

**bar() 함수**

막대그래프를 표현하는 명령어. 막대의 길이는 각 데이터의 크기를 의미.

~~~python
import matplotlib.pyplot as plt
plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7])
plt.show()
~~~

![8-2](https://i.imgur.com/4C2Ew5U.png)

<br>bar() 함수는 두 가지 값이 입력됨.

`bar(막대를 표시할 위치, 막대의 높이)`

<br>

우리 동네 인구 구조를 막대 그래프로 표현.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  if '평안동' in row[0] :
    for i in row[3:] :
      result.append(int(i))
      
plt.bar(range(len(row[3:])), result)
plt.show()
~~~

![8-4](https://i.imgur.com/L5SMtxX.png)

<br>

**barh() 함수**

막대그래프를 수직이 아닌 수평 방향으로 그릴 수도 있음.

- barh()에서 첫 번째 값은 y축의 막대 위치, 두 번째 값은 막대의 너비.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  if '평안동' in row[0]:
    for i in row[3:] :
      result.append(int(i))
      
plt.barh(range(len(row[3:])), result)
plt.show()
~~~

![8-5](https://i.imgur.com/k2qYjX7.png)

<br>

### 항아리 모양 그래프 그리기

성별 정보가 포함된 인구 구조 데이터를 표현하는데 항아리 모양 그래프가 적합.

- 이전과 같이 www.mois.go.kr에서 데이터 다운.

<br>

데이터 훑어보기

- 남성 데이터가 먼저 나오고, 이어서 여성 인구 숫자가 나옴.
  - CX-CZ열에는 남성 데이터, DA-끝까지는 여성 데이터. 

남성, 여성 데이터를 따로 저장하는 법.

1. 남성 데이터는 차례대로, 여성 데이터는 인덱스 -1부터 역순으로 저장.

~~~python
import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []

for row in data:
  if '평안동' in row[0] :
    for i in range(0, 101) :
      m.append(int(row[i+3])
      f.append(int(row[-(i+1)]))               
f.reverse()
~~~

<br>

2. 남성 데이터는 3-103번 인덱스까지 저장, 여성 데이터는 106부터 끝까지 저장.

~~~python
import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []

for row in data:
  if '평안동' in row[0] :
    for i in row[3:104] :
      m.append(int(i))
    for i in row[106:] :
      f.append(int(i))
~~~

<br>

**데이터 시각화하기**

~~~python
import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []

for row in data:
  if '평안동' in row[0]:
    for i in row[3:104] :
      m.append(int(i))
    for i in row[106:] :
      f.append(int(i))
      
plt.barh(range(len(row[3:104])), m)
plt.barh(range(len(row[106:])), f)
plt.show()
~~~

![8-10](https://i.imgur.com/AtbIxBz.png)

그래가 겹쳐서 출력됨. 두 데이터 모두 양수로 이루어져 있기 때문

- 남성 데이터를 왼쪽에 두려면 남성 데이터 모두 음수로 바꾸면 됨.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []

for row in data:
  if '평안동' in row[0]:
    for i in row[3:104] :
      m.append(-int(i))
    for i in row[106:] :
      f.append(int(i))
      
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('평안동 지역의 남녀 성별 인구 분포')
plt.barh(range(len(row[3:104])), m, label='남성')
plt.barh(range(len(row[106:])), f, label='여성')
plt.legend()
plt.show()
~~~

![8-11](https://i.imgur.com/FFVc5Q2.png)

<br>

**우리 동네 인구 구조를 항아리 모양 그래프로 그리기**

~~~python
import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
  if name in row[0] :
    for i in row[3:104] :
      m.append(-int(i))
    for i in row[106:] :
      f.append(int(i))
      
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+'지역의 남녀 성별 인구 분포')
plt.barh(range(len(row[3:104])), m, label='남성')
plt.barh(range(len(row[106:])), f, label='여성')
plt.legend()
plt.show()
~~~

![8-12](https://i.imgur.com/UzXX6v4.png)

**직접 작성한 코드 Ver.01**

- df로 저장까지는 성공했으나 아직 df를 항아리 모양 그래프로 plot() 하는 방법 찾지 못함.

~~~python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('gender.csv', encoding='cp949', index_col=0, thousands=",")

df2 = df[df.index.str.contains('평안동')].astype(int)
m = -df2[df2.columns[2:103]]
fm = df2[df2.columns[105:]]
~~~

