# Prob & Stats

**Quantitative Data with Graphs**

- Frequency table, dot plots, histogram, and stem and leaf plots.

<br>

**Describing Distributions**

- Comparing center and spread.
- Symmetrical, skewness, graph interpretation skills.

<br><br>

# Algorithm

### 하노이의 탑

n개의 원반을 가장 왼쪽에서 가장 오른쪽으로 옮기기.

<br>

**하노이의 탑 알고리즘**

~~~python
def hanoi(n, from_pos, to_pos, aux_pos):
  if n == 1:
    print(from_pos, "->", to_pos)
    return
  
  hanoi(n-1, from_pos, aux_pos, to_pos)
  print(from_pos, "->", to_pos)
  hanoi(n-1, aux_pos, to_pos, from_pos)
~~~

<br>

**알고리즘 분석**

- 계산복잡도는 $O(2^n)$. 입력 크기(탑의 층수)가 클수록 원반을 더 많이 움직여야 한다.

<br><br>

# Kaggle

### Home Credit Default Risk

**Missing Values**

- ML 모델이 제대로 작동하기 위해서는 missing value를 채워야 한다 (Imputation).
  - XgBoost처럼 Imputation 없이 구현 되는 모델도 있긴 하다.
- Missing value 비율이 높은 feature를 제거하는 방법도 있는데, 해당 feature의 중요도를 아직 모르므로 들고 간다.

<br>

**Column Types**

- 각 컬럼별 자료형을 확인하려면,

  ~~~python
  app_train.dtypes.value_counts()
  ~~~

  - 이 데이터셋에는 numeric value인 `int64`, `float64`와 categorical feature인 `string`이 있다.

- Categorical feature 내 category 개수를 확인하려면,

  ~~~python
  app_train.select_dtypes("object").apply(pd.Series.nunique, axis=1)
  ~~~
  - <u>대부분 작은 카테고리를 지니고 있다. Categorical feature를 처리할 방법을 알아보자.</u>

<br>

**Dealing with Categorical Features**

- 대부분의 ML 모델들은 categorical feature를 처리하지 못한다. 컴퓨터가 해석할 수 있도록 encode 해야 한다.
  - LightGBM처럼 필요 없는 모델도 있긴 하다.
- Categorical feature를 수치로 변환하는 방법은 크게 두 가지.
  - **Label encoding**: Category에 무작위 정수를 부여한다. 새 column을 생성하지 않는다.
  - **One-hot encoding**: Feature 내 category 개수만큼 column을 생성한다. 0 or 1.