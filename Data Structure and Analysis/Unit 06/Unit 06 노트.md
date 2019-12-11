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