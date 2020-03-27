# Unit 12 지하철 시간대별 데이터 시각화하기

- 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까요?
- 지하철 시간대별로 가장 많은 사람이 승하차 하는 역은 어디일까요?

<br>

### 지하철 시간대별 이용 현황 데이터 정제하기

'지하철 시간대별 이용현황' 데이터 사용.

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)

for row in data:
  print(row)
  
# result: 
# ['사용월', '호선명', '역ID', '지하철역',..., '03:00:00~03:59:59', '']
# ['', '', '', '', '승차', '하차',..., '승차', '하차']
# (생략)
~~~

헤더(header) 데이터가 2개의 행으로 이루어짐.

- 데이터 분석에 영향 없으므로 next() 함수로 제외.
- 4행부터의 str 데이터, map() 함수로 int 변환.

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

for row in data:
  row[4:] = map(int, row[4:])
  
# result:
# ['2019-01', '1호선', '0150', '서울역', 927,..., 7167, 0, 410, 0, 0, 0, 0]
# ['2019-01', '1호선', '0151', '시청', 74, 0, 2409,..., 0, 0, 0, 0]
# (생략)
~~~

> map()
>
> 일괄적으로 데이터에 특정 함수를 적용할 수 있음. 첫 번째 인자에는 일괄 적용할 함수 이름을 입력하고, 두 번째 인자에는 그 함수를 적용할 데이터를 입력.

<br>

### 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까

아침 7시 승차 데이터는 10번 인덱스(11열)에 저장되어 있음.

> 승차 시간 데이터는 교통카드를 찍고 들어오는 시각을 측정한거라 환승 인원을 확인 할 수 없음.

10번 인덱스의 데이터만 추출해 리스트에 저장 후 막대 그래프로 표현.

~~~	python
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

result = []

for row in data:
  row[4:] = map(int, row[4:])
  result.append(row[10])
  
print(len(result)) # 598

plt.bar(range(len(result)), result)
plt.show()
~~~

![A](https://i.imgur.com/t9dlgQO.png)

<br>

데이터 사이 편차가 매우 큼. 데이터를 오름차순으로 정렬 후 다시 그래프 표현.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

result = []

for row in data:
  row[4:] = map(int, row[4:])
  result.append(row[10])
result.sort()

plt.bar(range(len(result)), result)
plt.show()
~~~

![A](https://i.imgur.com/INURqmX.png)

598개의 역 중 85%는 5만 명이 넘지 않음. 이번엔 출근 시간대라고 할 수 있는 7-9시 승차 인원을 모두 합치기.

- 7시 승차 데이터가 10번 인덱스에 있었으므로 10, 12, 14번 인덱스의 값을 합쳐 막대그래프로 표현.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

result = []

for row in data:
  row[4:] = map(int, row[4:])
  result.append(sum(row[10:15:2]))
result.sort()

plt.bar(range(len(result)), result)
plt.show()
~~~

![A](https://i.imgur.com/NeUYQh4.png)

<br>

7-9시 3시간 동안 80만명이 승차하는 지하철 역 찾기.

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''

for row in data:
  row[4:] = map(int, row[4:])
  st = sum(row[10:15:2])
  if mx < st:
    mx = st
    mx_station = row[3] + ' ' + row[1]
print(mx_station, mx)

# result: 
# 신림 2호선 809541
~~~

<br>

반대로 출근 시간 동안 가장 많이 하차하는 역 찾기.

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''

for row in data:
  row[4:] = map(int, row[4:])
  st = sum(row[11:16:2])
  if mx < st:
    mx = st
    mx_station = row[3] + ' ' + row[1]
    
print(mx_station, mx)

# result: 
# 강남 2호선 984427
~~~

예측할 수 있듯이 강남역.

<br>

### 밤 11시에 사람들이 가장 많이 타는 역은 어디일까

분명히 술 마시고 놀다가 막차 직전에 가는 사람들과 

추가 근무로 야근하다 지하철 끊기기 전에 집에 가는 사람들.

<br>

밤 11시 데이터는 몇 번 인덱스에 있을까?

- 승하차 데이터는 4번 인덱스부터 시작하고, 승하차 반복해서 시간당 두개의 열이 존재.
- 데이터는 4시부터 시작하므로 밤 11시(23시)를 구하는 공식은 `2*(i-4)+4`.

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요 : '))

for row in data:
  row[4:] = map(int, row[4:])
  st = sum(row[2*(t-4)+4])
  if st > mx:
    mx = st
    mx_station = row[3] + ' ' + row[1]
print(mx_station, mx)

# result: 
# 강남 2호선 145504
~~~

<br>

### 시간대별로 사람들이 가장 많이 타고 내리는 역은 어디일까

이전 코드가 특정한 시간에 대한 결과를 알려주는 것이었으니까 이번엔 24시간 전체에 대한 계산.

- 시간대별 데이터를 저장할 리스트 24개 생성 - for 반복문 사용.
- range는 0~23까지 반복하니 인덱스에 맞게 공식을 사용해야. i = j*2 + 4

~~~python
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24

for row in data:
  row[4:] = map(int, row[4:])
  for j in range(24):
    st = row[2*j+4]
    if st > mx[j]:
    	mx[j] = a
    	mx_station[j] = row[3]

print(mx_station)
print(mx)

# ['구로', '홍대입구', '신림', '신림', '신림', '신림', '신림', '신림', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '강남', '성신여대입구(돈암)', '신방화']
# [8418, 42966, 80407, 243083, 355172, 211286, 113830, 98765, 126159, 170216, 169097, 203483, 227268, 291623, 431115, 292521, 235489, 295326, 314609, 145504, 27203, 36, 3, 1]
~~~

시간대별 승차 인원이 가장 많은 곳으로 신림역이 6번, 강남역이 14번 출력.

<br>

이 데이터를 바탕으로 막대그래프 그리기.

- x축에는 시간대별 1위 역 이름을 90도 회전해 표현.

**전체 코드**

~~~python
# 시간대별 승차 인원이 많은 역
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24

for row in data:
  row[4:] = map(int, row[4:])
  for j in range(24):
    st = row[2*j+4]
    if st > mx[j]:
      mx[j] = st
      if j > 20: # 시간에 25, 26, 27 출력되는 것을 막기 위해
      	mx_station[j] = row[3] + '('+str(j-20)+'시)'
      else:
        mx_station[j] = row[3] + '('+str(j+4)+'시)'
        
plt.rc('font', family='AppleGothic')
plt.bar(range(len(mx)), mx)
plt.xticks(range(len(mx)), mx_station, rotation=90)
plt.show()
~~~

![A](https://i.imgur.com/m7UW3eO.png)

<br>

~~~python
# 시간대별 하차 인원이 많은 지하철역
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24

for row in data:
  row[4:] = map(int, row[4:])
  for j in range(24):
    st = row[j*2+5]
    if st > mx[j]:
      mx[j] = st
      if j > 20: # 시간에 25, 26, 27 출력되는 것을 막기 위해
      	mx_station[j] = row[3] + '('+str(j-20)+'시)'
      else:
        mx_station[j] = row[3] + '('+str(j+4)+'시)'
       
plt.rc('font', family='AppleGothic')
plt.bar(range(len(mx)), mx, color='b')
plt.xticks(range(len(mx)), mx_station, rotation=90)
plt.show()
~~~

![A](https://i.imgur.com/HIjzmt3.png)

출근 시간에는 강남역이, 오후 시간대는 홍대입구역, 퇴근 시간에는 신림역이 출력됨.

<br>

### 모든 지하철역에서 시간대별 승하차 인원을 모두 더하면

알고리즘을 생각해보자.

1. 데이터 읽어오기.
2. 모든 역에 대해 시간대별(x) 승차 인원과 하차 인원(y)을 누적해 더함.
3. 시간대별 승하차 인원을 그래프로 표현.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

s_in = [0] * 24
s_out = [0] * 24

for row in data:
  row[4:] = map(int, row[4:])
  for j in range(24):
    s_in[j] = row[2*j+4]
    s_out[j] = row[2*j+5]
    
plt.rc('font', family='AppleGothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.plot(range(24), range(4, 28))
plt.show()
~~~

![A](https://i.imgur.com/eDwxqpk.png)