# Machine Learning

**군집 알고리즘 요약**

- k-means clustering, DBSCAN, 병합 군집.
- 각 알고리즘의 특징
  - k-평균 알고리즘: 클러스터 개수를 지정 가능. 클러스터 중심으로 클러스터 구분. 데이터 포인트를 클러스터 중심으로 표현할 수 있어 분해 방법이라 볼 수 있음.
  - 병합 군집: 클러스터 개수를 지정 가능. 데이터의 분할 계층도(덴드로그램) 생성 가능.
  - DBSCAN: eps를 사용해 간접적으로 클러스터의 크기를 조절할 수 있음. 이상치를 인식할 수 있음. 복잡한 클러스터 인식 가능. 클러스터마다 크기가 다를 수 있음.

<br>

**Ch 3 요약**

- 비지도학습은 탐색적 데이터 분석(EDA) 그리고 전처리 과정에서 사용될 수 있음.
- 레이블 정보가 없을 때 데이터를 효과적으로 분석할 수 있는 가장 효과적인 방법.

<br>

**범주형 변수**

- 일반적으로 연속형만 다뤘지만, 실제 변수의 전형적인 형태는 범주형.
- 범주형은 연속적이지 않고, 순서가 없고, 우열을 가릴 수 없다.
- "데이터의 구성"보다는 "데이터의 표현"이 ML 성능에 주는 영향이 더 큼.

<br>

**One-hot-encoding**

- 가변수라고도 함. 범주형 변수를 0과 1로 이루어진 한 개 이상의 특성으로 변환하는 것.
- 보통 raw dataset에서는 범주형 데이터가 있는지 확인하는게 좋다. 열의 내용을 확인하려면 `value_counts()` 사용.

> - 보통 모델링하기 전에 데이터셋에서 타깃값을 제거해야 한다. 출력 혹은 출력에서 유도된 변수를 사용하면 성능에 영향을 미친다.
>
> - 훈련 데이터, 테스트 데이터에 같은 방식(함수)을 적용해야 한다.

<br>

**숫자로 표현된 범주형 특성**

- 범주형 변수는 문자열로만 이루어진게 아니라 숫자로 인코딩된 경우도 있음.
- 해당 열을 str으로 형 변환 후 `pd.get_dummies()` 안 columns에 열 이름 명시.

<br>

**구간 분할**

- 데이터의 종류에 따라서도 표현을 다르게하지만, 어떤 모델을 사용하냐에 따라서도 표현이 달라진다.
- 효과적인 모델링을 위해 연속적 데이터를 구간 분할해 활용할 수 있음. 구간 분할된 연속형 데이터를 사용하면 강력한 선형 모델 생성 가능.
- 트리기반 모델은 한번에 여러 개의 특성을 활용할 수 있으므로 굳이 필요없음.