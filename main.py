from src.license_generator import LicenseGenerator
from src.options_dictionaries import (
    get_batch_license_dict,
    get_file_options_dict,
    get_license_characteristics_dict,
)


def main():
    print()

    print_header("File Options")
    file_options_dict = get_file_options_dict()
    print()

    print_header("Batch Options")
    batch_license_dict = get_batch_license_dict()
    print()

    print_header("License Characteristics Options")
    license_characteristics_dict = get_license_characteristics_dict(
        batch_license_dict["license_separator_character"]
    )
    print()

    print_header("Results")

    LicenseGenerator(
        file_options_dict,
        batch_license_dict,
        license_characteristics_dict,
    ).generate()

    print()


def print_header(header):
    print(header)
    separator_line = "=" * len(header)
    print(separator_line)


if __name__ == "__main__":
    main()
