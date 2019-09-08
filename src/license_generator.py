from index_list import IndexList
from pathlib import Path
from random import shuffle
from serial_characteristic import SerialCharacteristic
from string import *

class LicenseGenerator:
    def __init__(self, numberOfSerials, serialCharacteristic):
        self.numberOfSerials = numberOfSerials
        self.serialCharacteristic = serialCharacteristic

        self.characterList = self.__createCharacterList()
        self.characterListLen = len(self.characterList)
        self.listOfCharacterLists = self.__createListOfCharacterLists()
        self.indexList = IndexList(self.serialCharacteristic.len, self.characterListLen)

        self.fileName = str(self.numberOfSerials) + "_unique_serials.txt"
        self.totalPossibleSerialNumbers = self.characterListLen ** self.serialCharacteristic.len

    def generateSerialNumbers(self):
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

        for i in range(self.serialCharacteristic.len):
            shuffle(self.characterList)
            listOfCharacterLists.append(self.characterList.copy())

        return listOfCharacterLists

    def __createCharacterList(self):
        characterList = []

        if self.serialCharacteristic.useNumber:
            characterList += digits

        if self.serialCharacteristic.useUppercase:
            characterList += ascii_uppercase

        if self.serialCharacteristic.useLowercase:
            characterList += ascii_lowercase

        if self.serialCharacteristic.useSymbol:
            characterList += punctuation

        return characterList

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
            for y in range(self.serialCharacteristic.len):
                singleSerialNumberString += self.listOfCharacterLists[y][self.indexList.get()[y]]

            serialFile.write(singleSerialNumberString + "\n")
            singleSerialNumberString = ""

            self.indexList.printIndexList()
            self.indexList.increaseIndexListBy(distanceBetweenSerialNumbers)

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
