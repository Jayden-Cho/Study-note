# Machine Learning

**피마 인디언 당뇨병 데이터셋**



차례

- 데이터 불러오기 (+Colab)
- 필요한 모듈 import, DataFrame 생성
- 피처 타입과 Null 개수 살펴보기 (`info()`)
- 로지스틱 회귀 객체 생성 후 예측 수행하고 성능 평가 지표 출력 & 재현율 곡선 시각화
- 임계값 조절 전에 피처 값 분포도 살펴보기(`describe()`)
- Glucose 피처 데이터 분포 히스토그램으로 나타내기
- `min` 값이 0인 피처에 대해 0이 몇 퍼센트 비율로 존재하는지 확인.
- 0 값들을 해당 피처의 평균값으로 대체
- 스케일링 적용 후 로지스틱 회귀를 적용해 평가 지표 확인
- 재현율 수치 개선 - 임계값 변화에 따른 평가 지표 파악
- 최적의 임계값으로 다시 예측

<br>

**전체 코드**

~~~python
# 데이터 불러오기
diabetes_data = pd.read_csv('diabetes.csv')


# 필요한 모듈 import, DataFrame 생성
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score, recall_score
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.preprocessing import Binarizer, StandardScaler


# 피처 타입과 Null 개수 살펴보기
diabetes_data.info()


# 로지스틱 회귀 객체 생성 후 예측 수행하고 성능 평가 지표 출력 
X = diabetes_data.iloc[:, :-1]
y = diabetes_data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=156, stratify=y)

lr_clf = LogisticRegression()
lr_clf.fit(X_train, y_train)
pred = lr_clf.predict(X_test)

def get_clf_eval(y_test, pred):
  confusion = confusion_matrix(y_test, pred)
  accuracy = accuracy_score(y_test, pred)
  precision = precision_score(y_test, pred)
  recall = recall_score(y_test, pred)
  f1 = f1_score(y_test, pred)
  roc_auc = roc_auc_score(y_test, pred)
  print('오차행렬')
  print(confusion)
  print('정확도: {:.4f}, 정밀도: {:.4f}, 재현율: {:.4f}. F1: {:.4f}, AUC: {:.4f}'.format(accuracy, precision, recall, f1, roc_auc))

get_clf_eval(y_test, pred)


# 재현율 곡선 시각화
pred_proba = lr_clf.predict_proba(X_test)[:, 1]

def precision_recall_curve_plot(y_test, pred_proba_c1):
  precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_c1)

  plt.figure(figsize=(8, 6))
  threshold_boundary = thresholds.shape[0]
  plt.plot(thresholds, precisions[0: threshold_boundary], linestyle='--', label='precision')
  plt.plot(thresholds, recalls[0: threshold_boundary], label='recall')

  start, end = plt.xlim()
  plt.xticks(np.round(np.arange(start, end, 0.1), 2))

  plt.xlabel('Threshold value'); plt.ylabel('Precision and Recall value')
  plt.legend(); plt.grid()
  plt.show()

precision_recall_curve_plot(y_test, pred_proba)


# 임계값 조절 전에 피처 값 분포도 살펴보기 (describe())
diabetes_data.describe()


# Glucose 피처 데이터 분포 히스토그램으로 나타내기.
plt.hist(diabetes_data['Glucose'], bins=10)


# min 값이 0인 피처에 대해 0이 몇 퍼센트 비율로 존재하는지 확인.
zero_features = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for feature in zero_features:
  zero_count = diabetes_data[diabetes_data[feature]==0][feature].count()
  total_count = diabetes_data['Glucose'].count()

  print('{} 0 개수: {}, 0 비율: {:.2f}%'.format(feature, zero_count, 100*zero_count/total_count))
 

# 0 값들을 해당 피처의 평균값으로 대체.
zero_feature_mean = diabetes_data[zero_features].mean()
diabetes_data[zero_features] = diabetes_data[zero_features].replace(0, zero_feature_mean)


# 스케일링 적용 후 로지스틱 회귀를 적용해 평가 지표 확인
X = diabetes_data.iloc[:, :-1]
y = diabetes_data.iloc[: , -1]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=156, stratify=y)

lr_clf = LogisticRegression()
lr_clf.fit(X_train, y_train)
pred = lr_clf.predict(X_test)

get_clf_eval(y_test, pred)


# 재현율 수치 개선 - 임계값 변화에 따른 평가 지표 파악.
thresholds = [0.30, 0.33, 0.36, 0.39, 0.42, 0.45, 0.48, 0.50]

def get_clf_by_threshold(y_test, pred_proba_c1, thresholds):
  for custom_threshold in thresholds:
    binarizer = Binarizer(custom_threshold).fit(pred_proba_c1)
    custom_predict = binarizer.transform(pred_proba_c1)
    print('\n임계값:', custom_threshold)
    get_clf_eval(y_test, custom_predict)

pred_proba = lr_clf.predict_proba(X_test)[:, 1].reshape(-1, 1)
get_clf_by_threshold(y_test, pred_proba, thresholds)


# 최적의 임계값으로 다시 예측.
pred_proba = lr_clf.predict_proba(X_test)[:, 1].reshape(-1, 1)
pred = Binarizer(threshold=0.48).fit_transform(pred_proba)
get_clf_eval(y_test, pred)
~~~



