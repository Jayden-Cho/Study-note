# Machine Learning

**타이타닉**

~~~python
import pandas as pd
from sklearn.model_selection import train_test_split

# 타이타닉 데이터 불러오기
titanic_df = pd.read_csv('train.csv')

# 결측값 채우기
def fillna(df):
  df['Age'].fillna(df['Age'].mean(), inplace=True)
  df['Cabin'].fillna('N', inplace=True)
  df['Embarked'].fillna('N', inplace=True)
  return df

# 불필요한 피처 제거
def drop_features(df):
  df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
  return df

# 레이블 인코딩
def format_features(df):
  df['Cabin'] = df['Cabin'].str[:1]
  features = ['Cabin', 'Sex', 'Embarked']
  for feature in features:
    le = LabelEncoder()
    le = le.fit(df[feature])
    df[feature] = le.transform(df[feature])
  return df

# 위의 전처리 함수들 호출
def transform_features(df):
  df = fillna(df)
  df = drop_features(df)
  df = format_features(df)
  return df

# 원본 데이터를 재로딩하고, 피처 데이터셋과 레이블 데이터셋으로 나누기
titanic_df = pd.read_csv('train.csv')
y_titanic_df = titanic_df['Survived']
X_titanic_df = titanic_df.drop('Survived', axis=1)

X_titanic_df = transform_features(X_titanic_df)
    
# 데이터셋을 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X_titanic_df, y_titanic_df, test_size=.2, random_state=11)

# DecisionTreeClassifier로 타이타닉 생존자 예측.
from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier()


# GridSearchCV로 최적의 파라미터를 찾고 예측 성능을 측정.
from sklearn.model_selection import GridSearchCV

parameters = {'max_depth': [2, 3, 5, 10],
              'min_samples_split': [2, 3, 5],
              'min_samples_leaf': [1, 5, 8]}

grid_dclf = GridSearchCV(dt_clf, parameters, scoring='accuracy', cv=5)
grid_dclf.fit(X_train, y_train)

best_dclf = grid_dclf.best_estimator_
dpredictions = best_dclf.predict(X_test)
accuracy = accuracy_score(y_test, dpredictions)

print(accuracy)
~~~

<br>

**정리**

- ML 어플리케이션의 과정은 총 네 단계.
  - 전처리 작업 - 데이터의 가공 및 변환 과정
  - 데이터 분리 작업 - 데이터를 학습 / 테스트 데이터로 분리
  - 예측 - 학습된 모델을 기반으로 테스트 데이터에 대한 예측
  - 평가 - 예측값과 실제값을 비교, ML 모델에 대한 평가.

- 전처리 작업은 크게,
  - 데이터 클렌징 - 오류 데이터 보정, 결손값 처리
  - 인코딩 - 레이블 인코딩 / 원-핫 인코딩
  - 데이터 스케일링 / 정규화
- ML 모델은 학습 데이터로 학습한 뒤 별도의 테스트 데이터셋으로 평가되어야 한다.
  - 이를 위해 데이터를 여러 개의 폴드로 나눠 교차 검증을 진행한다.

