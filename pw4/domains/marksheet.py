from .colors import COLORS
from .course import Course
from .student import Student
import re
import numpy as np


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
