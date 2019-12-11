from ManufacturingProcess import ManufacturingProcess
from ProductionList import ProductionList
import matplotlib.pyplot as plt
class Factory(ManufacturingProcess):
    def __init__(self, strFilename):
        self.waitingProduct = ProductionList(strFilename)
        self.completedProduct = ProductionList('')

        row = 2
        col = 3

        self.processes = [[[] for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    self.processes[i][j] = ManufacturingProcess('queue')
                elif i == 1:
                    self.processes[i][j] = ManufacturingProcess('stack')

    def run(self):
        cntProduct = self.waitingProduct.getSize()

        while self.completedProduct.getSize() != cntProduct:
            fig = plt.figure()

            for j in range(3,-1, -1):
                for i in range(2):
                    if j == 0:
                        product = self.waitingProduct.removeFirst()
                        if product != 'none':
                            self.processes[i][j].arriveProduct(product)
                        plt.text(100, 50 + i * 100, self.processes[i][j].getListString(), style='italic')

                    # 마지막 complete 노드.
                    elif j == 3:
                        # 마지막 바로 전에 있는 product 뽑아내기.
                        product = self.processes[i][j - 1].leaveProduct()
                        # product가 그 위치에 있으면,
                        if product != 'none':
                            # 아까 뽑아낸 product를 completedProduct에 추가.
                            self.completedProduct.addLast(product)
                        # completeList에 그 동안 추가한 product 출력.
                        # 이제 이게 10이면 while loop 종료.
                        plt.text(100 + j * 50, 100, self.completedProduct.getListString(), style='italic')

                    else:
                        product = self.processes[i][j - 1].leaveProduct()
                        if product != 'none':
                            self.processes[i][j].arriveProduct(product)
                        plt.text(100 + 50 * j, 50 + i * 100, self.processes[i][j].getListString(), style='italic')

            plt.text(50, 100, self.waitingProduct.getListString(), style='italic')
            plt.axis([0, 350, 0, 200])
            plt.show()