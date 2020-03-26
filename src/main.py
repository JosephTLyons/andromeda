#!/usr/bin/env python3

from file_options import FileOptions
from license_generator import LicenseGenerator
from serial_characteristics import SerialCharacteristics


def main():
    print()

    LicenseGenerator(
        int(input("Serial number amount: ")),
        SerialCharacteristics(),
        FileOptions(),
    ).generate()

    print()


if __name__ == "__main__":
    main()
