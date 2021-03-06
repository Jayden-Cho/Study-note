# Machine Learning

**신경망의 장단점과 매개변수**

- 장점: 많은 데이터와 충분한 시간이 있으면 매우 복잡한 모델을 생성할 수 있다.
- 단점: 시간이 너무 많이 소요되고, 특성의 스케일에 민감하다.
- 매개변수: 은닉층 수, 은닉 유닛 수, alpha.

<br>

**신경망의 복잡도 추정**

- 은닉층/은닉 유닛의 수가 늘어날수록 복잡도가 크게 올라간다.
- 훈련 과정은 보통 충분히 과대적합된 모델을 만들고, 은닉층 축소나 alpha를 통한 규제로 일반화 성능을 향상시킨다.

<br>

**분류 예측의 불확실성 추정**

새 데이터의 예측도 중요하지만, 예측에 대한 확실성도 중요하다. scikit-learn에서 확실성 측정방법은 크게 `decision_function` 과 `predict_proba` 가 있다.

- `decision_function`
  - 새 데이터가 양성 클래스에 속한다고 믿는 정도.
  - 이진 분류에서의 크기는 (n_samples, ), 다중 분류에선 (n_samples, n_classes).
  - 출력 범위가 임의의 값이라 이해하기 어렵다.
- `predict_proba`
  - 각 클래스에 대한 출력.
  - 이진 분류 / 다중 분류 모두 출력의 크기는 (n_samples, n_classes)로 같다.
  - `decision_function` 에  비해 이해하기 쉽다.