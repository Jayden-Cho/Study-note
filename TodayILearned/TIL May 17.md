# English

**How have you been, Mr. Cho?**

- 조 선생님! 잘 지내시죠?

**Please stay healthy and happy.**

- 건강하시고 행복하세요. 

**I'm going to freshen up. **

- 저좀 씻고 올께요

**No wonder he didn't come to school. **

- 어쩐지 걔 학교 안 오더라. 

**He is a creep. **

- 그 사람 자꾸 나한테 찝쩍거려. 

**Easy-going** 사교적인

**Tidy ** 깔끔한 

**Sympathetic** 동정적인, 동정어린 

<br>

<br>

# Algorithm

**미로 찾기 알고리즘**

~~~python
def solve_maze(g, start, end):
  qu, done = [], set()
  
  qu.append(start)
  done.add(start)
  
  while qu:
    p = qu.pop(0)
    v = p[-1]
    if v == end:
      return p
   	for x in g[v]:
      if x not in done:
        qu.append(p+x)
        done.add(x)
~~~

<br>

**가짜 동전 찾기 - 하나씩 비교**

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
    if result == 1:
      return i
    
  return -1
~~~

**가짜 동전 찾기 - 두 그룹으로 나눠서 비교**

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
  
  half = (right-left+1)//2
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

<br>

**최대 수익 알고리즘 - 모두 비교**

~~~python
def find_profit(prices):
  n = len(prices)
  max_profit = 0
  for i in range(0, n-1):
    for j in range(i+1, n):
      profit = prices[j] - prices[i]
      if max_profit < profit:
        max_profit = profit
        
  return max_profit
~~~

**최대 수익 알고리즘 - 한 번씩 비교**

~~~python
def find_profit(prices):
  n = len(prices)
  min_price = prices[0]
  max_profit = 0
  for i in range(1, n):
    profit = prices[i] - min_price
    if profit > max_profit:
      max_profit = profit
    if min_price > prices[i]:
      min_price = prices[i]
      
  return max_profit
~~~

