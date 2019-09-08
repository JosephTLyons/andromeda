from string import digits
from string import ascii_uppercase
from string import ascii_lowercase
from string import punctuation

class SerialCharacteristics:
    def __init__(self):
        self.serialLen  = int(input("Serial number length: "))

        self.useNumber    = ("y" == input("Enter 'y' to use numbers: "))
        self.useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
        self.useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
        self.useSymbol    = ("y" == input("Enter 'y' to use symbols: "))

        self.characterList = []
        self.__buildCharacterList()

        self.numberOfCharacters = len(self.characterList)
        self.totalPossibleSerialNumbers = self.numberOfCharacters ** self.serialLen

    def __buildCharacterList(self):
        if self.useNumber:
            self.characterList += digits

        if self.useUppercase:
            self.characterList += ascii_uppercase

        if self.useLowercase:
            self.characterList += ascii_lowercase

        if self.useSymbol:
            self.characterList += punctuation
