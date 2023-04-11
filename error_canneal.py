import sys

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
        referenceCost = self.find_routing_cost(self.referenceFile)
        testCost = self.find_routing_cost(self.testFile)
        error = (abs(referenceCost - testCost)/referenceCost)*100
        print("Error is " + str(error) + "%")

    def find_routing_cost(self, file):
        fileLines = file.readlines()
        for i in range(len(fileLines)):
            if(fileLines[i].split()[0] == "Final"):
                return float(fileLines[i].split()[3])
        Exception("Could not find routing cost")
    

def main():
    errorFinder = ErrorFinder(sys.argv)
    errorFinder.find_error()
    


if __name__ == "__main__":
    main()
    
