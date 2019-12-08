 **Unit Objectives**

- Learn how to program recursive routines and dynamic programming concepts
  - Recurison
  - Dynamic programming
- Objectives are
  - Understanding the concept of recurisons
    - Repeating problems 
    - Divide and conquer
    - Recursion function call
    - Recursive escape
    - Recursion depth
  - Able to implement recursive programs
  - Understanding the concept of dynamic programming 
    - Reusing previous function call result
    - Memoization for time saving

<Br>

# Recursions

**Repeating Problems, Divide, and Conquer**

- Calculating a budget of a company?
  - Departments consist of the company.
  - Departments within departments.
- Can't avoid the below structures.
  - class Department
    - Dept = [sales, manu, randd]
    - def calculateBudget(self)
      - Sum = 0
      - For itr in range(0, numDepartments)
        - Sum = sum + dept[itr].calculateBudget()

- Repeating Problems?
  - 회사를 경영한다 치자. 회사에 600만원이 예산이 있다.
    - 판매 부서는 100만원, 생산은 300만원, 개발은 200만원 필요.
    - 판매 부서 중 서울, 부산, 대구 모두 100만원을 나눠 가짐.
  - 사장이 부서를 바라보는 관점, 부장이 파트를 바라보는 관점은 동일하다.
    - 600만원을 나누던 100만원을 나누던 제한된 예산 내에서 배분하는 건 모두 같은 틀.
      - 다만 예산의 크기가 다를뿐.
  - Repeating problem이란 큰 하나의 문제를 쪼개서 다시 반복되는 또 다른 문제로 만드는 것. 
    - 다만 문제 자체가 작아지게 만드는 게 목표.
- Divide and Conquer?
  - 부서의 중요성을 각 부서에 정해진 예산의 양으로 짐작할 수 있음.
  - 문제를 잘게 쪼개어서(divide) 문제를 해결해 나가는 것(conquer). 

<br>

**More examples**

- Great Common Divisior
  - GCD(32, 24) = 8
  - Euclid's algorithm
    - GCD(A, B) = GCD(B, A mod B)
      - GCD(32, 24) = GCD(24, 8)
      - GCD(24, 8) = GCD(8, 0)
  - Commonality
    - Repeating function calls
    - Reducing parameters
    - Just like the mathematical induction (수학적 귀납법)

<br>

**Recursion**

- A programming method to handle the repeating items in a self-similar way.
  - Often in a form of:
    - Calling a function within the function
      - def functionA(target) --> 이렇게 간략하게 적어둔 걸 pseudo code라 부름.
        - ....
        - functionA(target')
        - ....
        - if(escapeCondition): 
          - Return A

- Function을 call하는 그 function속에서 function을 call.
  - 속에 있는 function은 무조건 size가 작아야.

~~~python
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    intRet = Fibonacci(n-1) + Fibonacci(n-2)
    return intRet

for itr in range(0, 10):
    print(Fibonacci(itr), end=" ")
    
'''
result:
0 1 1 2 3 5 8 13 21 34 
'''
~~~

<Br>

**Recursions and Stackframe**

- Recursion of functions
  - Increase the items in the stackframe.
    - Stackframe is a <u>stack</u> storing function call history.
      - Push : When a function is invoked(called).
      - Pop : When a function hits return or ends.
  - What to store?
    - Local variables and function call parameters.
      - Local variables: function 속에서만 접근 가능한 variables.

- R.A. : Return Address. Address 속에 어떤 function이 call되었는지 저장됨. 다음 번에 function call한 위치로 돌아가게끔 도와주는 역할. 
- Stack 안에 function call parameter가 object로 들어가 있다. 
- Value를 return하는 순간 pop이 일어난다.   

![a](https://i.imgur.com/rKBXvTj.png)

<br>

# Merge Sort and Problems in Recursions

**Merge Sort**

- Merge sort: One example of recursive programming
  - Decompose into two smaller lists
  - Aggregate to one larger and sorted list
- 키 순서로 서봐. 가장 많이 사간 순서로 서봐. 이런게 sort.
- Merge sort는 일단 쪼갤 수 없을 때 까지 쪼갠 다음 비교를 시작해 나가는 것. 

![a](https://i.imgur.com/sq0QfhK.png)

<br>

**Implementation Example: Merge Sort**



~~~python
import random

def performMergeSort(lstElementSort):
    if len(lstElementSort) == 1:
        return lstElementSort

# Decomposition
    lstSubElementToSort1 = []
    lstSubElementToSort2 = []
    for itr in range(len(lstElementSort)):
        if len(lstElementSort)/2 > itr:
            lstSubElementToSort1.append(lstElementSort[itr])
        else:
            lstSubElementToSort2.append(lstElementSort[itr])

# Recursion
    lstSubElementToSort1 = performMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = performMergeSort(lstSubElementToSort2)

# Aggregation 
    idxCount1 = 0
    idxCount2 = 0
    for itr in range(len(lstElementSort)):
      	# 첫 번째 리스트 값 모두 떨어지면, 다음부턴 두 번째 리스트 값 입력.
        if idxCount1 == len(lstSubElementToSort1):
            lstElementSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        # 두 번째 리스트 값 모두 떨어지면, 다음부턴 첫 번째 리스트 값 입력.
        elif idxCount2 == len(lstSubElementToSort2):
            lstElementSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
        # 첫 번째 리스트 값이 두 번째 리스트 값보다 크면 전체 리스트에 작은 값 입력.
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2]:
            lstElementSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        else:
            lstElementSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
    return lstElementSort

lstRandom = []
for itr in range(0, 10):
    lstRandom.append(random.randrange(0, 100))
print(lstRandom)
lstRandom = performMergeSort(lstRandom)
print(lstRandom)

'''
result:
[47, 59, 68, 12, 13, 2, 94, 59, 17, 47]
[2, 12, 13, 17, 47, 47, 59, 59, 68, 94]
'''
~~~

<br>

**Problems in Recursions of Fibonacci sequence**

- Problems in recursions :
  - Excessive function calls.
    - Calling functions again and again.
    - Even though the function is executed before with the same paramteres.
- For instance, Fibonacci(4),
  - Has 2 repeated calls of F(0).
  - Has 3 repeated calls of F(1).
  - Has 2 repeated calls of F(2).
- These are unnecessarily taking time and space.

- 너무나 function call이 많다.
  - 공간도 많이 필요하고 시간도 많이 걸린다.
  - 이것의 해결법은 dynamic programming.
    - ​	한 번 call하고 기록해 두는 것.

<br>