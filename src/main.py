#!/usr/bin/env python3

from license_generator import LicenseGenerator
from options_dictionaries import get_file_options_dict, get_serial_characteristics_dict


def main():
    print()

    LicenseGenerator(
        int(input("Serial number amount: ")),
        get_serial_characteristics_dict(),
        get_file_options_dict(),
    ).generate()

    print()


if __name__ == "__main__":
    main()
