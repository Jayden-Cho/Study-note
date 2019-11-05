# Chapter 9 딕셔너리

### 딕셔너리 개념 및 특징

**컬렉션(Collection)**

리스트나 딕셔너리 같은 변수를 가지는 상황. 하나의 정보보다는 여러 개의 정보를 저장할 때 사용됨.

<br>

**리스트(List)**

순서대로 정리된 컬렉션. 데이터를 추가하면 항상 리스트 끝에 추가됨.

<br>

**딕셔너리(Dictionary)**

딕셔너리에는 순서가 없는 대신 키(Key)가 존재.

- 물건에 포스트잇으로 라벨을 붙이는 것.

~~~python
purse = dict() # purse = {}로도 생성 가능.
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)
# result: {'money': 12, 'candy': 3, 'tissues': 75}
~~~

<br>

candy라는 키에 저장된 값에 접근하려면

~~~python
print(purse['candy'])
# result: 3
~~~

<br>

접근한 내용을 업데이트할 수 있음.

~~~python
purse['candy'] = purse['candy'] + 2
print(purse)
# result: {'money': 12, 'candy': 5, 'tissues': 75}
~~~

<br>

**연관 배열**

키와 값이 연결되는 개념을 연관 배열이라고 함. 접근법이 리스트와 비슷하지만, 키를 갖고 접근한다는 차이가 있음.

<br>

### 딕셔너리를 활용한 데이터 빈도수 측정

**사람의 방식으로 이름 빈도수 세기**

사람의 방식은:

1. 새로운 이름을 보고 목록에 추가.
2. 추가된 이름이 1번 나왔다는 표시를 함.
3. 목록에 있는 이름이면 기존의 숫자에 1 더함.
4. 모든 이름을 살펴본 후 표시 갯수를 세어 가장 높은 것을 찾음.

<br>

파이썬으로 표현하면:

~~~python
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
# result: {'csev': 1, 'cwen': 1}

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
# result: {'csev': 1, 'cwen': 2}
~~~

<br>

**딕셔너리를 이용해 이름 빈도수 세기**

수백만 개의 이름이 있다면 이런 방법은 불가능. 딕셔너리의 방법을 사용.

1. 이미 저장되어 있는 이름인지 확인.
   1. 이미 저장되어 있는 이름일 경우: 1을 더함.
   2. 저장되지 않은 이름일 경우: 이름을 저장하고 1을 배정.
2. 최종 결과 중 가장 빈도가 많은 이름을 찾음.

~~~python
counts = dict()
names = ['A', 'B', 'B', 'D', 'E']

for name in names:
  if name in counts:
    counts[name] = counts[name] + 1
  else:
    counts[name] = 1
print(counts)
# result: {'A': 1, 'B': 2, 'D': 1, 'E': 1}
~~~

<br>

not 연산자를 사용해 동일하게 해결할 수 있음.

~~~python
counts = dict()
names = ['A', 'B', 'B', 'D', 'E']

for name in names:
  if name not in names:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1
print(counts)
# result: {'A': 1, 'B': 2, 'D': 1, 'E': 1}
~~~

<br>

**get 메소드**

딕셔너리에 존재하는 키인지 아닌지 여부에 따라 처리하는 패턴은 get() 메소드를 사용해 간결하게 해결할 수 있음.

- ***counts.get(name, 0)***: counts 딕셔너리에 name이라는 키가 존재할 경우 name을 불러오고, 그렇지 않을 경우 name에 0을 추가하라는 의미.

~~~python
counts = dict()
names = ['A', 'B', 'B', 'D', 'E']

for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)
# result: {'A': 1, 'B': 2, 'D': 1, 'E': 1}
~~~

<br>

### 딕셔너리 활용하기

**split 메소드**

띄어쓰기를 기준으로 문장을 분할해 단어들의 리스트로 만들어줌.

~~~python
counts = dict()
line = 'The general pattern to count the words'
words = line.split()
print(words)
# result: ['The', 'general', 'pattern', 'to', 'count', 'the', 'words']
~~~

<br>

리스트로 변환시키면 get 메소드를 활용해 문장에 있는 단어들의 빈도수를 구할 수 있게 됨.

~~~python
for word in words:
  counts[word] = counts.get(word, 0) + 1
print(counts.)
~~~

<br>

**딕셔너리에 루프를 적용하는 방법**

딕셔너리에 저장된 데이터를 다룰 때도 유용하게 사용됨.

- counts라는 딕셔너리를 for 반복문에 넣고 실행하면, 딕셔너리의 키와 값이 각각 출력됨.

~~~python
counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:
  print(key, counts[key])
# result: 
# chuck 1
# fred 42
# jan 100
~~~

<br>

딕셔너리를 리스트로 변환하면 키로만 구성된 리스트를 얻을 수 있음.

```python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))
# ['jan', 'chuck', 'fred']
```

<br>

딕셔너리의 keys 메소드를 사용해도 같은 결과를 얻을 수 있음.

~~~python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj.keys())
# ['jan', 'chuck', 'fred']
~~~

<br>

딕셔리의 값으로만 구성된 리스트를 얻으려면 values 메소드 사용.

~~~python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj.values())
# [100, 1, 42]
~~~

<br>

**items 메소드**

keys, values 메소드로는 각각 딕셔너리의 키와 값의 쌍을 얻을 수 없음.

- items 메소드로 키와 값의 쌍 얻을 수 있음. 튜플이라는 자료 구조 안에 키와 값이 쌍을 이루어 저장된 리스트가 반환됨.

~~~python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj.items())
# [('jan', 100), ('chuck', 1), ('fred', 42)]
~~~

<br>

이렇게도 활용할 수 있음.

~~~python
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items() :
  print(aaa, bbb)
  
# result:
# chuck 1
# fred 42
# jan 100
~~~

<br>

### 파일에 저장된 데이터 읽어와서 빈도 분석하기

**내가 만든 코드**

~~~python
word_dict = dict()
word_list = sentence.split(" ")

for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1

max_val = 0
for i in word_dict.values():
    if max_val < i:
        max_val = i
        
print(max_val)
~~~

<br>

키와 값의 쌍을 출력할 수 있도록 items 메소드를 사용.

- 최대 빈도를 저장할 bigcount와 가장 많이 나온 단어를 저장할 bigword라는 변수를 None으로 초기화.
- for 반복문을 통해  counts 딕셔너리의 키는 word에, 빈도수는 count에 저장.
- 이후 count 값이 가장 큰 단어를 bigword에, 그 단어의 빈도수를 bigcount에 저장하고 이것을 모든 단에 대해 반복.

~~~python
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle :
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
bigcount = None
bigword = None
for word, count in counts.items() :
  if bigcount is None or count > bigcount :
    bigword = word
    bigcount = count
    
print(bigword, bigcount)
~~~





