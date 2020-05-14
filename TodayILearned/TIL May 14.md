# 영어

**Stop playing around with words.**

- 말장난 하지마. 

**Wake up with determination. Go to bed with satisfaction.**

- 다짐하며 하루를 시작하고 만족하며 잠에 들자.

**You're a real go-getter.**

- 너 진짜 열심히 하는구나. 

**I wanna get a girlfriend.**

- 나 여자친구 사귀고 싶어. 

**Do you mind if I sit here? / No, go ahead. / Yes, I do.**

- 실례지만 여기 앉아도 될까요? / 네 그러세요. / 아니요 안돼요.

<br>

<br>

# 5/13 Review

재귀 호출을 사용해 최대공약수 찾기

~~~python
# 일반적인 방법 
def OrigGCD(a, b):
  i = min(a, b)
  while True:
    if a%i==0 and b%i==0:
      return i
  	i -= 1
  return -1
  
  
# 재귀호출을 사용한 방법
def RecurGCD(a, b):
  if b == 0:
    return a
 	return RecurGCD(b, a%b)
~~~

 재귀 호출로 리스트 내 최댓값 찾기

~~~python
def findMaxRecur(lst, idx):
  if idx == 1:
    return lst[0]
  mx = findMaxRecur(lst, idx-1)
  if mx < lst[idx-1]:
    return lst[idx-1]
  else:
    return mx

a = [1, 3, 5, 4, 2]
findMaxRecur(a, len(a))
~~~

선택 정렬 알고리즘

~~~python
def sel_sort(lst):
  n = len(lst)
  for i in range(0, n-1):
    mn_idx = i
    for j in range(i+1, n):
      if lst[j] < lst[mn_idx]:
        mn_idx = j
      lst[i], lst[mn_idx] = lst[mn_idx], lst[i]

a = [1, 3, 5, 4, 2]
sel_sort(a)
print(a)
~~~

<br>

<br>

# Algorithm

**삽입 정렬 - 기본**

~~~python
def find_ins_idx(lst, val):
  for i in range(0, len(lst)):
    if val < lst[i]:
      return i
  return len(lst)

def ins_sort(lst):
  result = []
  while lst:
    val = lst.pop(0)
    idx = find_ins_idx(result, val)
    result.insert(idx, val)
  return result
~~~

**기본 삽입 정렬 알고리즘**

~~~python
def ins_sort(lst):
  n = len(lst)
  for i in range(1, n):
    key = a[i]
    j = i-1
    while j >= 0 and lst[j] > key:
      lst[j+1] = lst[j]
      j -= 1
    lst[j+1] = key
~~~

**삽입 정렬을 내림차순으로**

~~~python
def ins_sort(lst):
  n = len(lst)
  for i in range(1, n):
    key = a[i]
    j = i-1
    while j >= 0 and lst[j] < key:
      lst[j+1] = lst[j]
      j -= 1
    lst[j+1] = key
~~~

<br>

**병합 정렬 알고리즘**

~~~python
def merge_sort(lst):
  n = len(lst)
  if n <= 1:
    return lst 

  mid = n // 2
  g1 = merge_sort(lst[:mid])
  g2 = merge_sort(lst[mid:])

  result = []
  while g1 and g2:
    if g1[0] < g2[0]:
      result.append(g1.pop(0))
    else:
      result.append(g2.pop(0))
  while g1:
    result.append(g1.pop(0))
  while g2:
    result.append(g2.pop(0))
  return result
~~~

<br>

**쉬운 퀵 정렬 알고리즘**

~~~python
def quick_sort(lst):
  n = len(lst)
  if n <= 1:
    return lst
  pivot = lst[-1]
  g1, g2 = [], []
  for i in range(0, n-1):
    if lst[i] < pivot:
      g1.append(lst[i])
    else:
      g2.append(lst[i])
  return quick_sort(g1) + [pivot] + quick_sort(g2)
~~~

**기본 퀵 정렬 알고리즘**

~~~python
def quick_sort_sub(lst, start, end):
  if end - start <= 0:
    return

  pivot = lst[end]
  i = start
  for j in range(start, end):
    if lst[j] <= pivot:
      lst[i], lst[j] = lst[j], lst[i]
      i += 1
  lst[i], lst[end] = lst[end], lst[i]
  quick_sort_sub(lst, start, i-1)
  quick_sort_sub(lst, i+1, end)

def quick_sort(lst):
  quick_sort_sub(lst, 0, len(lst)-1)
~~~

**버블 정렬 구현**

~~~Python
def bubble_sort(lst):
  n = len(lst)
  while True:
    changed = False
    for i in range(1, n):
      j = i-1
      if lst[j] > lst[i]:
        lst[i], lst[j] = lst[j], lst[i]
        changed = True
    if changed == False:
      return 
~~~

<br>

**이분 탐색 알고리즘**

~~~python
def binary_search(lst, val):
  start = 0
  end = len(lst) - 1
  
  while start <= end:
    mid = (start+end) // 2
    if lst[mid] == val:
      return mid
    elif lst[mid] < val:
      start = mid + 1
    else:
      end = mid - 1
      
a = [1, 2, 3, 4, 5]
binary_search(a, 4)
~~~



**재귀 호출을 사용한 이분 탐색**

~~~python
def binary_search_sub(lst, val, start, end):
  if start > end:
    return -1
  mid = (start+end) // 2
  if lst[mid] == val:
    return mid
  elif lst[mid] < val:
    return binary_search_sub(lst, val, mid+1, end)
  else:
    return binary_search_sub(lst, val, start, mid-1)

def binary_search(lst, val):
  return binary_search_sub(lst, val, 0, len(lst)-1)
~~~

