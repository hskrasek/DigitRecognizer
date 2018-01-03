'''
Created on Dec 5, 2012

@author: hunters
'''

if __name__ == '__main__':
    dataFile = open('/Users/hunters/Dropbox/Python/DigitRecognizer/Data/test2.csv', 'r')
    
    pixelListsOriginal = dataFile.readlines()
    dataFile.close()
    header = pixelListsOriginal.pop(0)
    avg = len(pixelListsOriginal) / float(2)
    last = 0.0
    count = 1
    while last < len(pixelListsOriginal):
        chunkList = pixelListsOriginal[int(last):int(last + avg)]
        chunkFile = open("smallTest%d.csv" % count,"w+")
        chunkFile.write(header)
        for line in chunkList:
            chunkFile.write("%s" % line)
        chunkFile.close()
        count += 1
        last += avg
#    ansFile = open('/Users/hunters/Dropbox/Python/DigitRecognizer/Data/ones.csv', 'w+')
#    
#    for i in range(28000):
#        ansFile.write("%d\n" % 1)

    
    
    