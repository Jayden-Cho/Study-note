# Algorithm

### 삽입 정렬

**이해하기 쉬운 삽입 정렬 알고리즘**

~~~python
def find_ins_idx(a, v):
  for i in range(0, len(a)):
    if v < a[i]:
      return i
  return len(a)

def ins_sort(a):
  result = []
  while a:
    value = a.pop(0)
    ins_idx = find_ins_idx(result, value)
  	result.insert(ins_idx, value)
  return result
~~~

<br>

**일반적인 삽입 정렬 알고리즘**

~~~python 
def ins_sort(a):
  n = len(a)
  for i in range(1, n):
    key = a[i]
    j = i-1
    while j>=0 and a[j]>key:
      a[j+1] = a[i]
      j -= 1
    a[j+1] = key
    
# 두 가지 경우.
# 1. 앞 숫자가 key보다 작다면 그 자리에.
# 2. 앞 숫자가 key보다 크다면 뒤로 보냄 (내 자리로)
~~~

<br>

**알고리즘 분석**

- 계산 복잡도의 최상의 경우는 리스트가 정렬된 경우. $O(n)$.
- 보통 삽입 정렬의 계산 복잡도는 선택 정렬과 같이 $O(n^2)$.

<br><br>

# NumPy

**넘파이 ndarray 개요**

- ndarray는 넘파이의 기본 데이터 타입.

- `array()`함수로 리스트를 ndarray 형태로 변환 가능하다.

~~~python 
array = np.array([1, 2, 3])
print(array, type(array))

'''
result:
[1 2 3] <class 'numpy.ndarray'>
'''
~~~

<br>

<u>두 ndarray를 살펴보자.</u>

~~~python
a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2, 3]])
print('a1 shape:',a1.shape, '\na2 shape:',a2.shape)

'''
result:
a1 shape: (3,) 
a2 shape: (1, 3)
'''
~~~

<u>두 ndarray의 shape 차이를 이해하는 것이 중요하다. 같은 값이라도 차원이 달라 오류가 생기는 경우가 많이 있다.</u>

<br>

**ndarray의 데이터 타입**

- 숫자형, 문자열, 불린값 등 모든 자료형이 가능하다. 단, **한 ndarray에 하나의 자료형만 가능하다**.
- 두 가지 이상의 자료형을 가진 리스트를 ndarray로 변환한다면, 가장 큰 데이터 타입으로 변환을 일괄 적용한다.
  - `astype()`메서드로 ndarray 전체 자료형을 변환할 수 있다. <u>보통 메모리를 절약해야 할 때 사용된다.</u>

~~~python
lst = [1, 2, 'test']
array = np.array(lst)
print(array, array.dtype)

'''
result:
['1' '2' 'test'] <U21
'''
~~~

<br>

**arange(), zeros(), ones()**



~~~python
seq_array = np.arange(10)
print(seq_array)
print(seq_array.dtype, seq_array.shape)

'''
result:
[0 1 2 3 4 5 6 7 8 9]
int64 (10,)
'''
~~~

`arange()`는 array를 `range()`화 한다고 생각하자.

<br>

~~~python
zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

'''
result:
[[0 0]
 [0 0]
 [0 0]]
int32 (3, 2)
'''
~~~

`zeros()`와 `ones()`는 튜플 인자를 크기로 받아 ndarray를 각각 0과 1로 채운다.

- <u>함수 인자로 `dtype`을 정하지 않으면 float64 형태로 ndarray을 채운다.</u>

<br>

**reshape()**

- ndarray를 특정 차원 및 크기로 변환한다. 지정된 사이즈로 변경할 수 없다면 오류를 발생한다.
- 보통 -1 인자를 적용해 사용한다. -1을 인자로 활용하면 ndarray와 호환되는 새로운 shape으로 변환한다.

~~~python
array = np.arange(10)
print(array)
array2 = array.reshape(-1, 5)  # 10개의 데이터를 2개의 row, 5개의 column에 할당.
print('array2 shape:', array2.shape)
array3 = array.reshape(5, -1)  # 10개의 데이터를 5개의 row, 2개의 column에 할당.
print('array3 shape:', array3.shape)

'''
result:
[0 1 2 3 4 5 6 7 8 9]
array2 shape: (2, 5)
array3 shape: (5, 2)
'''
~~~



<br>

**인덱싱 - 단일 값 인덱싱**

- 보통 인덱싱과 동일하다. 단, 2차원 이상에서는 좌표찍는거라 생각하자.
- 주목해야 할 부분은 **axis**.
  - axis0, axis1은 각각 로우, 컬럼을 의미한다. 하지만, 로우와 컬럼은 ndarray에선 사용하지 않는 방식이다.
  - ndarray는 축에 따른 연산을 지원하기 때문에 axis0, axis1은 꼭 알아두자.