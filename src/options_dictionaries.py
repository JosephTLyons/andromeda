from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def get_file_options_dict():
    license_separator = input("License separator (keep blank for newline): ")

    if license_separator == "":
        license_separator = "\n"

    file_extension = input("File extension (keep blank for txt): ")

    if file_extension == "":
        file_extension = "txt"

    file_options_dict = {
        "license_separator": license_separator,
        "file_extension": file_extension.replace(".", "")
    }

    return file_options_dict

def get_serial_characteristics_dict():
    length = int(input("Serial number length: "))
    character_list = __create_character_list()
    number_of_characters = len(character_list)
    total_possible_serial_numbers = number_of_characters ** length

    serial_characteristics_dict = {
        "length": length,
        "character_list": character_list,
        "number_of_characters": number_of_characters,
        "total_possible_serial_numbers": total_possible_serial_numbers,
    }

    return serial_characteristics_dict

def __create_character_list():
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
