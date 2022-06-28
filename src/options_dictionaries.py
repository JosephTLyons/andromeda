from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def get_batch_license_dict():
    number_of_licenses = int(input("Number of licenses: "))

    license_separator_character = ""

    while len(license_separator_character) != 1:
        license_separator_character = input(
            "License separator character (keep blank for newline): "
        )

        if len(license_separator_character) > 1:
            print("Only a single character can be used for a license separator character")

        if license_separator_character == "":
            license_separator_character = "\n"

    batch_license_dict = {
        "number_of_licenses": number_of_licenses,
        "license_separator_character": license_separator_character,
    }

    return batch_license_dict


def get_file_options_dict():
    file_extension = input("File extension (keep blank for txt): ")

    if file_extension == "":
        file_extension = "txt"

    file_options_dict = {"file_extension": file_extension.replace(".", "")}

    return file_options_dict


def get_license_characteristics_dict(license_separation_character):
    length = int(input("License length: "))
    character_list = __create_character_list()

    if license_separation_character != "\n" and license_separation_character in character_list:
        character_list.remove(license_separation_character)
        print()
        print(
            "License separation character was found in requested license characters and has been "
            "removed"
        )

    number_of_characters = len(character_list)
    total_possible_licenses = number_of_characters ** length

    license_characteristics_dict = {
        "length": length,
        "character_list": character_list,
        "number_of_characters": number_of_characters,
        "total_possible_licenses": total_possible_licenses,
    }

    return license_characteristics_dict


def __create_character_list():
    character_list = []

    if "y" == input("Enter 'y' to use numbers: "):
        character_list.extend(digits)

    if "y" == input("Enter 'y' to use uppercase letters: "):
        character_list.extend(ascii_uppercase)

    if "y" == input("Enter 'y' to use lowercase letters: "):
        character_list.extend(ascii_lowercase)

    if "y" == input("Enter 'y' to use symbols: "):
        character_list.extend(punctuation)

    return character_list
