from domains.colors import COLORS
from domains.course import Course
from domains.student import Student
import re
import math
import numpy as np


def rm_all_ws(text: str) -> str:
    return "".join(text.split())


class MarkSheet:
    def __init__(self):
        self.__student_list: list[Student] = []
        self.__course_list: list[Course] = []

    def get_course_list(self) -> list[Course]:
        return self.__course_list

    def get_student_list(self) -> list[Student]:
        return self.__student_list

    def load_course_file(self, path: str) -> None:
        with open(path, "r") as crs_txt:
            lines = crs_txt.readlines()
            for line in range(0, len(lines), 4):
                ID = rm_all_ws(lines[line]).split(":")[1]
                name = rm_all_ws(lines[line + 1]).split(":")[1]
                credit = int(lines[line + 2].strip().split(":")[1])
                new_course = Course(ID, name, credit)
                self.__course_list.append(new_course)

    def load_student_file(self, path: str):
        with open(path, "r") as std_txt:
            lines = std_txt.readlines()
            for line in range(0, len(lines), 4):
                ID = rm_all_ws(lines[line]).split(":")[1]
                name = rm_all_ws(lines[line + 1]).split(":")[1]
                dob = rm_all_ws(lines[line + 2]).split(":")[1]
                new_student = Student(ID, name, dob)
                self.__student_list.append(new_student)

    def load_mark_file(self, path: str):
        with open(path, "r") as mk_txt:
            total_std = len(self.__student_list)
            lines = mk_txt.readlines()
            for line in range(0, len(lines), total_std + 2):
                course_name = rm_all_ws(lines[line]).split(":")[1]

                # find the course mentioned in the list
                course: Course
                for c in self.__course_list:
                    if course_name == c.get_name():
                        course = c
                        break

                for index in range(1, total_std + 1):
                    std_mark = int(rm_all_ws(lines[line + index]).split(":")[1])
                    course.set_marks_now(std_mark)

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
                print(
                    f"{COLORS.RED}You've typed in the wrong ID format.{COLORS.ENDC}\nThe ID should be BI/BAxx-xxx (x is from 0-9)\n")
                ID = input("Enter student's ID: ")
            else:
                break

        dob = input("The DOB should be dd/mm/yyyy\nEnter student DOB: ")
        while True:
            checker = re.search('[0-3][0-9]/[0-1][0-9]/[1-2][0-9[0-9][0-9]', dob)
            if checker is None:
                print(f"{COLORS.RED}You've typed in the wrong DOB format.{COLORS.ENDC}\nThe DOB should be dd/mm/yyyy\n")
                dob = input("Enter student's DOB: ")
            else:
                break

        new_student = Student(ID, name, dob)
        self.__student_list.append(new_student)

    def list_course(self) -> None:
        if self.__course_list:
            for course in self.__course_list:
                course.display_info()
        else:
            print(f"{COLORS.RED}No course found!{COLORS.ENDC}")

    def list_student(self) -> None:
        for student in self.__student_list:
            student.display_info()

    def choose_course(self) -> Course:
        """
        List all course name, then ask user to choose one
        :return: Course object if found
        """

        while True:
            print("Available course(s):", end=" ")
            for course in self.get_course_list():
                print(course.get_name(), end="  ")
            name = input("\nYour choice: ")

            for course in self.__course_list:
                if name == course.get_name():
                    return course
            print(f"{COLORS.RED}Course not found!{COLORS.ENDC}")

    def set_marks_course(self) -> None:
        """
        Set marks for a course and write to file
        """
        c = self.choose_course()

        for std in self.__student_list:
            f_mark = float(input(f"Set the score for student {std.get_name()}: "))
            i_mark = math.floor(f_mark)
            c.set_marks(i_mark)

        # write marks of course to file
        mark_file = open("marks.txt", "a")
        mark_file.write(f"Course: {c.get_name()}\n")
        for i, mark in enumerate(c.get_marks()):
            mark_file.write(f"\t{self.get_student_list()[i].get_name()}: {mark}\n")
        mark_file.write("\n")

    def display_marks_course(self) -> None:
        """
        Display marks of a course
        """
        c = self.choose_course()

        if c.get_marks():
            c.display_marks(self.get_student_list())
        else:  # no marks in course
            print(f"{COLORS.RED}You haven't put any marks in this course!{COLORS.ENDC}")

    # How the matrix should look like:
    #           std_1       std_2      std_3        std_4
    # course_1  10          15          8           7
    # course_2  14          12          15          13
    # course_3  16          13          12          18

    def calculate_gpa(self) -> None:
        row = len(self.__course_list)
        col = len(self.__student_list)
        matrix = np.zeros(shape=(row, col))
        credit_arr = []  # get credits of course into an array for easier working

        for i, course in enumerate(self.__course_list):
            credit_arr.append(course.get_credit())
            matrix[i] = course.get_marks()

        for column in range(0, col):
            std_mark = matrix[:, column]  # Get the mark of student [column]
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
