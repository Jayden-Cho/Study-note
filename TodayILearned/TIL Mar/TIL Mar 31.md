# Algorithm

### 순차 탐색

**이해를 위한 순차 탐색 알고리즘**

~~~python
def find_min_idx(a):
  min_idx = 0
  for i in range(1, len(a)):
    if a[i] < a[min_idx]:
      min_idx = i
  return min_idx

def sel_sort(a):
  result = []
  while a:
  	min_idx = find_min_idx(a)
  	value = a.pop(min_idx)
  	result.append(value)
  return result
~~~

<br>

**정식 순차 탐색 알고리즘**

~~~python
def sel_sort(a):
  n = len(a)
  for i in range(0, n-1):
    min_idx = i
    for j in range(i+1, n):
      if a[j] < a[min_idx]:
        min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
~~~

<br>

**알고리즘 분석**

- 계산 복잡도는 $O(n^2)$. 
  - 같은 이름 찾기 알고리즘과 유사하게 최대 계산 횟수는 $\frac{n(n-1)}{2}$.

<br><BR>

# Python

**`ravel()` 함수를 사용하는 이유**

- 다차원 ndarray 배열을 1차원 배열(벡터)로 변환시키는 것. 배열을 평평하게 펴준다고 생각하자.

<BR><BR>

# Machine Learning

**tf-idf로 데이터 스케일 변경하기**

- tf-idf는 특성이 얼마나 의미있는지 수치로 나타낸다.
- scikit-learn에는 tf-idf에 대한 두 가지 파이썬 클래스가 구현되어 있다.
  - `TfidfTransformer`. `CountVectorizer`로 생성된 희소 행렬을 변환시킨다.
  - `TfidfVectorizer`. 텍스트 데이터로 BOW를 생성한 후 tf-idf 변환을 수행한다.

<br>

`TfidfVectorizer` 는 데이터의 통계적 특성을 사용하니 파이프라인을 사용해 그리드 서치를 진행한다.

~~~python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(TfidfVectorizer(min_df=5), LogisticRegression())
param_grid = {"logisticregression__C": [0.001, 0.01, 0.1, 1, 10]}

grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(text_train, y_train)  # TfidfVectorizer에서 BOW로 변환되기 때문에 text_train도 ㄱㅊ.
print("최상의 교차 검증 점수: {:.2f}".format(grid.best_score_))
~~~

완전한 비지도학습. 본래 목표인 감성 분석에는 영향이 없음.

- <u>대신 리뷰에 대한 구체적인 정보를 포함 할수도 있음.</u>

<br>

문장에서 중요한 특성들 찾아보기.

~~~python
vectorizer = grid.best_estimator_.named_steps["tfidfvectorizer"]
X_train = vectorizer.transform(text_train)
max_value = X_train.max(axis=0).toarray().ravel()
sorted_by_tfidf = max_value.argsort()
feature_names = np.array(vectorizer.get_feature_names())

print("tfidf가 가장 낮은 특성:\n{}".format(feature_names[sorted_by_tfidf[:20]]))
print("tfidf가 가장 높은 특성:\n{}".format(feature_names[sorted_by_tfidf[-20:]]))
~~~

<br>

idf값이 낮은 단어(<u>자주 나타나서 덜 중요하다고 생각되는 단어</u>) 확인하기.

~~~python
sorted_by_idf = np.argsort(vectorizer.idf_)
print("idf가 가장 낮은 특성:\n{}".format(feature_names[sorted_by_idf[:100]]))
~~~

- 3가지 종류: (1) 불용어, (2) 영화관련 단어("movie"), (3) 감성 단어("good", "bad")

<br>

**모델 계수 조사**

- `LogisticRegression()` 이 뭘 배웠는지 알아보기.
  - 특성 너무 많으니 극단값 20개만 조사.

<br>

**여러 단어로 만든 BOW(n-그램)**

- 일반적인 BOW는 순서를 무시. 1개 이상의 토큰을 사용해 BOW를 만든다면 순서와 문맥을 고려할 수 있음.
  - `ngram_range` 매개변수로 조절 가능.

~~~python
# 일반적인 BOW. 유니그램이라 불림.
vect = CountVectorizer(ngram_range=(1, 1)).fit(bards_words)
~~~

<br>

~~~python
# 바이그램만 생성.
vect = CountVectorizer(ngram_range=(2, 2)).fit(bards_words)
~~~

- 보통 바이그램을 자주 사용. n의 크기가 커질수록 과대적합될 확률 상승.

<br>

`pipeline`을 사용해 최적의 `ngram_range` 매개변수 찾기.

~~~python
pipe = make_pipeline(TfidfVectorizer(min_df=5), LogisticRegression())
param_grid = {'tfidfvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3)],
             'logisticregression__C': [0.001, 0.01, 0.1, 1, 10]}
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(text_train, y_train)
print("최상의 교차 검증 점수: {:.2f}".format(grid.best_score_))
print("최적의 매개변수: ", grid.best_params_)
~~~

