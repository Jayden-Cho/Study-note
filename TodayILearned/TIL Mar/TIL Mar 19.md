# Algorithm

**최댓값 찾기**

- 최댓값의 위치를 찾는 알고리즘

~~~python
def find_max_idx(a):
  mx_idx = 0
  for i in range(1, len(a)):
    if a[mx_idx] < a[i]:
      mx_idx = i
  return mx_idx
~~~

<br>

**동명이인 찾기**

- 자주 쓰이는 집합 관련 함수: `set.add(x)`, `set.discard(x)`

~~~python
def find_same_name(a):
  result = set()
  for i in range(0, len(a)-1):
    for j in range(1, len(a)):
      if a[i] == a[j]:
        result.add(a[i])
  return result
~~~

<br>

**연습 문제**

- n명 중 두 명을 뽑아 짝을 지을 때 짝 지을 수 있는 모든 조합을 출력하는 알고리즘.

~~~python
def NumOfCases(a):
  result = set()
  for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
      result.add((a[i], a[j]))
  return result
~~~

<br>

<br>

# Prob & Stats

- How many **fewer** students in March played a baseball than students in May?
  - 5월에 야구한 학생 수 - 3월 학생 수 

<br>

**two-way frequency table**

|        | baseball | soccer |
| ------ | -------- | ------ |
| male   | A        | B      |
| female | C        | D      |

- 이 때, A, B, C, D는 정수.

<br>

**two-way relative frequency table**

|        | baseball | soccer |
| ------ | -------- | ------ |
| male   | 0.AA     | 0.CC   |
| Female | 0.BB     | 0.DD   |
| Ratio  | 1        | 1      |

- 이 때, 각 요소들은 비율. 1보다 작다.
- ratio는 열, 행 모두 될 수 있다.

- Obviously, counts <u>might be</u> different even if the relative frequencies are identical.