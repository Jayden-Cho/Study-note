# Algorithm

### 병합 정렬

**이해하기 쉬운 병합 정렬 알고리즘**

~~~python
def merge_sort(a):
  n = len(a)
  result = []
  if n <= 1:
    return a
  mid = n // 2
  g1 = merge_sort(a[:mid])
  g2 = merge_sort(a[mid:])
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

**일반적인 병합 정렬 알고리즘**

~~~python
def merge_sort(a):
  n = len(a)
  if n <= 1:
    return
  mid = n // 2
  g1 = a[:mid]
  g2 = a[mid:]
  merge_sort(g1)
  merge_sort(g2)
  i1 = 0
  i2 = 0
  ia = 0
  while i1 < len(g1) and i2 < len(g1):
    if g1[i1] < g2[i2]:
      a[ia] = g1[i1]
      ia += 1
      i1 += 1
    else:
      a[ia] = g2[i2]
      ia += 1
      i2 += 1
  while i1 < len(g1):
    a[ia] = g1[i1]
    ia += 1
    i1 += 1
  while i2 < len(g2):
    a[ia] = g2[i2]
    ia += 1
    i2 += 1
~~~

<br>

**알고리즘 분석**

- 계산 복잡도는 $O(n \cdot \log n)$. 이전의 정렬 알고리즘들보다 계산 복잡도가 낮다.

<br><br>

# NumPy

**슬라이싱, 팬시 인덱싱, 불린 인덱싱**

~~~python
array = np.arange(1, 10).reshape(3, 3)
print('원본 행렬:\n', array)
print('슬라이싱:\n', array[0:2, 1])
print('팬시 인덱싱:\n', array[1:2, [0, 1]])
print('불린 인덱싱:\n', array[array<5])

'''result:
원본 행렬:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
슬라이싱:
 [2 5]
팬시 인덱싱:
 [[4 5]]
불린 인덱싱:
 [1 2 3 4]'''
~~~

<br>

**`sort()`, `argsort()`**

- `sort()` 의 종류는 두 가지. `np.sort()` 와 `ndarray.sort()`.
  - `ndarray.sort()` 는 기존 행렬에 정렬을 적용하고, `np.sort()` 는 정렬된 새로운 행렬을 생성한다.

~~~python
array = np.array([5, 2, 9, 1])
sorted_array = np.sort(array)  # 정렬된 새 행렬이 생김.
print('sorted_array:', sorted_array)
array.sort()  # 기존 행렬에 정렬이 적용됨.
print('sorted_array:', array)
~~~

<br>

내림차순을 적용하려면 기존의 코드에 `[::-1]` 을 적용한다.

~~~python
sorted_array_desc = np.sort(array)[::-1]
print(sorted_array_desc)

'''
result:
[9 5 2 1]
'''
~~~

<br>

2차원 이상의 행렬에선 axis 매개변수를 사용해 row, col 방향으로 정렬할 수 있다.

~~~python
array = np.array([3, 6, 8, 1, 4, 7, 2, 5, 9]).reshape(3, 3)
print('행 방향으로 정렬된 행렬:\n', np.sort(array, axis=0))
print('열 방향으로 정렬된 행렬:\n', np.sort(array, axis=1))

'''
result:
행 방향으로 정렬된 행렬:
 [[1 4 7]
 [2 5 8]
 [3 6 9]]
열 방향으로 정렬된 행렬:
 [[3 6 8]
 [1 4 7]
 [2 5 9]]
 '''
~~~

<br>

`np.argsort()` 는 정렬된 기존 행렬의 인덱스를 구하고 싶을 때 사용한다.

- 메타 데이터를 생성할 수 없는 넘파이에서 `np.argsort()` 가 메타 데이터의 역할을 대체한다.

~~~python
name_array = np.array(['John', 'Mike', 'Sam'])
score_array = np.array([95, 74, 86])

sorted_score_idx = np.argsort(score_array)
print('sorted_score_idx:', sorted_score_idx)
print('sorted_name:', name_array[sorted_score_idx])

'''
result:
sorted_score_idx: [1 2 0]
sorted_name: ['Mike' 'Sam' 'John']
'''
~~~

<br>

**선형대수 연산 - 내적과 전치 행렬**

~~~python
# 내적
a = np.array([[1, 2],
             [3, 4]])
b = np.array([[5, 6],
             [7, 8]])

print('내적:\n', np.dot(a, b))

'''result:
내적:
 [[19 22]
 [43 50]]'''
~~~

~~~python
# 전치 행렬
a = np.array([[1, 2],
             [3, 4]])

print('전치 행렬:\n', np.transpose(a))

'''result:
전치 행렬:
 [[1 3]
 [2 4]]'''
~~~

