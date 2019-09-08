class IndexList:
    def __init__(self, length, base):
        self.indexList = [0] * length
        self.length = length
        self.base = base

    def increaseIndexListBy(self, amount):
        increaseValueAtIndexBy = 0

        for i in reversed(range(len(self.indexList))):
            increaseValueAtIndexBy = amount % self.base
            self.indexList[i] += increaseValueAtIndexBy

            if (self.indexList[i] >= self.base):
                self.indexList[i] -= self.base

                if (i > 0):
                    self.indexList[i - 1] += 1

            amount = int(amount / self.base)

    def printIndexList(self):
        padding = len(str(self.base)) + 1

        for index in self.indexList:
            print(str(index).rjust(padding), end = '')

        print();

    def get(self):
        return self.indexList
