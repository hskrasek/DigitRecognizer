'''
Created on Oct 26, 2012

@author: hunters
'''
from FileIO import FileIO
from Model.PixelMatrix import PixelMatrix
from collections import Counter
import math

train = FileIO.openTrainingFile('/Users/hunters/Dropbox/Python/DigitRecognizer/Data/train.csv')
digits = FileIO.openDataFile('/Users/hunters/Dropbox/Python/DigitRecognizer/TestRunData/smallerTest.csv')
workingDigit = None

for digit in digits:
    workingDigit = digit[0]


def knn(ix,nx,k): return Counter([x[-1] for x in sorted([((sum([(math.sqrt((x1-x2)**2)) for x1,x2 in zip(x,nx)]),y)) for x,y in ix],key=lambda i:i[0])][0:k]).most_common()

trainArray = [t for t in train]
result = knn([(x[0], x[1]) for x in train], [x[0] for x in digits], 10)
print(result)
#print(workingDigit)
#for b in workingDigit.getBinaryTuple():
#    print(int(b, 2))
#workingString = workingDigit.__str__()
#workingList = list(workingString.split(' '))
#workingList = [s.replace('\n', '') for s in workingList]
#print("Best Match(From Training):\t\t\t\t\tTesting Pixel Matrix:")
#avg = len(workingList) / float(28)
#last = 0.0
#
#outputList = []
#while last < len(workingList):
#    output = ""
#    output += " ".join(workingList[int(last):int(last + avg)])
#    output += "\t\t"
#    output += " ".join(workingList[int(last):int(last + avg)])
#    outputList.append(output)
##    if int(last) == 756:
##        index = list(output.split('\n'))[len(list(output.split('\n'))) - 2].split(" ").index('')
##        
#    last += avg
#    
#lastLine = list(outputList[len(outputList) - 1])
#outputList.pop(outputList.index(outputList[len(outputList) - 1]))
#index = lastLine.index('\t')
#lastLine.pop(index-1)
#lastLine = "".join(lastLine)
#outputList.append(lastLine)
#for line in outputList:
#    print(line)
#    
#    
#def count_ones_64bit(b):
#    b = (b & 0x5555555555555555) + ((b >> 1) & 0x5555555555555555)
#    b = (b & 0x3333333333333333) + ((b >> 2) & 0x3333333333333333)
#    b = (b & 0x0F0F0F0F0F0F0F0F) + ((b >> 4) & 0x0F0F0F0F0F0F0F0F)
#    b = (b & 0x00FF00FF00FF00FF) + ((b >> 8) & 0x00FF00FF00FF00FF)
#    b = (b & 0x0000FFFF0000FFFF) + ((b >> 16) & 0x0000FFFF0000FFFF)
#    b = (b & 0x00000000FFFFFFFF) + ((b >> 32) & 0x00000000FFFFFFFF)
#    return b



#print(workingDigit.tupleMatrix)
#
#for b in workingDigit.tupleMatrix:
#    print(count_ones_64bit(int(b, 2)))

def xorTuples(trainingT, testingT):
        return tuple([bin(int(x, 2) ^ int(y, 2)) for x,y in zip(trainingT, testingT)])

#trainingT = (bin(7), bin(7))
#testingT = (bin(2), bin(2))
#print(zip(trainingT, testingT))
#for x, y in zip(trainingT, testingT):
#    print(x, y)
#print(trainingT)
#print(xorTuples(trainingT, testingT))
#print(bin(7))
#print(bin(2))
#xor = 7 ^ 2
#print(bin(xor))
#print(count_ones_64bit(xor))



#print(lastLine)
#print(output)