# Kaggle

**Data leakage & smoothing**

- train 데이터셋 이외에 test 데이터셋이라던지 다른 데이터가 모델링 과정에서 사용되면 data leakage라 부른다.
- Data leakage 해결 위해 smoothing 기법 사용하는데, 이런게 있다 알아만 두자.

<br>

**Data visualization**

- Categorical features: 변수마다 target=1을 가지고 있는 비율 `sns.barplot()`으로 시각화.
- Interval features: heatmap 함수 `corr_heatmap()` 만들어 상관관계 파악. 파악 후 상관관계 있는 feature들은 특별히 `sns.lmplot()`으로 한번 더 시각화.
- Ordinal features: 이것 또한 heatmap 함수 사용. 하지만 별다른 상관관계 없음.

<br>

**Dummification**

- 범주형 변수들에 `pd.get_dummies()` 사용해 dummification 진행.

<br>

**PolynomialFeatures**

- Interval features에 다항식 적용. `polynomialFeatures()`로 다항식 객체 생성후 이거 사용해 변수 추가 생성.

<br>

<br>

# Machine Learning

**LogisticRegression**

- 매개변수 C값을 내리면 규제가 높아진다.
  - 규제가 높다면 가중치가 0으로 향한다.
- LR은 Ridge와 같이 L2 규제 적용 (L1 규제 적용할 때도 있음. 특성 줄이고 싶을 때).

<br>

**다중 클래스 선형 모델**

- 대부분의 선형 모델은 다중 분류를 지원하지 않음 (LogReg 제외).
- 이진 분류 선형 모델은 1클래스 vs. 나머지 클래스로 만든 boundary로 분류 (일대다 방법).

<br>

**선형 모델 장단점과 매개변수**

- 중요한 부분은 (1) 매개변수 선택, (2) 규제 선택.
  - 매개변수: 회귀 모델은 alpha, SVC와 LR은 C.
  - 규제: 특성 축소를 원한다면 L1, default는 L2.
- 선형 모델은 예측를 설명하기 쉽다. 레코드보다 특성이 많을 때 잘 작동한다. 저차원에선 일반화 성능이 떨어진다.

<br>

**나이브 베이즈 분류기**

- 선형 모델과 유사하다. 훈련 속도는 빠르지만 일반화 성능은 떨어진다.

- 종류는 `GaussianNB`, `BernoulliNB`, `MultinomialNB`가 있음.

  - `GaussianNB`는 continuous, `BernoulliNB`는 binary, discrete, `MultinomialNB`는 discrete 데이터에 적용.

  