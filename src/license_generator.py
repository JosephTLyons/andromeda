from character_rule_set import CharacterSetRules
from pathlib import Path
from random import shuffle
from string import *

class LicenseGenerator:
    def __init__(self, numberOfSerials, lengthOfSerial, characterSetRules):
        self.numberOfSerials = numberOfSerials
        self.lengthOfSerial = lengthOfSerial
        self.characterSetRules = characterSetRules

        self.characterList = self.__createCharacterList()
        self.characterListLen = len(self.characterList)
        self.listOfCharacterLists = self.__createListOfCharacterLists()
        self.indexList = [0] * self.lengthOfSerial

        self.fileName = str(self.numberOfSerials) + "_unique_serials.txt"
        self.totalPossibleSerialNumbers = self.characterListLen ** self.lengthOfSerial

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

        for i in range(self.lengthOfSerial):
            shuffle(self.characterList)
            listOfCharacterLists.append(self.characterList.copy())

        return listOfCharacterLists

    def __createCharacterList(self):
        characterList = []

        if self.characterSetRules.useNumber:
            characterList += digits

        if self.characterSetRules.useUppercase:
            characterList += ascii_uppercase

        if self.characterSetRules.useLowercase:
            characterList += ascii_lowercase

        if self.characterSetRules.useSymbol:
            characterList += punctuation

        return characterList

    def __printErrorMessage(self):
        print("Requested serial number amount: {}".format(self.numberOfSerials))
        print("Total possible serial numbers given current inputs: {}".format(self.totalPossibleSerialNumbers))
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    def __printSerialNumbersToFile(self):
        serialFile = open(self.fileName, "w")

        singleSerialNumberString = ""
        distanceBetweenSerialNumbers = int(self.totalPossibleSerialNumbers / self.numberOfSerials)

        for _ in range(self.numberOfSerials):
            for y in range(self.lengthOfSerial):
                singleSerialNumberString += self.listOfCharacterLists[y][self.indexList[y]]

            serialFile.write(singleSerialNumberString + "\n")
            singleSerialNumberString = ""

            # self.__printIndexList()

            self.__increaseIndexListBy(distanceBetweenSerialNumbers)

        serialFile.close()

    def __printIndexList(self):
        for index in self.indexList:
            print(str(index).rjust(3), end = '')

        print();

    def __increaseIndexListBy(self, distanceBetweenSerialNumbers):
        increaseValueAtIndexBy = 0

        for i in reversed(range(len(self.indexList))):
            increaseValueAtIndexBy = distanceBetweenSerialNumbers % self.characterListLen
            self.indexList[i] += increaseValueAtIndexBy

            if (self.indexList[i] >= self.characterListLen):
                self.indexList[i] -= self.characterListLen

                if (i > 0):
                    self.indexList[i - 1] += 1

            distanceBetweenSerialNumbers = int(distanceBetweenSerialNumbers / self.characterListLen)

    def __printPathToTerminal(self):
        filePath = Path.cwd().joinpath(self.fileName)
        print("File path: {}".format(filePath))

    def __printStatsToTerminal(self):
        print("Requested serial number amount: {}".format(self.numberOfSerials))
        print("Total possible serial numbers given current inputs: {}".format(self.totalPossibleSerialNumbers))
        print("The printed licenses cover {}% of the total license pool".format((self.numberOfSerials / self.totalPossibleSerialNumbers) * 100))
