from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class SerialCharacteristics:
    def __init__(self):
        self.len = int(input("Serial number length: "))
        self.character_list = self.__create_character_list()
        self.number_of_characters = len(self.character_list)
        self.total_possible_serial_numbers = self.number_of_characters ** self.len

    def __create_character_list(self):
        character_list = []

        if ("y" == input("Enter 'y' to use numbers: ")):
            character_list += digits

        if ("y" == input("Enter 'y' to use uppercase letters: ")):
            character_list += ascii_uppercase

        if ("y" == input("Enter 'y' to use lowercase letters: ")):
            character_list += ascii_lowercase

        if ("y" == input("Enter 'y' to use symbols: ")):
            character_list += punctuation

        return character_list
