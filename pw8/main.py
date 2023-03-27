import os
import zipfile
import input as ip
import output as op
from marksheet import MarkSheet
from domains.colors import COLORS


def extract_data(ms: MarkSheet):
    current_path = os.getcwd()
    compress_path = current_path + "/students.zip"
    if not os.path.exists(compress_path):
        print(f"{COLORS.BLUE}Compressed data not found.{COLORS.ENDC}")
    else:
        compressed = zipfile.ZipFile("students.zip", "r")
        compressed.extractall()
        compressed.close()
        os.remove(compress_path)
        ms.load_student_file("students.pickle")
        ms.load_course_file("courses.pickle")
        ms.load_mark_file("marks.pickle")
        print(f"Files loaded successfully.")


def compress_data():
    current_path = os.getcwd()
    compress_path = current_path + "/students.zip"
    std_path = current_path + "/students.pickle"
    crs_path = current_path + "/courses.pickle"
    mk_path = current_path + "/marks.pickle"
    if not os.path.exists(std_path) or not os.path.exists(crs_path) or not os.path.exists(mk_path):
        print(f"{COLORS.BLUE}One or more of the files is missing. There will be no compression!{COLORS.ENDC}")
    else:
        compressed = zipfile.ZipFile("students.zip", "w", zipfile.ZIP_DEFLATED)
        compressed.write("students.pickle")
        compressed.write("courses.pickle")
        compressed.write("marks.pickle")
        compressed.close()
        print(f"Files compressed successfully. Path: {compress_path}")
        os.remove(std_path)
        os.remove(crs_path)
        os.remove(mk_path)


def main():
    ms = MarkSheet()

    # Extract data
    extract_data(ms)

    # Main menu
    while True:
        print("\nStudent Mark Management System")
        print("-" * 20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] Input info")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] Print info")
        print("-" * 20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Exit")
        choice = input("Your choice: ")
        match choice:
            # Exit
            case "0":
                print("Program terminated")
                break

            # Input
            case "1":
                ip.Input(ms)

            # Output
            case "2":
                op.Output(ms)

            # Invalid choice
            case _:
                print(f"{COLORS.RED}Invalid choice!{COLORS.ENDC}")

    # Compress data
    compress_data()


if __name__ == "__main__":
    main()
