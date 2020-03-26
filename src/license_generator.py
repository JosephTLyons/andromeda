from pathlib import Path
from random import shuffle

from file_options import FileOptions
from index_list import IndexList
from serial_characteristics import SerialCharacteristics


class LicenseGenerator:
    def __init__(self, requested_amount, serial_characteristics, file_options):
        self.requested_amount = requested_amount
        self.serial_characteristics = serial_characteristics
        self.file_options = file_options

        self.list_of_character_lists = self.__create_list_of_character_lists()
        self.index_list = IndexList(self.serial_characteristics.len,
                                    self.serial_characteristics.number_of_characters)

        self.file_name = str(self.requested_amount) \
            + "_unique_serials" \
            + "." \
            + self.file_options.file_extension

    def generate(self):
        if (self.serial_characteristics.total_possible_serial_numbers < self.requested_amount):
            self.__print_error_message()
            return

        self.__print_serial_numbers_to_file()
        print()
        self.__print_path_to_terminal()
        print()
        self.__print_stats_to_terminal()

    def __create_list_of_character_lists(self):
        list_of_character_lists = []

        for i in range(self.serial_characteristics.len):
            shuffle(self.serial_characteristics.character_list)
            list_of_character_lists.append(self.serial_characteristics.character_list.copy())

        return list_of_character_lists

    def __print_error_message(self):
        print("Requested serial number amount: {}".format(self.requested_amount))
        print("Total possible serial numbers given current inputs: ", end='')
        print(self.serial_characteristics.total_possible_serial_numbers)
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    def __print_serial_numbers_to_file(self):
        serial_file = open(self.file_name, "w")

        single_serial_number_string = ""
        distance_between_serial_numbers = self.serial_characteristics.total_possible_serial_numbers // self.requested_amount

        for _ in range(self.requested_amount):
            for i in range(self.serial_characteristics.len):
                single_serial_number_string += self.list_of_character_lists[i][self.index_list.at(i)]

            # This should never occur, based on the algorithm, however, it is better safe than
            # sorry.  If somehow the list could overflow, it returns back to 0 and duplicate
            # licenses could potentially be creted.
            if self.index_list.has_over_flown:
                raise ValueError("Index List has overflown.")

            serial_file.write(single_serial_number_string + self.file_options.license_separator)
            single_serial_number_string = ""

            # print(self.index_list.get_index_string())
            self.index_list.increase_by(distance_between_serial_numbers)

        serial_file.close()

    def __print_path_to_terminal(self):
        file_path = Path.cwd().joinpath(self.file_name)
        print("File path: {}".format(file_path))

    def __print_stats_to_terminal(self):
        self.__print_requested_amount()
        self.__print_total_possible_serial_numbers()
        self.__print_percent_of_license_pool_covered()

    def __print_requested_amount(self):
        print("Requested serial number amount: " + str(self.requested_amount))

    def __print_total_possible_serial_numbers(self):
        print("Total possible serial numbers given current inputs: ", end='')
        print(self.serial_characteristics.number_of_characters, end='')
        print("^", end='')
        print(self.serial_characteristics.len, end='')
        print(" = ", end='')
        print(self.serial_characteristics.total_possible_serial_numbers)

    def __print_percent_of_license_pool_covered(self):
        print("License pool coverage: (", end='')
        print(str(self.requested_amount) + " / ", end='')
        print("(" + str(self.serial_characteristics.number_of_characters), end='')
        print("^", end='')
        print(str(self.serial_characteristics.len) + ")) * 100 = ", end='')
        print(((self.requested_amount /
                self.serial_characteristics.total_possible_serial_numbers) * 100), end='')
        print("%")
