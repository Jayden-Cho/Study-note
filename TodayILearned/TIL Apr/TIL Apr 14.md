# Algorithm

### 가짜 동전 찾기

**하나씩 비교하기**

~~~python
def weigh(a, b, c, d):
  fake = 29
  if a <= fake and fake <= b:
    return -1
  if c <= fake and fake <= d:
    return 1
	return 0

def find_fakecoin(left, right):
  for i in range(left+1, right+1):
    result = weigh(left, left, i, i)
    if result == -1:
      return left
    elif result == 1:
      return i
    
  return -1
~~~

<br>

**반씩 그룹으로 나눠 비교하기**

~~~python
def weigh(a, b, c, d):
  fake = 29
  if a <= fake and fake <= b:
    return -1
  if c <= fake and fake <= d:
    return 1
  return 0

def find_fakecoin(left, right):
  if left == right:
    return left
  
  half = (right - left +1 ) // 2
  g1_left = left
  g1_right = left + half - 1
  g2_left = left + half
  g2_right = g2_left + half - 1
  
  result = weigh(g1_left, g1_right, g2_left, g2_right)
  if result == -1:
    return find_fakecoin(g1_left, g1_right)
  elif result == 1:
    return find_fakecoin(g2_left, g2_right)
  else:
    return right
~~~

