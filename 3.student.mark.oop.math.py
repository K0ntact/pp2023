import re
import math
import numpy as np

class COLORS:
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Info:
    def __init__(self, ID: str, name: str) -> None:
        self._id = ID
        self._name = name

    def get_name(self) -> str: return self._name
    def get_ID(self) -> str: return self._id

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")


class Student(Info):
    def __init__(self, ID: str, name: str, dob: str) -> None:
        super().__init__(ID, name)
        self.__dob = dob
        self.__gpa = 0

    def get_dob(self) -> str: return self.__dob
    def set_gpa(self, gpa: float) -> None: self.__gpa = gpa
    def get_gpa(self) -> float: return self.__gpa

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"DOB: {self.__dob}")
        print("\n")


class Course(Info):
    def __init__(self, ID: str, name: str, credit: int) -> None:
        super().__init__(ID, name)
        self.__credit = credit
        self.__marks = []

    def get_credit(self) -> int: return self.__credit
    def get_marks(self) -> list: return self.__marks

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Credits: {self.__credit}")
        print("\n")

    def display_marks(self, std_list: list) -> None:
        for std in std_list:
            std_pos = std_list.index(std)
            print(f"{std.get_name()}: {self.__marks[std_pos]}")

    def set_marks(self, std_list: list) -> None:
        for std in std_list:
            f_mark = float(input(f"Set the score for student {std.get_name()}: "))
            i_mark = math.floor(f_mark)
            self.__marks.append(i_mark)


class MarkSheet:
    def __init__(self):
        self.__student_list = []
        self.__course_list = []

    def get_course_list(self) -> list: return self.__course_list
    def get_student_list(self) -> list: return self.__student_list

    def add_course(self) -> None:
        name = input("Enter course name: ")
        ID = input("Enter course ID: ")
        credit = int(input("Enter course credit: "))
        new_course = Course(ID, name, credit)
        self.__course_list.append(new_course)

    def add_student(self) -> None:
        name = input("Enter student's name: ")

        ID = input("The ID should be BI/BAxx-xxx (x is from 0-9)\nEnter student ID: ")
        while True:
            checker = re.search('(BI|BA)[0-9][0-9]-[0-9][0-9][0-9]', ID)
            if checker is None:
                print(f"{COLORS.RED}You've typed in the wrong ID format.{COLORS.ENDC}\nThe ID should be BI/BAxx-xxx (x is from 0-9)\n")
                ID = input("Enter student's ID: ")
            else:
                break

        dob = input("The DOB should be dd/mm/yyyy\nEnter student DOB: ")
        while True:
            checker = re.search('[0-3][0-9]/[0-1][0-9]/[1-2][0-9[0-9][0-9]', dob)
            if checker is None:
                print(f"{COLORS.RED}You've typed in the wrong DOB format.{COLORS.ENDC}\nThe DOB should be dd/mm/yyyy\n")
                ID = input("Enter student's DOB: ")
            else:
                break

        new_student = Student(ID, name, dob)
        self.__student_list.append(new_student)

    def list_course(self) -> None:
        for course in self.__course_list:
            course.display_info()
        print("\n")

    def list_student(self) -> None:
        for student in self.__student_list:
            student.display_info()
        print("\n")

    # How the matrix should look like:
    #           std_1       std_2      std_3        std_4
    # course_1  10          15          8           7
    # course_2  14          12          15          13
    # course_3  16          13          12          18

    def calculate_gpa(self) -> None:
        row = len(self.__course_list)
        col = len(self.__student_list)
        matrix = np.zeros(shape=(row, col))
        credit_arr = []     # get credits of course into an array for easier working

        i = 0
        for course in self.__course_list:
            credit_arr.append(course.get_credit())
            matrix[i] = course.get_marks()
            i += 1

        for column in range(0, col):
            std_mark = matrix[:, column]     # Get the mark of student [column]
            temp = 0
            gpa = 0
            for index in range(0, row):
                temp += std_mark[index] * credit_arr[index]
                gpa = round(temp / sum(credit_arr), 2)
            (self.__student_list[column]).set_gpa(gpa)

    def sort_by_gpa(self) -> list:
        gpa_sorted = sorted(self.__student_list, key=lambda std: std.get_gpa())
        gpa_sorted.reverse()
        return gpa_sorted


def main():
    ms = MarkSheet()
    while True:
        print("\nStudent Mark Management System")
        print("-"*20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] Add a student")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] Add a course")
        print(f"[{COLORS.YELLOW}3{COLORS.ENDC}] Input marks for a course")
        print(f"[{COLORS.YELLOW}4{COLORS.ENDC}] List all student")
        print(f"[{COLORS.YELLOW}5{COLORS.ENDC}] List all course")
        print(f"[{COLORS.YELLOW}6{COLORS.ENDC}] Show student marks in a course")
        print(f"[{COLORS.YELLOW}7{COLORS.ENDC}] Sort student by GPA")
        print("-"*20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Exit")
        choice = int(input("Your choice: "))
        match choice:
            # Exit
            case 0:
                print("Program terminated")
                break

            # Add a student
            case 1:
                ms.add_student()

            # Add a course
            case 2:
                ms.add_course()

            # Input marks for a course
            case 3:
                if len(ms.get_course_list()) == 0:
                    print(f"{COLORS.RED}You have to add a course first!{COLORS.ENDC}")
                    continue

                if len(ms.get_student_list()) == 0:
                    print(f"{COLORS.RED}You have to add a student first!{COLORS.ENDC}")
                    continue

                print("Available course(s):", end=" ")
                for course in ms.get_course_list():
                    print(course.get_name(), end="  ")
                name = input("\nYour choice: ")

                count = 0
                for course in ms.get_course_list():
                    if name != course.get_name():
                        count += 1
                        if count == len(ms.get_course_list()):
                            print(f"{COLORS.RED}Course not found!{COLORS.ENDC}")
                            break
                        continue

                    # course found
                    course.set_marks(ms.get_student_list())

            # List all students
            case 4:
                ms.list_student()

            # List all courses
            case 5:
                ms.list_course()

            # Show all student marks in a course
            case 6:
                if len(ms.get_course_list()) == 0:
                    print(f"{COLORS.RED}You have to add a course first!{COLORS.ENDC}")
                    continue

                if len(ms.get_student_list()) == 0:
                    print(f"{COLORS.RED}You have to add a student first!{COLORS.ENDC}")
                    continue

                print("Available course(s):", end=" ")
                for course in ms.get_course_list():
                    print(course.get_name(), end="  ")
                name = input("\nYour choice: ")

                count = 0
                for course in ms.get_course_list():
                    if name != course.get_name():
                        count += 1
                        if count == len(ms.get_course_list()):
                            print(f"{COLORS.RED}Course not found!{COLORS.ENDC}")
                            break
                        continue

                    if course.get_marks():
                        course.display_marks(ms.get_student_list())
                        break
                    else:   # no marks in course
                        print(f"{COLORS.RED}You haven't put any marks in this course!{COLORS.ENDC}")
                        break

            case 7:
                if len(ms.get_course_list()) == 0:
                    print(f"{COLORS.RED}You have to add a course first!{COLORS.ENDC}")
                    continue

                if len(ms.get_student_list()) == 0:
                    print(f"{COLORS.RED}You have to add a student first!{COLORS.ENDC}")
                    continue

                for course in ms.get_course_list():
                    if not course.get_marks(): # no marks in course
                        print(f"{COLORS.RED}You haven't put any marks in {course.get_name()} course!{COLORS.ENDC}")
                        break

                ms.calculate_gpa()
                std_list = ms.sort_by_gpa()
                for index in range(0, len(std_list)):
                    print(f"{index + 1}. {std_list[index].get_name()}: {std_list[index].get_gpa()}")


if __name__ == "__main__":
    main()
