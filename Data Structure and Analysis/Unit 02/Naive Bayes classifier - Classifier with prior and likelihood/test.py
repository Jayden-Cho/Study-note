import numpy as np
import matplotlib.pyplot as plt


class SentiAnalyzer:

    def __init__(self, sentidata, word):
        self.sentidata = sentidata
        self.numTraining = 150
        self.wordLimit = 1500
        self.dataWord = word

    def runAnalysis(self, idxReview):
        probLogPositive = 0
        probLogNegative = 0
        idxUsedWords, usedWords = self.findUsedWords(idxReview)

        for i in range(len(idxUsedWords)):
            idxWord = idxUsedWords[i]
            positive, negative = self.calculateProbWord(idxWord)

            probLogPositive += np.log(positive)
            probLogNegative += np.log(negative)

        positiveProb1, negativeProb1 = self.calculateProbReview()
        probLogPositive += np.log(positiveProb1)
        probLogNegative += np.log(negativeProb1)

        if self.dataReviewTesting[idxReview] == 1:
            if probLogPositive > probLogNegative:
                correct = 1
            else:
                correct = 0
        else:
            if probLogPositive > probLogNegative:
                correct = 0
            else:
                correct = 1

        return probLogPositive, probLogNegative, correct

    def runWholeAnalysis(self):
        cnt = 0
        numCorrect = np.zeros((int(self.numTraining/30)+1, 1))

        for j in range(0, self.numTraining+1, 30):
            self.dataSentimentTraining = self.sentidata[self.shuffle[0:j+1], 0:self.wordLimit]
            self.dataReviewTraining = self.sentidata[self.shuffle[0:j+1], -1]

            nunCorrect[cnt] = 0
            for i in range(np.shape(self.dataSentimentTesting)[0]):
                p, n, c = self.runAnalysis(i)
                if correct == 1 :
                    numCorrect[cnt] += 1

            numCorrect[cnt] = numCorrect[cnt] / np.shape(self.dataSentimentTesting)[0]
            cnt += 1

        return numCorrect

    def runExperiments(self, numReplicate):
        average = np.zeros((int(self.numTraining/30)+1, 1))
        averageSq = np.zeros((int(self.numTraining/30)+1, 1))

        for i in range(numReplicate):
            self.shuffle = np.arange(len(sentidata))
            np.random.shuffle(self.shuffle)

            self.dataSentimentTesting = self.sentidata[self.shuffle[self.numTraining+1:198], 0:self.wordLimit]
            self.dataReviewTesting = self.sentidata[self.shuffle[self.numTraining+1:198], -1]

            correct = self.runWholeAnalysis()

            average += correct
            averageSq += correct * correct

        average = average / numReplicate
        averageSq = averageSq / numReplicate
        std = np.sqrt(averageSq - average * average)

        plt.errorbar(np.arange(0, self.numTraining+1, 30), average, std)
        plt.show()

    def calculateProbWord(self, idx):
        occurrence = [row[idx] for row in self.dataSentimentTraining]
        positive = np.

    def calculateProbReview():

    def findUsedWords():