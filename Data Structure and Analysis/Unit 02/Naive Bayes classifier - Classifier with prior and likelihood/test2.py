class AssemblyLines:
    timeStation = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
    timeBelt = [[2, 2, 3, 1, 3, 4, 3], [4, 2, 1, 2, 2, 1, 2]]

    timeScheduling = [list(range(6)), list(range(6))]
    stationTracing = [list(range(6)), list(range(6))]

    def startSchedulingDP(self):
        numStation = len(self.timeStation[0])
        self.timeScheduling[0][0] = self.timeStation[0][0] + self.timeBelt[0][0]
        self.timeScheduling[1][0] = self.timeStation[1][0] + self.timeBelt[1][0]

        for itr in range(1, numStation): # 1, 2, 3, 4, 5
            if self.timeScheduling[0][itr-1] > self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]:
                self.timeScheduling[0][itr] = self.timeStation[0][itr] + self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]
                self.stationTracing[0][itr] = 1

            else:
                self.timeScheduling[0][itr] = self.timeStation[0][itr] + self.timeScheduling[0][itr-1]
                self.stationTracing[0][itr] = 0

            if self.timeScheduling[1][itr-1] > self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]:
                self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]
                self.stationTracing[1][itr] = 0
            else:
                self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[1][itr-1]
                self.stationTracing[1][itr] = 1

        costLine1 = self.timeScheduling[0][numStation-1] + self.timeBelt[0][numStation]
        costLine2 = self.timeScheduling[1][numStation-1] + self.timeBelt[1][numStation]
        if costLine1 > costLine2:
            return costLine2, 1
        else:
            return costLine1, 0

    def printTracing(self, lineTracing):
        numStation = len(self.timeStation[0])
        print("Line :", lineTracing, ", Station :", numStation)
        for itr in range(numStation-1, 0, -1):
            lineTracing = self.stationTracing[lineTracing][itr]
            print("Line :", lineTracing, ", Station :", itr)

lines = AssemblyLines()
time, lineTracing = lines.startSchedulingDP()
print("Fastest production time :", time)
lines.printTracing(lineTracing)