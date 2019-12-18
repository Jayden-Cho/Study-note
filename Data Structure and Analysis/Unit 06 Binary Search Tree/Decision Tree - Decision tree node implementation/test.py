def calculateIntegerRangeSum(intFrom, intTo):
    intSum = 0

    for itr in range(intFrom, intTo):
        intSum = intSum + itr

    return intSum

print(calculateIntegerRangeSum(0, 10))