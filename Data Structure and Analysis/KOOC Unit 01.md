# Hello World in Python

파이썬의 기본은 Object-Oriented Programming.

- 하지만 Procedure-Oriented도 생성 가능.

<br>

**Procedure-Oriented Program**

- Function 기반 프로그램.
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
  -  `__init__`, `__del__` 은 특별한 메소드인 생성자(constructor)

**전체 코드**

~~~python
# Definition Part
class HelloWorld:
    def __init__(self): 
        print("Hello World! Just one more time")
    def __del__(self): 
        print("Good bye!")
    def performAverage(self, val1, val2):
        average = (val1 + val2) / 2.0
        print("The average of the scores is : ", average)
           
def main():
    world = HelloWorld() 
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2)) 
    
# Execution part
main()
~~~

<br>

**detail**

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
  - `self`: 자기 자신을 의미. `self` 를 통해 정보에 접근. `self`는 인스턴스라고 생각하자.
  - 이처럼 method로 선언되면 paramter에 `self` 있어야.
- Class가 instantiation을 통해 instance로 생성될 때 `__init__`  이 발생.

<br>

~~~python
del __del__(self):
~~~

- instance가 없어질 때 `__del__` 실행. **Destructor**.

<br>

~~~python
def performAverage(self, val1, val2):
    average = (val1+val2) / 2.0
    print("The average of the scores is : ", average)
~~~

- input paramter 존재(`val1`, `val2`).
  - 하단 `main()` : 함수의 `score1`, `score2`를 불러옴.
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
  - ex) numOfStats, scoreOfExam.

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
  1. 블록주석 (`''' '''`) (`""" """`)
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

<br>

<br>

# List, Tuple, Dictionary

****

**Index in Sequence**

This index applies to strings as well as tuples, lists.

- Applies to any sequence variables.

~~~python
strTest = 'Hello World! ISE'
print(strTest[1:3]) # 실제 인덱스 범위는 1부터 2.
print(strTest[1:9:2]) # 1부터 8까지 2씩 띄어서 가기. 그래서 1, 3, 5, 7.
print(strTest[1::2]) # 1부터 끝까지 2씩 띄어서 가기.
print(strTest[5::-1]) # 5부터 역순으로 1씩 띄어서 가기. 그래서 5, 4, 3, 2, 1, 0. 6글자 출력.
# 이동방향이 (-)일땐 기존과 다르게 끝까지 간다. [1:3]하면 2까지 밖에 안가지만.

# result:
# el
# el o
# el ol!IE
#  olleH --> 한 칸 띄워진거 이상한게 아니라 인덱스 5가 공란이라서.
~~~

<br>

**List**

Another type of sequence variables.

- `del` 은 입력된 인덱스 위치에 있는 값을 제거하고, `remove` 는 입력된 값을 제거.

~~~python
lstTest = list(range(1, 20, 3))
print(lstTest) 
lstTest.append('A')
del lstTest[0] # 리스트에서 인덱스 0에 있는 값을 지우는 것.
print(lstTest)
lstTest.remove(4) # 4를 리스트에서 지우는 것.
print(lstTest)
lstTest.sort()
print(lstTest) 

# result:
# [1, 4, 7, 10, 13, 16, 19]
# [4, 7, 10, 13, 16, 19, 'A']
# [7, 10, 13, 16, 19, 'A']
# TypeError: '<' not supported between instances of 'str' and 'int'
# python 3에서는 int와 str 값의 비교가 불가함.
~~~

<br>

**Tuple**

Tuple and List are almost alike.

- Only different in <u>changing values</u>. Tuple does not allow value changes.

~~~python
tplTest = (1, 2, 3)
tplTest[0] = 100

# result:
# TypeError: 'tuple' object does not support item assignment


# 여러 사람이 코딩을 하다보면 고정된(Constant)상수가 필요할 때가 온다.
# 고정되어야 할 값을 바꿀 수 없게끔 고정시킬 때 종종 사용.
~~~

<br>

**Dictionary**

Also a collection variable type.

- Not sequential and works by a pair of keys and values.

~~~Python
dicTest = {1:'one', 2:'two', 3:'three'}
print(dicTest[1]) # Dict에서는 []안의 값이 인덱스가 아니라 key 값.
dicTest[1] = 'hana'
print(dicTest)

# result: 
# one
# {1: 'hana', 2: 'two', 3: 'three'}
~~~

<br>

# Condition and Loop Statement

**if**

- `if`, `elif` boolean: Statements for True.
- `else` boolean: Statements for False.
- Python does not have a switch-case statement.

<br>

**for**

- Some useful statements for loops
  - `continue`, `break`

~~~python
for itr in range(1, 100, 10):
    if itr == 51: 
        continue # 51이 나오면 건너뛰기
    else:
        print(itr,end=" ") # 한 줄에 출력되게
        
# result: 
# 1 11 21 31 41 61 71 81 91

for itr in range(5):
    print(itr, end=' ')
else:
    print('!')
print('done')

# result:
# 0 1 2 3 4 !
# done

for itr in range(5):
    if itr == 3:
        break
    print(itr, end=' ')
else: # else loop도 break되서 for loop과 함께 탈출된다.
    print('!')
print('done')

# result: 
# 0 1 2 done
~~~

<br>

# Function Statement

For, if, while loop 모두 control하기 위해 사용되는 statement. Function을 정의할 수 있게 해줌.

~~~python
def name(params):
  statements
  return var1, var2
~~~

- Can return multiple variables.
  - Keep them in order.
- Don't have to specify return types.
- One line function is called **lambda** function.

~~~python
numA, numB = 1, 2

def multiply(numParam1, numParam2):
  	return numParam1*2, numParam1*3 

def increase(numParam1, step=1)
		return numParam1+step

numD, numE = multiply(numA, numB) # result: 2 3
numF = increase(numA, 5) # result: 6
numG = increase(numA) # result: 2

lambdaAdd = lambda numParam1, numParam2 : numParam1 + numParam2

numH = lambdaAdd(numA, numB) # result: 3
~~~

<br>

**Sample Program: Finding Prime Numbers**

~~~python
def isPrimeNumber(numParam1):
  	for itr in range(2, numParam1):
      	if numParam1 % itr == 0:
        		break
    else:
      	return True
    return False
  
def findPrime(numParam1, numParam2):
  	NumCount = 1
    for itr in range(numParam1, numParam2):
      	if isPrimeNumber(itr) == True:
         	  print(NumCount,' th prime : ', itr)
          	NumCount += 1
          
findPrime(1, 10)

# result: 
# 1  th prime :  1
# 2  th prime :  2
# 3  th prime :  3
# 4  th prime :  5
# 5  th prime :  7
~~~

<br>

# Assignment and Equivalence

상수와 상수 비교는 많이 해왔지만, object나 리스트 값 사이 비교는 까다로움.

~~~python
x = [1, 2, 3]
y = [100, x, 120] # nested list
z = [x, 'a', 'b'] # nested list

print('x :',x)
print('y :',y)
print('z :',z)

x[1]  = 1717 # x 안의 값이 바뀌면 xlist를 포함하고 있는 nested list 모두 값이 바뀜.

print('\nx :',x)
print('y :',y) # y는 x를 reference한다 (기존의 [1, 2, 3]을 먼저 가져온게 아니라, 그때그때마다 불러옴.)
print('z :',z) # z는 x를 reference한다.

x[1] = 2
x2 = [1, 2, 3]

# x를 reference하기 때문에 xlist의 값이 바뀌어도 유연하게 대처할 수 있는 것. 
if x == x2:
    print('Values are equivalent.')
else:
    print('Values are not equivalent.')

# is는 reference, 저장 장소가 같으냐에 대한 관점에서의 비교.
# False가 출력됨. 비록 값은 같지만 다른 reference(다른 저장 장소)를 가지고 있기 때문에.
if x is x2:
    print('Values are stored at the same place.')
else:
    print('Values are not stored at the same place.')
    
# True가 출력됨. x[1]이나 y[1][1] 모두 같은 reference인 xlist에서 가져오기 때문에.
if x[1] is y[1][1]:
    print('Values are stored at the same place.')
else:
    print('Values are not stored at the same place.')
~~~

Why this happended?

- Because of references.
- x has two references from y and z.
- The values of y and z are determined by x, and x is changed.

`==`

- Checks the equivalence of two reference values.

`is`

- Chekcs the equivalence of two referenced object's IDs.

<br>

# Class and Instance

`설계도(class)` -(Instantiation)-> `실제 집(instance)`

~~~python
# class definition
class MyHome:
    # 2 variables, and 4 functions.
    colorRoof = 'red'
    stateDoor = 'closed'
    # self는 instance(homeAt...)를 의미.
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDOor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Roof color is",self.colorRoof+', and door is',self.stateDoor+'.')

# function call
homeAtDaejeon = MyHome() # homeAtDaejeon에 MyHome()의 한 instance가 들어감.
homeAtSeoul = MyHome()
homeAtDaejeon.paintRoof('blue')
homeAtDaejeon.printStatus()
homeAtSeoul.printStatus()

# result:
# Roof color is blue, and door is closed.
# Roof color is red, and door is closed.
~~~

<br>

**Important Methods in Class - Constructor, Destructor**

Some basic methods, or member function in classes.

- Constructor
  - Called when instantiated.
- Destructor
  - Called when the instance is removed from the value table.

~~~python
from time import ctime

class MyHome:
    colorRoof = 'red'
    stateDoor = 'closed'
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Roof color is", self.colorRoof+", and door is",self.stateDoor+'.')
    # constructor의 self는 존재하지 않음.
    # 나중에 instance화 된 자신을 말하는 것. Return 되는 값이 self. 
    def __init__(self, strAddress):
        print("Built on", strAddress)
        print("Built at", ct ime())
    def __del__(self):
        print("Destroyed at", ctime())

homeAtDaejeon = MyHome('Daejeon KAIST') # Constructor parameter에 들어갈 내용 입력.
homeAtDaejeon.printStatus()
del homeAtDaejeon

# result:
# Built on Daejeon KAIST
# Built at Tue Nov 19 09:40:58 2019
# Roof color is red, and door is closed.
# Destroyed at Tue Nov 19 09:40:58 2019
~~~

