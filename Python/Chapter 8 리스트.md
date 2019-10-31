# Chapter 8 리스트

> 프로그래밍
>
> 프로그래밍은 알고리즘과 자료구조로 나눌 수 있음. 알고리즘이 특정 문제를 해결하기 위한 규칙 또는 단계라면, 자료구조는 컴퓨터내에서 자료를 구조화 하는 특별한 방식.

<br>

**리스트 예시**

~~~python
friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
colors = ['red', ['yellow', 'blue'], 'black']
emptyList = []
print(color[0]) # result: red
lotto = [2, 14, 26, 41, 63]
print(lotto) # result: [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto) # result: [2, 14, 28, 41, 63]
~~~

<br>

**len()**

~~~python
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) # result: 3
~~~

<br>

**range()**

range() 함수는 인자로 전달되는 값에 따라서 숫자로 이루어진 리스트를 반환.

~~~python
for i in range(5):
  print(i)
  
# result:
# 0
# 1
# 2
# 3
# 4
~~~

<br>

**연산자 활용**

'+' 연산자를 활용해 서로 다른 리스트를 더할 수 있음.

~~~python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# result:
# [1, 2, 3, 4, 5, 6]
~~~

<br>

**리스트 슬라이싱**

리스트도 ':'(콜론)을 통해 슬라이싱 할 수 있음.

~~~python
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # result: [41, 12]
print(t[:4]) # result: [9, 41, 12, 3]
print(t[3:]) # result: [3, 74, 15]
print(t[:]) # result: [9, 41, 12, 3, 74, 15]
~~~

<br>

**dir() 메소드**

특정 타입에서 사용할 수 있는 메소드의 목록들을 볼 수 있는 함수.

~~~python
x = list()
print(dir(x))
~~~

<br>

**리스트 만들기**

~~~python
friends = list()
friends.append('Joseph')
friends.append('Glenn')
friends.append('Sally')
print(friends) # result: ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends) # result: ['Glenn', 'Joseph', 'Sally']
print('Glenn' in friends) # result: True
~~~

<br>

**문자열과 리스트**

~~~python
abc = 'With three words'
stuff = abc.split()
print(stuff) # result: ['With', 'three', 'words']
~~~

<br>

**구분자**

구분자를 명시하지 않으면 빈칸은 구분자로 인지하고 나눔.

~~~python
words2 = 'first;second;third'
stuff2 = words2.split() 
print(stuff2) # result: ['first:second:third']
stuff2 = words2.split()
print(stuff2) # result: ['first', 'second', 'third']

~~~

<br>

**이메일 주소 추출하기**

~~~python
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# line에 uct.ac.za만 추출하기.
words = line.split()
print(words[1]) # result: stephen.marquard@uct.ac.za
email = words[1]
address = email.split('@')
print(address) # result: ['stephen.marquard', 'uct.ac.za']
print(address[1]) # result: uct.ac.za
~~~

<br>

#### Quiz

- append()는 기존의 리스트에 원소를 추가.

- '+' 연산자는 리스트를 합치는 것.

~~~python
words = ['A', 'B']
words.append(['C', 'D', 'E'])
print(len(words)) # result: 3
print(words) # result: ['A', 'B', ['C', 'D', 'E']]

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(len(list1 + list2)) # result: 8 
print(list1 + list2) # result: [1, 2, 3, 4, 5, 6, 7, 8]
~~~



