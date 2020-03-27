**Unit Objectives**

- Study tree data structure. Particularly focusing on the structure and the operation of the binary search tree.
- Objectives are :
  - Memorizing the definitions, the terminologies, and the characteristics of trees.
  - Understanding the structures of trees.
  - Understanding the structure and the operations of a binary search tree.
    - Insert, search, delete operations
    - Tree traversing operations.
      - Depth first search
        - In-order, post-order, pre-order sequences
      - Breadth first search
      - Level order search
  - Understanding the performance of binary search tree.

<br>

# Tree as an Abstract Data Type and Structure

***Detour*: Abstract Data Types**

- An abstract data type (ADT) is an abstraction of a data structure. 
  - An ADT specifies :
    - Data stored
    - Operations on the data
    - Error conditions associated with operations
- Example: ADT modeling a simple stock trading system
  - The data stored are buy/sell orders.
  - The operations supported are 
    - order buy(stock, shares, price)
    - order sell(stock, shares, price)
    - void cancel(order)
  - Error conditions:
    - Buy/sell a nonexistent stock.
    - Cancel a nonexistent order.
- Tree도 abstract data type중 하나.

<br>

**Tree as an Abstract Data Type**

- Tree structure - abstract data type.
  - Data stored
    - As a tree structure.
  - Operatons
    - Ordinary data structure operations just as linked lists :
      - Insert
      - Delete
      - Search
    - Special searching approaches for trees and networks :
      - <u>Traverse</u>. 각각의 노드를 한번만 체계적인 방법으로 방문하는 과정.
  
- 일반적인 트리와 다르게 upside down. 
  - 위의 뿌리에서 밑의 줄기로 뻗어나간다. 
- 기본적인 data structure의 operation을 지원해준다. 이외에도 특별한 'traverse'가 가능하다.

<br>

**Why do we use trees?**

- Because the structure of trees is a good analogy to the various real world structures.	
  - Corporate structures
  - Group bank accounts
  - Command and control structures
- Why is this structure one of the most favorite structures?
  - A clear approach of *Divide and Conquer*.
- 공통적으로 divide and conquer를 할 수 있다.
  - 데이터의 특성을 반영해서 divide하고 그리고 그것을 conquer하는게 tree structure.
  - Tree 구조를 다룰 때도 recursion 사용.

<br>

**Structure of Stored Data**

- Nothing but with multiple *'next'*s.
  - Each node has multiple next nodes.
  - Particularly, this structure maintains the next nodes as an array or variables.

- Linked list는 노드들을 정의.
  - 노드에는 Object, Next를 저장하는 reference 두 개가 존재한다.
- Tree 구조는 노드에 다수의 next reference를 가지고 있을 수 있다.
  - Next가 많으니 그에 대한 rule를 제대로 설정해야.

<br>

# Terminologies of Tree Structure

**Terminologies (1)**

![a](https://imgur.com/ahCfcYg.png)

- Tree는 하나의 노드에서 출발해 여러 개의 next reference를 가지고 exponential하게 밑의 노드가 커진 것.

- 하나의 next reference가 다음 node를 가리킬 때 가리키는 것을 **edge**라고 한다.
- 트리에서 맨 위에 있는 노드를 **root**라고 한다.
  - Head와 동일한 의미.
- Edge로 연결된 두 노드 중 위에 있는 것은 **parent**, 밑에 있는 것은 **child**.
- 같은 레벨에 있는 여러 개의 노드(동일한 parent에서 나온 노드)들을 **siblings**라고 부른다.
- 더 이상 다른 next ref를 가지고 있지 않은 경우(가장 하단의 노드)를 **Leaves, Terminal Nodes** 라고 부른다.
- Terminal nodes가 아닌 것을 **Internal nodes** 라고 부른다. 

<br>

**Terminologies (2)**

![a](https://imgur.com/Fj6cA7B.png)

- root에서 파생된 모든 노드들을 **descendant** 라고 부른다.
- 하나의 노드의 이전 노드들을 **ancestor** 라고 부른다.
- **Path** 라는 것은 root의 위치에서 특정 노드까지의 최단 거리.

<br>

**Terminologies (3)**

![a](https://imgur.com/M1n2L9n.png)

- 특정 노드의 **depth** 는 특정 노드의 path의 길이.
- Tree의 **height** 는 maximum path length.

- 특정 노드의 **degree**는 특정 노드가 가질 수 있는 child의 개수.
  - Next reference의 개수.
- Tree의 **size**는 Tree 속 노드의 개수.

<br>

**Terminologies (4)**

![a](https://imgur.com/F9HboLs.png)

- **Full Tree**
  - leaf가  모두 동일 level에 위치. 
  - Internal node들은 모두 다음 노드를 가리키고 있다. 
  - 삼각형 모양을 가지고 있다. 
- **Complete Tree**
  - 바로 직전 depth까지는 full tree, 그 다음 level의 노드가 모두 채워지지 않았다면(채워지는 과정이라면) complete tree.
  - 모두 왼쪽에서 순서대로 채워야 complete tree. Filed from left.

<br>

# Characteristics of Tree

**Characteristics**

![a](https://imgur.com/r1OIuLy.png)



- Num of edges = Num of nodes - 1

- Depth of root = 0

- Height of root = Height of tree = 3

- Maximum num. of nodes at level *i* with degree *d* = $d^i$

  - degreer가 4고 level이 2라면 node는 최대 16개.

- Maximum num. of leaves with height *h* and degree *d* = $d^h$

- Maximum size of a tree with height *h* and degree *d*

  = $1+d+d^2+...+d^h=\frac{d^{h+1}}{d-1}$

- Height of a **complete** tree with size *s* and degree *d* 

  = 위의 공식을 *h*로 풀어주면 된다.

  $h=[log_d(s(d-1)+1)]-1$

<br>

# Binary Search Tree and Implementation

**Binary Search Tree : A Simple Structure**

- Binary tree
  - Tree with degree 2
- Binary search tree
  - Tree with degree 2
  - Tree designed for a fast search of stored data.
  - So far, what we have studied is the definitions and the characteristics of stored data.
  - Now, this is related to the operations
  - **How to perform a faster search?**

- Binary tree는 degree가 그냥 2인 것.

- 어떻게 해야 빠르게 검색이 가능할까?

<br>

***Detour*: Intuitive Analogy - Finding Restroom in Building**

- 알 수 없는 호텔에 들어갔다 치자. 근데 갑자기 화장실 마려움.
  - 어떻게 화장실을 찾을까? 무작위로? 화장실 사인을 보고? 주변 사람들에게 물어보기? 아니면 그냥 찍어보기? 기존의 관념으로 유추하기?
  - 규칙을 넣어두면 보다 빠르게 검색할 수 있다.

<br>

**A Scenario of Using Binary Search Tree**

- 다음과 은행 계좌 정보가 있다 치자. 1004인 은행 계좌를 찾는다고 할 때,
  - Linked list처럼 차례대로 찾으면 된다. 4개 밖에 없기 때문에.
- Binary Search Tree를 사용한다면?
  - root를 기준으로 왼쪽은 큰 값, 오른쪽은 작은 값 저장한다는 rule을 생성.
  - 규칙을 생성하면 보다 적은 retrieval로 검색이 가능하다.

<br>

**Implementation of Tree Node**

- Has 4 references :
  - Left hand side (LHS)
  - Right hand side (RHS)
  - Its own value
  - Its parent node
  - Not implemented here, but
    - LHS stores
      - Values have lower than its own value.
    - RHS stores
      - Values have higher than its own value.
    - Just as we all know that the department stores do not have a restroom on the first floor.
- Other than four references,
  - Simple get/set methods
    - What are the get/set methods?
      - Coming from encapsulation

~~~python
class TreeNode:
  	# 4 references
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS

    def getRHS(self):
        return self.nodeRHS
    
    def getValue(self):
        return self.value
    
    def getParent(self):
        return self.nodeParent
    
    def setLHS(self):
        self.nodeLHS = LHS
        
    def setRHS(self):
        self.nodeRHS = RHS
        
    def setValue(self):
        self.value = value
        
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent
~~~

<br>

**Implementation of BST**

- root에 대해서만 reference 저장 가능.

~~~Python
class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value, node=None):

    def search(self, value, node=None):

    def delete(self, value, node=None):
        
    def findMax(self, node=None):
        
    def findMin(self, node=None):
        
    def traverseLevelOrder(self):
        
    def traverseIndOrder(self, node=None):
        
    def traversePreOrder(self, node=None):
        
    def traversePostOrder(self, node=None):
~~~

- BST handles the data stored through its root
  - Root has its own value.
  - Tree instance access to the root.
  - Only through the root, the tree instances access to the descendant nodese of the root.

<br>

# Insert and Search Operation of Binary Search Tree

**Insert Operation of Binary Search Tree**

- 이해 안되면  3:50-10:14 보기
- Insert operation
  - Retrieve the current node value.
    - (1) If the value is equal to the value to insert,
      - Return already there!
    - (2) If the value is smaller than the value to insert,
      - If there is a node in RHS, then move to the RHS node(*Recursion*).
      - If there is no node in RHS, create a RHS node with the value to insert.
    - (3) If the value is larger than the value to insert
      - If there is a node in LHS, then move to the LHS node(*Recursion*).
      - If there is no node in LHS, create a LHS node with the value to insert.
- Insert는 BST에 value들을 배치하는 것.
  - Recursion 존재.

~~~Python
# 어느 node에 어떤 value를 insert.
def insert(self, value, node=None):
  
    # Escape 구문
    # node 입력받지 않았다면 root를 받아옴  .
    if node is None:
        node = self.root
    # root가 비어있다면 value를 저장.
    if self.root is None:
        self.root = TreeNode(value, None)
        return
      
    # (1) node에서 나온 value가 우리가 insert하려는 값과 같다면, 중복된 값을 insert하지 않고 바로 return.
    if value == node.getValue():
        return
     
    # (2)
    if value > node.getValue():
      	# RHS가 비어있다면 RHS 생성.
        if node.getRHS() is None:
            node.setRHS(TreeNode(value, node))
        else:
          	# Recursion; RHS 부분 트리에 대해서만 insert.
            self.insert(value, node.getRHS())
            
    # (3)
    if value < node.getValue():
        if node.getLHS() is None:
            node.setLHS(TreeNode(value, node))
        else:
          	# Recursion
            self.insert(value, node.getLHS())
    return
~~~

<br>

**Example**

- 3, 2, 0, 5, 7, 4를 insert한다 하자.	

1. 먼저 3을 root로 설정. 
2. 2는 3보다 작으므로 (3)에 의해 LHS에 저장됨.
   - 하지만 LHS가 없으므로 LHS 생성.
3. 위의 과정 반복.

- (1) - 3
- (2) - 5, 7, 4
- (3) - 2, 0

  <br>

**Search Operation of Binary Search Tree**

- Search operation
  - Retrieve the current node value.
    - If the value is equal to the value to search,
      - Return **TRUE**.
    - If the value is smaller than the value to search,
      - If there is a node in RHS, then move to the RHS node(*Recursion*)
      - If there is no node in RHS, return **FALSE**.
    - If the value is larger than the value to search,
      - If there is a node in the LHS, then move to the LHS node(*Recursion*)
      - If there is no node in LHS, return **FALSE**.

~~~python
def search(self, value, node=None):
    if node is None:
        node = self.root
    if value == node.getValue():
        return True
    if value > node.getValue():
        if node.getRHS() is None:
            return False
        else:
            return self.search(value, node.getRHS())
    if value < node.getValue():
        if node.getLHS() is None:
            return False
        else:
            return self.search(value, node.getLHS())
~~~

<br>

**Example**

- `tree.search('4')` 를 한다치자.
  - '4'가 tree 안에 있는지에 대해 `search()` 함수는 오로지 root reference만 사용.
    - root에 '4'가 있으면 True. 아니라면 recursion 사용.
  - 하지만 root는 3이므로 RHS로 이동. LHS는 아예 search하지 않음.
  - RHS의 node는 5. '4'는 5보다 작으므로 LHS로 이동.
    - '4'가 있다면 **TRUE**. 
- Linked list는 모든 chain을 모두 통과해야만 값을 찾을 수 있는데, BST는 max.depth 만큼만 찾으면 ok.

> BST가 Linked list보다 search 성능이 뛰어남.

<br>

# Delete Operation and Minimum & Maximum of Binary Search Tree

**Delete Operation of Binary Search Tree (1)**

- First, you need to find the node to delete through recursions.
- Three deletion cases :
  - Case 1 : deleting a node with no children
    - Just remove the node by modifying its parent.
  - Case 2 : deleting a node with one child
    - Replace the node with the child.
  - Case 3 : deleting a node with two children 
    - Find either
      - A maximum in the LHS or a minimum in the RHS.
        - RHS에서 LHS로 계속 내려가면 최솟값.
      - Substitute the node to delete with the found value.
      - Delete the found node in the LHS or the RHS.

- delete는 트리 구조에서 쉽지 않다.
  - 구조 자체에 여파가 생김.
- Child가 없으면 그냥 없애버리면 됨.
  - Reference 값만 조정해주면 된다.
- Child가 있는 parent를 remove할 때는 child에게 문제가 생긴다. 
- 특히 children이 두 개 있을 때.
  - 방법은 두 가지 : LHS의 max, RHS의 min.
  - 각각의 방법을 max,min을 찾는다.
    - 각각의 value는 0 or 1 child. 만약 value가 없어지면 위의 child 1 있을 때 방법 쓰면 됨.
  - 해당 value를 copy해서 삭제할 node에 붙여넣기 (값만 그대로).
  - copy한 그 value를 삭제.

<br>

**Delete Operation of Binary Search Tree (2)**

~~~python
def delete(self, value, node=None):
    if node is None:
        node = self.root
    if node.getValue() < value:
        return self.delete(value, node.getRHS())
    if node.getValue() > value:
        return self.delete(value, node.getLHS())
    if node.getValue() == value:
      	# LHS, RHS 모두 존재한다면,
        if node.getLHS() is not None and node.getRHS() is not None:
          	# RHS의 최솟값을 찾아라.  
            nodeMin = self.findMin(node.getRHS())
            # 최솟값을 copy해 node에 붙이기
            node.setValue(nodeMin.getValue())
            self.delete(nodeMin.getValue(), node.getRHS())
            return
        parent = node.getParent()
        # RHS가 없다.
        if node.getLHS() is not None:
            if node == self.root:
                self.root = node.getLHS()
            elif parent.getLHS() == node:
                parent.setLHS(node.getLHS())
                node.getLHS().setParent(parent)
            else:
                parent.setRHS(node.getLHS())
                node.getLHS().setParent(parent)
            return
        if node.getRHS() is not None:
            if node == self.root:
                self.root = node.getRHS()
            elif parent.getLHS() == node:
                parent.setLHS(node.getRHS())
                node.getRHS().setParent(parent)
            else:
                parent.setRHS(node.getRHS())
                node.getRHS().setParent(parent)
            return
        if node == self.root:
            self.root = None
        elif parent.getLHS() == node:
            parent.setLHS(None)
        else:
            parent.setRHS(None)
        return
~~~

<br>

**Minimum and Maximum in Binary Search Tree**

- Finding minimum in a BST :
  - Just keep following the LHS.
    - Because this will always result in the smaller value than the value of the current node.
    - When you can't any LHS, then the value of the current node is the smallest.
- Finding maximum in a BST :
  - Just keep following the RHS.
    - Because this will always result in the larger value than the value of the current node.
    - When you can't find any RHS, then the value of the current node is the largest.

~~~python
def findMax(self, node=None):
    if node is None:
        node = self.root
    if node.getRHS() is None:
        return node
    return self.findMax(node.getRHS())

def findMin(self, node=None):
    if node is None:   # node가 없을땐  
        node = self.root    # 루트가 min.
    if node.getLHS() is None:    # node LHS가 없을 때	
        return node    # 그 value가 min.
    return self.findMin(node.getLHS())    # node LHS가 있으면 Recursion
~~~

<br>

# Tree Traversing

 **Tree Traversing**

- Tree
  - Complicated than a list
  - Multiple ways to show the entire dataset. 레벨별로 출력할 수도, depth-first 접근 방법도 있다.
    - If it were a list
      - Just show the values from the start to the end.
    - Since this is a BST,
      - Must choose what to show at a time.
        - The value in LHS
        - The value in RHS
        - The value that you have
- Hence there are multiple traversing approaches.
- 트리 구조안에 있는 노드들을 <u>어떤 순서로</u> 출력해야 할까?에 대한 답. Traversing.

<br>

**Depth First Traverse**

![a](https://i.imgur.com/YyBgZ7p.png)


- Pre-order traverse
  - Order : Current, LHS, RHS in *Recursion*
- In-order traverse
  - Order : LHS, Current, RHS in *Recursion*
  - 얘는 **sorting가 동일하다**.
- Post-order traverse
  - Order : LHS, RHS, Current in *Recursion*
- root를 언제 출력하냐에 따라 3가지 방법이 존재.

~~~python
def traverseInOrder(self, node=None):
    if node is None:
        node = self.root
    ret = []
    if node.getLHS() is not None:
        ret = ret + self.traverseInOrder(node.getLHS())
    ret.append(node.getValue())
    if node.getRHS() is not None:
        ret = ret + self.traverseInOrder(node.getRHS())
    return ret

def traversePreOrder(self, node=None):
    if node is None:
        node = self.root
    ret = []  # return할 list.
    ret.append(node.getValue())  # current node value를 먼저 append.
    if node.getLHS() is not None:
      	# small scale에 대한 문제에 대해 동일한 preorder recursion하고, 그에 대한 return 값을 ret에 저장. 
        ret = ret + self.traversePreOrder(node.getLHS())
    if node.getRHS() is not None:
        ret = ret + self.traversePreOrder(node.getRHS())
    return ret

def traversePostOrder(self, node=None):
    if node is None:
        node = self.root
    ret = []  
    if node.getLHS() is not None:
        ret = ret + self.traversePostOrder(node.getLHS())
    if node.getRHS() is not None:
        ret = ret + self.traversePostOrder(node.getRHS())
    ret.append(node.getValue())
    return ret
~~~

<br>

**Example**

Pre-order traverse: 3 - 2 - 0 - 1 - 5 - 4 - 7 - 6 - 9 - 8

In-order traverse: 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9

Post-order traverse: 1 - 0 - 2 - 4 - 6 - 8 - 9 - 7 - 5 - 3

<BR>

**Breadth First Traverse**

- <u>Queue-based</u> **level-order** traverse
  
  - 3, 2, 5, 0, 4, 7, 1, 6, 9, 8
  - Enqueue the root. Root를 queue에 넣는다.
    - While until queue is empty :
      - Current = Dequeue one element
      - Print current
      - If Current's LHS exist :
        - Enqueue current LHS
      - If Current's RHS exist :
        - Enqueue curent RHS
  
- Depth는 recursion을 사용하고, 그 속에는 stackframe이 들어 있었다.

- 이번에는 queue를 사용해 traverse. 
  - 먼저 root를 enqueue.
    - Queue가 empty할 때까지 while loop.
    - 첫 번째 element를 dequeue. 그 값은 root.
  
- Level별로 traverse하기 위해.

- 순서 

  (1) root를 먼저 enqueue한다. 

  (2) queue가 empty될 때 까지 while loop을 돌리는데, 

  ​		(2-1) 먼저 첫 번째 element를 dequeue하고 그 값을 출력한다. 

  ​		(2-2) 그리고 그 첫 번째 element의 LHS, RHS를 차례로 enqueue한다. (3) 그리고 다시 while loop 위로 올라가서 empty될 때 까지 반복한다.

~~~Python
def traverseLevelOrder(self):
    ret = []
    # 1. Queue 먼저 생성.
    Q = Queue()
    # 2. Queue에 먼저 root 추가.
    Q.enqueue(self.root)
    # 3. Queue에 없을 때 까지 loop.
    while not Q.isEmpty():
      	# 3-1. 첫 번째 dequeue.
        node = Q.dequeue()
        # 3-2. Queue안에 value 없으면 다시 위로.
        if node is None:
            continue
        # 3-3. value있으면 리스트에 그 value 추가.
        ret.append(node.getValue())
        # 3-4. LHS, RHS 있으면 Queue에 추가.
        if node.getLHS() is not None:
            Q.enqueue(node.getLHS())
        if node.getRHS() is not None:
            Q.enqueue(node.getRHS())
    return ret
~~~

<br>

**Performance of Binary Search Tree**

![a](https://i.imgur.com/eBUt2wD.png)

