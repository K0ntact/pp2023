from domains.marksheet import MarkSheet
import input
"""
TO GENERATE DATA FOR TESTING:
Search "TEST" in input.py, course.py, marksheet.py and uncomment the code
"""


def main():
    ms = MarkSheet()
    input.Input(ms)


if __name__ == "__main__":
    main()