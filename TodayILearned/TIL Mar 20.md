# Algorithm

### 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만드시오.

**재귀 호출**

- 재귀 호출은 어떤 함수 안에서 자기 자신을 부르는 것.
- 대신, 종료 조건이 필요하다. `return` 을 사용해 종료 조건의 결괏값부터 돌려준다.

<br>

**팩토리얼 알고리즘**

~~~python
# for loop을 사용한 팩토리얼 알고리즘
def fact(n):
  total = 1
  for i in range(1, n+1):
    total *= i 
  return total
~~~

~~~python
# 재귀 호출을 사용한 팩토리얼 알고리즘
def fact2(n):
  if n <= 1:
    return 1
  return n * fact2(n-1)
~~~

<br>

**알고리즘 분석**

- <u>for 반복문을 이용한 프로그램의 경우 n!을 구하려면 곱셈이 n번 필요하다.</u>
- <u>재귀 호출 알고리즘은 n!을 구하려면 곱셈이 n-1이 필요하다.</u>
  - <u>큰 수에서는 n이나 n-1이나 차이 없다. 두 경우 모두 계산복잡도는 $O(n)$.</u>

**연습 문제**

~~~python
# 1부터 n까지의 합을 구하는 알고리즘을 재귀 호출로 구현하기
def sumFact(n):
  if n == 1:
    return 1
  return n + sumFact(n-1)
~~~

~~~ python
# n개의 숫자 중 최댓값을 구하는 알고리즘을 재귀 호출로 구현하기
def findMaxRecur(a, n):
  if n == 1:
    return a[0]
  maxNum = findMaxRecur(a, n-1)
  if maxNum > a[n-1]:
    return maxNum
  else:
    return a[n-1]
~~~

