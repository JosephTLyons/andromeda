#!/usr/bin/env python3

from character_rule_set import CharacterSetRules
from license_generator import LicenseGenerator

def main():
    print()

    numberOfSerials = int(input("Serial number amount: "))
    lengthOfSerial  = int(input("Serial number length: "))

    characterSetRules = CharacterSetRules()
    characterSetRules.setRules()

    generator = LicenseGenerator(numberOfSerials, lengthOfSerial, characterSetRules)
    generator.generateSerialNumbers()

    print()

main()
