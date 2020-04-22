

# Algorithm

### 미로 찾기 알고리즘

**문제 분석과 모델링**

- 사람이 풀면 간단하지만 컴퓨터는 다르다.
- 문제를 모델링해 컴퓨터가 이해할 수 있도록 번역한다.
  - 문제를 그래프로, 그래프를 프로그래밍 언어로 변환한다.

<br>

**미로 찾기 알고리즘**

~~~python
def solve_maze(g, start, end):
  qu = []
  done = set()
  
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
        
	return "?"
~~~

<br><br>

# Pandas

**`apply lambda`를 활용한 데이터 가공**

- 복잡한 데이터 가공이 필요할 땐 `lambda`를 사용한다. `lambda`는 파이썬에 함수형 프로그래밍을 지원하기 위해 만들어졌다.

~~~python
titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x: len(x))
~~~

<br>

- if, else를 사용해 복잡한 가공이 가능하다.

~~~ python
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x: 'Adult' if x>=20 else 'Child')
~~~

<br>

- else if는 지원되지 않지만 구현할 수는 있다. 너무 많은거 같다 싶으면 별도의 함수를 구현하자.

~~~python
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x: 'Child' if x<=20 else('Elderly' if x>=60 else 'Adult'))
~~~

<br><br>

# Machine Learning

**붓꽃 품종 예측하기**

- <u>분류는 대표적인 지도학습 방법.</u>
  - <u>데이터의 피처와 레이블로 모델을 학습한 뒤, 테스트셋에서 미지의 레이블을 예측.</u>
- 붓꽃 데이터셋을 불러오고, 데이터셋을 나누고, ML 알고리즘을 불러와 훈련, 예측, 평가한다.

~~~python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
iris_data = iris.data
iris_label = iris.target

iris_df = pd.DataFrame(iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label,
                                                   test_size=.2, random_state=11)

dt_clf = DecisionTreeClassifier(random_state=11)
dt_clf.fit(X_train, y_train)

pred = dt_clf.predict(X_test)

print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, pred)))
~~~

<br>**Estimator 이해 및 `fit()`, `predict()` 메서드**

- Estimator는 `fit()`, `predict()`, 비지도학습 알고리즘은 `fit()`, `transform()`이 기본적으로 내장되어 있다.

<br>

**내장된 예제 데이터셋**

- 사이킷런에 내장된 분류/회귀 데이터셋은 보통 `data`, `target`, `target_names`, `feature_names`, `DESCR` 키로 구성되어 있는 딕셔너리.
- `load_iris()`의 tpye 반환 결과는 sklearn.util.Bunch 객체를 반환한다.
  - Bunch 클래스는 딕셔너리 자료형과 유사하다. 위에 쓰인 Key로 value를 불러올 수 있다.