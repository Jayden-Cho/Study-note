# Machine Learning

**주성분분석**

특성들이 통계적으로 상관관계가 없도록 데이터셋을 회전시키는 기술. Unsupervised feature extraction.

- 데이터에서 분산이 가장 큰 방향을 찾고,
- 데이터를 정규화(데이터를 평균으로 빼기)한 후 회전(eigenstuff로 전환)
- (필요하다면) 중요도가 낮은 주성분 제외
- 다시 데이터에 평균을 더하고 재회전해 제 위치로

<br>

**scikit-learn에서의 주성분분석**

~~~python
from sklearn.decomposition import PCA

pca = PCA(n_components=i)  # PCA객체 생성. n_components를 정하면 중요도 높은 특성 선택 가능.
pca.fit(X) # fit 메서드 호출해 주성분 찾기.
X_pca = pca.transform(X) # transform 메서드를 호출해 데이터를 회전. 기본값일 때는 회전만 시키고 모든 주성분을 유지한다.
~~~

PCA의 단점은 추출된 변수의 해석이 어렵다는 것.

<br>

**고유얼굴(eigenface) 추출**

- 얼굴인식의 경우 클래스는 무수히 많지만 개별 훈련 데이터는 적다는 단점이 있다.
  - 유사도 측정에 픽셀 간의 거리를 계산하는 건 옳지 않다. 한 픽셀만 오른쪽으로 움직이면 다른 결과를 빚어낸다.
  - PCA의 화이트닝 옵션으로 주성분들에 데이터 스케일링 적용.
- 주성분을 다시 이미지로 나타낸 것을 고유얼굴(eigenface)라고 한다.

