# Machine Learning

**개요**

- 회귀는 보통 실제값과 예측값의 오차 평균값을 기반으로 한 평가.
- 분류는 다양하다. 정확도, 오차행렬, 정밀도, 재현율, ...

<br>

**정밀도와 재현율**

- 정밀도와 재현율은 Positive 데이터셋의 예측 성능에 초점을 맞춘 평가 지표.
  - 정밀도 = TP / (TP + FP)
  - 재현율 = TP / (TP + FN)
- 이전 타이타닉에 오차행렬, 정밀도, 재현율과 같은 예측 평가를 적용해 보자.

~~~python
# 예측 평가를 한꺼번에 수행할 수 있는 함수 만들기
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion

def get_clf_eval(y_test, pred):
  confusion = confusion_matrix(y_test, pred)
  accuracy = accuracy_score(y_test, pred)
  precision = precision_score(y_test, pred)
  recall = recall_score(y_test, pred)
  print('오차 행렬')
  print(confusion)
  print('정확도: {:.4f}, 정밀도: {:.4f}, 재현율: {:.4f}'.format(accuracy, precision, recall))
  
# 로지스틱 회귀 기반 타이타닉 생존자 예측
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

lr_clf = LogisticRegression()
lr_clf.fit(X_train, y_train)
pred = lr_clf.predict(X_test)
get_clf_eval(y_test, pred)
~~~



