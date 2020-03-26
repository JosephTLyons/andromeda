#!/usr/bin/env python3

from license_generator import LicenseGenerator
from options_dictionaries import get_file_options_dict, get_serial_characteristics_dict


def main():
    print()

    file_options_dict = get_file_options_dict()
    serial_characteristics_dict = get_serial_characteristics_dict(file_options_dict["license_separator_character"])

    LicenseGenerator(
        int(input("Serial number amount: ")),
        file_options_dict,
        serial_characteristics_dict,
    ).generate()

    print()


if __name__ == "__main__":
    main()
