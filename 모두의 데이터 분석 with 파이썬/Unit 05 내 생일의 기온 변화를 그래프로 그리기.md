# Unit 05 내 생일의 기온 변화를 그래프로 그리기

> 내 생일의 기온 변화(최고 기온, 최저 기온) 그래프로 그리기.

<br>

### 데이터에 질문하기

**데이터 읽어오기**

헤더 부분을 next() 함수로 제외시킨 후, 최고 기온 데이터만 출력.

~~~python
import csv
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)

for row in data:
  print(row[-1])
  
# result:
# 20.7
# 22
# (생략)
~~~

<br>

**데이터 리스트에 저장하기**

최고 기온 데이터를 날짜 순으로 저장하기 위해 result 리스트 생성. 

~~~python
import csv
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
  if row[-1] != '' : # 최고 기온 데이터 값이 존재한다면
    result.append(row[-1])
print(result)
print(len(result))

# result:
# [20.7, 22.0, 21.3, 22.0, 25.4, 21.3, 16.1, 14.9, 21.1, 24.1,... (생략)]
# 39463
~~~

<br>

### 데이터 시각화하기

저번 단원에서 했던것처럼.

~~~python
import csv
import matplotlib.pyplot as plt
(생략)
plt.plot(result, 'r') # result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show()
~~~

![figure 5-1]( https://i.imgur.com/bVdVXre.png)

> 그래프 크기 조절하기
>
> figure() 함수의 figsize 속성 값을 변경해 그래프의 크기를 조절할 수 있음. figsize=(가로 길이, 세로 길이)로 크기 설정할 수 있고, 단위는 인치(inch).
>
> ~~~python
> plt.figure(figsize = (10,2)) # 가로로 10인치, 세로로 2인치로 설정.
> ~~~

![figure 5-1-1](https://i.imgur.com/1pSKx42.png)

<br>

### 날짜 데이터 추출하기

split() 함수를 사용해 8월의 최고 기온 데이터만 추출해 그래프 그리기.

~~~python
for row in data:
  if row[-1] != '' :
    if row[0].split(".")[1] == '8' :
      result.append(float(row[-1]))
plt.plot(result, 'hotpink')
plt.show()
~~~

![figure 5-2](https://i.imgur.com/T5117ei.png)

전에 비해 훨씬 간결하지만, 여전히 복잡함.

- 매년 돌아오는 생일을 기준으로 그래프 그리기. 매년 2월 14일의 최고 기온 데이터 추출에 그래프 그리기.

~~~python
for row in data:
  if row[-1] != '' :
    if row[0].split(".")[1] == '2' and row[0].split(".")[2] == '14' :
      result.append(float(row[-1]))
~~~

![figure 5-3](https://i.imgur.com/YaAKlDF.png)

<br>

더 자세히 살펴보기 위해 1983년 이후 데이터만 추출해 그래프 그리기. 최저 기온도 데이터에 포함.

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
high, low = [], []

for row in data:
  if row[-1] != '' :
    if 1983 <= int(row[0].split(".")[0]):
      if row[0].split(".")[1] == '2' and row[0].split(".")[2] == '14' :
        high.append(float(row[-1]))
        low.append(float(row[-2]))
   
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()
~~~

![figure 5-4](https://i.imgur.com/eTu1svS.png)

<br>

제목과 범례 등 다양한 내용을 추가해 생일 기온 그래프 꾸며보기.

~~~python
plt.rc('font', family='AppleGothic')
plt.title("내 생일의 기온 변화 그래프")
# 마지막 코드 넣어야 (-) 기호 깨지지 않고 출력됨.
plt.rcParams['axes.unicode_minus'] = False
~~~

> macOS에서는 'AppleGothic', 윈도우 운영체제를 사용하고 있다면 'Malgun Gothic' (띄어쓰기에 주의).



![figure 5-5](https://i.imgur.com/hUMEcdB.png)



### 전체 코드

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
high, low = [], []

for row in data:
  if row[-1] != '' and row[-2] = '' :
    # 날짜 값을 . 문자 기준으로 구분하여 저장.
    date = row[0].split(".")
    if 1983 <= int(date[0]):
      if date[1] == '2' and date[2] == '14' :
        high.append(float(row[-1]))
        low.append(float(row[-2]))

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title("내 생일의 기온 변화 그래프")
plt.plot(high, 'hotpink' ,label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()
~~~

![figure 5-6](https://i.imgur.com/o6xWBIJ.png)



### 내 코드 ver.1

~~~python
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
temp_high, temp_low, date = [], [], []

for row in data:
  if row[-1] != '':
  	for yr in range(1998, 2020):
    	if row[0] == str(i) + "." + '2.23' :
      	temp_high.append(float(row[-1]))
        temp_low.append(float(row[-2]))
        date.append(row[0])

table_high, table_low = dict(zip(temp_high, date)), dict(zip(temp_low, date))

print('가장 더웠던 날은', str(max(temp_high))+'도였던', table_high[max(temp_high)],'.')
print('가장 추웠던 날은', str(min(temp_low))+'도였던', table_low[min(temp_low)], '.')

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('내 생일의 기온 변화 그래프')
plt.plot(list(range(1998, 2019)), temp_high, label='최고 기온')
plt.plot(list(range(1998, 2019)), temp_low, label='최저 기온')
plt.legend()
plt.xlabel('연도')
plt.ylabel('기온(C)')
plt.show()
~~~

![figure 5-7](https://i.imgur.com/BYTXaF3.png)

### 내 코드 ver.02

~~~python
import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)

temp_high, temp_low = [], []
yr = np.arange(1998, 2019)

for row in data:
    if row[-1] != '':
        year = row[0].split(".")[0]
        month = row[0].split(".")[1]
        day = row[0].split(".")[2]    
        if year >= '1998':
            if month == '2' and day == '23': 
                temp_high.append(float(row[-1]))
                temp_low.append(float(row[-2]))
                           
plt.style.use('ggplot')
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.plot(yr, temp_high, 'r', label='최고 기온')
plt.plot(yr, temp_low, 'b', label='최저 기온')
plt.xlabel('연도')
plt.ylabel('기온(C)')
plt.title('내 생일의 기온 변화 그래프')
plt.legend()
plt.show()
~~~

![A](https://i.imgur.com/NaVmw6H.png)