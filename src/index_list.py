class IndexList:
    def __init__(self, length, base):
        self.indexList = [0] * length
        self.length = length
        self.base = base

    def increaseBy(self, amount):
        for i in reversed(range(len(self.indexList))):
            self.indexList[i] += amount % self.base
            amount = amount // self.base

            if (self.indexList[i] >= self.base):
                self.__carryOver(i)

    def __carryOver(self, index):
        self.indexList[index] -= self.base

        if (index > 0):
            self.indexList[index - 1] += 1

    def print(self):
        padding = len(str(self.base)) + 1

        for index in self.indexList:
            print(str(index).rjust(padding), end = '')

        print();

    def at(self, index):
        return self.indexList[index]
