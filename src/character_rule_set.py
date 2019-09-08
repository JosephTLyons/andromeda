class CharacterSetRules:
    useNumber    = bool()
    useUppercase = bool()
    useLowercase = bool()
    useSymbol    = bool()

    def __init__(self):
        useNumber    = True
        useUppercase = True
        useLowercase = True
        useSymbol    = True

    def setRules(self):
        self.useNumber    = ("y" == input("Enter 'y' to use numbers: "))
        self.useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
        self.useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
        self.useSymbol    = ("y" == input("Enter 'y' to use symbols: "))
