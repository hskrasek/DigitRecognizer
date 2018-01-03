'''
Created on Nov 8, 2012

@author: hunters
'''
class TrainingData(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.trainingData = dict()
        
    def addDigit(self, key, value):
        self.trainingData[key] = value

    def keys(self):
        return self.trainingData.keys()
    
    def getAnswer(self, key):
        return self.trainingData[key]