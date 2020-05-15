# English

**We are distressed to learn of the delay.**

- 지연 소식을 들어 힘듦니다.

**There is a delay of shipment from the manufacturer.**

- 제조업체 배달이 지연됩니다. 

**The seasoning is amazing!**

- 소스가 훌륭한데요!

**What is the name of the plant in the vase?**

- 저 화분에 있는 식물 이름이 뭐에요?

**The odds are against us.**

- 승산이 거의 없어요. 

**What a small world!**

- 세상 참 좁다!

**I'm not an ideal boyfriend material, am I?**

- 난 이상적인 남친감은 아닌 것 같아. 그치?

**What makes you so sure?**

- 왜 그리 확신해?

<br>

<Br>

# 5/14 Review

**삽입 정렬**

~~~python
def ins_sort(lst):
  n = len(lst)
  for i in range(1, n):
    key = lst[i]
    j = i-1
    while j >= 0 and lst[j] > key:
      lst[j+1] = lst[j]
      j -= 1
    lst[j+1] = key
~~~

**병합 정렬**

~~~python
def merge_sort(lst):
  n = len(lst)
  if n<= 1:
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

**퀵 정렬**

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

**버블 정렬**

~~~python
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

**이분 탐색 - 기본 버전**

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
~~~

**이분 탐색 - 재귀 호출**

~~~python
def binary_search_sub(lst, val, start, end):
  
  while start <= end:
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

<br>

<br>

# Algorithm

**회문 찾기 with 큐/스택**

**큐/스택 설명**

- 둘 다 넣고 빼고 가능. 둘 다 자료 일렬로 보관. 
- 큐: FIFO. 넣(enqueue), 빼(dequeue). 줄 서기. 
- 스택: LIFO. 넣(push), 빼(pop). 접시 쌓기. 

<br>

**회문 찾기 - 내 버전**

~~~python
def palindrome(s):
  name_list = [x.lower() for x in s if x.isalpha()]
  while len(name_list) >= 2:
    if name_list.pop(0) != name_list.pop():
      return False
  return True    
~~~

<br>

**회문 찾기 - 책 버전**

~~~python
def palindrome(s):
  qu, st = [], []
  
  for x in s:
    if x.isalpha():
      qu.append(x)
      st.append(x)
      
  while qu:
    if qu.pop(0) != st.pop():
      return False
    
  return True
~~~

**큐/스택 없이 회문 찾기**

~~~python
def palindrome(s):
  i = 0
  j = len(s) - 1

  while i < j:
    if s[i].isalpha() == False:
      i += 1
    elif s[j].isalpha() == False:
      j -= 1
    elif s[i].lower() != s[j].lower():
      return False
    else:
      i += 1
      j -= 1
~~~

<br>

**딕셔너리 몰랐던 함수 5가지**

- `len(d)`, `d[key]`, `d[key] = value`, `del d[key]`, `d.clear()`

<br>

**동명이인 with 딕셔너리**

~~~python
def find_same_name(lst):
  name_dict = {}
  for name in lst:
    if name not in name_dict:
      name_dict[name] = 1
    else:
      name_dict[name] += 1
      
  result = set()
  for name in name_dict:
    if len(name_dict[name]) >= 2:
      result.add(name)
~~~

<br>

**친구 찾기 알고리즘**

~~~Python
def print_all_friends(g, start):
  qu, done = [], set()
  
  qu.append(start)
  done.add(start)
  
  while qu:
    p = qu.pop(0)
    for x in g[p]:
      if x not in done:
        qu.append(x)
        done.add(x)
~~~

<br>

**친밀도 계산 알고리즘**

~~~python
def print_all_friends(g, start):
  qu, done = [], set()
  
  qu.append((start, 0))
  done.add(start)
  
  while qu:
    (p, d) = qu.pop(0)
    for x in g[p]:
      if x not in done:
        qu.append(x, d+1)
        done.add(x)
~~~



