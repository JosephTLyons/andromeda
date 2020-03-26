class IndexList:
    def __init__(self, length, base):
        self.indexList = [0] * length
        self.base = base
        self.has_over_flown = False

    def increase_by(self, amount):
        if amount <= 0:
            raise ValueError("Must increment by a positive value")

        for i in reversed(range(len(self.indexList))):
            self.indexList[i] += amount % self.base

            if (i == 0) and (amount + self.indexList[i] >= self.base):
                self.has_over_flown = True

            amount = amount // self.base

            if (self.indexList[i] >= self.base):
                self.__carry_over(i)
            elif amount <= 0:
                return

    def __carry_over(self, index):
        self.indexList[index] -= self.base

        if (index > 0):
            self.indexList[index - 1] += 1

    def get_index_string(self):
        padding = 1 if (self.base <= 10) else 2

        index_string = ""

        for index in self.indexList:
            index_string += (str(index).rjust(padding, '0') + " ")

        return index_string

    def at(self, index):
        return self.indexList[index]

    def len(self):
        return len(self.indexList)
