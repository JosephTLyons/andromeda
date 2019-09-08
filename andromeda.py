#!/usr/bin/env python3

from character_rule_set import CharacterSetRules
from license_generator import LicenseGenerator

def main():
    print()

    numberOfSerials = int(input("Serial number amount: "))
    lengthOfSerial  = int(input("Serial number length: "))

    characterSetRules = CharacterSetRules()
    characterSetRules.useNumber    = ("y" == input("Enter 'y' to use numbers: "))
    characterSetRules.useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
    characterSetRules.useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
    characterSetRules.useSymbol    = ("y" == input("Enter 'y' to use symbols: "))

    generator = LicenseGenerator(numberOfSerials, lengthOfSerial, characterSetRules)
    generator.generateSerialNumbers()

    print()

main()
