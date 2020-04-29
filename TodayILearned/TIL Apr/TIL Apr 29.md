# Machine Learning

**결정 트리**

- 결정 트리는 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 트리 기반의 분류 규칙을 만드는 것.

- 최대한 균일한 데이터셋을 구성할 수 있도록 분할하는 것이 중요하다.

<br>

**정보의 균일도 측정**

- 균일도를 측정하는 방법은 **정보 이득 지수**와 **지니 계수**가 있다.
  - 정보 이득 지수는 1- 엔트로피 지수. 엔트로피는 데이터가 복잡할수록 높다. 
  - 지니 계수는 낮을수록 데이터 균일도가 높다. 지니 계수가 낮은 속성을 기준으로 분할한다.
- `DecisionTreeClassifier` 는 지니 계수를 이요해 데이터셋을 분할한다.

<br>

**결정 트리 모델의 특징**

- 장점
  - 시각화로 표현할 수 있다.
  - 피처 스케일링이나 정규화 같은 전처리 작업이 필요 없다.
- 단점
  - 과적합으로 정확도가 떨어질 수 있다.

<br>

**결정 트리 파라미터**

- `min_samples_split`: 노드 분할에 필요한 최소 샘플 수.
- `min_samples_leaf`: 리프가 되기 위한 최소 샘플 수.
  - 불균형 데이터의 경우 특정 클래스의 데이터 개수가 작을 수 있으므로 작게 설정해야 한다.
- `max_features`: 최적의 분할을 위해 고려할 최대 피쳐 개수.
  - `sqrt`, `auto`, `log`, `None` , 또는 int형, float형을 사용할 수 있다.
- `max_depth`: 트리의 최대 깊이를 규정.
- `max_leaf_nodes`: 리프의 최대 개수.

<br>

**결정 트리 모델의 시각화**

- `Graphviz` 패키지를 사용하면 결정 트리를 시각화할 수 있다.

~~~python
# 붓꽃 데이터셋에 결정 트리를 적용하고 시각화해보자.
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# DTC 객체 생성
dt_clf = DecisionTreeClassifier(random_state=156)

# 붓꽃 데이터를 로딩하고, 학습/테스트 데이터셋으로 분리
iris_data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=11)

# DecisionTreeClassifier 학습.
dt_clf.fit(X_train, y_train)
~~~

<br>

- `export_graphviz()` 는 `Graphviz` 가 읽어 들여 그래프 형태로 시각화할 수 있는 출력 파일을 생성한다.
  - 인자로 (1) Estimator, (2) Output 파일명, (3) 결정 클래스 명칭, (4) 피처의 명칭.

~~~python
from sklearn.tree import export_graphviz

# export_graphviz()의 호출 결과로 out_file로 지정된 tree.dot 파일을 생성한다.
export_graphviz(dt_clf, out_file='tree.dot', class_names=iris_data.target_names, feature_names=iris_data.feature_names, impurity=True, filled=True)

import graphviz
# 위에서 생성된 tree.dot 파일을 Graphviz가 읽어서 시각화.
with open("tree.dot") as f:
  dot_graph = f.read()
 graphviz.Source(dot_graph)
~~~

<br>

각 노드의 색깔은 붓꽃 데이터의 레이블 값을 의미한다.

- 색깔이 짙어질수록 지니 계수가 낮고 해당 레이블에 속하는 샘플 데이터가 많다는  뜻.

<br>

결정 트리는 피처의 중요한 지표를 `feature_importances_` 속성으로 제공한다.

- Ndarray 형태로 값을 반환하고 피처 순서대로 값이 할당된다.

~~~python
# 붓꽃 데이터셋에서 피쳐별로 결정 트리 알고리즘에서 중요도를 추출해보자.
import seaborn as sns
import numpy as np
%matplotlib inline

# feature importance 추출
print("Feature importances:\n{}".format(np.round(dt_clf.feature_importances_, 3)))

# feature별 importance 매핑
for name, value in zip(iris_data.feature_names, dt_clf.feature_importances_):
  print('{}: {:.3f}'.format(name, value))
  
# feature importance를 column 별로 시각화하기
sns.barplot(x=dt_clf.feature_importances, y=iris_data.feature_names)
~~~

