# Design and Programming

Unit 01에서는 '프로그래밍 하는 법'을 배웠다면, 이번 Unit에서는 '프로그램을 잘 설계하는 법'을 배운다.

- Unit 01: 톱질, 망치질, ... 도구를 사용하는 방법 터득.
- Unit 02: 설계를 잘하는 법 터득.
  - 설계도를 보고 읽을줄 아는 능력. Good/Bad design 판별할 수 있는 능력.

<br>

**Unit 02 Objectives**

- Learn the object-oriented paradigm(OOP) and the basic of software design.
- Objectives are
  - Understanding object-oriented concepts.
    - Class, instance, inheritance, encapsulation, polymorphism,...
  - Understanding a formal representation of software design
    - Memorizing a number of Unified Modeling Language(UML) notations
  - Understanding a number of software design patterns (강의는 없지만 자료는 있음)
    - Factory, Adapter, Bridge, Composite, Observer
    - Memorizing their semantics and structures

<bR>

**Design and Programming**

큰 틀을 만들되 그 틀을 사용해서 다른 방식으로 창조한다.

- 호텔을 예시로 들자. 
  - 전체적인 호텔 내부 구조는 비슷하다. 층마다 객실이 있고 휴게 시설이 존재한다. 
  - 하지만 모든 객실이 동일한 것은 아니고, 같은 방이라도 위치나 물품들이 달라질 수 있다. 
  - 구조가 달라질 때 마다 설계를 처음부터 다시한다는 것은 비효율적이므로 큰 틀을 창조하고 그 틀 안에서 구성물들을 변환시키면 된다.

<Br>

**Good Software Design**

좋은 Software design이란?

- <u>Correctness</u> - 일단 클라이언트의 목적에 맞게 실행되어야 한다. 하지만 목적이 맞더라도 결과물이 incorrect하면 안된다. 물론 에러도 없어야 한다.
- <u>Robustness</u> - 보통 프로그램 사용자들은 프로그램 마음대로 사용한다. 틀린 입력은 없더라도, 예측하지 못한 값이나, 가중된 값들을 입력받았을 때 (overload가 생길 때) 에러가 생기지 않게 설계하자.
- <u>Flexibility</u> - 시간이 지나면 새로운 설계 방법이 고안될 수 있다. 그러므로 미래의 수정을 반영할 수 있게 유연하게 설계하자.

- <u>Usability and Reusability</u> - 사용자가 프로그램을 잘 사용할수 있도록 지원을 해야 한다. 인터페이스를 이해하게 쉽게 한다거나 아니면 다른 목적으로도(다른 환경에서도) 사용될 수 있게 해줘야 한다.
- <u>Efficiency</u> - 빠르게 실행되고 크기가 작아야 하는 efficiency와 너무 복잡하지 않게 개발되야하는 두 가지 efficiency가 존재한다.

> 외울 필요는 없고 일단 중요하다고만 알아두는게 중요. 이런 차원에서 스스로의 프로그램을 판단해보자.

<br>

**Object-Oriented Design**

앞의 내용까지는 아주 일반적인 내용. 비단 프로그래밍에만 해당되는게 아니라 건축 등 모든 분야에서 폭 넓게 해당된다.

Design concept이 여러 발전해왔지만 요즘에 쓰는건 Object-Oriented Design. 

- 현실 개념을 추상화하여 프로그래밍 하는 것.

- 은행 시스템을 예를 들자.

  - 개념의 이름(concept1): Customer
    - 개념의 특성(Member variable, or Attribute) - ID, AccountNum
    - 개념의 행동 - login(), requestWithdrawal(), confirmSecurityCard()
  - concept2: Transcation 
    - 개념의 특성 - Amount(얼마인지), releaseATMID(어느 지점인지)
    - 개념의 행동 - releaseMoney()
  - concept3: Banking
    - 개념의 특성 - amountInAccount
    - 개념의 행동 - reduceMoney(), sendNotice()

  > Transaction이나 Banking같은 concept은 추상적이지만 충분히 프로그래밍으로 특성화될 수 있다.

  >  **Real World Concepts -(Abstract)-> Software Design Entities**

추상화(abstract)는 무엇인가?

- 목적에 맞게끔 간략하게 만드는 것.

<br>

**What are Class and Inheritance?**

우리가 만드는 concept들은 하나의 entity로 표현하는게 아니라 많은 class들로 표현되는 것이다.

- Class vs. Inheritance - 실행하기전에 만들어져 있다.
- Class = template, Instance = realized version.
  - Class
    - Result of design and implementation
    - Conceptualization
    - Corresponds to design abstractions
  - Instance - 실행을 하면서 만들어진다.
    - Result of exection
    - Realization
    - Corresponds to real world entities

Class들의 특성을 이용해 개별적인 instance를 생성하는 것이다.

- 모두 공유하고 있는 것은  template.
- 은행에서 고객을 표현할 때 ID와 accountNum만 필요하다. 
  - 모든 고객에게 적용된다. 머리 색깔 이딴거 필요없다. 
  - 이미 설계된 class에 의해 function을 사용할 수 있다.
- 추상화라는 것을 통해 균일하게 설계된 여러개의 인스턴스를 만들 수 있고 하나의 설계를 이용해 실제의 entity를 표현한 것이다.

<br>

#  UML notation 1

**Software Design as House Floorplan** 

- Need to learn how to communicate with colleagues.
  - Learn standard.
  - Learn how to represent your design to your boss.
- In software engineering.
  - UML is the standard.

software design은 house floorplan(평면도)를 그리는 것과 같다.

- 마음대로 그리는 것이 아니다. 표준이 있다. 표준에 맞게 그림을 그리는 것이다.

- Software 설계에서는 'UML'을 표준으로 한다.

<br>

**UML notation : Class and Instance**

많은 UML-based 설계도가 존재하지만 일단은 class UML만 다룬다.

**전체 예시**

 ~~~
'''
Abstract class - Person
Class - Customer
Named instance - Park:: Customer
Unnamed instance - :Customer
'''

						Park::Customer 
-ID : String
# AccountNum : Integer
+ Name : String = Hey
+ logIn() : void
+ requestWithdrawal() : Boolean
+ confirmSecurityCard() : Boolean
 ~~~

<br>

**세부 내용**

~~~
'''
Abstract class - Person
Class - Customer
Named instance - Park::Customer
Unnamed instance - :Customer
'''
~~~

- `Named instance - Park::Customer` : `Customer`라는 class를 기반으로 해서 `Park`라는 instance를 생성.
- `Unnamed instance - :Customer` : instance 이름이 정해지진 않았지만 instance가 생성된 경우.

~~~
						Park::Customer 
~~~

- `Park` : Instance Name	
  - Instance name이 정해지지 않은 경우 비워둘 수 있다.
- `Customer` : Class Name

<br>

Member variables (Attribute, Property라고도 불림)

~~~
-ID : String
# AccountNum : Integer
+ Name : String = Hey
~~~

- `+-#(name):(type) = (default value)`
  - `default value`를 원하면 `+ Name : String = Hey` 처럼.
- Visibility options : `+` (public), `#` (protected), `-` (private)
  -  현실에서는 private을 주로 사용. 안전하게 만들고 안전하게 데이터를 지키기 위해.

<br>

Methods (Member function이라고도 불림)

~~~
+ logIn() : void
+ requestWithdrawal() : Boolean
+ confirmSecurityCard() : Boolean
~~~

- `+-#(name)(arguments):(return type)`
- Member variable과 같이 visibility option들이 존재한다.

<Br>

# Encapsulation and Inheritance

Encapsulation - 클래스 내부에 모든 내용이 있고 외부에서만 메소드를 사용하여 건들 수 있다.

**Encapsulation**

일단 값은 줄께. 속에 있는건 내가 알아서 할테니까 건들지마.

- Object(객체) = Data(Attribute) + Behavior(Method)
  - Data: field, member variable, operation
  - Behavior: method, member function, operation
    - Object안에 Data가 있는걸 알지만, Behavior를 통해서 Data를 생성하겠다.
    - 내부 건들지 말고 내가 제공하는 Behavior를 이용해서 접근해라.
    - 전구 안의 전선 어떻게 연결되어있는지 모름. 하지만 입구 앞에 전선 두개가 나와있음. 안쪽은 건들지 말고 전선 두개만 이용하라는 뜻.
- Delegating the implementation responsibility! 구현에 대한 책임이 없음.
  - Bring me a sausage. and I don't care how you made it. 
- 어떻게 구현하는가? Utilizing the visibility.
  - private: seen only within the class. 이걸 이용해 encapsulation 구현.
    - method는 public으로, data는 private.
  - protected: seen only within the class and its descendants
  - public: seen everywhere
- Python does not support the visibility options. 
  - 하지만 약속할 수 있음. 앞에 underscore 두개가 있으면 private이라는 뜻.

<br>

**Inheritance**

- Inheritance
  - Giving my attributes to my descendants. 내 특성을 자손들에게 물려주는 것.
    - My attributes include:
      - Member variables
      - Methods
  - My descendants may have new attributes of their own. 자손들 스스로 새로운 특성을 가질수도 있음.
  - My descendants may mask the received attributes. 물려준 값을 mask하고 자신 나름대로의 값으로 바꿀 수 있음.
    - 새로운 attribute는 아니다.
  - But, if not specified, sons follow their father. 위 두 경우가 아니면 물려진 특성을 따른다.
- Superclass. 조상(아버지)
  - My ancestors, specifically my father
  - <u>Generalized</u> from the conceptual view
- Subclass. 자손
  - My descendants, specifically my son
  - <u>Specialized</u> from the conceptual view
- How about having a mother?
  - Yes. It is possible in Python. 여러 클래스에서 inheritance 가능하다.

> 두번 몇번 칠꺼 한번만 쳐도 된다.

<br>

**Inheritance in Python**

~~~python
class Father(object):
    strHometown = "Jeju"
    def __init__(self):
        print("Father is created")

    def doFatherThing(self):
        print("Father's action")

    def doRunning(self):
        print("Slow")

class Mother(object):
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created")

    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother):
    strName = "Moon"
    def __init__(self):
      	# superclass를 call.
        super(Child, self).__init__()
        print("Child is created")
    def doRunning(self):
        print("Fast")

me = Child()
me.doFatherThing() # Child()에는 없지만, Father()를 inherit 했기 때문에.
me.doMotherThing()
me.doRunning() # Child()의 특성이 overwrite한 것.
print(me.strHometown) # 첫 번째 inherit 받는 것.
print(me.strName) # 자신의 attribute.

'''
result:
Father is created
Child is created
Father's action
Mother's action
Fast
Jeju
Moon
'''
~~~

<br>

***self* and *super***

- *self* : reference variable pointing the instance itself. 인스턴스 자기자신을 가리키는 것.
- *super* : reference variable pointing the base class instance. 자신이 상속받고 있는 것.
  - super is used to call the base class methods

~~~python
class Father(object):
    strHometown = "Jeju"
    def __init__(self, paramHome):
        self.strHometown = paramHome
        print("Father is created")

    def doFatherThing(self):
        print("Father's action")

    def doRunning(self):
        print("Slow")

class Mother(object):
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created")

    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother):
    strName = "Moon"
    def __init__(self, paramName, paramHome):
        super(Child, self).__init__(paramHome)
        self.strName = paramName
        print("Child is created")
    def doRunning(self):
        print("Fast")

me = Child("Sun", "Universe")
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)

'''
Father is created
Child is created
Father's action
Mother's action
Fast
Universe
Sun
'''
~~~

<br>

# Polymorphism and Abstract Class

**Polymorphism**

- Polymorphism - 다양한 모양. 공통적으론 같지만 세부 내용이 다르다.
  - Poly : Many
  - Morph : Shape
  - Different behaviors with <u>similar signature</u>.
    - Signature  = Method name + Parameter list. 메소드 이름이 같아도 구성품이 다르면 다른거다.
  - **Method Overriding**
    - Base class has a method A(num), and its derived class has a method A(num). 그렇다면 Base class의 A를 무시하고 새로이 정의된 class의 A로 override.
  - **Method Overloading** 
    - A class has a method A(num), A(num, name). 메소드 이름은 같지만 param이 달라 overload 된다.

<br>

~~~python
class Building:
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door Opened")

class Hotel(Building):
  	# override
    def openDoor(self):
        print("Bellboy opens a door")
    def checkIn(self):
        print("Someone checks in for 1 day")
    def checkIn(self, days):
        print("Someone checks in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(2)
~~~

<br>

~~~python
class Building:
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door Opened")

class Hotel(Building):
  	# override
    def openDoor(self):
        print("Bellboy opens a door")
    def checkIn(self, days = 1):
        print("Someone checks in for", days, "days")
        
lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(2)

# result:
# Bellboy opens a door
# Someone checks in for 1 days
# Someone checks in for 2 days
~~~

<br>

**Abstract Class**

- Abstract class, or Abstract Base Class in Python.
  - A class with an <u>abstract method</u>. 
  - What is the abstract method?
    - Method <u>with signature</u> but with no implementation. 시그니쳐만 있는 메소드. 세부 내용은 없다.
    - Why use it then?
    - I want to have a window here, but I don't know how it will look like, but you shoule have a window here!
      - 사람들이 여러 명 작업할 때, Window 클래스를 만들었다치자. Abstract class를 만들었다는 의미는 '일단 Window() 어떻게 만들던 상관없다. 다만 문이 열리게끔 알아서 코딩해라'라는 것.
  - Abstract class is not a complete implementation, it is more like a half-made produce.
  - Therefore, you can't make an instance. 실제로 설계되지 않은 그냥 틀만 있는 상태이기 때문에. 
- The concrete with full implementations and inheriting the abstract class will be a basis for instances.

~~~python
# abstract class를 만드려면 abc 모듈 import.
from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod
    def openDoor(self):
        pass
    @abstractmethod
    def openWindow(self):
        pass
      
# Room class는 그저 틀이고 그것을 이용하려면 개별 class를 만들고 그 안의 method들을 채워넣고 instantiate해야 작동한다.
class BedRoom(Room):
  	# 껍데기만 있던 openDoor()를 채워넣는다.
    def openDoor(self):
        print("Open bedroom door")
    def openWindow(self):
        print("Open bedroom window")

# 이것처럼 abstract class의 메소드 중 하나만 구현한다면 에러가 발생.
class Lobby(Room):
    def openDoor(self):
        print("Open lobby door")

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))

# result:
# True True
# TypeError: Can't instantiate abstract class Lobby with abstract methods openWindow
~~~

<br>

**Overriding Methods in object**

- All of Python classes are the descendants of *object*. 그니까 모든 class들은 *object*라는 클래스의 자손.
  - If you don't specify the base class of your class, then your class is the direct derived class of *object*. 특정 inheritance를 선언하지 않으면 *object*가 inherit된다.
- *object* has many hidden methods:
  - `__init__` : Constructor
  - `__del__` : Destructor
  - `__eq__` : Equality. 값을 비교하는 것.
  - `__cmp__` : Comparison
  - `__add__` : 더하기.
- You override them to make the methods behave as you please.

~~~python
# Inheritance가 없는 상황. ()가 없다. 그렇다면 Inheritance는 object.
class Room:
    numWidth = 100
    numHeight = 100
    numDepth = 100
		# 기존의 object에 있는 method에 override해 constructor를 생성한다.
    def __init__(self, parWidth, parHeight, parDepth):
        self.numDepth = parDepth
        self.numWidth = parWidth
        self.numHeight = parHeight
    def getVolume(self):
        return self.numDepth*self.numHeight*self.numWidth
    def __eq__(self, other):
        if isinstance(other, Room):
          	# Duck Typing. 덕 테이프. 
            # Room은 class인거 알지만, other는 어떤게 들어올지 class 설계 당시에는 모른다. 만약 class가 아닌 다른 형태가 들어온다면 후에 실행할 때 다른 형이면 에러 발생. Easier to Ask for Forgiveness then Permission(EAFP)
            if self.getVolume() == other.getVolume():
                return True
        return False
      
room1 = Room(100, 20, 30)
room2 = Room(100, 10, 60)
print(room1 == room2)

# result:
# True
~~~

<br>

Duck Typing

~~~python
        if isinstance(other, Room):
            if self.getVolume() == other.getVolume():
                return True
~~~

- Room은 class인거 알지만, other는 어떤게 들어올지 class 설계 당시에는 모른다.
- 만약 class가 아닌 다른 형태가 들어온다면 후에 실행할 때 다른 형이면 에러가 발생한다.
- Easier to Ask for Forgiveness then Permission (EAFP).

<br>

# UML notation 2

**More about UML Notations**

현실에서는 다양한 UML이 존재한다.

- Many types of UML diagrams used for different stages of development. 
  - Use-case diagram
  - <u>Class diagram</u>
  - State diagram
  - Deployment diagram
- We are dealing with OOP in this week.
  - Mainly, class and instances.
  - Also, some of software design patterns.
  - Hence, we focus on
    - *Class diagram*.
  - OOP에 집중하기 때문에 Class diagram에 알아보는 중.

<br>

**UML notation : Class and Instance(one more time)**

~~~
'''
Abstract class - Person
Class - Customer
Named instance - Park::Customer
Unnamed instance - :Customer
'''
~~~

- `Cusotmer`를 사용하려면 Abstract class인 `Person` class를 override(Inherit)해야 한다.

~~~
Visibility options
+ → public
# → protected
- → private
~~~

- Visibility options는 <u>encapsulation</u>의 특성을 만드는 데 활용된다.

<br>

~~~
						Park::Customer 
-ID : String
# AccountNum : Integer
+ Name : String = Hey
+ logIn() : void
+ requestWithdrawal() : Boolean
+ confirmSecurityCard() : Boolean
~~~

- `+ logIn()` 같은 것을 Method signature라고 부른다.
  - Method signature가 동일한 경우 <u>Method override</u>가 가능하다. (물론 super class와 자식 클래스 사이)
  - Method signautre가 similar할 경우 <u>Method overload</u>가 가능하다.

<br>

**Structure of Classes in Class Diagram**

![a](https://i.imgur.com/aXtoh4R.png)

- 클래스 사이의 직선 - Association. Association으로 클래스 간의 관계를 알 수 있음.

- Generalization(Hollow point arrow) - Inheritance. Credit, Cash, Check class 모두 일반적으로(공통적으로) Payment라는 속성을 가지고 있다.

- Aggregation(마름모꼴 화살표)

<br>

# Structure and Relationship

  **Generalization**

- Generalization의 모든 관계, 특성은 inheritance-based.

- Generalization between classes:
  - *is-a* relationship.
    - Customer *is-a* Person. 
  - <u>Inheritance relationship</u>.
  - `Customer`(sub) → `Person`(super)
    - Direction of generalization : From subclass to superclass
  - Hollow triangle shape.
- Base class
  - Person
- Leaf class
  - Park::Customer. Person class의 맨 끝에 달린 잎사귀들.

<br>

**Association**

~~~python
# '하나의' customer가 '여러 개의' accounts를 가지고 있다.
class Customer:
    ID = "No one"
    lstAccounts = [] # 여러 개의 계정을 넣어둘 곳.
    def addBankAccount(self, account):
        self.lstAccounts.append(account)

# '하나의' account가 '하나의' customer를 가지고 있다.
class BankAccount:
    strAccountHolder = "No one"
    def changeAccountHolder(self, holder):
      	# 하나의 AccountHolder만 가질수 있다.
        self.strAccountHolder = holder    
~~~

- Association between classes

  - <u>*has-a*</u> relationship. '어떤 클래스가 무엇을 가지고 있다'라는 관계.
  - Member variables(Attribute)
    - Multiplicity 정보를 필요로 함. 예를 들어 무언가가 얼마만큼을 가지고 있다.
    - A customer *has-a* number of holding accounts.
      - '하나의' customer가 '여러 개의' accounts를 가지고 있다.
    - An account *has-an* account holder customer.
      - '하나의' account가 '하나의' customer를 가지고 있다.
  - 표현 방법 : Simple line. 화살표 없는 라인. 화살표 있다면 '→'.
  - If a simple arrow is added, 방향성을 나타내는 것.
    - A customer has a <u>reference</u> to bank accounts.
      - 고객 클래스가 계좌 클래스를 레퍼런스할 권한(정보)을 가지고 있다.
    - A bank account has a <u>reference</u> to a customer
    - Navigability. 화살표 방향을 navigate.
    - 그니까 화살표가 있으면 reference처럼 하나가 일방적인 관계를 가지고 있고, 화살표가 없으면 상호 보완적인 관계를 가지고 있다.

  ![a](https://i.imgur.com/JsDSaC3.png)

  - Line ends are tagged by roles
    - `Account holder`
      -  `Customer`의 관점에서 볼 때, `Customer`는 `BankAccount`를 들고 있는 `Account Holder`이다.
    - `Holding accounts`
      - `BankAccount`의 관점에서 볼 때, `BankAccount`는 `Customer`가 들고 있는 `Holding Accounts`이다.
    - With prefix showing the visibility
      - `+` : public, `-` : private, `#` : protected
    - `1`과 `*`의 관계는 일대다 관계.
      - `Customer`는 `BankAccount`를 *개 가질수 있지만, 반대로 `BankAccount`는 `Customer`를 한 개 가질수 있다.

<br>

**Multiplicity of Association**

- In CS and Eng,
  - `*` often means many.
  - Hence,
    - `1..*` : 1 to Many
    - `*` : 0 to Many. `0..*`와 같다.
      - 위의 `BankAccount`에 `*`였던 이유는 계좌가 0개부터 *개까지 있을 수 있기 때문에.
  - Naturally,
    - `1` : Exactly one
    - `0..1` : One or zero
- If not specified, it means one.

<br>

**Aggregation**

![a](https://i.imgur.com/6U2kKHE.png)

- Special case of association.
  - <u>Special</u> *has-a* relationship.
  - More like, <u>*part-whole*</u> or <u>*part-of*</u> relationship
  - A family member is a <u>part of</u> a family.
    - The existence of the family depends one the aggregation of the family member
    - If nothing to aggregate, there is no family. 
      - `FamilyMember`가 하나도 없을 경우, `Family` 또한 존재하지 않는다.
  - <u>Hollow diamond shape.</u>
- Aggregation often occur:
  - When an aggregating class is a <u>collection class</u>.
  - When the collection class's life cycle depends on the collected classes.

<br>

**Dependency**

~~~python
class Calculator:
    def calculateSomething(self):
        return ....

class Engineer:
    def drawFloorplan(self):
      	# Method 내부에 있는 변수라 Method가 끝나면 저장되지 않고 사라진다.
        calc = Calculator()
        value = calc.calculateSomething()
        return value
~~~

- Dependency between classes
  - <u>*use*</u> relationship. 다른 클래스를 import해서 import한 메소드를 이용하는 것.
  - An engineer *uses* a calculator.
    - May use for 
      - Local variables
      - Method signatures
        - Parameter types
      - Method return types
  - Something that you import for the implementation
  - 점선으로 관계가 표현된다.

<br>

**Let's Practice**

![a](https://i.imgur.com/CJ4wX4M.png)

<br>

`Customer` --(line)-- `Order`. **Association**

- 주문을 처음 해본 사람부터 여러 번 해본 사람까지 다양하게 존재하기 때문에 `Order`와  `0..*` 관계를 가진다.  
  - 쉽게 말해, `Customer`는 0명부터 *명까지 존재할 수 있다.

- `Order`는 무조건 한 명의 고객이 주문을 하기 때문에 `Customer`와  `1`의 관계를 가진다.
  - 쉽게 말해, `Order`는 무조건 한 번이다. 고객 한 명에 주문 하나만 할당된다.

<br>

`Order` <--(diamond arrow)-- `OrderDetail`. **Aggregation**

- `Order`는 여러 개 (한개 이상)의 `OrderDetail`을 가질 수 있지만, `OrderDetail`이 없다면 `Order`는 존재하지 않는다.

<br>

`OrderDetail` --(Simple Arrow)--> `Item`. **Association** 

- `OrderDetail`은 `Item`을 하나를 가지고 있어야 한다. 반대로 `Item`은 `OrderDetail`을 `0..*`개 가질 수 있다.
  - 아이템 자체는 한 번도 주문이 안됐었을 수도 있고, 인기 상품이라 여러 번 주문됐을 수도 있다. 
- `OrderDetail`에서 `Item`으로 단방향 화살표를 들고 있다.
  - `OrderDetail`은 `Item`의 정보를 가지고 있다. 반대로 `Item`은 `OrderDetail`의 정보를 하나하나 가지고 있지는 않다.
  - `OrderDetail`은 `Item`을 정의할 수 있는 하나의 변수가 있어야 한다.  

<br>

`Order` --(Simple Arrow)--> `Payment`

- `Order`를 할수 있는 방법은 여러가지이므로 `1..*`. 반대로 `Payment`는 하나의 `Order`에만 적용이 된다.