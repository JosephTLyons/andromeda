#!/usr/bin/env python3

from license_generator import LicenseGenerator
from serial_characteristic import SerialCharacteristic

def main():
    print()

    numberOfSerials = int(input("Serial number amount: "))

    serialCharacteristic = SerialCharacteristic()
    serialCharacteristic.define()

    LicenseGenerator(numberOfSerials, serialCharacteristic).generateSerialNumbers()

    print()

if __name__ == "__main__":
    main()
