from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class SerialCharacteristics:
    def __init__(self):
        self.len = int(input("Serial number length: "))
        self.characterList = self.__createCharacterList()
        self.numberOfCharacters = len(self.characterList)
        self.totalPossibleSerialNumbers = self.numberOfCharacters ** self.len

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
