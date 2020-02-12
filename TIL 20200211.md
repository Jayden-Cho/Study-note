## Kaggle

#### metadata 생성

- metadata를 생성해두면 feature 추출할 때 편리. 여기선 metadata에 type(role), level, keep, dtype.
- `pd.DataFrame()` 안 data에는 dict나 ndarray가 주로 들어감.

<br>

#### Descriptive Statistics

- 변수의 범위가 너무 크다면 scaling (e.g. `StandardScaler`) 진행.

<br>

#### Undersampling

- PortoSeguro dataset은 데이터가 많으므로 undersampling 진행.
- 작은 데이터에 목표 비율을 맞추고 거기에 맞춘다.

<br>

#### Impute

- `from impute import SimpleImputer` 로 바뀜.

<br><br>



