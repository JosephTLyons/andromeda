#!/usr/bin/env python3

from license_generator import LicenseGenerator
from serial_characteristics import SerialCharacteristics


def main():
    print()

    requested_amount = int(input("Serial number amount: "))
    serial_characteristics = SerialCharacteristics()
    LicenseGenerator(requested_amount, serial_characteristics).generate()

    print()


if __name__ == "__main__":
    main()
