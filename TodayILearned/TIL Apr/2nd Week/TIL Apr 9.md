# Pandas

**`sort_values()`**

- 주요 매개변수는 `by`, `ascending`, `inplace`.
  - `by`에 정렬의 기준이 될 칼럼명을 입력한다.
  - `ascending`이 True면 오름차순, False면 내림차순.
  - `inplace`가 False면 기존 DataFrame은 유지하고 정렬된 DataFrame을 반환한다.

<br>

**Aggregation 함수**

- DataFrame에 aggregation 함수를 적용하면 모든 칼럼에 적용이 된다.

  ~~~python
  titanic_df.count()
  ~~~

  

- 특정 칼럼에 aggregation 함수를 적용하고 싶다면 따로 인덱싱해야 한다.

  ~~~python
  titanic_df[['Pclass', 'Age']].mean()
  ~~~

<br>

**`groupby()`**

- `by`에 칼럼명을 입력하면 그것에 따라 groupby를 진행한다.

  ~~~python
  titanic_df.groupby(['Pclass'])
  ~~~

- 여러 칼럼으로 groupby를 진행할 수도 있다.

  ~~~python
  titanic_df.groupby([['Pclass', 'Sex']])
  ~~~

- groupby를 호출하면 `DataFrameGroupBy`라는 객체를 반환한다.

- 서로 다른 aggregation 함수를 적용하라면 groupby() 객체 안에 리스트를 사용한다.

  ~~~python
  titanic_df.groupby(['Pclass']).(['min', 'max'])
  ~~~

  

- 여러 칼럼에 서로 다른 aggregation을 적용하려면 딕셔너리를 사용한다.

  ~~~python
  agg = {'Pclass': 'min', 'Sex': 'count'}
  titanic_df.groupby(agg)
  ~~~

  

