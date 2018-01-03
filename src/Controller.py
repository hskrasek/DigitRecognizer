'''
Created on Nov 9, 2012

@author: hunters
'''
from FileIO import FileIO
from Model.Classifier import Classifier
from Model.TestData import TestData
from Model.TraingingData import TrainingData

class Controller(object):

    def __init__(self, testDataPath, trainingDataPath):
        self.testDataPath = testDataPath
        self.trainingDataPath = trainingDataPath
        self.testingData = TestData()
        self.trainingData = TrainingData()
        self.classifier = Classifier(self.trainingData)
        self.testOrder = []
        
    def openTrainingData(self):
        print('Opening Training Data...')
        digits = FileIO.openTrainingFile(self.trainingDataPath)
        for digit in digits:
            self.trainingData.addDigit(digit[0], digit[1])
            
    def openTestingData(self):
        print('Opening Testing Data...')
        digits = FileIO.openDataFile(self.testDataPath)
        for digit in digits:
            self.testOrder.append(digit[0])
            self.testingData.addDigit(digit[0], digit[1])
            
    def classifyDigits(self):
        count = 1
        for digitPixelMatrix in self.testingData.keys():
            print("Now classifying PixelMatrix %d" % count)
            self.classifier.classify(digitPixelMatrix)
#            ans = self.trainingData.getAnswer(classification[0])
#            self.niceOutput(classification[0], digitPixelMatrix, classification[1], ans)
#            self.testingData.addDigit(digitPixelMatrix, ans)
            count += 1
#        bestMatches = self.classifier.getBestMatches()
        for digit in self.testingData.keys():
            ans = self.classifier.searchBestMatch(digit)
            self.testingData.addDigit(digit, ans[0])
            self.niceOutput(ans[1], digit, 1, ans[0])
#        self.writeTestDataToFile()
        
    def getBestMatches(self):
        print('These PixelMatrixes matched the best from the training data:')
        for key, value in self.classifier.getBestMatches().items():
            print("%d:\n%sDistance: %d" % (key, value[0], value [1]))
            
    def writeTestDataToFile(self):
        testDataFile = open("%s.dump" % self.testDataPath, 'w+')
        
        for key in self.testOrder:
            testDataFile.write("%s, %s, %d\n" % (key, key.originalList, self.testingData.getValue(key)))
    
    def saveAnwsersToFile(self, anwserFilePath):
        print('Saving Answers to: %s' % anwserFilePath)
        FileIO.writeAnwsersToFile(anwserFilePath, self.testingData, self.testOrder)
        print('Answers Saved!')
        
    def niceOutput(self, trainingPM, testingPM, distance, predictedDigit):
        print("Best Match(From Training):\t\t\t\t\tTesting Pixel Matrix:")
        
        trainingString = trainingPM.__str__()
        testingString = testingPM.__str__()
        
        trainingList = list(trainingString.split(' '))
        trainingList = [s.replace('\n', '') for s in trainingList]
        
        testingList = list(testingString.split(' '))
        testingList = [s.replace('\n', '') for s in testingList]

        avg = len(trainingList) / float(28)
        last = 0.0
        outputList = []
        while last < len(trainingList):
            output = ""
            output += " ".join(trainingList[int(last):int(last + avg)])
            output += "\t\t"
            output += " ".join(testingList[int(last):int(last + avg)])
            outputList.append(output)
            last += avg
    
        lastLine = list(outputList[len(outputList) - 1])
        outputList.pop(outputList.index(outputList[len(outputList) - 1]))
        index = lastLine.index('\t')
        lastLine.pop(index-1)
        lastLine = "".join(lastLine)
        outputList.append(lastLine)
        for line in outputList:
            print(line)
        print("With a score of: %d" % distance)
        print("Predicted Digit: %d\n" % predictedDigit)