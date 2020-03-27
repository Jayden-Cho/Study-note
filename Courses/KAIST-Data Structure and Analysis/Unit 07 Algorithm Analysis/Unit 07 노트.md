**Unit 07 Objectives**

- Learn how to analyze the efficiency of our program
  - <u>Algorithm analysis</u>
- Objectives are :
- Memorizing the definition and the rules of the **big-Oh notation**
- Understanding <u>what determines</u> the **efficiency** of programs
- Understanding simple algorithms
  - Memorizing the insert and the delete of lists, stacks, and queues
  - Memorizing the bubble sort
- Able to apply the big-Oh notation analysis to programs

<br>

# Factors of Program's Efficiency

**Factors of program's efficiency**

- Algorithm

  - A clearly specified set of simple instructions to be followed to solve a problem.
    - Takes a set of values as inputs,
    - Produces a set of values as outpus.
  - Specified in :
    - English
    - A computer program
    - Pseudo-code

- Data structures

  - Methods of organizing data.

- Program

  = algorithms + data structures

-  자료구조에 새로운 object를 추가한다고 생각해보자. 
  - Array에서는 $N$ iteration이 필요.
  - Binary Search Tree에서는 $logN$ iteration이 필요 (잘 balanced 되었을 때).

<br>

# Bubble Sort Algorithm

- Examples of algorithms
  - Insertion, deletion, search of linked lists, stacks, queues...
  - Sorting of linked lists ...
    - Various sorting methods
      - Bubble sort, Quick sort, Merge sort ...
- Bubble Sort's pseudo code
  - For `itr1=0` to length(list)
    - For `itr2=itr+1` to length(list)
      - If` list[itr1] < list[itr2]`
        - Swap `list[itr1], list[itr2]`
  - `Return list`
- This program uses
  - Data structure: List
  - Algorithm: Bubble sort

- 최종적으로 descending order로 sort하는 것.
  - 값들을 비교하고 특정 값이 다른 값보다 크다면 swap.

<br>

**Example of Bubble Sort Execution**

- Let's observe the execution of the bubble sort

~~~python
import random

def performSelectionSort(lst):
    for itr1 in range(0, len(lst)):
        for itr2 in range(itr1+1, len(lst)):
            if lst[itr1] < lst[itr2]:
                lst[itr1], lst[itr2] =\
                lst[itr2], lst[itr1]
    return lst

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)
print(performSelectionSort(lstNumbers))

lstNumbers2 = [2, 5, 0, 3, 3, 3, 1, 5, 4, 2]

print(lstNumbers2)
print(performSelectionSort(lstNumbers2))

'''
result:
[1, 3, 6, 2, 5, 8, 0, 9, 7, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[2, 5, 0, 3, 3, 3, 1, 5, 4, 2]
[5, 5, 4, 3, 3, 3, 2, 2, 1, 0]
'''
~~~

- `itr1`이 커질수록 `itr1`에 해당하는 iteration은 줄어듦.

  - `itr1=1`일 때, 9 iterations.
  - `itr1=8`일 때, 1 iteration.

- Total iterations

  = 9+8+...+1

  = 45 iterations

  = $\frac{n(n-1)}{2} = \frac{1}{2}n^2- \frac{1}{2}n$

- 프로그램이 주어지면, iteration이 얼마나 돌아가는지 수학적으로 계산할 수 있다.

<br>

# Importance of Efficiency

- Writing a working program is not good enough.
  - The program could be inefficient.
  - If the program runs on a large data, the running time becomes a big issue.
    - Sometimes, a program may not be usable because of the efficiency.
    - Imagine a transaction system of a financial company.
      - 1 transaction = 0.001 sec
      - 10 transactions by 10,000 account holders = 100 sec
      - Side effect :
        - If there is no reaction from the system, the users click the request again.
        - Increased requests when there is a delay.
    - Imagine a bubble sorting function for bank accounts.
      - 10,000 accounts need roughly 50,000,000 iterations for sorting.
- Therefore, we need a guarantee of the worst-case scenario.
  - The worst-case running time of a single transaction.
  - The worst-case transaction request numbers of a single day.
- 프로그램이 '동작하는 것' 만으로는 충분하지 않다.
  - 돌아가는데 3년걸린다면 큰일난다. 프로그램이 비효율적이면 안된다.
  - runtime이 중요한 이슈. inefficiency 때문에 프로그램이 사장되는 경우도 많다.
- 항상 프로그래머는 최악을 생각해야 한다.

<br>

# Definition of Algorithm Analysis and Examples

 **Definition of Algorithm Analysis**

- Analyzing an algorithm
  - Estimating the resources that the algorithm requires
    - Memory
    - Communication bandwidth
    - **Computational time** (the most important resource in the most of cases)
- Factors affecting the running time
  - Computer used for executions
  - Algorithms
  - Data structures
  - Input data size
- After analyzing the algorithms
  - We estimate the worst-case of the costs by the factors
    - i.e. Computational time by input data size
    - i.e. Iterations by input data size

- 알고리즘을 분석한다는 것 = 알고리즘에 필요한 resource를 추측.
  - 계산 시간이 가장 중요한 resource.

- running time에 영향을 주는 것?
  - 컴퓨터 성능, 알고리즘, 자료구조, 데이터셋의 크기 등.
- runtime의 factor를 가지고 runtime을 esetimate하는게 algorithm analysis.

<br>

**Simple Algorithm Analysis**

~~~Python
def calculateIntegerRangeSum(intFrom, intTo):
    intSum = 0
    for itr in range(intFrom, intTo):
        intSum = intSum + itr
    return intSum

print(calculateIntegerRangeSum(0, 10))
~~~

- Line 1 to 4

  - Line 1 : 1 iteration

  - Line 2, 3:

    (intTo-intFrom) iterations X 2 lines = N iterations X 2 lines

    = 2N iterations

  - Total # of iterations = 2N+2 iterations = **$O(N)$**

<br>

**Bubble Sort Algorithm Analysis**

~~~python
def performBubbleSort(lst):
    for itr1 in range(0, N):
        for itr2 in range(itr1+1, N):
            if lst[itr1] < lst[itr2]:
                lst[itr1], lst[itr2] =\
                lst[itr2], lst[itr1]
    return lst
print(performBubbleSort(lst))
~~~

- Line 1 to 5
  - Line 1 : N iterations
  - Line 2, 3, 4 : N-i iterations (i is from 0 to N-1) X 3 times
    - 1 to N, 2 to N, ... , N-1, to N
    - $\frac{n(n-1)}{2} = \frac{1}{2}n^2- \frac{1}{2}n$ X 3 times
    - Assuming that "if" always results in true.
  - Line 5 : 1 iteration
- Total # of iterations = $\frac{3}{2}n^2- \frac{3}{2}n+n+1$ iterations = **$O(N^2)$**
- 우리는 최악의 상황을 분석.
  - If문이 모두 실행되는 상황 설정.

<br>

# Big-Oh Notation

**Asymptotic notation: Big-Oh**

- What do $O(N)$ and $O(N^2)$ mean?
- That's the Big-Oh notation
  - Notation to show the **worst-case** running time
    - Do you remember?
      - Asumming that "if" always results in true.
      - So, this is the worsrt scenario for the run-time.
        - Because the program should run the statements in the "if" block
- Definition of the Big-Oh notations
  - $f(N)=O(g(N))$
  - There are positive constants $c$ and $n_0$ such that.
    - $f(N) \leqq c\ g(N)$ when $N \geqq n_0$
    - The growth rate of $f(N)$ is less than or equal to the growth rate of $g(N)$
    - $g(N)$ is an upper bound on $f(N)$ 

- 현업에서 가장 중요한 것이 worst case이기 때문에 big oh notation을 주로 사용.
- Example :
  - 이전 예에서 $f(n) = O(N^2)$ 이고, $f(N)=\frac{3}{2}n^2- \frac{3}{2}n$ 이고, $g(N) = n^2$이라할 때,
  - $f(N) \leq O(g(N)\\=\frac{3}{2}n^2- \frac{3}{2}n \leq c\times n^2$
  - $c, n_0$ 가 뭔지는 모르지만 이게 양의 constant이면 된다.
    - 모두 그럴 필요는 없고 최소한 한 경우만 있으면 된다.

<Br>

# Growth Rate

**Growth rate**

![a](https://i.imgur.com/y7zWP5A.png)

- Definition of the Big-Oh notations
  - $f(N)=O(g(N))$
  - There are positive constants $c$ and $n_0$ such that.
    - $f(N) \leqq c\ g(N)$ when $N \geqq n_0$
    - The growth rate of $f(N)$ is less than or equal to the growth rate of $g(N)$
    - $g(N)$ is an upper bound on $f(N)$. 

- 다양한 형태의 function에 대해 growth rate을 정할수 있고, 그 rate에 따라 big-oh 속에 있는 $g(N)$을 $f(N)$에 맞게 표현을 할 수 있다.

<br>

# Examples & Rules of Big-Oh Notation

**Examples of Big-Oh Notation**

- Assume $f(N)=7N^2$. Then 
  - $f(N)=O(N^4)$
  - $f(N) = O(N^3)$
  - $f(N)=O(N^2)$ -- best answer. asymptotically tight.
  - 셋 다 모두 가능함. 하지만 세번째 정답이 가장 맞는 정답.
- $N^2 / 2-3N$ -- ans: $O(N^2) $ 
- $1+4N$ -- ans : $O(N)$
- $7N^2+10N+3$ -- ans : $O(N^2) $
- $log_{10}N=log_2N/log_210$ -- ans : $O(log_2N)=O(logN)$

- $sinN$ -- ans : $O(1)$ N이 어떻든 커봤자 폭이 1보다 커지지 않음.
- $10$ -- ans : $O(1)$
- $10^{10}$ -- ans : $O(1)$
- $logN+N$ -- ans : $O(N)$

- 어차피 큰 수 오면 차수 가장 큰값이 압도적으로 커지니까 상관없음.

<br>

**Rules of BIg-Oh Notation**

- When considering the growth rate of a function using Big-Oh
  - Ignore the lower order terms and the coefficients of the highest-order term.
    - When we have $N^3$, then $N^2$ and $N$ means nothing in terms of Big-Oh
    - From the growth rate order
      - $c^N>N^k>N^2>NlogN>N>logN>C$
      - $C\geq2\ and\ k>2$
  - No need to specify the base of logarithm
    - $O(logN)=O(log_cN)$
- If $T_1(N)=O(f(N))$ and $T_2(N)=O(g(N))$. 알고리즘 1을 실행하고 바로 알고리즘 2를 실행할 때, 
  - $T_1(N)+T_2(N)=max(O(f(N)),O(g(N)))$
    - 예를 들어, $max(O(N), O(N^2))=O(N^2)$
  - $T_1(N)\times T_2(N)=O(f(N)\times g(N))$. 알고리즘 1안에서 알고리즘 2가 돌아간다.
    - $O(N)\times O(logN)=O(NlogN)$

<br>

**Big-Oh notation of list, stack, and queue**

![a](https://i.imgur.com/oj0K0ll.png)

<br>

***Detour*: Performance of Binary Search Tree**

 ![a](https://i.imgur.com/S5zpv9x.png)