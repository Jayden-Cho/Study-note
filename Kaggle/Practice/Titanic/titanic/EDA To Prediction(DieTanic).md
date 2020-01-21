# Part 1: Exploratory Data Analysis (EDA)

> Analysis of the features.
>
> Finding any relations or trends considering multiple features.



### A. 사용할 패키지 import.

1. `pandas`, `matplotlib.pyplot`, `seaborn`, `warnings`

   - `plt.style.use('fivethirtyeight')`
     - `plt` 스타일을 `fivethirtyeight`  으로 변경.

   - `warnings.filterwarnings('ignore')`
     - 경고 메세지 무시하고 숨기기.



### B. 기본

- EDA에 사용할 train.csv를 data로 초기화.
- `head()` 로 데이터 형태, feature 등 대략적인 개요 파악.
- `isnull().sum()` 으로 데이터에 결측값이 얼마나 있는지 파악.
  - **Age**, **Cabin**, **Embarked**에 결측값 존재. 후에 결측값 따로 제거.



### C. Feature Analysis

1. **How many survived?**
   - 전체 탑승객의 생존율을 `plot.pie()`로.
     - 생존율을 파악하기 위해선 `Survived` column을 `value_counts()`  로 세고 그것을 `plot.pie()`. pie chart를 `ax[0]`  로 설정.
     - 생동감 주기 위해 pie chart의 parameter `shadow=True` 로.
     - pie chart의 불필요한 ylabel을 `ax[0].set_ylabel('')`  로 없애줌.
   - 생존자와 사망자의 수를 `sns.countplot()` 으로.
     - `sns.countplot`은 기본적으로 count하고 싶은 column과 그 column이 속해있는 data를 지정해주면 된다.



2. **Sex** - Categorical Feature

   - 일단 남성, 여성 각각 사망자, 생존자가 몇명인지 파악하자.
     -  `groupby` 를 사용해 Sex와 Survived 기준으로 데이터를 묶는다. 그 다음 `count`로 사망자와 생존자의 수를 파악할 수 있다.
   - 파악한 통계를 시각화 한다 - 성별당 생존률과 성별당 생존자와 사망자.
     - 성별당 생존률
       - 위에 `groupby`로 묶은 것들을 `mean`처리해 `plot.bar()`.
     - 성별당 사망자와 생존자
       - `sns.countplot()`을 사용해 Sex를 기준으로 데이터를 count. count한 데이터를 Survived 기준으로 또 분할.

   

3. **Pclass** - Ordinal Feature

   - 먼저 `pd.crosstab()`으로 등급 당 생존자와 사망자의 수를 파악.
     - `margins=True`하면 각 등급 당 sum을 볼 수 있음.
     - `pd.crosstab()`의 테마를 `style.background_gradient()`를 사용해 변경할 수 있음. 여기선 `cmap='summer_r'`.
   - 파악한 통계를 시각화 - 등급 당 탑승객 수와 등급 당 생존자와 사망자의 수
     - 등급 당 탑승객 수
       - Pclass column을 `value_counts()` 하고 그것을 `plot.bar`.
     - 등급 당 생존자와 사망자의 수
       - 타겟(Pclass)별로 기준을 잡아(Survived) 나누는 건 `sns.countplot()`으로.
   - 위에서 분석한 Sex와 Pclass를 사용해 분석.
     - `pd.crosstab()`을 사용해 성별 당 생존자와 사망자가 어떤 등급에 분포되어있는지 파악.
     - 파악한 통계를 근거로 `sns.factorplot()`을 사용해 시각화.
       - `sns.factorplot()`은 categorical value들을 분리시키는 데 유용하다.

   

4. **Age** - Continuous Feature

   - 기본 통계 파악 - 최저령, 최고령, 평균 연령.
   - 시각화 - Pclass당 연령별 사망자와 생존자 분포와 Sex당 연령별 사망자와 생존자 분포.
     - Continuous feature는 `sns.violinplot()`을 사용. 
       - `split=True`하면 violin plot 생성됨. `split=False`면 개별적인 plot.
       - `set_yticks()`로 y 범위를 `range(0, 110, 10)`로 정해 보다 쉽게 파악할 수 있도록.
   - Age에는 결측값이 존재.
     - 해결할 방법은 다양하다. 여기서는 Name column의 Initial을 사용한 평균으로 결측값을 제거.	
       - Initial이라는 column을 만들고, 그 column에 Name에서 추출한 initial들을 대입. 추출하는 방법은 regex.
         -  `Name.str.extract('([A-Za-z+])\.')`의 뜻은 알파벳으로 시작해 점(.)으로 끝나는 단어를 추출.
       - `pd.crosstab()`으로 각각의 성에 어떤 initial이 있는지 파악.
         - 많은 initial들을 추려내 크게 다섯 종류로 축소 - Master, Miss, Mr, Mrs, Other.
         - `groupby()`로 initial별 연령 평균을 구하기.
       - 구한 initial별 연령 평균을 결측값이 있는 initial들에 대입.
   - 시각화 - 연령별 사망자 분포와 연령별 생존자 분포.
     - 생존자, 사망자 따로 테이블을 만들고(`data[data['Survived']==0 or 1])` 두 plot 모두 `plot.hist()` 사용.
       - `bins=20`로 설정해 눈금을 보기 좋게. 
       - `edgecolor=black`으로 설정해 각각의 바를 파악하기 쉽게.
       - 두 plot의 색깔을 red, blue로 설정해 차이를 부각.
       - 최고령자가 80세였으니 x 범위를 `set_xticks()`를 사용해 `range(0, 85, 5)`로 설정.
   - 시각화 - Initial별 Pclass당 생존율
     - `sns.factorplot()`을 사용해 세 feature 모두 비교할 수 있게.
       - `col='Initial'`으로 plot을 initial별 총 5개로 분할.

   

5. **Embarked** - Categorical Feature

   - `pd.crosstab()`으로 데이터를 항구별 Pclass인원으로 나누고 그것을 성별 생존, 사망자 수로 나눔..

     - 쉽게말해 y축에는 Embarked와 Pclass가, x축에는 Sex와 Survived가 있음. 각각 두 번째는 첫 번째 안쪽에 존재함.

   - 시각화 - `sns.factorplot()`으로 항구별 생존율 측정.

     - plot의 크기를 조절하려면 `plt.gcf()`로 plot의 객체를 만들고 만들어진 객체로 `set_size_inches()`로 크기 조절.
     - 나였으면 그냥 `value_counts()` 사용하거나, `groupby()` 한 것을 mean처리하거나, 보다 쉽게 `sns.countplot()`하고 Survived로 나눴을 듯.

   - 시각화 - (1) 항구별 탑승객, (2) 항구별 탑승객을 성별로 분할, (3) 항구별 탑승객을 생존 유무로 분할, (4) 항구별 탑승객을 Pclass로 분할.

     - 4 plot 모두 `sns.countplot()` 사용. 방법은 스스로 생각해보기.
     - 4 plot들의 간격을 `plt.subplots_adjust()`로 조절.

   - 시각화 - 항구별 Pclass와 성별 당 생존율

     - 말이 어렵지만 `sns.factorplot()`으로 해결 가능.
       - `col='Embarked`로 plot 나누고, x, y축에 각각 Pclass와 Survived, 그리고 plot들을 `hue='Sex'` 처리.

   - 결측값 처리

     - 결측값은 딱 2개. 그냥 가장 많이 탑승한 항구인 S로 대체.
       - Embarked column에 `fillna()`를 사용해 S로 대체.

     

6. **SibSp** - Discrete Feature

   - `pd.crosstab()`으로 SibSp별 생존유무 파악.
   - 시각화 - SibSp별 생존율 두 가지 방법으로 plot.
     - `sns.barplot()`을 사용해 (아마도) 기존의 `sns.countplot()`에 오차 막대도 함께.
     - `sns.barplot()` 있는데 굳이 `sns.factorplot()`을 사용했어야 하나 라는 생각이 듦.
   - `pd.crosstab()`으로 SibSp 별 Pclass 분포 알아내기.

   

7. **Parch** - Discrete Feature

   - 위의 SibSp과 비슷하게. `pd.crosstab()`으로 Parch별 Pclass 파악.
   - 시각화 - Parch별 생존율 두 가지 방법으로.

   

8. **Fare** - Continuous Feature

   - 기본적인 통계 먼저 - 최고 금액, 최저 금액, 평균 금액.
   - 시각화 - Pclass당 Fare 분포.
     - `sns.distplot()`을 사용하면 선과 막대 그래프 모두 plot 안에.



### D. Correlation Between The Features

- `sns.heatmap()`을 사용해 상관관계 파악. 높은 상관관계의 feature들이 있다면 삭제하기 위해.
  - `annot=True`로 상관관계 박스 안에 수치 출력.
  - 위에서 했던 것처럼 heatmap 객체를 만들어 `set_size_inches()` 사용.

<br>



# Part 2: Feature Engineering and Data Cleaning

> Adding any few features.
>
> Removing redundant features.
>
> Converting features into suitable form for modeling.



### A. Age_band

- Age는 continuous feature. Sex나 Pclass라면 grouping하기 쉽지만 숫자가 많은 Age는 어렵다.
  - 컴퓨터가 데이터를 이해하기 쉽게 grouping을 해준다. grouping 방법은 크게 normalization과 binning. 여기서는 binning 사용.
  - 최고령이 80. 5개의 bin으로 나눠 16세씩 담는다.
    - Age_band column을 만들고, `data.loc[]`을 사용해 binning.
- Age_band의 bin에 각각 몇명이 포함되있는지 확인.
  - `value_counts()`한 것을 `to_frame()`으로 씌우면 테이블이 생긴다.
  - `pd.crosstab()`처럼 `style.background_gradient()`으로 테마 변경이 가능하다.
- 시각화 - Pclass별 Age_band 당 생존율
  - 가지고 있는 feature가 Age_band, Survived, Pclass 세개이므로 `sns.factorplot()`이 적합.



### B. Family_Size and Alone

- Family_Size, Alone column을 새로 만들기.
- 시각화 - Family_Size 당 생존율과 Alone 유무에 따른 생존율
  - 여기선 `sns.factorplot()`을 사용했지만, 막대그래프 사용해도 괜찮을 듯(예를 들어 `sns.barplot()`)

- 시각화 - Pclass별 Alone 유무 당 생존율



### C. Fare_Range

- Fare도 continuous feature이므로 구간 데이터로 바꿔야 한다.
  - `pd.qcut()`을 사용. 원하는 개수의 bin을 입력하면 개수에 맞게 데이터를 나눠준다.
  - 나눈 것 위의 Age_band처럼 `loc[]` 함수를 사용해 분할.
- 시각화 - 성별 당 Fare_cat 변화에 따른 생존율의 변화.



### D. Converting String Values into Numeric

- 컴퓨터는 문자열을 이해할 수 없기 때문에 String을 숫자로 변형한다.
- 우리가 바꿔야할 것은 Sex, Embarked, Initial.
  - 개수에 맞게 0부터 숫자를 대입. 예를 들어 Sex는 male, female 두 가지가 존재하는데, 각각 0과 1을 대입.
- 필요 없는 Feature를 제외하기. 제외는 `data.drop(['column name'])`으로 간단하게 가능.
  - **Name** - 이름은 categorize할 수 없음. 제외.
  - **Age** - Age 이미 binning 끝났으니 제외.
  - **Ticket** - 규칙성이 없으니 categorize 불가. 제외.
  - **Fare** - 이것도 binning 끝났으니 마찬가지로 제외.
  - **Cabin** - 결측값이 너무 많고 많은 탑승객이 복수개의 cabin을 소유. 복잡하니 제외.
  - **Fare_Range** - Fare_cat을 만들기 위한 중간책일 뿐이니 제외.
  - **PassengerId** - Categorize 불가능.





# Part 3: Predictive Modeling

> Running Basic Algorithms.
>
> Cross Validation.
>
> Ensembling.
>
> Important Features Extraction.



EDA를 통해 데이터에 대한 인사이트를 얻고, feature engineering을 통해 feature들을 모델링에 적용될 수 있게 변형시켰다. 하지만 아직 그것으로 예측할 수 없음. 분류 알고리즘을 사용하여 예측할 차례.



### A. 각각 7개의 모델을 훈련/예측

- 모델링에 필요한 패키지들 import.
- 모델 7개 train시키고 predict.
  - KNN은 neighbor 개수에 따라 예측값이 달라지므로 neighbor 개수 조절.
    -  `pd.Series()` 를 생성하고 n_neighbor에 따른 예측값을 저장.



### B. Cross Validation

- 정확도만 높아서는 안됨. 특정 dataset이 overfit될 가능성 있음. 교차검증은 필수.

  - 먼저 교차검증에 필요한 패키지들 import.
  - 10개의 bin을 가진 KFold 생성.
  - 7개의 모델에 `cross_val_score` 적용.
    - 적용된 값 `cv_result`를 초기화하고 그값의 mean과 std를 구한다.
  - 구한 값들을  `pd.DataFrame()`에 저장.

  

- 시각화 - 위에서 구한 7개 모델의 예측값들을 `boxplot()`.

  - 우리가 현재 가지고 있는건 예측값과 classifier의 인덱스 뿐. 이것을 `pd.DataFrame()`으로 만들어 plot을 할 수 있게 변형.



- 시각화 - 교차검증 평균 예측값을 시각화
  - 7가지 모델이 존재하니 `plot.barh()`로 정렬.



- 시각화 - 7개 모델에 confusion matrix 적용.
  - `cross_val_predict()`으로 각 모델 교차검증.
  - 교차검증된 예측값과 실젯값으로 `sns.heatmap()` 안에  `confusion_matrix()` 대입.



### C. Hyper-Parameter Tuning

- 가장 성능 좋은 모델 두 개에 GridSearchCV 사용.



### D. Ensembling

- 모델 성능을 높이는 방법. 약한 모델의 합으로 강한 모델을 만든다.
- Voting Classifier, Bagged(KNN, Decision Tree), Boosting(Adaptive, Gradient. XgBoost는 주피터에서 불가능)













로드맵

2. 남은 Part 3 카피하고 commit해보기.
3. 다음 넘어가기 - 전체 그냥 script로 글씨 안보고 코딩만해서 commit.
4. 전체 파트 별 정리
5. 전체 모두 복사해서 commit. 







Questions:

- `drop()` 함수에 있는 axis는 무슨 역할?