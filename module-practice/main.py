import os
import re


def scan_directory(directory):
    phone_numbers = {}
    for folders, sub_folders, files in os.walk(directory):
        if len(files) > 0:
            for file in files:
                file_path = os.path.join(folders, file)
                search_phone_number(phone_numbers, file_path)

    if len(phone_numbers) > 0:
        for path, phone in phone_numbers.items():
            print(f"Directory: {path}")
            print(f"\tFound {len(phone)} number")
            for index, number in enumerate(phone):
                print(f"\t{index + 1}. {number}")


def search_phone_number(phone_numbers, file):
    # using with to open and close file at the same time
    if file.endswith(".txt"):
        with open(file, "r") as contents:
            phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
            phone = re.findall(phone_pattern, contents.read())
            if phone:
                phone_numbers[file] = phone


if __name__ == '__main__':
    # shutil.unpack_archive("unzip_me_for_instructions.zip", os.getcwd(), "zip")

    scan_directory("extracted_content")
