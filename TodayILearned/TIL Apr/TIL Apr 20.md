# Machine Learning

**`GridSearchCV()`**

- 사이킷런은 `GridSearchCV()`를 이용해 알고리즘에 사용되는 하이퍼 파라미터를 순차적으로 입력해 최적의 파라미터를 도출할 수 있는 방안을 제공한다.

~~~python
# 필요한 라이브러리 불러오기
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.metrics import accuracy_score

# 사용할 예제 붓꽃 데이터셋 불러오기
iris = load_iris()

# 붓꽃 데이터셋을 훈련/학습 데이터셋으로 분리
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=.2, random_state=121)

# 학습할 ML 알고리즘 객체 생성
dtree = DecisionTreeClassifier()

# GridSearchCV에 사용할 그리드 생성
parameters = {'max_depth': [1, 2, 3],
              'min_samples_leaf': [2, 3]}

# 생성된 그리드를 바탕으로 GridSearchCV 객체 생성
grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3)

# 붓꽃 데이터셋으로 GridSearchCV 객체 훈련
grid_dtree.fit(X_train, y_train)

# 학습된 결과 DataFrame으로 출력
cv_results = pd.DataFrame(grid_dtree.cv_results_)
cv_results[['split0_test_score', 'split1_test_score', 'split2_test_score', 'mean_test_score', 'rank_test_score']]

# 최적의 파라미터, 최고의 성능 파악
print('최적의 파라미터:',grid_dtree.best_params)
print('최고의 성능:{:.4f}', grid_dtree.best_score_)

# 학습된 객체로 테스트 데이터셋의 결과 예측
pred = grid_dtree.predict(X_test)
print('테스트 데이터셋 최고 예측 성능:{:.4f}'.format(accuracy_score(y_test, pred)))
~~~

<br>

**레이블 인코딩**

- 데이터 인코딩하는 방법은 두 가지. 레이블 인코딩과 원-핫 인코딩.
  - 레이블 인코딩은 간단하게 텍스트형 범주를 숫자로 인코딩하는 것.

~~~python
from sklearn.preprocessing import LabelEncoder

items = ['A', 'B', 'C', 'C', 'D', 'E', 'E', 'A']

# LabelEncoder 객체 생성
encoder = LabelEncoder()

# 생성된 객체 훈련
encoder.fit(items)

# 훈련시킨 객체로 주어진 레이블을 변환
labels = encoder.transform(items)

print('인코딩 클래스:', encoder.classes_)
print('디코딩 클래스:', encoder.inverse_transform([1, 3, 2, 4, 2, 2, 5, 4]))
~~~

