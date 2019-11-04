# Unit 07 우리 동네 인구 구조 시각화하기

> '인구 통계의 변화는 미래와 관련된 것 가운데 정확한 예측을 할 수 있는 유일한 사실.' - 피터 드러커

<br>

### 인구 공공데이터 내려받기

www.mois.go.kr - 정책자료 - 통계 - 주민등록 인구통계

> 한글이 깨져보인다면? 인코딩 방식을 바꿔야.
>
> 1. csv 파일을 메모장으로 열기.
> 2. 파일의 '인코딩'을 UTF-8로 바꾼 다음, '파일 형식'을 모든 파일로 설정한 뒤 저장.

<br>

### 인구 데이터 살펴보고 질문하기

데이터 살펴보기

- A열에는 행정 구역 이름과 10자리 숫자로 이루어진 행정 구역 코드가 있음.
- B~C열에는 해당 지역 전체 인구수가 있음.
- D열부터 만 0세부터의 연령별 인구가 기록됨.
  - 0세부터 100세 이상까지 총 101개 구간 데이터가 제공됨.

![7-8](https://i.imgur.com/chw3KaO.png)

<br>

### 우리 동네 인구 구조 시각화하기

알고리즘 설계

1. 인구 데이터 파일 읽어오기.
2. 전체 데이터에서 한 줄씩 반복해서 읽어오기.
3. 우리 동네에 대한 데이터인지 확인.
4. 우리 동네일 경우 0세부터 100세 이상까지의 인구수를 순서대로 저장.
5. 저장된 연령별 인구수 데이터를 시각화.

<br>

인구 데이터 파일(age.csv) 읽어오기.

~~~python
import csv 
f = open('age.csv', encoding='cp949')
data = csv.reader(f)

for row in data:
  print(row)
  
# result: ['행정구역', '2019년02월_계_총인구수', '2019년02월_계_연령구간인구수', '2019년02월_계_0세', '2019년02월_계_1세', '2019년02월_계_2세', '2019년02월_계_3세', '2019년02월_계_4세', '2019년02월_계_5세', ...(생략)]
~~~

<br>

우리 동네 데이터만 선택해서 출력하기.

- row[0]에 지역명이 저장되어 있다.

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)

for row in data:
	if '경기도 안양시 동안구 평안동(4117357600)' == row[0]:
    print(row)
~~~

<br>경기도 안양시 동안구 평안동(4117357600)처럼 지역명 모두 적는건 번거로움.

- 파이썬 in 연산자로 보다 편리하게 코드 작성 가능.
- 'A in B'는 A가 B 안에 존재하면 참, 아니면 거짓.

~~~python
print('평안동' in '경기도 안양시 동안구 평안동(4117357600)') # True
print('4117' in '경기도 안양시 동안구 평안동(4117357600)') # True
~~~

<br>

in 연산자를 적용하면:

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)

for row in data:
  if '평안동' in row[0]:
    print(row)
~~~

<br>

A~C열은 불필요하니 3번 인덱스부터 끝까지 데이터 읽어오기.

~~~python
import csv 

f = open('age.csv', encoding='cp949')
data = csv.reader(f)

for row in data:
  if '평안동' in row[0]:
    for i in row[3: ]: 
      print(i)
~~~

<br>

데이터 읽어왔으니 순서대로 저장. 순서대로 저장할 때는 리스트를 사용하는 것이 좋음.

~~~python
import csv

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  if '평안동' in row[0] :
    for i in row[3: ] :
      result.append(int(i)) # 문자열로 저장되어있으므로 정수로 전환.
    
print(result)
~~~

<br>

데이터 시각화하기

~~~python
import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  if '평안동' in row[0] :
    for i in row[3: ]:
      result.append(int(i))
      
plt.style.use('ggplot')
plt.plot(result)
plt.show()
~~~

![7-11](https://i.imgur.com/5Y0RZlX.png)

> ggplot 스타일 외에도 다양한 스타일 적용 가능.
>
> - print(plt.style.available)로 적용 가능한 스타일의 이름 확인 가능.