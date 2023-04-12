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
        bodytrackError = 0
        bodytrackValueCount = 0
        for i in range(len(testFileLines)):
            testFileLine = testFileLines[i].split()
            referenceFileLine = referenceFileLines[i].split()
            assert len(referenceFileLines)==len(testFileLines),"Input line lengths are not the same"
            for j in range(len(testFileLine)):
                referenceValue = float(referenceFileLine[j])
                testValue = float(testFileLine[j])
                if not (math.isclose(0.0, referenceValue, rel_tol=1e-9, abs_tol=0.0)):
                    percentDifference = (abs(referenceValue - testValue)/referenceValue)*100
                    bodytrackError += percentDifference
                    bodytrackValueCount += 1
                else:
                    continue
        finalError = (bodytrackError/bodytrackValueCount)*100
        print("Error is " + str(finalError) + "%")
                

def main():
    errorFinder = ErrorFinder(sys.argv)
    errorFinder.find_error()
    


if __name__ == "__main__":
    main()
    
