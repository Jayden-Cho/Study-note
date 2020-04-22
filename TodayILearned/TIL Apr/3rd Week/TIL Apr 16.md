#  Algorithm

### 최대 수익 알고리즘

~~~Python
stock = [10300, 9600, 9800, 8200, 7800, 9500, 9800, 10200, 9500]
~~~



**방법 1: 가능한 모든 경우를 비교하기**

~~~python
def max_profit(prices):
  n = len(prices)
  max_profit = 0
  
  for i in range(0, n-1):
    for j in range(i+1, n):
      profit = prices[j] - prices[i]
      if profit > max_profit:
        max_profit = profit
  return max_profit
~~~

<br>

**방법 2: 한 번 반복으로 최대 수익 찾기**

~~~python
def max_profit(prices):
  n = len(prices)
  max_profit = 0
  min_price = prices[0]
  
  for i in range(1, n):
    profit = prices[i] - min_price
    if profit > max_profit:
      max_profit = profit
    if min_price > prices[i]:
      min_price = prices[i] 
  return max_profit
~~~

<br>

**알고리즘 분석**

- 방법 1의 계산 복잡도는 문제 3과 동일한 $O(n^2)$.
- 방법 2의 계산 복잡도는 $O(n)$.

<br>

<Br>

# Machine Learning

**교차 검증**

- 교차 검증은 본고사 전에 치르는 여러 번의 모의고사같은 개념.
  - 본고사가 테스트 세트에 대해 평가하는 것이라면, 모의고사는 학습, 검증 세트에서 알고리즘 학습과 평가를 수행하는 것.

<br>

**KFold 교차 검증**

- K개의 데이터 폴드 세트를 만들어 K번 만큼 각 폴드 세트에 학습, 검증을 반복적으로 수행하는 방법.

<br>

**계층별 교차 검증**

- StratifiedKFold. 불균형한 분포를 가진 레이블 데이터 집합을 위한 KFold 방식.

<br>

**cross_val_score()**

- 교차 검증을 간단히 하기 위한 API.
- `cross_val_score()` 수행 후 반환값은 `scoring` 파라미터로 지정된 성능 지표 측정값을 배열 형태로 반환한다.
  - classifier에서는 계층별 교차 검증, regressor에선 일반 교차 검증을 진행한다.
- 일반적으로 반환된 배열을 평균해 평가 수치로 사용한다.
- <u>비슷한 API로 `cross_validate()`가 있다.</u>
  - 한 번에 여러 평가 지표를 반환할 수 있고, 수행 시간도 같이 제공한다.
    