'''
Created on Nov 6, 2012

@author: hunters
'''
from Model.PixelMatrix import PixelMatrix
    
def listStringToInt(strlist):
    return [int(i) for i in strlist]

def openDataFile(filePath):
    dataFile = open(filePath, 'r')
    
    pixelListsOriginal = dataFile.readlines()[1:]
    pixelListsOriginal = [[int(i) for i in pixelList.split(',')] for pixelList in pixelListsOriginal]

    dataFile.close()
    return generatePMITuple(pixelListsOriginal, training=False)
        
def openTrainingFile(filePath):
    dataFile = open(filePath, 'r')
    
    pixelListsOriginal = dataFile.readlines()[1:]
    pixelListsOriginal = [[int(i) for i in pixelList.split(',')] for pixelList in pixelListsOriginal]
        
    dataFile.close()
    return generatePMITuple(pixelListsOriginal, training=True)
        
def generatePMITuple(lines, training=False):
    for line in lines:
        if training:
            ans = line[0]
            line.remove(ans)
        else:
            ans = None
        pm = PixelMatrix(line)
        yield (pm, ans)
        
def writeAnwsersToFile(anwsersFilePath, testData, order):
    answersFile = open(anwsersFilePath, "w+")
    
    for matrix in order:
        answersFile.write("%d\n" % (testData.getValue(matrix)))
        
    answersFile.close()