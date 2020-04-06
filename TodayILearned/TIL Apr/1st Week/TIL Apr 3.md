# Algorithm

### 퀵 정렬

**이해하기 쉬운 퀵 정렬 알고리즘**

~~~python
def quick_sort(a):
  n = len(a)
  if n <= 1:
    return a
  pivot = a[-1]
  g1, g2 = [], []
  for i in range(0, n-1):
    if a[i] < pivot:
      g1.append(a[i])
    else:
      g2.append(a[i])
      
  return quick_sort(g1) + [pivot] + quick_sort(g2)
~~~

<br>

**일반적인 퀵 정렬 알고리즘**

~~~python
def quick_sort_sub(a, start, end):
  if end - start <= 0:
    return 
  i = start
  pivot = a[end]
  for j in range(start, end):
    if a[j] <= pivot:
      a[i], a[j] = a[j], a[i]
      i += 1
  a[i], a[end] = a[end], a[i]
  quick_sort_sub(a, start, i-1)
  quick_sort_sub(a, i+1, end)
 
def quick_sort(a):
  quick_sort_sub(a, 0, len(a)-1)
~~~

<br>

**알고리즘 분석**

- 퀵 정렬에서는 기준값이 중요하다.
  - 열 명의 학생의 키를 비교하려 할 때, 선정된 기준 학생의 키가 가장 크다면(작다면) 두 그룹으로 나누는 의미가 없다.
  - 하지만 이미 좋은 기준을 선정하는 방법이 있으니 걱정 ㄴ. 하지만 선정 방식은 배울 범위를 벗어난 부분.
- 최상의 계산 복잡도는 $O(n)$. 최악일 경우는 $O(n^2)$. 하지만 평균적으로 선택, 삽입 정렬과 비슷한 $O(n \cdot \log n)$.

**연습 문제: 버블 정렬**

~~~python
def bubble_sort(a):
  for i in range(0, len(a)-1):
    j = i + 1
    if a[j] < a[i]:
      a[j], a[i] = a[i], a[j]
      bubble_sort(a)
~~~

<br><br>

# Pandas

**DataFrame과 다른 자료형의 상호 변환**

- DataFrame <--> ndarray

  ~~~python
  df = np.DataFrame(ndarray)
  ndarray = df.values
  ~~~

- DataFrame <--> list

  ~~~python
  df = np.DataFrame(lst)
  lst = df.values.tolist()
  ~~~

- DataFrame <--> dict

  ~~~python
  df = np.DataFrame(dct)
  dct = df.to_dict('list')
  ~~~

<br>

**DataFrame 생성과 수정**

새로운 column을 추가하려면 `DataFrame[]` 내에 새 칼럼명을 입력하고 값을 할당하면 된다.

~~~python
df['Age'] = 0
~~~

<br>

기존 칼럼에 연산을 적용해 새로운 칼럼을 생성할 수 있다.

~~~python
df['Age_10'] = df['Age'] * 10
~~~

<br>

기존 칼럼 Series도 일괄적으로 업데이트 할 수 있다.

~~~python
df['Age_10'] = df['Age_10'] * 100
~~~

