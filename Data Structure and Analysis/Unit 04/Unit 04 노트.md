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

**Repeating Problems and Divide and Conquer**

- Calculating a budget of a company?
  - Departments consist of the company.
  - Departments within departments
- Can't avoid the below structures
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

- A programming method to handle the repeating items in a self-similar way
  - Often in a form of
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

