'''
Created on Nov 2, 2012

@author: hunters
'''
#from Model.PixelMatrix import PixelMatrix
#from collections import Counter
import math
import random
class Classifier(object):
    '''
    classdocs
    '''
    
    def __init__(self, training_data):
        self.trainingData = training_data
        self.bestMatch = dict()
        
    def classify(self, pixel_matrix):
        possibleAnswers = ()
        firstTime = True
        for trainingPM in self.trainingData.keys():
            xorTuple = self.xorTuples(trainingPM.getBinaryTuple(), pixel_matrix.getBinaryTuple())
            distance = self.bineuclid_distance(xorTuple)
            if firstTime:
                possibleAnswers = (trainingPM, distance)
                firstTime = False
            if distance < self.bestMatch.get(self.trainingData.getAnswer(trainingPM), (None, 784))[1]:
                self.bestMatch[self.trainingData.getAnswer(trainingPM)] = (trainingPM, distance)
#            if distance < 15:
#                possibleAnswers = (trainingPM, distance)
#                break
#            if distance < possibleAnswers[1]:
#                possibleAnswers = (trainingPM, distance)
#        self.niceOutput(possibleAnswers[0], pixel_matrix, possibleAnswers[1], self.trainingData.getAnswer(possibleAnswers[0]))
#        return self.trainingData.getAnswer(possibleAnswers[0])
#        return self.bestMatch
    
    def euclid_distance(self, trainingTuple, testingTuple):
        returnValue = 0
        for x, y in zip(trainingTuple, testingTuple):
            returnValue += abs(x - y)
        return returnValue
    
    def searchBestMatch(self, testingMatrix):
        testingDensity = self.bineuclid_distance(testingMatrix.getBinaryTuple())
#        if self.findSmallestDistance(self.bestMatch)[1] < 25:
        for key, value in self.bestMatch.items():
            bestMatchDensity = self.bineuclid_distance(value[0].getBinaryTuple())
#            print("Testing Density: %d\tBest Match Density: %d" % (testingDensity, bestMatchDensity))
            if bestMatchDensity == testingMatrix:
                return (key, value[0])
            if bestMatchDensity - 30 <= testingDensity <= bestMatchDensity + 30:
                return (key, value[0])
        return random.randint(0,9)
#        print(testingMatrix)
#        print(possibleAnsw[0])
    
    def findSmallestDistance(self, bestMatches):
        return min([x[1] for x in bestMatches.values()])
    
    def xorTuples(self, trainingT, testingT):
        return tuple([bin(int(x, 2) ^ int(y, 2)) for x,y in zip(trainingT, testingT)])
    
    def bineuclid_distance(self, xorTuple):
        countList = []
        for x in xorTuple:
            countList.append(self.count_ones_64bit(int(x, 2)))
        return sum(countList)
    
    def count_ones_64bit(self, b):
        b = (b & 0x5555555555555555) + ((b >> 1) & 0x5555555555555555)
        b = (b & 0x3333333333333333) + ((b >> 2) & 0x3333333333333333)
        b = (b & 0x0F0F0F0F0F0F0F0F) + ((b >> 4) & 0x0F0F0F0F0F0F0F0F)
        b = (b & 0x00FF00FF00FF00FF) + ((b >> 8) & 0x00FF00FF00FF00FF)
        b = (b & 0x0000FFFF0000FFFF) + ((b >> 16) & 0x0000FFFF0000FFFF)
        b = (b & 0x00000000FFFFFFFF) + ((b >> 32) & 0x00000000FFFFFFFF)
        return b
    
    def getBestMatches(self):
        return self.bestMatch