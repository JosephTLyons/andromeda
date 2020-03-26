from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def get_file_options_dict():
    license_separator_character = input("License separator character (keep blank for newline): ")

    if license_separator_character == "" or len(license_separator_character) > 1:
        license_separator_character = "\n"

    file_extension = input("File extension (keep blank for txt): ")

    if file_extension == "":
        file_extension = "txt"

    file_options_dict = {
        "license_separator_character": license_separator_character,
        "file_extension": file_extension.replace(".", "")
    }

    return file_options_dict

def get_serial_characteristics_dict(license_separation_character):
    length = int(input("Serial number length: "))
    character_list = __create_character_list()

    if license_separation_character != "\n" and license_separation_character in character_list:
        character_list.remove(license_separation_character)
        print()
        print("License separation character was found in requested license characters and has been removed")

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
