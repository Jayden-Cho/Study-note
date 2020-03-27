# Prob & Stats

**Why Do We Divide Sample Variance by N-1, not N?**

- Main 2 reasons.
  - sample variance's underestimation on population variance
  - sample variance's degree of freedom is N-1

<Br>

**Underestimation of Sample Variance**

- If we do random sampling the population several times and continually adds up sample average, then the sample average would eventually converge to the population average.
- It's not the case for sample variance. Sample variance does not converge to population variance and it underestimates population variance.
- Therefore we substract 1 on the number of sample in order to make sample variance bigger (lessen the underestimation).
  - But why only 1?

<br>

**Sample Variance's Degree of Freedom**

- Suppose <u>population mean</u> (we don't know. Just an assumption) is 8, and we randomly sampled 3 variables. 
  - Two numbers are 4 and 9. The last variable can be anything; it is independent of mean and variables.
- Let's say <u>sample mean</u> is 8 and the number of sample is 3. 
  - If two variables are 4 and 9, the other variable must be 11; last variable is dependent of mean and variables. 
- Since the final value(sample variance) is dependent on the middle value(sample mean), degree of freedom must be N-1.

<br><br>

**왜 표본 분산 공식의 분모는 N-1인가?**

- 표본 평균은 무작위 표본 추출에 의해 모평균에 수렴하지만, 분산은 모집단을 underestimate해 계속 반복 추출하더라도 본래의 모분산에 가까워지지 않을 수 있다.
  - 분산의 값이 과소평가 (실제값보다 작게 예측)되기 때문에(그럴 가능성이 있기 때문에) 분모의 값을 줄여 분산을 높여준다.
- 분모를 줄이는 건 알겠는데, 왜 하필 "N-1"인가>
  - 표본 분산의 자유도가 "N-1"이기 때문. 최종 값(표본 분산)을 구할 때 사용되는표본 개수에 중간 값(표본 평균)의 개수만큼 빼기.

<br>

**표본 분산의 자유도**

- 모평균을 안다고 가정하고 샘플을 세 개 추출하고 그 중 두 숫자만 공개됐을 때, 마지막 숫자에는 아무 숫자가 와도 상관없다.
- 이번엔 표본 평균을 안다고 가정하자. 표본의 개수는 세 개이고 그 중 두 숫자를 알 때, 마지막 숫자는 계산으로 구할수 있다. 세 숫자중 자유로운 숫자는 두 개 뿐이다.



