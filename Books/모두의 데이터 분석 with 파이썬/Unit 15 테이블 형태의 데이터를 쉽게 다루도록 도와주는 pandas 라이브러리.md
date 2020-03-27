# Unit 15 테이블 형태의 데이터를 쉽게 다루도록 도와주는 pandas 라이브러리

>

Pandas - 파이썬 데이터 분석에 가장 많이 쓰이는 라이브러리.

- Unit 14에서 만들어본 데이터 프로젝트를 pandas 라이브러리를 활용해 해결해보기.

<br>

### 위키피디아 데이터 엑셀로 저장하기

구글 검색 창에 olympic medal 검색.

- 웹 브라우저의 주소 창에서 주소를 복사한 후, 코드 작성.

~~~python
import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
print(df)
~~~

`read_html()`함수는 웹 페이지에서 테이블 형태의 데이터를 추출하는 함수.

- 위키피디아 페이지에 있는 테이블 데이터를 추출해 df라는 변수에 저장.

![A](https://i.imgur.com/b6Ewfug.png)

뭔가 되게 복잡함. 데이터가 어떻게 구성되어 있는지 파악하기 어려움.

- 대괄호([])가 있는걸 보아하니 리스트 형태.

<br>

df 리스트의 1번 인덱스에 저장된 내용이 무엇인지 살펴보기.

~~~python
import pandas as pd
df = pd.read_html('올림픽 메달 주소')
df[1]
~~~

![A](https://i.imgur.com/f0RCz8i.png)

더 깔끔하게 정리됨.

- `header`로 하계, 동계올림픽에 대한 구분을 주고,
- `index_col`을 사용해 인덱스를 나라 이름으로 바꾸기.

<br>

~~~python
import pandas as pd
df = pd.read_html('올림픽 메달 주소', header=0, index_col=0)
df[1]
~~~

![A](https://i.imgur.com/8ZpRoEn.png)

<br>

데이터 중 하계올림픽에 대한 데이터만 추출 (앞의 5개 데이터).

~~~python
summer = df[1].iloc[:, :5]
summer
~~~

`iloc` 인덱스 방식을 사용.

- 데이터의 순서에 따라 접근하는 것. 콤마(,)를 중심으로 앞은 행, 뒤는 열에 접근.
  - `[:, :5]`는 모든 행에 접근하고 첫 5열을 슬라이싱 하는 것.

![A](https://i.imgur.com/rFhoDvq.png)

<br>

열 이름이 정확하지 않으므로 다시 설정하기.

~~~python
summer.columns = ['경기수', '금', '은', '동', '계']
summer
~~~

![A](https://i.imgur.com/IDHHdYt.png)

<br>

알파벳순으로 정렬된 나라 이름을 금메달 기준으로 정렬.

- `sort_values`에서 `ascending` 속성을 변경함으로써 정렬할 수 있음.
- 오름차순으로 정렬하고 싶으면 `False`를 `True`로 변경.
  - 오름차순: 차례로 늘어나는 것.

~~~python
import pandas as pd
df = pd.read_html('올림픽 메달 주소', header=0, index_col=0)
summer = df[1].iloc[:, :5]
summer.columns = ['경기수', '금', '은', '동', '계']
summer.sort_values('금', ascending=False)
~~~

이 표를 엑셀 파일로 저장.

~~~python
summer.sort_values('금', ascending=False).to_excel('하계올림픽메달.xlsx')
~~~

이제 본격적으로 pandas에 대해 알아보기.

<br>

### pandas란

panel datas(패널 자료)의 약자. numpy를 기반으로 만들어졌고, 데이터 분석을 위한 효율적인 데이터 구조를 제공.

- 1차원 배열 형태의 데이터 구조를 Series, 2차원 배열 형태의 데이터 구조를 DataFrame라고 불림.

<br>

### 데이터 프레임 기초

날짜 형태로 된 8개의 인덱스를 간단히 만들기.

~~~python
import pandas as pd
index = pd.date_range('1/1/2000', periods=8)
print(index)

# result:
# DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
#                '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08'],
#                 dtype='datetime64[ns]', freq='D')
~~~

<br>

numpy 라이브러리를 활용해 8행 3열로 구성된 랜덤 데이터를 생성한 후, 인덱스와 컬럼 이름을 정해 데이터 프레임으로 만들기.

~~~python
import numpy as np

df = pd.DataFrame(np.random.rand(8, 3), index=index, columns=list('ABC'))
df
~~~

![a](https://i.imgur.com/U81iy49.png)

데이터 프레임 df의 각 열에 접근하려면 열의 이름을 대괄호 안에 넣으면 됨(df['A']처럼).

- 인덱스는 선택하지 않아도 함께 출력됨.
- 특정 행이나 열을 선택하면 Series 형태로 표현됨.

~~~python
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8, 3), index=index, columns=list('ABC'))
print(df['B'])

'''result:
2000-01-01    0.386258
2000-01-02    0.917309
2000-01-03    0.742480
2000-01-04    0.079404
2000-01-05    0.521959
2000-01-06    0.177331
2000-01-07    0.751848
2000-01-08    0.233249
Freq: D, Name: B, dtype: float64'''
~~~

B열을 선택했더니 날짜로 이루어진 인덱스와 1차원 배열로 값이 출력됨.

<br>

numpy에서 사용했던 mask 기능을 데이터 프레임에서도 사용할 수 있음.

- 마스크는 특정한 조건을 만족하는지에 따라 참과 거짓을 반환.
- 데이터를 골라내는 데 유용함.

~~~python
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8, 3), index=index, columns=list('ABC'))
print(df['B'] > 0.4)

'''result:
2000-01-01    False
2000-01-02     True
2000-01-03     True
2000-01-04    False
2000-01-05     True
2000-01-06    False
2000-01-07     True
2000-01-08    False
Freq: D, Name: B, dtype: bool'''
~~~

<br>

이걸 데이터 프레임에 적용시켜 다시 저장하기.

~~~python
df2 = df[df['B']>0.4]
df2
~~~

![a](https://i.imgur.com/cyn7hZH.png)

행렬을 뒤집으려면 T(Transpose)만 붙여주면 된다.

~~~python
df2.T
~~~

<br>

2차원 배열 형태의 데이터 프레임 연산 알아보기.

- 행을 기준으로 계산할 수도 있고, 열을 기준으로 계산할 수도 있음.

> 2차원 데이터일 경우 pandas에서는 기본적으로 행 방향을 축으로 계산함.
>
> - 열 방향 축으로 계산하려면 axis=1.
>   - 계산해 내려가는 방향이 축.

<br>

행 방향 축을 기준으로 한 나눗셈 연산.

~~~python
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8, 3), index=index, columns=list('ABC'))
df['D'] = df['A']/df['D']
df
~~~

![a](https://i.imgur.com/d5S4XS9.png)

<br>

열 방향 축을 기준으로 sum() 계산.

~~~python
df['D'] = df['A'] / df['B']
df['E'] = df.sum(df, axis=1)
df.head()
~~~

![a](https://i.imgur.com/vkPtd3E.png)

<br>

1개의 열을 1개의 열로 나누는 계산이여서 산술 연산자를 사용할 수 있었지만, 여러 개의 열에 대한 계산을 하려면 pandas 라이브러리 사용해여 한다.

전체 데이터를 A값으로 뺄 때는 sub() 함수 사용.

~~~python
df.sub(df['A'], axis=0)
~~~

![a](https://i.imgur.com/ngiCWDx.png)

<br>

데이터 전체를 C열 값으로 나눌 땐 div() 함수 사용.

~~~python
df.div(df['C'], axis=0)
~~~

![a](https://i.imgur.com/Mtuw1rj.png)

<br>

데이터 프레임을 CSV 파일로도 쉽게 저장할 수 있음.

~~~python
df.to_csv('test.csv')
~~~

<br>

### pandas로 인구 구조 분석하기

Unit 14에서 구현했던 알고리즘

1. 데이터 읽어오기.

   1-1. 전체 데이터를 총 인구수로 나누어 비율로 변환.

   1-2. 총 인구수와 연령구간 인구수를 삭제.

2. 궁금한 지역의 이름을 받기.

3. 궁금한 지역의 인구 구조를 저장.

4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기.

   4-1. 전국의 모든 지역 중 한 곳(B)을 선택.

   4-2. 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 빼기.

   4-3. (4-2)를 100세 이상 인구수에 해당하는 값까지 반복한 후 차이의 제곱을 모두 더하기.

   4-4. 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역 찾기.

5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화.

<br>

**1. 데이터 읽어오기**

pandas에서는 `read_csv()`함수를 활용.

~~~python
import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col=0, thousands=",")
df.head()
~~~

> 나같은 경우는 csv파일에 1,000이 넘어가는 숫자는 콤마(,) 구별점이 있어 thousands=","가 필수.

<br>

연령별 인구 숫자를 비율로 바꾸고 총인구수, 연령구간인구수 데이터를 삭제.

- `del`명령어로 특정 열 삭제 가능.

~~~python
df.div(['총인구수'], axis=0)
del df['총인구수'], df['연령구간인구수']
~~~

> 열 이름이 다를 수 있으므로 꼭 csv 파일 체크하기.

<br>

**2~3. 궁금한 지역 이름 받고 해당 지역의 인구 구조 저장하기**

`df.index.str.contains()`함수는 데이터 프레임의 인덱스 문자열에 원하는 문자열이 포함된 행을 찾음.

~~~python
name = input('원하는 지역의 이름을 입력 : ')
a = df.index.str.contanis(name)
df2 = df[a]
df2
~~~

![a](https://i.imgur.com/cweiMG6.png)

<br>

그래프로 그리려면 행렬을 바꾼 후 `plot()`함수 실행.

~~~Python
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
df2.T.plot()
plt.xticks(rotation=90)
plt.show()
~~~

![a](https://i.imgur.com/ioiWa0M.png)

<br>

**4~5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 시각화하기**

각 알고리즘 코드를 개별로 살펴보고 마지막에 전체 코드 실행.

먼저 궁금한 지역의 연령별 비율과 다른 지역의 연령별 비율의 차이를 계산.

~~~python
import numpy as np

# 데이터 프레임에서 궁금한 지역의 연령별 비율을 모두 빼기.
x = df.sub(df2.iloc[0], axis=1)
# 뺀 값에 제곱 값을 모두 더함.
y = np.power(x, 2)
z = y.sum(axis=1)
~~~

<br>

pandas의 `sort_values()`와 슬라이싱을 이용하면 상위 몇 개 지역까지 쉽게 찾을 수 있음.

- `ascending` 입력하지 않았으므로 가장 작은 값부터 내림차순으로 출력.

~~~python
i = z.sort_values().index[:5]
~~~

<br>

이제 이 결과를 꺾은선 그래프로 그리기.

~~~python
df.loc[i].T.plot()
plt.show()
~~~

<br>

**전체 코드**

~~~python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('age.csv', encoding='cp949', index_col=0, thousands=",")
df = df.div(df['총인구수'], axis=0)
del df['총인구수'], df['연령구간인구수']

name = input('원하는 지역의 이름을 입력해주세요 : ')
a = df.index.str.contains(name)
df2 = df[a]

# index[1:6]으로 해야 자기 자신을 제외.
df.loc[np.power(df.sub(df2.iloc[0]), 2).sum(axis=1).sort_values().index[1:6]].T.plot()

plt.rc('font', family='AppleGothic')
plt.xticks(rotation=45)
plt.show()
~~~

![a](https://i.imgur.com/1s0GfCc.png)