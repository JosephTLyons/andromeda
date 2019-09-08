class SerialCharacteristic:
    def __init__(self):
        self.len = 20

        self.useNumber    = True
        self.useUppercase = True
        self.useLowercase = True
        self.useSymbol    = True

    def define(self):
        self.len  = int(input("Serial number length: "))

        self.useNumber    = ("y" == input("Enter 'y' to use numbers: "))
        self.useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
        self.useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
        self.useSymbol    = ("y" == input("Enter 'y' to use symbols: "))
