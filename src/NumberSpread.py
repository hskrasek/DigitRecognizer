'''
Created on Dec 7, 2012

@author: hunters
'''
ansFile = open("/Users/hunters/Dropbox/Python/DigitRecognizer/Data/ans.csv")

numbersTest = [int(x) for x in ansFile.readlines()]

numberDictionary = dict()

for number in numbersTest:
    numberDictionary[number] = numberDictionary.get(number, 0) + 1

total = len(numbersTest)
print("Percentages for %d digits:" % total)
for key, value in numberDictionary.items():
    percent = (value / total) * 100
    print("#%d showed up %d times: %f" % (key,value, percent) + "%")