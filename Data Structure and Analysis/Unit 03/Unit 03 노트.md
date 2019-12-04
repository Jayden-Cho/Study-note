**Weekly Objectives**

- Learn the first set of <u>data structures</u>: linked list, stack, and queue.
  - 세 개 모두 선형적.
- Objectives are:
  - Understanding the definition of <u>abstract data types</u>.
  - Firmly understanding <u>how references work</u>. (매우 중요)
  - Understanding various linked lsit, stack and queue structures
    - <u>Singly linked list</u>, doubly linked list, circular linked list, ...
    - Able to implement <u>a stack and a queue</u> with a list
  - Understanding the procedures of linked list, stack, and queue management
    - Insert, delete, search, ...
    - Should be able to estimate the number of steps for inserts, deletes, and searches

<br>

# Abstract Data Type

**Scenario for List**

- 군중들 속에서 김씨를 찾는 경우. 
  - 무작정 돌아다니면서 이름을 외치는 방법: 순서없이 돌아다니니 혼란도 오고 매우 비효율적이다.
  - 현실의 방법 : 사람들을 줄 세우고 차례대로 찾다보면 결국엔 김씨 찾는다.
    - <u>선형으로 만들어 정돈한 후 원하는 것을 찾는게 포인트</u>.
- 복도에서 화장실을 찾는 경우.
  - 긴 복도가 있고 그 복도에 문이 여러개가 있다. 복도를 따라가다 보면 언젠간 화장실을 찾을 수 있다.
  - 어떻게 생각하지 않아도 결국에 따라가다 보면(선형적 공간을 따라가다 보면) 화장실을 찾을수 있다.
- 여러 구매자들의 정보가 있다 가정하자.
  - 이런 정보들을 탐색하거나 분석할 때, 무턱대로 마구잡이로 저장하는 것보다 구조화된 형태로 저장해야 하면 사용하기 편리하다.
  - 그 방법 중 가장 쉬운 것은 **List**.  

<br>

**Abstract Data Types**

- An abstract data type (ADT) is an <u>abstraction</u>(추상화) of a data structure. 자료 구조를 간단히 표현한 것.
  - An ADT specifies:
    - **Data stored**. 무슨(어떤 형태의) 데이터가 저장되어 있는지.
    - **Operations on the data**. 그 데이터에 어떤 operation이 작동하는지.
    - Error conditions associated with operations 
      - (현실에서 가장 중요한 것. 하지만 강의에서는 다루지 않음.)
      - 구조에서 지울 아이템이 없는데 지우라는 명령이 들어올 경우, 자리가 없는데 저장하라는 명령이 들어올 경우 등등.
  - Example: ADT modeling a simple stock trading system.
    - The <u>data stored</u> are buy/sell orders. 
    - The <u>operations</u> supported are:
      - order buy (stock, shares, price)
      - order sell (stock, shares, price)
      - void cancel (order)
    - Error conditions:
      - Buy/sell a nonexistent stock
      - Cancel a nonexistent order
- 현실에 존재하는 것을 간단화해서 표현하는 것이라 할수 있다.
- 자료 구조의 추상화란? 
  - 자료 구조는 자료를 추가하거나, 검색하거나, 삭제하거나 등의 일을 하는 것.
  - 다양한 일들이 일어나는 것을 일일히 세세하게 표현하는 것은 abstraction이 아니다.
  - 다양한 행동들을 <u>추상적으로 표현하는게</u> abstract data types.

- 데이터가 어떤 것이 될 것이고 어떤 operation이 가능한지 설명하는 것.
  - Class diagram처럼 구조 자체가 이러이러 하다 라고 나타내는 것과 비슷한것 같다. 

> 주머니 속이 어떻게 구성, 저장 되어있는지는 모른다. 대신 이 속에 어떤 데이터가 있는지 명시해두었고 어떤 operation을 사용가능한지 명시해둔게 ADT. 

<br>

# Array

**Creating a List by Array**

파이썬의 리스트를 사용해서 Array를 만든다고 생각해보자.

- Array (in our Python example, List, yet we will use only its index function)
  - <u>Each element</u> is accessible by **index**.
  - Index is typically zero or a positive integer
  - Very simple creation
    - Thay's why people use it

- Array는 일반적인 프로그래밍 언어들에서의 명칭이고, 파이썬에서는 List라 부른다.
- Array는 '동일한 data를 index를 활용해 저장, access 할수 있는 것' 

~~~python
x = ['a', 'b', 'd', 'e', 'f']

x[0] = 'a'
...
x[4] = 'f'
~~~

- 파이썬은 리스트 생성이 매우 간단하다.

<br>

**Search procedure in array**

- Let's find 'd' and 'c' from the list in an array.
  - Of course, you can use `in`, but we commit ourselves to use indexes only.
  - 파이썬만의 특징이기 때문에, 다른 언어에선 사용 불가. 원초적인 방법부터 알아보자.
- Then navigating from the first to the last until hit is the only way. 처음부터 마지막까지 search. index가 증가하기 때문에 단방향이다.

<br>

**Insert procedure in array**

- Let's insert 'c' between 'b' and 'd' in the list *(a = insert position index)*
  - First, make new list, or y, with six cells
  - Second, copy the reference link of `x[0:a-1]` to `y[0:a-1]` *(retrieval cnt.: a)*
  - Thrid, put a reference link to 'c' in `y[a]` *(retrieval cnt.: 1)*
  - Fourth, copy the reference links of `x[a:]` to `y[a+1:]` *(retrieval cnt.: n-a-1)*
  - Fifth, change x's reference to y's reference
  - Total count of retrievals = a+1 + n-a-1 = n

~~~python
x = ['a', 'b', 'd', 'e', 'f']
idxInsert = 2
valInsert = 'c'

# 1. make new list with six cells
y = range(6)

# 2. copy the reference link x[0:a-1] to y[0:a-1] (retrieval cnt.: a)
for itr in range(0, idxInsert):
  y[itr] = x[itr]   # 예를 들어 itr=0이라면 x[0], y[0] 모두 같은 'a'를 reference.
  
# 3. put a reference link to 'c' in y[a] (retrieval cnt.: 1)
y[idxInsert] = valInsert

# 4. copy the reference links of x[a:] to y[a+1:] (retrieval cnt.: n-a-1)
for itr in range(idxInsert, len(x)):
  y[itr+1] = x[itr]
 
# 5. change x's reference to y's reference
x = y   # x가 y를 reference. 기존의 x는 사라지고 새로운 리스트를 이용.
~~~

<br>

**Delete procedure in array**

- Let's remove 'd' in the list *(a = delete position index)*
  - First, make new list, or y, with five cells
  - Second, copy the reference links of `x[0:a-1]` to `y[0:a-1]` *(retrieval cnt. : a)*
  - Third, copy the reference links of `x[a+1]` to `y[a]` *(retrieval cnt. : n-a-1)*
  - Fourth, change x's reference to y's reference
  - Total count of retrievals = a+n - n-a-1 = n-1

~~~python
idxDelete = 3

# 1. make new list, or y, with five cells
y = range(5)

# 2. copy the reference links of x[0:a-1] to y[0:a-1] (retrieval cnt. : a)
for itr in range(0, idxDelete):
  y[itr] = x[itr]
  
# 3. copy the reference links of x[a+1] to y[a] (retrieval cnt. : n-a-1)
for itr in range(idxDelete+1, len(x)):
  y[itr+1] = x[itr]
 
# 4. change x's reference to y's reference
x = y
~~~

<br>

**Problems in Array**

- Whenever you put something in or get something out
  - You have to perform line-wise retrievals
    - Which is N retrievals
  - This process is just like that
    - There is a line of airline passengers
    - You want to put a passenger in the middle of the line because the filght is about to leave
    - You are moving all the passengers one step back
    - Then, you put the customer in the line.
- What-if we have a magic to create a space in the middle of the line?
  - Array → you are bounded to the 1-dimension that you have
  - Linked list → you are bounded no more.

- 우리가 넣고 뺄 때 line-wise retrieval해야 한다.
  - N개의 retrieval. 5개 정도면 괜찮지만, 100만개 일 때는 문제가 생긴다.

- 공항에서 사람들이 줄 서있다 치자. 근데 어떤 사람이 중간에 들어가고 싶다 할 때, 
  - 앞에 있는 사람들은 상관없지만, 뒤에 있는 사람들은 큰일난다. 모두 뒤로 움직여야 한다.
  - 그렇다면, 마법이 있어서 그 사람이 들어갈 자리를 만들어준다 치자. 
    - 소프트웨어에서 가능할까? 할수는 있다. 하지만 그렇게 한다면 선형적 공간이 아니게 될 것.
- Linked list는 0,1, 2, 3,.. 1차원 선형적으로 저장하지 않는다.

<br>

# Linked List 1

인덱스 구조가 아닌 레퍼런스 구조 동작. 마법처럼 중간에 공간을 만들어 준다. 

<br>

***Detour*: Assignment and Equivalence**

reference는 기존의 값을 그냥 적어두는게 아니라, 불러오는 것.

- reference되는 값들이 변경되면 reference하는 값들도 바뀐다.
- `==` 는  값의 동일함을 비교, `is` 는 레퍼런스의 동일함을 비교.

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

<br>

**Basic Structure: Singly linked list**

![a](https://i.imgur.com/EDJBTZw.png)

- Construct a singly linked list with nodes and references.
  - A <u>node</u> consists of:
    - A <u>variable</u> to hold a reference to its <u>next node</u>. **Next**. 
      - 다음 노드를 가리키는 레퍼런스를 저장한 변수.
    - A <u>variable</u> to hold a reference to its <u>value object</u>. **Object**.
      - 그 노드에 어떤 값이 저장될지 알려주는 레퍼런스를 저장한 변수.
  - Special nodes: <u>Head</u>(리스트의 첫 노드) and <u>Tail</u>(리스트의 마지막 노드)
    - Head와 Tail은 object에 아무 것도 저장되지 않음.
    - You can construct the singly linked list without them.
    - But, using them makes search, insert, and delete more convenient.
  - Generally, requires more coding than array.
- 중간에 레퍼런스를 조작하여 공간을 한 번에 생성할 수 있다는 장점이 있지만, 코딩이 길다는 단점도 존재한다.
- Object에는 값 자체가 저장되어 있지 않고, 단지 reference만 저장되어 있다.
- Next는 다음 노드를 가리키는 것 뿐 다음 노드의 값이 바뀐다고 해서 레퍼런스가 변하지 않는다.

> 레퍼런스는 특정 값을 가리키는 화살표 같은 것.

<br>

**Implementation of Node class**

- Member variables
  - Variable to **reference** the <u>next node</u>.
  - Variable to **hold** a <u>value object</u>.
  - (Optional) Variable to check whether it is a head or not.
  - (Optional) Variable to chekc whether it is a tail or not.
- Member functions
  - Various set/get methods.

~~~python
class Node:
    nodeNext = None
    nodePrev = ''
    objValue = ''
    binHead = False
    binTail = False

    def __init__(self, objValue='', nodeNext=None, binHead=None, binTail=None):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail

    def getValue(self):   # value를 가져와라
        return self.objValue
    def setValue(self, objValue):   # value를 저장해라
        self.objValue = objValue
    def getNext(self):   # 다음의 노드는 무엇인가
        return self.nodeNext
    def setNext(self, nodeNext)   # 다음 노드를 정의
        self.nodeNext = nodeNext
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail

node1 = Node(objValue='a')
nodeTail = Node(binTail=True)
nodeHead = Node(binHead=True, nodeNext=node1)
~~~

<br>

# Linked List 2

**Head and Tail**

- Specialized node
  - Head : Always at the first of the list. 
  - Tail : Always at the last of the list.
  - These are the two corner stone showing the start and the end of the list.
- These are optional nodes.
  - Linked list works okay without these.
  - However, having these makes implementation very convenient.

<br>

Empty Linkd List

![a](https://i.imgur.com/m4HR4gy.png)

<br>

Linked List with Two Nodes

![a](https://i.imgur.com/EDJBTZw.png)

<br>

**Search procedure in singly linked list**

- Again, let's find 'd' and 'c' from the list.
- Just like an array, navigaring from the first to the last until hit is the only way.
- No differene in the search pattern, though you <u>cannot use index</u> any further.
  - 그 대신 `Next` 사용.
  - Your list implementation may include the index function, but it is not required in the linked list.

찾는 방법

1. head를 리스트에서 찾는다.
2. `Next` 노드를 찾는다. `Next` 노드가 tail이면 `break` (검색 끝), 아니면 `Next.object` 가 'd'인지 확인.
3. 만약 'd'가 아니라면 `Next.node` .

<br>

**Insert procedure in singly linked list**

- This is the moment that you see the power of a linked list
- Last time, you need N retrievals to insert a value in the array list
- This time, you need only three operations.
  - With an assumption that you have a reference to the node, $Node_{prev}$ that you want to put yout new node next.
  - First, you store a $Node$, or a $Node_{next}$ pointed by a reference from $Node_{prev}$'s nodeNext member variable
  - Second, you change a reference from $Node_{prev}$'s nodeNext to $Node_{new}$ 
  - Third, you change a reference from $Node_{new}$'s nodeNext to $Node_{next}$.

- 어디에 새 값을 추가할지 정도는 알고 있어야 한다. $Node_{prev}$나 $Node_{next}$.
-  $Node_{prev}$와 $Node_{next}$를 연결하고 있는 `Next` 덮어써서(overwrite) 끊어버린다.
  - $Node_{prev}$의 `Next`를 $Node_{new}$를 가리키도록 덮어쓴다.
  - `node_prev.next = Node_new` 이렇게.
- 그 다음 $Node_{new}$의 `Next`를  기존에 있던 $Node_{next}$ 로 대치.

![a](https://i.imgur.com/0YRo2C4.png)

- 'a'까지의 레퍼런스 구조와 'd'부터의 레퍼런스 구조는 변한게 없다.

<br>

**Delete procedure in singly linked list**

- This is the another momnet that you see the power of a linked list

- Last time, you need N retrievals to delete a value in the array list.

- This time, you need only 3 operations.

  - - With an assumption that you have a reference to the node, $Node_{prev}$ that you want to remove the new node next.
    - First, you retrieve $Node_{next}$ that is two steps from $Node_{prev}$.
    - Second, you change a reference from $Node_{prev}$'s nodeNext to $Node_{new}$.

  - The node will be removed because there is no reference to $Node_{remove}$

- $Node$를 따로 instantiate할 필요 없다.

![a](https://i.imgur.com/Tj9EvrA.png)

- `NodeRemove = NodePrev.Next` 로 설정하고, `NodeNext = NodePrev.Next.Next`.
- $Node_{prev}$에서 $Node_{remove}$로 가는 reference를 끊어줘야 한다. 어떻게? 
  - $Node_{prev}$의 `Next`를 $Node_{next}$로 설정.
  - 그렇다면 값이 overwrite되어 더 이상 $Node_{remove}$로 향하지 않는다.
  - $Node_{remove}$의 `Next`가 여전히 $Node_{next}$로 향하지만 어떤 레퍼런스도 $Node_{remove}$를 가리키는게 없기 때문에 그것으로 찾아갈 방법이 없어 삭제될 것 같이 되는 것.
    - 하지만 저장된 것이 삭제된 것이 아니다. Garbage collector에 저장됨.
    - 어느 레퍼런스도 향하지 않는 것을 받아 삭제함.
- 이 과정에서 사용한 노드는 $Node_{prev}$, $Node_{remove}$, $Node_{next}$. 

<br>

**Implementation of Singly linked list**

~~~python
class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0

    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)

    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue=objInsert)
        nodePrev = self.get(idxInsert-1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove-1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve+1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print("")

    def getSize(self):
        return self.size

list1 = SinglyLinkedList()
list1.insertAt('a', 0)
list1.insertAt('b', 1)
list1.insertAt('d', 2)
list1.insertAt('e', 3)
list1.insertAt('f', 4)
list1.printStatus()

list1.insertAt('c', 2)
list1.printStatus()

list1.removeAt(3)
list1.printStatus()
~~~

