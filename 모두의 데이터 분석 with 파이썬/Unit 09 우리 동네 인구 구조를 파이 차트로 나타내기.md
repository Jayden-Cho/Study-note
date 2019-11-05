# Unit 09 우리 동네 인구 구조를 파이 차트로 나타내기

항아리 모양의 그래프로는 어떤 성별의 비율이 높을지 알기 어려움. **파이 차트로 비율을 비교.**

<br>

### 제주도에는 여성의 비율이 더 높을까

먼저 제주특별자치도의 성별 분포를 항아리로 표현하기.

~~~python
import csv 
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
m, f = [], []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data:
  if name in row[0]:
    for i in row[3:104] :
      i = i.replace(",", "")
      m.append(-int(i))
    for i in row[106:] :
      i = i.replace(",", "")
      f.append(int(i))

plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(len(row[3:104])), m, label='남성')
plt.barh(range(len(row[106:])), f, label='여성')
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.legend()
plt.show()

# result: ValueError: shape mismatch: objects cannot be broadcast to a single shape
~~~

**에러 발생.**

- '제주특별자치도'라는 단어가 포함된 지역 이름이 총 46개. 
  - 우리가 찾는 데이터는 제주특별자치도 전체에 대한 데이터 하나만 필요한 것.
- 사용자로부터 입력받은 내용이 포함되는 데이터 중 처음 만나는 데이터만 m, f에 추가시키는 방법 사용.
  - ***break*** 키워드 추가.
- 내 경우에는 csv 파일 숫자들에 ","가 쳐져 replace 함수로 제거했음.

<br>

~~~python
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data:
  if name in row[0] :
    for i in row[3:104] :
      m.append(-int(i))
    for i in row[106:] :
      f.append(int(i))
    break 
~~~

![9-4](https://i.imgur.com/iYuDkfq.png)

항아리 모양의 그래프에서는 연령대별 인구 차이는 확인할 수 있지만, 어떤 성별이 더 많은지 비교는 어려움.

<br>

### 혈액형 비율 표현하기

**pie() 함수**

~~~python
import matplotlib.pyplot 

size = [2441, 2312, 1031, 1233]
plt.axis('equal') # 책에는 이 줄 안쓰면 원 찌그러진다했지만, 주피터는 문제 없이 출력됨.
plt.pie(size)
plt.show()
~~~

![9-7](https://i.imgur.com/6h8eZVV.png)

<br>

**레이블 추가하기**

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
plt.pie(size, labels=label)
plt.show()
~~~

![9-8](https://i.imgur.com/iqiwDg6.png)

파이트 차트의 기본 시작 지점은 3시 방향이라는 것을 알 수 있음.

<br>

**비율 및 범례 표시하기**

autopct 속성 사용.

- auto percent를 의미. 어떤 형태로 값을 표시할지 작성하면 각 항목의 비율을 자동으로 계산해서 표시.
- 정확한 계산을 위해 소수점까지 나타내는 float 형태로 표시.

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
plt.pie(size, labels=label, autopct='%1.1f%%')
plt.legend()
plt.show()
~~~

![9-9](https://i.imgur.com/dGaLVnt.png)

<br>

**색 및 돌출 효과 정하기**

- 색은 colors 속성으로, 돌출 효과는 explode 속성으로.
  - 돌출되는 정도는 데이터 순서에 따라 설정할 수 있음. 0은 돌출하지 않음을 의미.

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.pie(size, labels=label, colors=color, autopct='%1.1f%%', explode=(0, 0, 0,1 0))
plt.legend()
plt.show()
~~~

![9-10](https://i.imgur.com/QHNvJNU.png)

> Https://matplotlib.org/gallery/color/named_colors.html에서 자세히 확인 가능.
>
> RGB 코드를 활용하는 방법도 있음.

<br>

### 제주도의 성별 인구 비율 표현하기

저번 그래프에서는 연령대별 성별 데이터를 구했지만, 이번에는 성별 합계 데이터를 구해야.

- 성별 합계 데이터를 구할 변수 2개가 필요.
- range() 함수를 이용하면 row 리스트의 인덱스를 좀더 쉽게 다룰 수 있음.

~~~python
import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
size = []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data:
  if name in row[0]:
    m, f = 0, 0
    for i in range(101): # 나이 데이터의 구간 개수
      m += int(row[i+3])
      f += int(row[i+106])
    break
size.append(m)
size.append(f)
print(size)

# result: [335838, 331657]
~~~

<br>

**내가 했던 방식**

~~~python
import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)
size = []

for row in data:
  if '제주특별자치도' in row[0]:
    m, f = 0, 0
    for i in row[3:104] :
      i = i.replace(",", "")
      m += int(i)
    for i in row[106:] :
      i = i.replace(",", "")
      f += int(i)  
    break
size.append(m)
size.append(f)
print(size)
~~~

<br>

결과를 파이 차트로 표현하기만 하면 됨.

~~~python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
color = ['crimson', 'darkcyan']
plt.pie(size, labels=['남', '여'], autopct='%1.1f%%', colors=color, startangle=90)
plt.title(name+' 지역의 남녀 성별 비율')
plt.show()
~~~

![9-11](https://i.imgur.com/AKRQHR5.png)

