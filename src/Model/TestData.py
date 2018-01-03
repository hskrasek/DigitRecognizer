'''
Created on Nov 8, 2012

@author: hunters
'''
from Model.PixelMatrix import PixelMatrix

class TestData(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.digits = dict()
        
    def addDigit(self, key, value):
        assert isinstance(key, PixelMatrix)
        self.digits[key] = value
        
    def __iter__(self):
        return self.digits.__iter__()
    
    def keys(self):
        return self.digits.keys()
    
    def values(self):
        return self.digits.values()
    
    def getValue(self, key):
        return self.digits[key]