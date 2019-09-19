from pathlib import Path
from random import shuffle

from index_list import IndexList
from serial_characteristics import SerialCharacteristics


class LicenseGenerator:
    def __init__(self, requestedAmount, serialCharacteristics):
        self.requestedAmount = requestedAmount
        self.serialCharacteristics = serialCharacteristics

        self.listOfCharacterLists = self.__createListOfCharacterLists()
        self.indexList = IndexList(self.serialCharacteristics.len,
                                   self.serialCharacteristics.numberOfCharacters)

        self.fileName = str(self.requestedAmount) + "_unique_serials.txt"

    def generate(self):
        if (self.serialCharacteristics.totalPossibleSerialNumbers < self.requestedAmount):
            self.__printErrorMessage()
            return

        self.__printSerialNumbersToFile()
        print()
        self.__printPathToTerminal()
        print()
        self.__printStatsToTerminal()

    def __createListOfCharacterLists(self):
        listOfCharacterLists = []

        for i in range(self.serialCharacteristics.len):
            shuffle(self.serialCharacteristics.characterList)
            listOfCharacterLists.append(
                self.serialCharacteristics.characterList.copy())

        return listOfCharacterLists

    def __printErrorMessage(self):
        print("Requested serial number amount: {}".format(self.requestedAmount))
        print("Total possible serial numbers given current inputs: ", end='')
        print(self.serialCharacteristics.totalPossibleSerialNumbers)
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    def __printSerialNumbersToFile(self):
        serialFile = open(self.fileName, "w")

        singleSerialNumberString = ""
        distanceBetweenSerialNumbers = self.serialCharacteristics.totalPossibleSerialNumbers // self.requestedAmount

        for _ in range(self.requestedAmount):
            for i in range(self.serialCharacteristics.len):
                singleSerialNumberString += self.listOfCharacterLists[i][self.indexList.at(
                    i)]

            # This should never occur, however, it is better safe than sorry
            if self.indexList.hasResetToZero:
                raise ValueError("Index List has reset to zero.")

            serialFile.write(singleSerialNumberString + "\n")
            singleSerialNumberString = ""

            # self.indexList.print()
            self.indexList.increaseBy(distanceBetweenSerialNumbers)

        serialFile.close()

    def __printPathToTerminal(self):
        filePath = Path.cwd().joinpath(self.fileName)
        print("File path: {}".format(filePath))

    def __printStatsToTerminal(self):
        self.__printRequestedAmount()
        self.__printTotalPossibleSerialNumbers()
        self.__printPercentOfLicensePoolCovered()

    def __printRequestedAmount(self):
        print("Requested serial number amount: " + str(self.requestedAmount))

    def __printTotalPossibleSerialNumbers(self):
        print("Total possible serial numbers given current inputs: ", end='')
        print(self.serialCharacteristics.numberOfCharacters, end='')
        print("^", end='')
        print(self.serialCharacteristics.len, end='')
        print(" = ", end='')
        print(self.serialCharacteristics.totalPossibleSerialNumbers)

    def __printPercentOfLicensePoolCovered(self):
        print("License pool coverage: (", end='')
        print(str(self.requestedAmount) + " / ", end='')
        print("(" + str(self.serialCharacteristics.numberOfCharacters), end='')
        print("^", end='')
        print(str(self.serialCharacteristics.len) + ")) * 100 = ", end='')
        print(((self.requestedAmount /
                self.serialCharacteristics.totalPossibleSerialNumbers) * 100), end='')
        print("%")
