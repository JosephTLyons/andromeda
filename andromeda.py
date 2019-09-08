#!/usr/bin/env python3

import os
from character_rule_set import CharacterSetRules
from pathlib import Path
from random import shuffle
from string import *

def main():
    print()

    numberOfSerials = int(input("Serial number amount: "))
    lengthOfSerial  = int(input("Serial number length: "))

    charSetRules = CharacterSetRules()
    charSetRules.useNumber    = ("y" == input("Enter 'y' to use numbers: "))
    charSetRules.useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
    charSetRules.useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
    charSetRules.useSymbol    = ("y" == input("Enter 'y' to use symbols: "))

    listOfCharacterLists = createListOfCharacterLists(lengthOfSerial, charSetRules)
    totalPossibleSerialNumbers = len(listOfCharacterLists[0]) ** lengthOfSerial

    if (totalPossibleSerialNumbers < numberOfSerials):
        printErrorMessage(numberOfSerials, totalPossibleSerialNumbers)
        return

    generateSerialNumbers(numberOfSerials, lengthOfSerial, listOfCharacterLists, totalPossibleSerialNumbers)

    print()

def createListOfCharacterLists(lengthOfSerial, charSetRules):
    characterList = createCharacterList(charSetRules)
    listOfCharacterLists = []

    for i in range(lengthOfSerial):
        shuffle(characterList)
        listOfCharacterLists.append(characterList.copy())

    return listOfCharacterLists

def createCharacterList(charSetRules):
    characterList = []

    if charSetRules.useNumber:
        characterList += digits

    if charSetRules.useUppercase:
        characterList += ascii_uppercase

    if charSetRules.useLowercase:
        characterList += ascii_lowercase

    if charSetRules.useSymbol:
        characterList += punctuation

    return characterList

def printErrorMessage(numberOfSerials, totalPossibleSerialNumbers):
    print("Requested serial number amount: {}".format(numberOfSerials))
    print("Total possible serial numbers given current inputs: {}".format(totalPossibleSerialNumbers))
    print("Try one or more of the following:")
    print("- Increasing the length of the serial numbers")
    print("- Allowing more types of symbols to be used")
    print("- Decreasing the amount of serial numbers to be generated")

def generateSerialNumbers(numberOfSerials, lengthOfSerial, listOfCharacterLists, totalPossibleSerialNumbers):
    fileName = str(numberOfSerials) + "_unique_serials.txt"
    printSerialNumbersToFile(fileName, numberOfSerials, lengthOfSerial,
                             listOfCharacterLists, totalPossibleSerialNumbers)
    print()
    printPathToTerminal(fileName)
    print()
    printStatsToTerminal(numberOfSerials, totalPossibleSerialNumbers)

def printSerialNumbersToFile(fileName, numberOfSerials, lengthOfSerial, listOfCharacterLists, totalPossibleSerialNumbers):
    serialFile = open(fileName, "w")

    singleSerialNumberString = ""
    indexList = [0] * lengthOfSerial
    distanceBetweenSerialNumbers = int(totalPossibleSerialNumbers / numberOfSerials)

    for _ in range(numberOfSerials):
        for y in range(lengthOfSerial):
            singleSerialNumberString += listOfCharacterLists[y][indexList[y]]

        serialFile.write(singleSerialNumberString + "\n")
        singleSerialNumberString = ""

        # printIndexList(indexList)

        increaseIndexListBy(indexList, len(listOfCharacterLists[0]), distanceBetweenSerialNumbers)

    serialFile.close()

def printIndexList(indexList):
    for index in indexList:
        print(str(index).rjust(3), end = '')

    print();

def increaseIndexListBy(indexList, rolloverNumber, distanceBetweenSerialNumbers):
    increaseValueAtIndexBy = 0

    for i in reversed(range(len(indexList))):
        increaseValueAtIndexBy = distanceBetweenSerialNumbers % rolloverNumber
        indexList[i] += increaseValueAtIndexBy

        if (indexList[i] >= rolloverNumber):
            indexList[i] -= rolloverNumber

            if (i > 0):
                indexList[i - 1] += 1

        distanceBetweenSerialNumbers = int(distanceBetweenSerialNumbers / rolloverNumber)

def printPathToTerminal(fileName):
    filePath = Path.cwd().joinpath(fileName)
    print("File path: {}".format(filePath))

def printStatsToTerminal(numberOfSerials, totalPossibleSerialNumbers):
    print("Requested serial number amount: {}".format(numberOfSerials))
    print("Total possible serial numbers given current inputs: {}".format(totalPossibleSerialNumbers))
    print("The printed licenses cover {}% of the total license pool".format((numberOfSerials / totalPossibleSerialNumbers) * 100))

main()
