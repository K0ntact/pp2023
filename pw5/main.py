from domains.marksheet import MarkSheet
from domains.colors import COLORS
import input, os, zipfile
"""
TO GENERATE DATA FOR TESTING:
Search "TEST" in input.py, course.py, marksheet.py and uncomment the code
"""


def main():
    # Extract compressed data
    current_path = os.getcwd()
    compress_path = current_path + "/students.zip"
    if not os.path.exists(compress_path):
        print(f"{COLORS.BLUE}Compressed data not found.{COLORS.ENDC}")
    else:
        compressed = zipfile.ZipFile("students.zip", "r")
        compressed.extractall()
        compressed.close()
        print(f"Files extracted successfully.")
        os.remove(compress_path)

    ms = MarkSheet()
    input.Input(ms)

    # Compress data
    std_path = current_path + "/students.txt"
    crs_path = current_path + "/courses.txt"
    mk_path = current_path + "/marks.txt"
    if not os.path.exists(std_path) or not os.path.exists(crs_path) or not os.path.exists(mk_path):
        print(f"{COLORS.BLUE}One or more of the files is missing. There will be no compression!{COLORS.ENDC}")
    else:
        compressed = zipfile.ZipFile("students.zip", "w", zipfile.ZIP_DEFLATED)
        compressed.write("students.txt")
        compressed.write("courses.txt")
        compressed.write("marks.txt")
        compressed.close()
        print(f"Files compressed successfully. Path: {compress_path}")
        os.remove(std_path)
        os.remove(crs_path)
        os.remove(mk_path)


if __name__ == "__main__":
    main()