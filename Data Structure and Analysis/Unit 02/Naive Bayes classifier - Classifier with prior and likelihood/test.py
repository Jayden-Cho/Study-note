def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    intRet = Fibonacci(n-1) + Fibonacci(n-2)
    return intRet

for itr in range(0, 10):
    print(Fibonacci(itr), end=" ")