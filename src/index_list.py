class IndexList:
    def __init__(self, length, base):
        self.index_list = [0] * length
        self.base = base
        self.has_overflowed = False

    def __getitem__(self, index):
        return self.index_list[index]

    def __len__(self):
        return len(self.index_list)

    def increase_by(self, amount):
        if amount <= 0:
            raise ValueError("Must increment by a positive value")

        for i in reversed(range(len(self.index_list))):
            self.index_list[i] += amount % self.base

            if (i == 0) and (amount + self.index_list[i] >= self.base):
                self.has_overflowed = True

            amount //= self.base

            if self.index_list[i] >= self.base:
                self.__carry_over(i)
            elif amount <= 0:
                return

    def __carry_over(self, index):
        self.index_list[index] -= self.base

        if index > 0:
            self.index_list[index - 1] += 1

    def get_index_string(self):
        padding = len(str(self.base))

        index_string = ""

        for index in self.index_list:
            index_string += (str(index).rjust(padding, "0") + " ")

        return index_string
