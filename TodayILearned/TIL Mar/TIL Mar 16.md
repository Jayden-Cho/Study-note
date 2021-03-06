# Machine Learning

**Ch 5 정리**

- 5장에서는 **교차 검증 방법**, **그리드 서치**, **평가 지표**에 대해 알아보았다.

- 초보 ML 기술자가 주의해야 할 유의 사항 두 가지.

  1. 교차 검증은 필수.

     - 테스트/검증 세트를 모델 생성이나 매개변수 선택에 사용한다면 낙관적인 결과를 만든다.

     - 보통 훈련/테스트 데이터로 분할 후 훈련 데이터에 교차 검증 적용.

  2. 모델 선택과 평가에 평가 지표가 중요하게 작용.

     - 높은 정확도만 요구하는 비즈니스 상황은 거의 없다. 평가 지표가 실제 상황을 대변할 수 있어야.
     - 실제 필드에서는 불균형한 데이터셋이 많다. 적합한 평가 지표들을 사용해야.

<br>

**Ch 6 Intro**

- 매개변수에 민감한 ML 알고리즘이 몇몇 있다.
  - 특성 스케일 조절, 특성 연결, 심지어는 비지도 학습으로 특성 생성도 한다.
  - ML 알고리즘은 이러한 여러 단계로 이루어져 있다.
- 파이프라인은 데이터 변환과 모델 생성 과정을 연결시켜준다.

<br>

**데이터 전처리와 매개변수 선택**

- 스케일 조정된 데이터로 `GridSearchCV`를 적용하면 안된다.
  - 데이터 스케일을 조정할 때 이미 검증 폴드의 정보도 사용해 지나치게 낙관적인 결과를 만든다.
  - 새로운 데이터에는 전처리 과정이 없었기 때문에 전처리 결과가 훈련 데이터와 다를 수 있다.
- 선 교차 검증, 후 전처리
  - <u>데이터셋을 사용하는 모든 처리 과정은 데이터셋의 훈련 부분에만 적용되므로 교차 검증 안에 있어야 한다.</u>

<br>

**파이프라인 구축하기**

- SVM 모델을 사용하고 데이터에 `MinMaxScaler` 전처리를 진행한다 하자.

- 파이프라인은:

  ~~~python
  pipe = Pipeline([('scaler', MinMaxScaler()), ('svm', SVC())])
  ~~~

  - `scaler`로 먼저 전처리 진행한 후에 `svm` 모델로 훈련을 한다.
  - <u>`pipe.fit()`한다면, `scaler`로 스케일링 진행하고, `svm`으로 모델을 훈련한다.</u>
  - <u>`pipe.score()`한다면, `scaler`로 테스트 세트를 변환한 후 SVM의 `score`로 평가한다.</u>

- 장점은:

  - 전처리 + 모델 생성을 위한 코드가 줄어든다.
  - `cross_val_score`나 `GridSearchCV`에 `Pipeline`을 하나의 추정기처럼 사용할 수 있다.

<br>

**그리드서치에 파이프라인 적용하기**

- 그리드서치 객체를 생성하기 위해선

  ~~~python
  param_grid = {'svc__C': [0.001, 0.01, 0.1],
               'svc__gamma': [0.001, 0.01, 0.1]}
  
  grid = GridSearchCV(pipe, param_grid=param_grid)
  ~~~

  - `param_grid`로 매개변수 그리드를 생성하고,
    - 기존에 `Pipeline` 객체 안에 명시한 모델과 매개변수명을 밑줄 두개 `__`로 연결한다.
  - 생성한 매개변수 그리드와 파이프라인 객체를 매개변수로 `GridSearchCV()` 객체를 생성.

- <u>교차 검증에서 정보 누설에 의한 영향은 전처리 종류에 따라 다르다.</u>
  - <u>검증 폴드로 데이터 스케일을 조정했다면 문제는 별로 없다.</u>
  - <u>검증 폴드로 특성을 추출하고 선택한다면 문제가 생긴다.</u>