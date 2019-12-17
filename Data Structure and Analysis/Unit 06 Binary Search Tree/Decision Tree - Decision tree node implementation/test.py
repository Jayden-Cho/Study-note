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