# Unit 03 서울이 가장 더웠던 날은 언제였을까

> 질문은 명확하게.
>
> 데이터로 답을 찾을 수 있는지 확인.

### 질문 다듬기

- 구체적이고 명확한 질문인지 생각해보고 보유한 데이터로 해결할 수 있게 질문을 수정하기.
  - 기록이 누락된 날은 질문에 반영하지 않음.
  - 질문을 다듬는 과정은 질문자의 주관적인 판단에 따라 달라질 수 있음.



### 문제 해결 방법 구상하기

- 먼저 데이터를 읽어오기.	

  - 기온 데이터에는 '날짜', '지점코드', '평균기온', '최저기온', '최고기온'이 저장되있음.
  - 질문을 해결하는데 필요한 데이터는 '날짜'와 '최고기온' 데이터.

- 해결을 위한 알고리즘

  - 순차적으로 최고 기온 값을 확인.
  - 최고 기온이 가장 높은 날짜의 데이터를 변수(별도의 저장 공간)에 저장.

  > 문제 해결 방법을 코드로 표현하다 보면 문제 해결 방법을 구상할 때 생각하지 못했던 오류가 발생할 수도 있고, 예외 상황에 대해 처리해야 하는 경우도 생김.
  >
  > 그럴 때 문제의 원인을 생각해 보면 문제를 해결할 수 있음.



### 파이썬 코드로 구현하기

**기존에 작성했던 코드**

~~~python
import csv
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)
for row in data:
  print(row)
f.close()
~~~

- 현재 최고 기온 데이터는 str 형식이기 때문에 숫자 형식으로 형 변환이 필요하다.
  - 기온 데이터는 소수점이 존재는 실수이므로 float 형식을 사용한다.



~~~python
import csv
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)
for row in data:
  row[-1] = float(row[-1])
  print(row)
f.close()

# result:
# ['1907.10.1', '108', '13.5', '7.9', 20.7]
# ['1907.10.2', '108', '16.2', '7.9', 22.0]
# (생략)
# ValueError: could not convert string to float: 

~~~

- 문자열을 실수로 변환할 수 없다고 에러가 발생.
  - 문자열을 실수의 형태로 변환하던 중에 빈 문자열('')이 발견되어 오류가 생긴 것.
  - 대체로 이런 경우 대체할 특정 값을 넣어주면 됨.

~~~python
import csv
f = open('seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)

for row in data:
  if row[-1] == '':
    row[-1] = -999
  row[-1] = float(row[-1])
  print(row)
f.close()

# result:
# ['1907.10.1', '108', '13.5', '7.9', 20.7]
# ['1907.10.2', '108', '16.2', '7.9', 22.0]
# 에러없이 출력됨.
~~~



규칙 없이 섞여 있는 데이터 중에 가장 큰 값을 찾으려면?

- '탐색'과 '비교'의 과정 거치기.
  - 기준이 되는 값을 설정, 기준값과 새로운 값을 비교한 후, 기준값보다 더 큰 값이 나타나면 기준값을 업데이트.
  - '기준이 되는 값'을 저장할 '변수'가 필요 - *max_temp, max_date*

~~~python
import csv
max_temp = -999
max_date = ''
f = open('seoul.csv', encoding='cp949')
(생략)
~~~

- 최고 기온을 탐색하는 코드를 추가하기.
  - 직접 코딩하기 전에 말로 표현해보면 쉽게 바꿀 수 있음.

> 만약 지금까지의 최고 기온 값보다 현재 형의 최고 기온 값이 더 크다면
>
> ​	최고 기온 날짜 업데이트
>
> ​	최고 기온 값 업데이트



이 표현을 파이썬 코드로 옮기면:

~~~python
if max_temp < row[-1]:
  max_date = row[0]
  max_temp = row[-1]
~~~



**전체 코드**

~~~python
import csv
f = open('seoul.csv', encoding='cp949')    # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)    # 맨 윗줄 header 변수에 저장하기.
max_temp = -999    # 기본 변수 초기화
max_date = ''

for row in data:
  if row[-1] = '':    # NA val을 -999로 바꾸기
    row[-1] = -999
  row[-1] = float(row[-1])    # str을 float으로 전환.
  
  if max_temp < row[-1]:   # max_temp 보다 높다면 업데이트
    max_date = row[0]
    max_temp = row[-1]
f.close()
print(max_date, max_temp)

# result: 
# 2018.8.1 39.6
~~~

![스크린샷 2019-10-30 오후 4.34.14](/Users/seonggeun/Desktop/스크린샷 2019-10-30 오후 4.34.14.png)