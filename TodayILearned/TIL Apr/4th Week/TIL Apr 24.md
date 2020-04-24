# Machine Learning

**정밀도/재현율 트레이드오프**

- 임계값을 조정하면 정밀도와 재현율을 조정할 수 있다.
- 보통 이진 분류 알고리즘은 레이블별 결정 확률을 구하고, 기준 값보다 값이 크다면 Positive, 작다면 Negative.
- 사이킷런에서는 `predict_proba()` 로 예측 확률을 얻을 수 있다.
  - `predict()` 와 유사하지만 반환 결과는 예측 확률 결과이다.

~~~python
# 훈련된 LR 객체에 predict_p
from sklearn.preprocessing import Binarizer

pred_proba = lr_clf.predict_proba(X_test)
pred_proba_1 = pred_proba[:, 1].reshape(-1, 1)

custom_threshold = 0.5

binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_1)
pred = binarizer.transform(pred_proba_1)
~~~

<br>

- 임계값이 낮아지면,
  - 재현율이 높아진다. 양성을 음성이라 예측하는 횟수가 줄어든다.
  - 정밀도가 낮아진다. 애꿎은 음성을 양성이라 예측하기도 한다.

~~~python
# 임계값을 0.4에서 0.6까지 0.05씩 증가시키며 평가 지표를 조사해보자.
thresholds = [0.4, 0.45, 0.5, 0.55, 0.6]

def get_eval_by_threshold(y_test, pred_proba_c1, thresholds):
  for custom_threshold in thresholds:
    binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_c1)
    custom_predict = binarizer.transform(pred_proba_c1)
    print("임계값:", custom_threshold)
    get_clf_eval(y_test, custom_predict)
  
get_eval_by_threshold(y_test, pred_proba[:, 1].reshape(-1, 1), thresholds)
~~~

<br>

- 사이킷런은 임계값의 변화에 따른 평가 지표(정밀도, 재현율)를 알아볼 수 있는 `precision_recall_curve()` 메서드를 지원한다.

~~~python
from sklearn.metrics import precision_recall_curve

# 레이블 값이 1일 때의 예측 확률을 추출
pred_proba_class1 = lr_clf.predict_proba(X_test)[:, 1]

# 실제값 데이터셋과 레이블 값이 1일 때의 예측 확률을 precision_recall_curve 인자로 입력.
precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_class1)
print('반환된 분류 결정 임계값 배열의 shape:', thresholds.shape)

# 반환된 임계값 배열 로우가 155건이므로 샘플로 10건만 추출하되, 임계값을 15 단계로 추출.
thr_index = np.arange(0, thresholds.shape[0], 15)
print('샘플 추출을 위한 임계값 배열의 index 10개:', thr_index)
print('샘플용 10개의 임곗값:', np.round(thresholds[thr_index], 2))

# 15 단계 단위로 추출된 임계값에 따른 정밀도와 재현율 값
print('샘플 임계값별 정밀도:', np.round(precisions[thr_index], 3))
print('샘플 임계값별 재현율:', np.round(recalls[thr_index], 3))
~~~

<br>

- `precision_recall_curve()`는 시각화하는데도 사용될 수 있다.

~~~python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
%matplotlib inline

def precision_recall_curve_plot(y_test, pred_proba_c1):
  # threshold ndarray와 이 threshold에 따른 정밀도, 재현율 ndarray 추출
  precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_c1)

  # X축을 threshold값으로, Y축은 정밀도, 재현율 값으로 각각 plot. 정밀도는 점선으로 표시.
  plt.figure(figsize=(8, 6))
  threshold_boundary = thresholds.shape[0]
  plt.plot(thresholds, precisions[0:threshold_boundary], linestyle='--', label='precision')
  plt.plot(thresholds, recalls[0:threshold_boundary], label='recall')

  # threshold 값 X축 scale을 0.1 단위로 변경
  start, end = plt.xlim()
  plt.xticks(np.round(np.arange(start, end, 0.1), 2))

  # x축, y축 label과 legend, 그리고 grid 설정
  plt.xlabel('Threshold value'); plt.ylabel('Precision and Recall value')
  plt.legend(); plt.grid()
  plt.show()

precision_recall_curve_plot(y_test, lr_clf.predict_proba(X_test)[:, 1])
~~~

<br>

**F1 스코어**

- F1 스코어는 정밀도와 재현율을 결합한 지표.
  - 정밀도와 재현율이 어느 쪽으로 치우치지 않는 수치를 나타낼 때 높은 값을 가진다.

<br>

**ROC 곡선과 AUC**

- ROC 곡선은 FPR이 변할 때(x축) TPR(y축)이 어떻게 변하는지 나타내는 곡선이다.
  - TPR은 재현율. 전체 양성 중 양성으로 정확히 예측된 수준.
  - FPR은 **FP/(FP+TN)**. 전체 음성 중 양성으로 잘못 예측된 수준.
- FPR은 **1-TNR**이기도 하다. 
  - TNR은 TPR의 반대되는 개념으로, 전체 음성 중 음성으로 정확히 예측된 수준.
  - FPR은 높을수록 음성이 양성으로 잘못 예측되었다는 것.

<br>

~~~python
# 사이킷런이 제공하는 roc_curve()로 타이타닉 생존자 예측 모델의 FPR, TPR, 임계값을 구하자.
from sklearn.metrics import roc_curve

# 레이블 값이 1일 때의 예측 확률을 추출
pred_proba_class1 = lr_clf.predict_proba(X_test)[:, 1]

fprs, tprs, thresholds = roc_curve(y_test, pred_proba_class1)
# thresholds[0]은 max(예측확률)+1로 임의 설정됨. 이를 제외하고 1부터 시작.
thr_index = np.arange(1, thresholds.shape[0], 5)

print("샘플 추출을 위한 임계값 배열의 index 10개:", thr_index)
print("샘플용 10개의 임계값:", np.round(thresholds[thr_index], 2))

# 5 step 단위로 추출된 임계값에 따른 FPR, TPR 값
print("샘플 임계값별 FPR:", np.round(fprs[thr_index], 3))
print("샘플 임계값별 TPR:", np.round(tprs[thr_index], 3))
~~~

<br>

~~~python
# ROC 곡선을 시각화 해보자.
def roc_curve_plot(y_test, pred_proba_c1):
  fprs, tprs, thresholds = roc_curve(y_test, pred_proba_c1)
  plt.plot(fprs, tprs, label='ROC')
  plt.plot([0, 1], [0, 1], 'k--', label='Random')
  
  # FPR X축의 scale을 0.1 단위로 변경 & X, Y축 이름 설정
  start, end = plt.xlim()
  plt.xticks(np.round(np.arange(start, end, 0.1), 2))
  plt.xlim(0, 1); plt.ylim(0, 1)
  plt.xlabel('FPR( 1-Sensitivity )'); plt.ylabel('TPR( Recall )')
  plt.legend()
  
roc_curve_plot(y_test, pred_proba[:, 1])
~~~



