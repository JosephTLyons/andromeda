#!/usr/bin/env python3

from license_generator import LicenseGenerator
from serial_characteristics import SerialCharacteristics

def main():
    print()

    numberOfSerials = int(input("Serial number amount: "))

    serialCharacteristics = SerialCharacteristics()
    serialCharacteristics.define()

    LicenseGenerator(numberOfSerials, serialCharacteristics).generate()

    print()

if __name__ == "__main__":
    main()
