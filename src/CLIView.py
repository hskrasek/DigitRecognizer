'''
Created on Nov 12, 2012

@author: hunters
'''
from Controller import Controller

if __name__ == '__main__':
    print('Digit Recognizer 1.0')
    print('Please enter the path to the Testing Data File:')
    testDataPath = input()
    trainingDataPath = '/Users/hunters/Dropbox/Python/DigitRecognizer/Data/train.csv'
    controller = Controller(testDataPath, trainingDataPath)
    controller.openTestingData()
    controller.openTrainingData()
    controller.classifyDigits()
    print('Digits Classified!')
    anwsersFilePath = input('Where would you like to save the answers?')
    controller.saveAnwsersToFile(anwsersFilePath)
    controller.getBestMatches()