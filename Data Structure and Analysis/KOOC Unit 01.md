# Hello World in Python

파이썬의 기본은 Object-Oriented Programming.

- 하지만 Procedure-Oriented도 생성 가능.

<br>

**Procedure-Oriented Program**

- Funtion 기반 프로그램.
- Block 1에서는 함수를 정의하고 Block 2에서 함수를 실행시킴.

**전체 코드**

~~~python
# Block1: 함수를 define.
def main():
  print("Hello World!")
  print("This program computes the average of two exam scores.")
  
  score1, score2 = input("Enter two scores separated by a comma :").split(",")
  average = (int(score1) + int(score2)) / 2.0
    
  print("The average of the scores is : ",average)
    
# Block 2: 함수를 execute.
main()
~~~

<br>

**detail**

~~~python
# Block 1: 함수를 define.
def main(): 
~~~

- `def`: function declaration의 keyword.
  - `main`: function name.
  - `()`: parameter가 들어가는 자리. 현재 정의되있지 않음.

<br>

**Object-Oriented Program**

- Class 기반 프로그램.
- `HelloWorld`가 object, `__init__`, `__del__`, `performAverage` 는 method.

**전체 코드**

~~~python
# Definition Part
class HelloWorld:
    def __init__(self): 
        print("Hello World! Just one more time")
    def __del__(self): 
        print("Good bye!")
    def performAverage(self, val1, val2):
        average = ( val1 + val2 ) / 2.0
        print("The average of the scores is : ", average)
           
def main():
    world = HelloWorld() 
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2)) 
    
# Execution part
main()
~~~

<br>

**details**

~~~python
class HelloWorld():
~~~

- Class declaration.
- Instantiation created.

<br>

~~~Python
def __init__(self):
~~~

- 함수 definition과 동일. 특이점은 Parameter에 `self` 존재.
  - `self`: 자기 자신을 의미. `self` 를 통해 정보에 접근.
  - 이처럼 method로 선언되면 paramter에 `self` 있어야.
- Class가 instantiation을 통해 instance로 생성될 때 `__init__`  이 발생.

<br>

~~~python
del __del__(self):
~~~

- instance가 없어질 때 `__del__` 실행.

<br>

~~~python
def performAverage(self, val1, val2):
    average = (val1+val2) / 2.0
    print("The average of the scores is : ", average)
~~~

- input paramter 존재(val1, val2).
  - 하단 `main()`  함수의 score1, score2를 불러옴.
- `self` 는?
  - `world`. `self` 는 점(.) 앞의 값. 다시 말해 `world` 그 자체.

<br>

~~~python
def main():
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2))
~~~

- `HelloWorld()` 는 빵틀, `world` 는 빵.
  - `HelloWorld()`: instance template. 
  - `world`: instance storage variable.`HelloWorld()` 에 의해 생성된 인스턴스.

<br>

<br>

# Naming, Styling, Comments

자신이 내키는대로 코딩 하면 안된다. 나중에 대학에서, 사회에서 다른 사람들과 협업에서 작성해야될 때가 분명 온다.

- 그럴 때를 대비해서 규칙에 맞게 코딩하는 법을 배워야 한다.
- 코드에 대해 설명을 할 줄 알아야 한다. 
- 변수 이름 또한 잘 정해야 한다.
  - `val1`, `val2` 는 좋은 naming이 아니다. 하지만 저번처럼 간단한 코딩에는 OK.

<br>

**Naming**

- 의미를 잘 전달할 수 있어야 한다.
- <u>camel casing</u>: `HelloWorld` 처럼 문장 사이에 대문자 쓰는 것.
  - 낙타 등처럼 생겼다해서 camel casing.

<br>

**Class name**

- 명사 위주로 정하기. 첫 번째 letter를 capitalize.
  - ex) HelloWorld, MaleNum.
  - 변수에는 첫 번째 글자를 capitalize 하지 않음.

<br>

**Variable name**

- 명사 위주로 정하기. 어떤 정보가 저장되어 있는지 잘 나타내야(다른 Naming도 마찬가지).
- 소문자로 대부분 시작.
  - Ex) numOfStats, scoreOfExam.

- Python에서는 data type 선언할 필요 없음. 나중에 변수에 assign되면 그것에 따라 data type이 결정됨.
  - 다른 언어들은 `intCount` 처럼 변수명 앞에 data type을 적어줌.

<br>

**Method name**

- 동사 위주로 정하기. 대부분 소문자로 시작.
  - ex) calculateAvg.

<br>

**Indentation**

- 모두 기준이 다르지만, 대부분 4 spaces.

<br>

**Comments(주석)**

- 주석을 달면 execution이나 declaration에 영향을 주지 않음.
  1. 블록주석 (''' ''') (""" """)
  2. `#` 사용.

<br>

<br>

# Variable Statements and Operators

### Variable Statements

~~~python
print('a','b') 
print('a'+'b')
# result:
# a b
# ab
~~~

- 콤마(,)로 출력을 하게 되면 두 data 사이에 space가 생성된 채 출력됨.
- 더하기(+)로 출력을 하게 되면 space 간격 없이 그래도 출력됨.

<br>

~~~python
va1 = 10
va2 = 20
print("%d, %f" % (va1, va2))
# result:
# 10, 20,000000
~~~

- `%d`  는 decimal, `%f` 는 float.

<br>

### Operators

- *int* + *float* = *int*
- *int* / *float* = *float*

<br>

**Type casting**

- `int(variable_name)`: 기존의 `variable_name` 의 자료형을 int로 변환.
  - 굳이 int 말고도 다른 자료형으로 전환 가능.

<br>

**Swapping**

~~~python
num2, num1 = num1, num2
~~~

- 당연해보이지만 다른 언어에서는 여러 줄이 필요함.

<Br>

<br>

# String

**String value equivalence test**

~~~python
strTest = 'a'
strTestComp = 'a'
print(strTestComp, strTest == strTestComp)

# result:
# a True
~~~

-  String variable is actually a linear collection of letters, and the letters have indexes.

