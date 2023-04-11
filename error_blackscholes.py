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
        referenceLength = int(referenceFileLines[0])
        testLength = int(testFileLines[0])
        assert referenceLength==testLength,"Input files do not have the same number of lines"
        blackscholesErrorCount = 0
        for i in range(1,testLength+1):
            referenceValue = float(referenceFileLines[i])
            testValue = float(testFileLines[i])
            if not (math.isclose(0.0, referenceValue, rel_tol=1e-9, abs_tol=0.0)):
                percentDifference = (abs(referenceValue - testValue)/referenceValue)*100
            if percentDifference > 1.0:
                blackscholesErrorCount += 1
        finalBlackscholesError = (blackscholesErrorCount/testLength)*100
        print("Error is " + str(finalBlackscholesError) + "%")
                

def main():
    errorFinder = ErrorFinder(sys.argv)
    errorFinder.find_error()
    


if __name__ == "__main__":
    main()
    
