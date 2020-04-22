# Machine Learning

**One-Hot Encoding**

- 피처의 개수만큼 새로운 피처를 추가해 해당하는 칼럼에는 1, 나머지 칼럼에는 0으로 표시하는 방법.
- Pandas에는 `get_dummies()` 를 사용하면 쉽게 원-핫 인코딩이 가능하다.

~~~python
import pandas as pd

df = pd.DataFrame({'item': ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']})
pd.get_dummies(df)
~~~

<br>

**Feature Scaling**

- 피처 스케일링에는 크게 두 가지가 있는데, 바로 표준화와 정규화.

  - 표준화는 데이터를 가우시안 정규 분포(평균0, 분산1)에 맞게 변환시키는 것.

  $$
  x=\frac{x_i-\bar{x}}{std(x)}
  $$

  - 정규화는 데이터의 크기를 같은 단위로 변경하는 것.
    $$
    x = \frac{x_i-min(x)}{max(x)-min(x)}
    $$

<br>

**StandardScaler**

- 가우시안 정규 분포는 몇몇 알고리즘(SVM, 선형 회귀, 로지스틱 회귀)에게 중요하게 작용한다.

~~~python
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import StandardScaler

iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

scaler = StandardScaler()
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
~~~

<br>

**MinMaxScaler**

- `MinMaxScaler` 는 데이터 값을 0과 1(음수라면 -1에서 1)로 변환한다.

~~~python
# MinMaxScaler 객체 생성
scaler = MinMaxScaler()

# 객체에 fit(), transform() 적용.
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

# 변환된 값 DataFrame으로 변환
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)

print('feature들의 최솟값')
print(iris_df_scaled.min())
print('\nfeature들의 최댓값')
print(iris_df_scaled.max())
~~~

<br>

**학습 데이터와 테스트 데이터의 스케일링 변환 시 유의점**

- 학습 데이터에는 `fit_transform()` 을 적용해도 되지만, 테스트 데이터에는 적용하면 안된다.
- 서로 다른 기준으로 `fit()`을 적용하게 된다면 스케일링 기준 정보가 달라지기 대문에 올바른 예측 결과를 도출하지 못할 수 있다.

<br>

**타이타닉 생존자 예측**

~~~python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 타이타닉 탑승자 정보 불러오기
titanic_df = pd.read_csv('train.csv')

# null값 대체하기
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Cabin'].fillna('N', inplace=True)
titanic_df['Embarked'].fillna('N', inplace=True)

# Cabin 속성의 앞 글자 추출하기
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]

# LabelEncoder로 문자열 피처들을 숫자형 피처로 변환.
def encode_features(dataDF):
  features = ['Cabin', 'Sex', 'Embarked']
  for feature in features:
    le = LabelEncoder()
    le = le.fit(dataDF(feature))
    dataDF[feature] = le.transform(dataDF[feature])
	return dataDF

titanic_df = encode_features(titanic_df)
~~~

<br>

이 내용을 하나의 함수로 정리하자.

~~~python
# Null 처리 함수
def fillna(df):
  df['Age'].fillna(df['Age'].mean(), inplace=True)
  df['Cabin'].fillna('N', inplace=True)
  df['Embarked'].fillna('N', inplace=True)
  return df

# ML 알고리즘에 불필요한 속성 제거
def drop_features(df):
  df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
  return df

# 레이블 인코딩 수행
def format_features(df):
  df['Cabin'] = df['Cabin'].str[:1]
  features = ['Cabin', 'Sex', 'Embarked']
  for feature in features:
    le = LabelEncoder()
    le = le.fit(df[feature])
    df[feature] = le.transform(df[feature])
  return df

# 앞에서 설정한 데이터 전처리 함수들 호출
def transform_features(df):
  df = fillna(df)
  df = drop_features(df)
  df = format_features(df)
  return df
~~~

