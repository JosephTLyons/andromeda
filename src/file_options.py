class FileOptions:
    def __init__(self):
        self.license_separator = input("License separator (keep blank for newline): ")

        if self.license_separator == "":
            self.license_separator = "\n"

        self.file_extension = input("File extension: ")
