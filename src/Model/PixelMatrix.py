'''
Created on Nov 2, 2012

@author: hunters
'''

class PixelMatrix(object):
    '''
    classdocs
    '''
    
    def __init__(self, list_of_pixels):
        '''
        Constructor
        '''
#        self.matrix = []
#        avg = len(list_of_pixels) / float(28)
#        last = 0.0
#        while last < len(list_of_pixels):
#            self.matrix.append(self.__binarylizer__(list_of_pixels[int(last):int(last + avg)]))
#            last += avg
        self.originalList = list_of_pixels
        self.pixelList = self.__binarylizer__(list_of_pixels)
        tupList = []
        avg = len(list_of_pixels) / float(12.25)
        last = 0.0
        while last < len(self.pixelList):
            temp = self.pixelList[int(last):int(last+avg)]
            value = "0b"
            for i in temp:
                value += str(i)
            tupList.append(value)
            last += avg
        self.tupleMatrix = tuple(tupList)
            
    def getPixelValue(self, row, col):
        assert row <= 27 and row >= 0
        assert col <= 27 and col >= 0
        
#        row = self.matrix[row]
#        pixel = row[col]
        return self.pixelList[28*row + col]
#        return pixel
    
    def getBinaryTuple(self):
        return self.tupleMatrix
    
#    def setPixelValue(self, row, col, pixel):
#        assert row <= 27 and row >= 0
#        assert col <= 27 and col >= 0
#        
#        self.matrix[row][col] = pixel
    
    def __str__(self):
        retStr = ''
        for i in range(28):
            for j in range(28):
                retStr += '%d ' % (self.getPixelValue(i, j))
            retStr += '\n'
        return retStr
    
#    def convertToTuple(self):
#        tupleList = list()
#        for row in self.matrix:
#            for col in row:
#                tupleList.append(col)
#        return tuple(tupleList)
    
    def __binarylizer__(self, pixelList):
        binList = [x for x in pixelList]
        for i, pixel in enumerate(pixelList):
            if pixel <= 125:
                binList[i] = 0
            elif pixel >= 125:
                binList[i] = 1
        return binList