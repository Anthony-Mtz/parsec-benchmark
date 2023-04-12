import sys
import math

class ErrorFinder:
    def __init__(self, args):
        self.referenceFile = open(args[1], "r")
        self.testFile = open(args[2], "r")
        return

    def __del__(self):
        self.referenceFile.close()
        self.testFile.close()
        return
    
    def find_error(self):
        referenceFileLines = self.referenceFile.readlines()
        testFileLines = self.testFile.readlines()
        assert len(referenceFileLines)==len(testFileLines),"Input files do not have the same number of lines"
        ferretError = 0
        ferretValueCount = 0
        for i in range(len(testFileLines)):
            testFileLine = testFileLines[i].split()
            referenceFileLine = referenceFileLines[i].split()
            testQueury = testFileLine[0]
            referenceQueury = referenceFileLine[0]
            testResults = set(testFileLine[1:])
            referenceResults = set(referenceFileLine[1:])
            intersection = testResults & referenceResults
            referenceLen = len(referenceResults)
            intersectionLen = len(intersection)
            if(referenceLen != 0):
                percentDifference = (abs(referenceLen - intersectionLen)/referenceLen)*100
                ferretError += percentDifference
                ferretValueCount += 1

        finalError = (ferretError/ferretValueCount)*100
        print("Error is " + str(finalError) + "%")
                

def main():
    errorFinder = ErrorFinder(sys.argv)
    errorFinder.find_error()
    


if __name__ == "__main__":
    main()
    
