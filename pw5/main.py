from domains.marksheet import MarkSheet
from domains.colors import COLORS
import input as ip
import output as op
import os, zipfile
"""
TO GENERATE DATA FOR TESTING:
Search "TEST" in input.py, course.py, marksheet.py and uncomment the code
"""


def main():
    ms = MarkSheet()
    while True:
        print("\nStudent Mark Management System")
        print("-"*20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] Input info")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] Print info")
        print("-"*20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Exit")
        choice = int(input("Your choice: "))
        match choice:
            # Exit
            case 0:
                print("Program terminated")
                break

            # Input
            case 1:
                ip.Input(ms)

            # Output
            case 2:
                op.Output(ms)


if __name__ == "__main__":
    main()