# Algorithm

### 순차 탐색

**알고리즘**

~~~python
def seq_search(lst, a):
  lst_len = len(lst)
  for i in range(0, lst_len):
    if x == lst[i]:  # 리스트에 찾는 숫자가 있다면
      return i  # 해당 숫자의 인덱스를 리턴한다.
  return -1  # 없다면 -1을 리턴.


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(seq_search(v, 18))  # 2
print(seq_search(v, 33))  # 3
print(seq_search(v, 900))  # -1
~~~

<br>

**알고리즘 분석**

- 찾는 숫자가 리스트 맨 앞에 있다면 계산 한 번으로 끝나지만 리스트 맨 뒤나 아예 없다면 리스트의 길이만큼 계산해야 한다.
- 계산 복잡도는 보통 최악의 경우를 생각한다. 순차 탐색의 계산 복잡도는 $O(n)$.

<br><br>

# Machine Learning

**영화 리뷰에 대한 BOW**

~~~python
# 1. 영화 데이터셋으로 BOW 생성.
vect = CountVectorizer().fit(text_train)  # 훈련 데이터로 단어 사전 생성.
X_train = vect.transform(text_train)  # 생성된 사전을 바탕으로 BOW 생성.

# 2. BOW의 특성 확인하기.
feature_names = vect.get_feature_names()
print("특성 개수: {}".format(len(feature_names)))

# 3. LogisticRegression으로 교차 검증 진행.
#      CountVectorizer는 통계적 특성을 사용하지 않아 전처리와 교차 검증을 
#      한 번에 진행해도 무관.
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
scores = cross_val_score(LogisticRegression(), X_train, y_train, cv=5)
print("교차 검증 점수: {:.2f}".format(np.mean(scores)))

# 4. LogisticRegression의 그리드 서치 진행.
from sklearn.model_selection import GridSearchCV
param_grid = {"C": [0.001, 0.01, 0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X_train, y_train)
print("최상의 교차 검증 점수: {:.2f}".format(grid.best_score_))
print("최적의 매개변수: ", grid.best_params_)

# 5. 테스트셋으로 일반화.
X_test = vect.transform(text_test)
print("일반화 점수: {:.2f}".format(grid.score(X_test, y_test)))

# 6. 재설정된 조건으로 단어 사전 재생성.
vect = CountVectorizer(min_df=5).fit(text_train)
X_train = vect.transform(text_train)

# 7. 재생성된 단어 사전의 특성 확인.
feature_names = vect.get_feature_names()
print("특성 개수: {}".format(len(feature_names)))

# 8. 재생성된 훈련 데이터로 그리드 서치 재진행.
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X_train, y_train)
print("최상의 교차 검증 점수: {:.2f}".format(grid.best_score_))

'''
results:
특성 개수: 74849
교차 검증 평균 점수: 0.88
최상의 교차 검증 점수: 0.89
최적의 매개변수:  {'C': 0.1}
일반화 점수 점수: 0.87
재추출한 특성 개수: 27271
최상의 교차 검증 점수: 0.89
'''
~~~

<br>

**불용어**

- 불용어를 제거하는 방법은: 
  - 해당 언어의 불용어 전체를 제거하거나,
  - BOW에서 자주 쓰이는 단어를 제거하는 것.
- 이번엔 첫 번째 방법을 사용.

~~~python
# 1. 불용어 확인
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
print("불용어 개수: {}".format(len(ENGLISH_STOP_WORDS)))

# 2. 불용어를 제외하고 BOW 생성.
vect = CountVectorizer(min_df=5, stop_words="english").fit(text_train)
X_train = vect.transform(text_train)

# 생성된 BOW에 그리드 서치 진행.
grid = GridSearchCV(LogsticRegression(), param_grid, cv=5)
print("최상의 교차 검증 점수: {:.2f}".format(grid.best_score_))

'''result:
불용어 개수: 318
최상의 교차 검증 점수: 0.88
'''
~~~

