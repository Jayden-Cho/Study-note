# Machine Learning

**그룹별 교차 검증**

- 데이터 안에 연관된 그룹들이 있을 때도 교차 검증을 사용한다. 하지만 기존의 계층별 교차 검증 방법으로는 제대로 된 평가가 어렵다.
- 얼굴 표정을 인식하는 프로그램을 예로 들자. 100명에 대한 표정 데이터가 있을 때, 새 표정을 분류하는 것이 목표.
  - 훈련 데이터에 있는 얼굴은 새 얼굴보다 쉽게 식별할 수 있어 일반화 성능 평가에 영향을 미침.
  - 그러므로 훈련/테스트 세트에 서로 다른 사람의 사진이 들어가야 한다.
- 이 경우 **GroupKFold**를 사용한다.
  - groups 매개변수에 따로 그룹을 지정한다.
  - groups는 데이터 레이블이 아니라 같은 그룹끼리 묶어놓은 배열.
  - <u>group 매개변수 내 배열을 정렬할 필요는 없다.</u>
- 의료, 음악 데이터 분야에 자주 쓰인다.
  - 같은 환자(그룹)의 데이터를 묶어두기.

<br>

**그리드 서치**

- 이제는 일반화 성능 향상시키는 법 배우기.
- 그리드 서치는 가능한 모든 매개변수 조합해 최고 성능 내는 매개변수 선택하는 것.
- 기존의 훈련+테스트 데이터 방식은 테스트 데이터에 정보 누출이 있어 제대로 성능 평가가 어려움.
  - 훈련 데이터로 훈련시키고 테스트 데이터로 매개변수를 찾았기 때문에, 모델을 평가할 데이터가 없는 것.
- 훈련, 테스트 데이터이외에 검증 데이터로 나눠야.
  - 데이터셋을 `train_test_split()` 로 훈련검정, 테스트로 나누고,
  - 훈련검정을 다시 `train_test_split()`로 훈련, 검정으로 나눈다.
  - 훈련으로 데이터를 훈련시키고, 검정으로 그리드 서치 진행해 최적 매개변수 찾기.
  - 찾은 최적 매개변수로 추정기 생성 후 훈련검정 데이터로 훈련시키고, 테스트로 성능 평가.
