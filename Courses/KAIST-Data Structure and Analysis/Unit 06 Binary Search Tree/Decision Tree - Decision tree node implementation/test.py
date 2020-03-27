import numpy as np
def whatFloor(A, B):
    ary = np.zeros((A+1, B+1)).astype(int)

    ary[0] = np.arange(0, B+1)

    for i in range(1, A+1):
        for j in range(B+1):
            ary[i][j] = sum(ary[i-1][:j+1])
    return ary[A][B]

print(whatFloor(1, 3))