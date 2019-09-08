from string import digits
from string import ascii_uppercase
from string import ascii_lowercase
from string import punctuation

class SerialCharacteristics:
    def __init__(self):
        self.serialLen = int(input("Serial number length: "))
        self.characterList = self.__createCharacterList()
        self.numberOfCharacters = len(self.characterList)
        self.totalPossibleSerialNumbers = self.numberOfCharacters ** self.serialLen

    def __createCharacterList(self):
        characterList = []

        if ("y" == input("Enter 'y' to use numbers: ")):
            characterList += digits

        if ("y" == input("Enter 'y' to use uppercase letters: ")):
            characterList += ascii_uppercase

        if ("y" == input("Enter 'y' to use lowercase letters: ")):
            characterList += ascii_lowercase

        if ("y" == input("Enter 'y' to use symbols: ")):
            characterList += punctuation

        return characterList
