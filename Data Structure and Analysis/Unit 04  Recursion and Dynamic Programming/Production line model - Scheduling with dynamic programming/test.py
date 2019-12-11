import numpy as np
f = open('Plan-2012.12.24.csv')
line = f.readlines()
f.close()

dataset = []
for row in line:
    dataset.append(row[:-1].split(','))

Dataset = np.asarray(dataset)
print(Dataset[1:])


