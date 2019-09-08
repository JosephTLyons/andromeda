from index_list import IndexList
from pathlib import Path
from random import shuffle
from serial_characteristics import SerialCharacteristics

class LicenseGenerator:
    def __init__(self, requestedAmount, serialCharacteristics):
        self.requestedAmount = requestedAmount
        self.serialCharacteristics = serialCharacteristics

        self.listOfCharacterLists = self.__createListOfCharacterLists()
        self.indexList = IndexList(self.serialCharacteristics.serialLen,
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

        for i in range(self.serialCharacteristics.serialLen):
            shuffle(self.serialCharacteristics.characterList)
            listOfCharacterLists.append(self.serialCharacteristics.characterList.copy())

        return listOfCharacterLists

    def __printErrorMessage(self):
        print("Requested serial number amount: {}".format(self.requestedAmount))
        print("Total possible serial numbers given current inputs: ", end = '')
        print(self.serialCharacteristics.totalPossibleSerialNumbers)
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    def __printSerialNumbersToFile(self):
        serialFile = open(self.fileName, "w")

        singleSerialNumberString = ""
        distanceBetweenSerialNumbers = int(self.serialCharacteristics.totalPossibleSerialNumbers / self.requestedAmount)

        for _ in range(self.requestedAmount):
            for i in range(self.serialCharacteristics.serialLen):
                singleSerialNumberString += self.listOfCharacterLists[i][self.indexList.at(i)]

            serialFile.write(singleSerialNumberString + "\n")
            singleSerialNumberString = ""

            # self.indexList.print()
            self.indexList.increaseBy(distanceBetweenSerialNumbers)

        serialFile.close()

    def __printPathToTerminal(self):
        filePath = Path.cwd().joinpath(self.fileName)
        print("File path: {}".format(filePath))

    def __printStatsToTerminal(self):
        print("Requested serial number amount: ", end = '')
        print(self.requestedAmount)
        print("Total possible serial numbers given current inputs: ", end = '')
        print(self.serialCharacteristics.totalPossibleSerialNumbers)
        print("The printed licenses cover ", end = '')
        print(((self.requestedAmount / self.serialCharacteristics.totalPossibleSerialNumbers) * 100), end = '')
        print("% of the total license pool: ", end = '')
