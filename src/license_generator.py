from index_list import IndexList
from pathlib import Path
from random import shuffle
from serial_characteristics import SerialCharacteristics

class LicenseGenerator:
    def __init__(self, numberOfSerials, serialCharacteristics):
        self.numberOfSerials = numberOfSerials
        self.serialCharacteristics = serialCharacteristics

        self.characterList = serialCharacteristics.createCharacterList()
        self.characterListLen = len(self.characterList)
        self.listOfCharacterLists = self.__createListOfCharacterLists()
        self.indexList = IndexList(self.serialCharacteristics.len, self.characterListLen)

        self.fileName = str(self.numberOfSerials) + "_unique_serials.txt"
        self.totalPossibleSerialNumbers = self.characterListLen ** self.serialCharacteristics.len

    def generate(self):
        if (self.totalPossibleSerialNumbers < self.numberOfSerials):
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
            shuffle(self.characterList)
            listOfCharacterLists.append(self.characterList.copy())

        return listOfCharacterLists

    def __printErrorMessage(self):
        print("Requested serial number amount: {}".format(self.numberOfSerials))
        print("Total possible serial numbers given current inputs: ", end = '')
        print(self.totalPossibleSerialNumbers)
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    def __printSerialNumbersToFile(self):
        serialFile = open(self.fileName, "w")

        singleSerialNumberString = ""
        distanceBetweenSerialNumbers = int(self.totalPossibleSerialNumbers / self.numberOfSerials)

        for _ in range(self.numberOfSerials):
            for i in range(self.serialCharacteristics.len):
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
        print(self.numberOfSerials)
        print("Total possible serial numbers given current inputs: ", end = '')
        print(self.totalPossibleSerialNumbers)
        print("The printed licenses cover ", end = '')
        print(((self.numberOfSerials / self.totalPossibleSerialNumbers) * 100), end = '')
        print("% of the total license pool: ", end = '')
