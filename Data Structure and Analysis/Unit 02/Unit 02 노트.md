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



