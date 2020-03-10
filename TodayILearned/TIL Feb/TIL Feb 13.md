# Kaggle

**Removing Features with Zero Variance**

- variance가 0이거나 0에 가까우면 값들이 일정해서 특성으로써의 가치가 없다고 판단, 제거하는 것으로 보임.

- 그 과정은 `VarianceThreshold()`로 진행되고, PortoSeguro 데이터셋에는 zero variance 없으니 threshold를 1%로 맞춘다.

  - Boolean값을 toggle하기 위해 함수를 생성하는데, 신기하다.

    `np.vectorize(lambda x: not x)`

  - 생성한 `selector` 함수에 `get_support()`를 적용하면 masked 된 결과를 볼 수 있다.

<br>

**SelectFromModel**

- `VarianceThreshold`말고 `SelectFromModel`도 있음. 이건 모델 훈련해 해당 모델에서 중요한 특성을 임계치를 기준으로 추출함.
  - 여기선 임계치를 median으로 설정.

<Br>

**Feature Scaling**

- `StandardScaler()` 진행. 자세한건 다음에.

<br><br>

# Machine Learning

**나이브 베이즈의 장단점과 매개변수**

- 매개변수는 alpha. 모델의 복잡도를 조절해줌. 모델의 복잡도를 낮추기 위해 그리고 통계 데이터를 완만하게 해주기 위해(과대적합을 줄이기 위해) smoothing이라는 기법으로 무작위 positive 데이터 포인트를 추가한다.
- 장단점은 선형 모델과 유사하다.
  - `GaussianNB`는 고차원 데이터, `BernoulliNB`나 `MultinomialNB`는 희소한 데이터(텍스트)에 사용됨.
  - 장점은 훈련, 예측의 속도가 빠르고, 예측을 이해하기 쉽고, 희소 고차원 데이터에서 잘 작동하고, (비교적) 매개변수에 덜 민감하다.
  - 선형 모델에서 학습 시간이 오래 걸리는 데이터셋에 나이브 베이즈를 적용할 수 있다.

<br>

**결정 트리**

- 분류나 회귀 둘 다 적용됨.
  - Binary search tree 만든다고 보면 됨.
  - 분류에서는 leaf node의 다수 값, 회귀에서는 leaf node의 평균값.

<br>

**결정 트리 복잡도 제어**

- 깊이를 설정하지 않으면 완벽히 과대적합되어 훈련 데이터에 100% 예측도를 나타냄.
  - 사전 가지치기나 사후 가지치기를 적용해 과대적합 방지. scikit-learn에서는 사전 가지치기만 제공.

- 회귀에서는 범위 밖 데이터에 대해 예측이 어려움.
  - 마지막 데이터로 예측값이 쭉 나감.

<br>

**결정 트리 분석**

- `tree` 모듈의 `export_graphviz` 함수로 시각화 가능하다.
- 시각화로 전체 트리를 살피는 대신, `feature_importances_`를 활용해 트리를 살펴보기.



