__author__ = 'Ray'

class LargeSumBase:
    rawData = None
    filename = "data.in"
    def __init__(self):
        return

    def loadData(self, filename = filename):
        try:
            with open(filename, 'r') as file:
                content = file.readlines()
            splitContent = [[int(d) for d in x if d.isdigit()] for x in content]
            self.rawData = splitContent
        except IOError as e:
            print(e.message)

class LargeSum(LargeSumBase):
    def sumUp(self):
        if self.rawData == None:
            self.loadData()
        try:
            carrier = 0
            sum = []
            for i in range(len(self.rawData[0])-1, -1, -1):
                localSum = 0
                for largeNum in self.rawData:
                    localSum += largeNum[i]
                localSum += carrier
                carrier = int(localSum / 10)
                localDigit = localSum % 10
                sum.insert(0, localDigit)
            if carrier != 0:
                sum.insert(0, carrier)
            return "".join([str(i) for i in sum])
        except Exception as e:
            print(e.message)
