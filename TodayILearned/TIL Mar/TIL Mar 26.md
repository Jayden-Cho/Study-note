# Prob & Stats

**InterQuartile Range (IQR)**

- IQR = Q3 - Q1 (75% percentile - 25% percentile)

<br>

**Standard Deviation**

$$SD = \sqrt{\frac{(x-\bar{x})^2}{N}}$$

<br>

**Variance**

$Var = \frac{(x-\bar{x})^2}{?}$

- Two options on $?$.
  - $N$ if $N$ = population.
  - $N-1$ if $N$ = sample of population.

<br><Br>

# Machine Learning

**Introduction**

- 데이터 형태에는 기존에 다뤘던 연속형, 범주형 이외에 **텍스트** 데이터도 존재한다.
- 텍스트 데이터는 수치형 자료들과는 달라 ML 모델에 적용하기 전에 전처리가 필수적이다.

<br>

**문자열 데이터 종류**

- <u>문자열이라고 해서 모두 텍스트로 다뤄야하는 것은 아니다.</u>
- 크게 (1) 범주형 데이터, (2) 범주의 의미를 연결시킬수 있는 임의의 문자열, (3) 구조화된 문자열 데이터, (4) 텍스트 데이터가 있다.

1. 범주형 데이터
   - 객관식 설문.
   - 응답값이 범주에 적절한지 생각해봐야 한다. 오타같은 오류는 같은 범주로 처리해야 한다.

2. 범주의 의미를 연결시킬수 있는 임의의 문자열
   - 주관식 설문. 사용자 임의의 주관으로 입력된 데이터.
   - 모두 수작업이고 자동화하기 어렵다. 범주형으로 받을 수 있다면 범주형으로 받는게 낫다.
3. 구조
   - 주소, 연락처, 이름.
   - 분석하기 어렵다. 분석하는 방법은 이 책의 범주를 벗어난다.
4. 텍스트 데이터
   - 대부분 단어로 구성된 문장에 정보를 담고 있다.
   - 데이터셋을 말뭉치<sup>corpus</sup>, 데이터 포인트를 문서<sup>documents</sup> 라고 한다.

<br>

**텍스트 데이터를 BOW로 표현**

- 텍스트 데이터를 표현하는 간단하고 효과적인 방법. 세 단계로 분류된다.
  - 토큰화 -> 사전 생성 -> 인코딩
- <u>BOW에선 단어의 순서는 완전히 무시된다.</u>
- <u>출력은 각 문서에서 나타난 단어의 횟수가 담긴 벡터.</u>
  - <u>단어 하나하나가 특성이 된다.</u>

<br>

**샘플 데이터에 BOW 적용**

- `CountVectorizer` 변환기로 구현된다
  - (1) 패키지를 임포트하고, (2) 객체를 생성하고, (3) `fit` 메서드를 적용한다.
  - `vocabulary_` 매개변수로 생성된 사전을 확인할 수 있다.
- 훈련 데이터에 대해 BOW 표현을 만드려면 `transform` 메서드를 적용한다.
  - 0과 1로 이루어진 sparse matrix가 출력된다.

~~~python
from sklearn.feature_extraction.text import CountVectorizer

word_list = [...]
vect = CountVectorizer()
vect.fit(word_list)
vect.transform(word_list)

# result: sparse matrix
~~~

