# Chapter 10 튜플

### 튜플 개념 및 특징

**리스트(List)와 비슷한 컬렉션, 튜플(Tuple)**

리스트와의 차이는 단지 대괄호 대신 소괄호를 사용했다는 정도.

- 리스트와 같이 순서가 있어 접근 가능하고, 최대값도 찾을 수 있음.

~~~python
x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) # 'Joseph'
y = (1, 9, 2)
print(y) # (1, 9, 2)
print(max(y)) # 9
~~~

<br>

for loop에서 반복을 시키면 리스트와 같이 원소를 순서대로 출력해줌.

~~~python
for iter in y:
  print(iter)
# result:
# 1
# 9
# 2
~~~

<br>

**변경 불가능한 속성(immutable)**

리스트와 다른 특성은 값을 변경할 수 없다는 점.

~~~python
# 튜플에서 원소의 값을 변경하려 할 경우:
x = (9, 8, 7)
x[2] = 6
print(x)
# TypeError: 'tuple' object does not support item assignment
~~~

이런 특성 때문에 튜플은 리스트보다 더 효율적으로 동작함.

- 용량도 적게 차지하고, 접근도 훨씬 빠름.
- 하지만 한 번 생성된 튜플은 정렬하거나, 값을 추가하거나, 순서를 바꿀 수 없음.

~~~python
x = (3, 2, 1)
x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'
x.append(5)
# AttributeError: 'tuple' object has no attribute 'append'
x.reverse()
# AttributeError: 'tuple' object has no attribute 'reverse'
~~~

<br>

**튜플의 장점**

1. 임시 변수로 활용

~~~python
(x, y) = (4, 'fred')
print(y) # 'fred'

(a, b) = (99, 98)
print(a) # 99
~~~

<br>

함수에서 여러 개의 값을 한꺼번에 반환할 수도 있음.

~~~python
def t():
  return (10, 20)
x, y = t()
print(x, y) # 10 20
~~~

> 팁
>
> 소괄호를 사용하지 않아도 콤마(,)로 여러 값을 나열하면 파이썬에서는 튜플로 인시함.
>
> ~~~python
> x, y = 1, 10
> print(x, y) # 1 10
> 
> x, y = y, x
> print(x, y) # 10 1
> ~~~

<br>

**딕셔너리를 처리하는데 활용**

딕셔너리의 items 메소드는 딕셔너리에 저장된 각 키와 값의 한 쌍을 튜플로 이루어진 리스트 형태로 만들어줌.

~~~python
d = dict()
d['csev'] = 2
d['cwen'] = 4
for k, v in d.items():
  print(k, v)
# result:
# csev 2
# cwen 4

tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])
~~~

<br>

**여러 값에 대해 비교 가능**

각 튜플의 가장 왼쪽 값끼리 비교한 후 둘의 값이 다를 경우 나머지 값들을 비교하지 않고 큰지 작은지 여부를 판단.

- 왼쪽 값이 동일할 경우 그 다음 값으로 계속 넘어가며 비교.

~~~python
(0, 1, 2) < (5, 1, 2) # True
(0, 1, 2000) < (0, 3, 4) # True
~~~

<br>

### 튜플을 이용한 딕셔너리 정렬

**키를 기준으로 정렬하기**

1. 딕셔너리에서 items() 메소드를 실행해 튜플로 이루어진 리스트 형태로 만듦.
2. 이 리스트를 sorted 함수로 정렬. 키를 기준으로 정렬이 됨.

~~~python
d = {'b': 1, 'a': 10, 'c': 22}
d.items()
# dict_items([('b': 1), ('a': 10), ('c': 22)])
sorted(d.items())
#[('a': 10), ('b': 1), ('c': 22)]

for k, v in sorted(d.items()):
  print(k, v)
  
# a 10
# b 1
# c 22
~~~

<br>

**값을 기준으로 정렬하기**

1. 딕셔너리에서 items 메소드를 실행.
2. 튜플을 활용해 키와 값을 분리.
3. 키와 값의 위치를 바꾼 리스트 생성.
4. 생성된 리스트를 정렬.

~~~python
c = {'a':10, 'b':1, 'c':22}
temp = list() # []로 대체 가능.
for k, v in c.items():
  tmp.append((v, k))
  
print(tmp)
# [(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp)
# [(1, 'b'), (10, 'a'), (22, 'c')]

# 내림차순으로 정렬하고 싶다면:
tmp = sorted(tmp, reverse=True)
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]
~~~

<br>

**가장 많이 등장한 단어 Top 10 출력하기**

~~~python
fhand = open('Romeo.txt')
counts = {}
for line in fhand:
  words = line.split()
	for word in words:
  	counts[word] = counts.get(word, 0) + 1
 
lst = []
for k, v in counts.items():
  lst.append( (v, k) )
 
lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
  print(k, v)
~~~

<br>

**List Comprehension**

방금 작성했던 코드:

~~~python
c = {'a':10, 'b':1, 'c':22}
tmp = []

for k, v in c.items():
  tmp.append((v, k))
  
tmp = sorted(tmp)
print(tmp)
# result: [(1, 'b'), (10, 'a'), (22, 'c')]
~~~

<br>

이걸 List Comprehension으로 간단히 코딩 가능.

~~~python
c = {'a':10, 'b':1, 'c':22}
print(sorted([ (v, k) for k, v in c.items() ]))
# result: [(1, 'b'), (10, 'a'), (22, 'c')]
~~~

