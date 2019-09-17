#!/usr/bin/env python3

from license_generator import LicenseGenerator
from serial_characteristics import SerialCharacteristics


def main():
    print()

    requestedAmount = int(input("Serial number amount: "))
    serialCharacteristics = SerialCharacteristics()
    LicenseGenerator(requestedAmount, serialCharacteristics).generate()

    print()


if __name__ == "__main__":
    main()
