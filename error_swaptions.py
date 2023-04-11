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
        swaptionCount = 0
        totalSwaptionError = 0

        for i in range(len(testFileLines)):
            testFileLine = testFileLines[i].split()
            referenceFileLine = referenceFileLines[i].split()
            if(len(testFileLine)<1 or len(referenceFileLine)<1):
                continue
            if(testFileLine[0] == "Swaption" and referenceFileLine[0] == "Swaption"):
                swaptionCount += 1
                assert testFileLine[1]==referenceFileLine[1],"Compared swaptions are not comparable"
                approxPriceError = float((testFileLine[5][:-1]))
                referencePrice = float(referenceFileLine[3])
                if not (math.isclose(0.0, referencePrice, rel_tol=1e-9, abs_tol=0.0)):
                    swaptionError = approxPriceError/referencePrice
                else:
                    swaptionError = 0 
                    swaptionCount -= 1
                totalSwaptionError += swaptionError
        finalSwaptionError = (totalSwaptionError/swaptionCount)*100
        print("Error is " + str(finalSwaptionError) + "%")
                

def main():
    errorFinder = ErrorFinder(sys.argv)
    errorFinder.find_error()
    


if __name__ == "__main__":
    main()
    
