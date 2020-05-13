# Algorithm

**리스트 함수 몰랐던 것 3가지**

- `insert(x, a)` : x index에 a 넣기 

  ~~~python
  a = [1, 2, 3]
  a.insert(2, 4)
  # result: [1, 2, 4, 3]
  ~~~

- `pop(x)` : x index의 value 뽑기. x 입력 안하면 리스트 마지막 value. 

  ~~~Python 
  a = [1, 2, 3]
  val1 = a.pop(0)
  val2 = a.pop()
  print(val1, val2)
  # result: 1 3
  ~~~

- `clear()` : 리스트 내 모든 value 삭제

  ~~~python
  a = [1, 2, 3]
  a.clear()
  # result: []
  ~~~

<br>

**최댓값 위치 알려주는 알고리즘 구하기**

~~~python
def findMaxIdx(lst):
  mx_idx = 0
  for i in range(len(lst)):
    if lst(mx_idx) < lst[i]:
      mx_idx = i  
  return mx_idx
~~~

<br>

**집합 함수 몰랐던 것 2 가지**

- `add(x)` : 집합에 x 추가

  ~~~python
  a = set([1, 2, 3])
  a.add(4)
  # result: {1, 2, 3, 4}
  ~~~

- `discard(x)` : 집합에서 x 삭제

  ~~~Python
  a = set([1, 2, 3])
  a.discard(3)
  # result: {1, 2}
  ~~~

<br>

**리스트에서 동명이인 찾기**

~~~python
def findSameName(lst):
  for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
      if lst[i] == lst[j]:
        return lst[i]
~~~

<br>

**n명 중 모든 두 명 조합 찾기**

~~~python
def findSet(lst):
  result = set()
  for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
      result.add((lst[i], lst[j]))
  return result
~~~

<br>

**1부터 n까지의 정수의 곱 구하기**

~~~python
def findgop(n):
  if n == 1:
    return 1
  return n * findgop(n-1)
~~~

<br>

**숫자 n개 중 최댓값 재귀 호출로 찾기**

~~~python
def findMaxRecur(lst, idx):
  if idx == 1:
    return lst[0]
  mx = findMaxRecur(lst, idx-1):
  if mx < lst[idx-1]:
    return lst[idx-1]
  else:
    return mx
~~~

<br>

**최대공약수 알고리즘 - 기본**

~~~python
def GCD(a, b):
  i = min(a, b)
  while True:
    if a%i==0 and b%i==0:
      return i
  	i -= 1
  return -1
~~~

<br>

**최대공약수 알고리즘 - 재귀 호출**

~~~python
def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a%b)
~~~

<br>

**피보나치 수열을 재귀 호출로 구현**

~~~python
def fib(n):
  if n <= 1:
    return 1
  return fib(n-1) + fib(n-2)
~~~

<br>

**선택 정렬으로 오름차순 정렬**

~~~python
def sel_sort(a):
  n = len(a)
  for i in range(0, n-1):
    mn_idx = i
    for j in range(i+1, n):
      if a[j] < a[mn_idx]:
        mn_idx = j
    a[i], a[mn_idx] = a[mn_idx], a[i]
~~~



