from pathlib import Path
from random import shuffle

from src.index_list import IndexList
from src.exceptions import Unreachable


class LicenseGenerator:
    def __init__(self, file_options_dict, batch_license_dict, license_characteristics_dict):
        self.file_options_dict = file_options_dict
        self.batch_license_dict = batch_license_dict
        self.license_characteristics_dict = license_characteristics_dict

        self.list_of_character_lists = self.__create_list_of_character_lists()
        self.index_list = IndexList(
            self.license_characteristics_dict["length"],
            self.license_characteristics_dict["number_of_characters"],
        )

        self.file_name = (
            str(self.batch_license_dict["number_of_licenses"])
            + "_unique_licenses"
            + "."
            + self.file_options_dict["file_extension"]
        )

    def generate(self):
        if (
            self.license_characteristics_dict["total_possible_licenses"]
            < self.batch_license_dict["number_of_licenses"]
        ):
            self.__print_error_message()
            return

        self.__print_licenses_to_file()
        self.__print_path_to_terminal()
        self.__print_statistics_to_terminal()

    def __create_list_of_character_lists(self):
        list_of_character_lists = []

        for _ in range(self.license_characteristics_dict["length"]):
            shuffle(self.license_characteristics_dict["character_list"])
            list_of_character_lists.append(
                self.license_characteristics_dict["character_list"].copy()
            )

        return list_of_character_lists

    def __print_error_message(self):
        print(f"Requested number of licenses: {self.batch_license_dict['number_of_licenses']}")
        print("Total possible licenses given current inputs: ", end="")
        print(self.license_characteristics_dict["total_possible_licenses"])
        print("Try one or more of the following:")
        print("- Increasing the length of the license")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of licenses to be generated")

    def __print_licenses_to_file(self):
        with open(self.file_name, "w") as license_file:
            single_license_string = ""
            distance_between_licenses = (
                self.license_characteristics_dict["total_possible_licenses"]
                // self.batch_license_dict["number_of_licenses"]
            )

            for i in range(self.batch_license_dict["number_of_licenses"]):
                for j in range(self.license_characteristics_dict["length"]):
                    single_license_string += self.list_of_character_lists[j][self.index_list[j]]

                # This should never occur, based on the algorithm, however, it is better safe than
                # sorry.  If somehow the list could overflow, it returns back to 0 and duplicate
                # licenses could potentially be created.
                if self.index_list.has_overflowed:
                    raise Unreachable("Index List has overflowed.")

                if i < self.batch_license_dict["number_of_licenses"] - 1:
                    single_license_string += self.batch_license_dict["license_separator_character"]

                license_file.write(single_license_string)
                single_license_string = ""

                # print(self.index_list.get_index_string())
                self.index_list.increase_by(distance_between_licenses)

    def __print_path_to_terminal(self):
        file_path = Path.cwd().joinpath(self.file_name)
        print(f"File path: {file_path}")

    def __print_statistics_to_terminal(self):
        self.__print_number_of_licenses()
        self.__print_total_possible_licenses()
        self.__print_percent_of_license_pool_covered()

    def __print_number_of_licenses(self):
        print("Requested number of licenses: " + str(self.batch_license_dict["number_of_licenses"]))

    def __print_total_possible_licenses(self):
        print("Total possible number of licenses given current inputs: ", end="")
        print(self.license_characteristics_dict["number_of_characters"], end="")
        print("^", end="")
        print(self.license_characteristics_dict["length"], end="")
        print(" = ", end="")
        print(self.license_characteristics_dict["total_possible_licenses"])

    def __print_percent_of_license_pool_covered(self):
        print("License pool coverage: (", end="")
        print(str(self.batch_license_dict["number_of_licenses"]) + " / ", end="")
        print("(" + str(self.license_characteristics_dict["number_of_characters"]), end="")
        print("^", end="")
        print(str(self.license_characteristics_dict["length"]) + ")) * 100 = ", end="")
        print(
            (
                self.batch_license_dict["number_of_licenses"]
                / self.license_characteristics_dict["total_possible_licenses"]
            )
            * 100,
            end="",
        )
        print("%")
