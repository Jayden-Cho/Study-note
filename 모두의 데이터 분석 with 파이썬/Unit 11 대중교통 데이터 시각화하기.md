# Unit 11 대중교통 데이터 시각화하기

수도권 대중교통 데이터는 국가기관이 아닌 티머니 홈페이지(https://www.t-money.co.kr)에서 제공.

### 지하철 유무임별 이용현황 데이터 정제하기

4개의 탭 중 지하철 유무임별 이용현황 탭을 선택.

- 무임승차는 65세 이상부터 가능.
- 필요 없는 '작업일시' 데이터는 삭제 

> 숫자에 콤마(,)가 되어있을 땐, 엑셀에서 바꾸기 기능(`Ctrl`+`F`) 을 활용해 모두 빈 문자로 바꾸기.
>
> 아니면 전에 했던 것 처럼 파이썬 코드로도 가능한데, 그냥 엑셀 써서 일괄적으로 바꾸자.	
>
> ~~~python
> i = i.replace(",", "")
> ~~~

<br>

헤더가 있으니 next() 함수로 제외하고, 4~7열 데이터는 정수(int)로 바꾸기.

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
~~~

<br>

### 유임 승차 비율이 가장 높은 역은 어디일까

유임 승차 비율을 어떻게 구할까.

- 일단 rate = 유임승차인원 / 무임승차인원 으로.

알고리즘은 이렇게.

1. 데이터를 읽어오기.
2. 모든 역의 데이터로 각 역의 비율을 계산.
3. 비율이 가장 높은 역을 찾기.
4. 비율이 가장 높은 역은 어디인지, 그 비율이 얼마인지 출력.

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx, rate = 0, 0

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
  rate = row[4] / row[6]
  if rate > mx:
    mx = rate
print(mx)
# result: 
# ZeroDivisionError: division by zero
~~~

> 팁
>
> rate 변수 초깃값을 넣지 않아도 에러는 발생하지 않지만, 변수 선언하고 초기화하는 습관을 들이면 다른 언어를 배울 때 어려움 줄일 수 있음. 계속 변수 선언하자.

row[6] 값들중 하나가 0이 있어 발생한 에러.

- row[6]에 대한 예외 처리(0이 아닌 경우)를 간단히 하고 다시 작성.

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx, rate = 0, 0

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
  if row[6] != 0:
    rate = row[4] / row[6]
    if rate > mx:
      mx = rate
      print(row, round(rate, 2))
# result
# ['2019-01', '1호선', '0150', '서울역', 1516452, 1400464, 221180, 211764] 6.86
# ['2019-01', '1호선', '0152', '종각', 1240810, 1177643, 162410, 152062] 7.64
# (생략)
# ['2019-01', '3호선', '0321', '충무로', 55, 0, 2, 0] 27.5
~~~

충무로역 데이터를 보면, 유임하차, 무임하차 둘다 없었다는 결과가 출력되는데 이상.

- 아마 환승이 가능한 역은 데이터를 취합하는 방식이 다른 듯.

<br>

취합하는 방식을 모르므로 rate 계산법을 바꾸기.

- rate = 유임 승차 인원 / 전체(무임+유임) 인원
- 전체 인원이 100,000명 이상인 경우만 찾아 이상값에 대비.

~~~python
import csv

f = open('subwayfee.csv')


for row in data:
  for i in range(4, 8): 
    row[i] = int(row[i])
  if row[6]!=0 and (row[4]+row[6]) > 100000:
    rate = row[4] / (row[4]+row[6])
    if rate > mx:
      mx = rate
      print(row, round(rate, 2))
# result:
# ['2019-01', '1호선', '0150', '서울역', 1516452, 1400464, 221180, 211764] 0.87
# ['2019-01', '1호선', '0152', '종각', 1240810, 1177643, 162410, 152062] 0.88
# (생략)
# ['2019-01', '2호선', '0239', '홍대입구', 2351935, 2507561, 114832, 111488] 0.95
~~~

보통 유동인구가 많다고 생각되는 곳이 출력됨.

- 하지만 작성된 코드 자체가 max 값을 출력해 나가는 과정을 보여줘 중간에 생략된 값들이 존재.

if 조건문을 수정하면 다른 결과가 나온다.

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx, rate = 0, 0

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
  if row[6]!=0 and (row[4]+row[6]) > 100000:
    rate = row[4] / (row[4]+row[6])
    if rate > 0.94:
      print(row, round(rate, 2))
        
# result: 
# ['2019-01', '2호선', '0222', '강남', 3153418, 3210437, 186486, 167666] 0.94
# ['2019-01', '2호선', '0239', '홍대입구', 2351935, 2507561, 114832, 111488] 
# (생략)
# ['2019-01', '공항철도 1호선', '4210', '청라국제도시', 174320, 164483, 9921, 9676] 0.95
~~~

딱 젊은 사람들이 많이 모이는 곳이라고 알려진 곳들이 많이 포함.

- 이름을 모르는 역이라도 아마 젊은 사람들이 많이 찾는 곳이라 예측할 수 있음.

<br>

**유임 승차 비율이 가장 높은 역 찾기**

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx, rate = 0, 0
mx_station = ''

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
  if row[6]!=0 and (row[4]+row[6]) > 100000:
    rate = row[4] / (row[4]+row[6])
    if rate > mx:
      mx = rate
      mx_station = row[3] + ' ' + row[1]
        
print(mx_station, round(mx*100, 2)
# result:
# 홍대입구 2호선 95.34
~~~

<br>

### 유무임 승하차 인원이 가장 많은 역은 어디일까

이번에는 비율이 아니라 인원이 가장 많은 역 찾기.

~~~python
import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
    if row[i] > mx[i-4]:
      mx[i-4] = row[i]
      mx_station[i-4] = row[3] + ' ' + row[1]
      
for i in range(4):
  print(label[i] + ' : ' + mx_station[i], mx[i])
  
# result:
# 유임승차 : 강남 2호선 3153418
# 유임하차 : 강남 2호선 3210437
# 무임승차 : 종로3가 1호선 387062
# 무임하차 : 제기동 1호선 400607
~~~

<br>

### 모든 역의 유무임 승하차 비율은 어떻게 될까

이번에는 데이터가 있는 모든 역에 대한 유무임 승하차 비율을 표현.

- 파이 차트로 표현하기.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차', '유임하차', '무임승차', '무임하차']

for row in data:
  for i in range(4, 8):
		row[i] = int(row[i])
		plt.pie(row[4:8])
		plt.plot()
~~~

![A](https://i.imgur.com/ZuzFIze.png)

이런 파이 차트가 여러 개 출력됨.

<br>

조금 더 보완한 코드.

**모든 역의 유무임 승하차 비율을 파이 차트로 나타내기**

- 그래프 이미지를 저장하기 위해 savefig() 함수 사용.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차', '유임하차', '무임승차', '무임하차']
color = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family='AppleGothic')

for row in data:
  for i in range(4, 8):
    row[i] = int(row[i])
  plt.figure(dpi=300) 
  plt.pie(row[4:8], labels=label, colors=color, autopct='%1.1f%%')
  plt.title(row[3]+' '+row[1])
  plt.savefig(row[3]+' '+row[1]+'.png')
  plt.show()
~~~

![A](https://i.imgur.com/sNaHcRP.png)

<br>

**내가 작성한 코드 : 호선별 유무임 승하차 비율**

~~~python
import csv
import matplotlib.pyplot

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

cost_ride, cost_off, free_ride, free_off = [], [], [], []
for i in range(9):
    cost_ride.append([])
    cost_off.append([])
    free_ride.append([])
    free_off.append([])

label = ['유임승차', '유임하차', '무임승차', '무임하차']
color = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family='AppleGothic')

for row in data:
    for n in range(9):
        for i in range(4, 8):
            row[i] = int(row[i])
        if (str(n+1)+'호선') in row[1]:
            cost_ride[n].append(row[4])
            cost_off[n].append(row[5])
            free_ride[n].append(row[6])
            free_off[n].append(row[7])
            

for i in range(9):
    cost_ride[i] = sum(cost_ride[i])
    cost_off[i]  = sum(cost_off[i])
    free_ride[i] = sum(free_ride[i])
    free_off[i] = sum(free_off[i])

sub = list(zip(cost_ride, cost_off, free_ride, free_off))

for i in range(9):
    plt.pie(sub[i], labels=label, colors=color, autopct='%1.1f%%', startangle=90)
    plt.title(str(i+1)+'호선 승하차 비율')
    plt.show()
~~~

![A](https://i.imgur.com/ra0se5L.png)



