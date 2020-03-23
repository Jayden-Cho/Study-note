# Kaggle

**Intro: Home Credit Default Risk**

- Use historical loan application data to predict whether an applicant will be able to repay a loan.

<br>

**Metric: ROC AUC**

- False Positive Rate(x-axis) vs. True Positive Rate(y-axis)
- Generate a probability between 0 and 1, but a prediction either 0 or 1.

<br>

**Imports**

- `numpy`, `pandas`, `warnings`, `os`, `LabelEncoder`, `matplotlib.pyplot`, `seaborn`

<br>

**Read in Data**

- 1 main training set, 1 main testing set, 1 example submission, and 6 other addition information.

  ~~~python
  print(os.listdir("../input/home-credit-default-risk"))
  
  app_train = pd.read_csv("../input/home-credit-default-risk/application_train.csv")
  # app_test: same with app_train
  ~~~

<br>

**Exploratory Data Analysis (EDA)**

- From a high level overview to narrowed specific areas.

<br>

**Examine target class**

- 0 for repaid loan, 1 for unpaid loan

~~~Python
# count the number of target
app_train["TARGET"].value_counts()

# visualize the distribution of the target class
app_train["TARGET"].value_counts().plot.hist()
~~~

- <u>Imbalanced class problem. We can weight the classes by their representatio n in the data to reflect this imbalance.</u>

<br>

**Examine Missing values**

- Create a function for examining missing values.

~~~python
def missing_values_table(df):
  mis_val = df.isnull().sum()
  mis_val_percent = 100 * mis_val / len(df)
  
  mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
  
  mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing values', 1: '% of Total values'})
  
  mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total values', ascending=False).round(1)
  
  print("Your selected dataframe has "+str(df.shape[1])+" columns.\n There are "+str(mis_val_table_ren_columns.shape[0])+" columns that have missing values.")
  
  return mis_val_table_ren_columns
~~~

~~~Python
mis_val_table = missing_values_table(app_train)
mis_val_table.head(20)
~~~

<br>

<br>

# Prob & Stat

**Marginal vs. Conditional Distribution**

|       | Freshman | Sophomore | Junior | Total |
| ----- | -------- | --------- | ------ | ----- |
| A     | 0        | 4         | 16     | 20    |
| B     | 20       | 26        | 34     | 80    |
| C     | 40       | 30        | 10     | 80    |
| total | 60       | 60        | 60     |       |

- <u>Joint distribution</u>: point.

  - Ex) student who is sophomore and got a grade of B = 26 students.

- <u>Marginal distribution</u>: total. percentage와 count 둘 다 됨.

  - Ex) marginal distribution of grade = column total
  - Ex) marginal distribution of student level = row total

- <u>Conditional distribution</u>: distribution under certain condition. percentage만.

  - Ex) distribution of grade given that student level is sophomore

    |      | Sophomore     |
    | ---- | ------------- |
    | A    | 4/60 = 6.67   |
    | B    | 26/60 = 43.3% |
    | C    | 30/60 = 50%   |

<br>

<br>

# Algorithm

> 최대공약수 구하기

<br>

**유클리드 알고리즘**

- a, b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'와 같다. 즉, `gcd(a, b) = gcd(b, a%b)`이다.
- 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, `gcd(n, 0) = n`이다.

~~~python
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)
~~~

<br>

**연습 문제**

- 피보나치 수열을 재귀 호출을 사용해 알고리즘 작성.

~~~python
def fib(n):
  if n <= 1:
    return n
  return fib(n-2) + fib(n-1)
~~~

<br>

<Br>

# Quiz

**Stat & Prob**

|       | Freshman | Sophomore | Junior | Total |
| ----- | -------- | --------- | ------ | ----- |
| A     | 0        | 4         | 16     | 20    |
| B     | 20       | 26        | 34     | 80    |
| C     | 40       | 30        | 10     | 80    |
| total | 60       | 60        | 60     |       |

1. Joint distribution of students with grade of B and a sophomore.
2. Marginal distribution of students with grades.
3. Conditional distribution of student's grade given that student level is Junior.