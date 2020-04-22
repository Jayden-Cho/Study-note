# Pandas

**명칭 기반 인덱싱 vs. 위치 기반 인덱싱**

- 위치(Position) 기반 인덱싱은 0을 기준으로 행, 열 위치를 기반으로 데이터를 저장.
- 명칭(Label) 기반 인덱싱은 칼럼의 명칭을 기반으로 위치를 지정하는 방식.

<br>

**`iloc[]` 연산자**

- 위치 기반 인덱싱. 명칭을 입력하면 오류가 생긴다.

  ~~~python 
  data_df.iloc[0, 0]
  ~~~

<br>

**`loc[]` 연산자**

- 명칭 기반 인덱싱. 행에는 DataFrame index 값, 열에는 칼럼명을 입력한다.

  - `loc[]`의 슬라이싱은 `[a:b]`라면 b로 포함한다.

  ~~~python
  data_df.loc[0, 'col1']
  ~~~

<br>

**불린 인덱싱**

- 조건을 입력하면 원하는 값을 필터링한다.

  ~~~python
  titanic_df[titanic_df['Age']>60]
  ~~~

<br><br>

# Algorithm

### 딕셔너리를 이용한 동명이인 찾기

**동명이인을 찾는 알고리즘 with 딕셔너리**

~~~python
def find_same_name(a):
  name_dict = {}
  for name in a:
    if name in name_dict:
      name_dict[name] += 1
    else:
      name_dict[name] = 1
      
	result = set()
  if name_dict[name] >= 2:
    result.add(name)
  return result
~~~

<br>

**알고리즘 분석**

- 기존 동명이인 알고리즘의 계산 복잡도는 $O(n^2)$. 
- 딕셔너리를 사용한 동명이인 알고리즘은:
  - 먼저 리스트에서 뽑아 딕셔너리에 저장하고(n번),
  - 딕셔너리에 저장된 요소를 확인해 2 이상인 key를 찾는다(n번 이하)
- 결국 계산 복잡도는 $O(n).$

