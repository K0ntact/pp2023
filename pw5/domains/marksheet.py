from .colors import COLORS
from .course import Course
from .student import Student
import re
import numpy as np

# GENERATE DATA FOR TEST

# import random
# name = ["Marshall Yoder", "Grover Miranda", "Myah Alvarado", "Luther Burgess", "Carol Davenport", "Gerald Hobbs",
#         "Nora Bowman", "Kyan Boone", "Deacon Delacruz", "Ida Arnold", "Omer Payne", "Joshua Rogers", "Conrad Mccoy",
#         "Tiago Skinner", "Filip Parks", "Leonie Landry", "Anton Savage", "Saskia Dennis", "Stephen Edwards",
#         "Floyd Cross", "Eileen Mcgee", "Sophie Hess", "Millicent Whitney", "Cohen Stephenson", "Alejandro Richard",
#         "Roman Chapman", "Lester Benton", "Angus Garner", "Greta Tucker", "Carl Martinez"]
# ID = []
# dob = []
# course_1 = []
# course_2 = []
# course_3 = []
# course_4 = []
#
# for i in range(0, 30):
#     iden = "BI12-0" + str(i)
#     ID.append(iden)
#
#     day = str(random.randint(0, 3)) + str(random.randint(0, 9))
#     month = str(random.randint(0, 1)) + str(random.randint(0, 9))
#     year = str(random.randint(1, 2)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
#     date_of_birth = day + "/" + month + "/" + year
#     dob.append(date_of_birth)
#
#     course_1.append(random.randint(1, 20))
#     course_2.append(random.randint(1, 20))
#     course_3.append(random.randint(1, 20))
#     course_4.append(random.randint(1, 20))
#
#
# def rand_std() -> list[Student]:
#     rstd_lst = []
#     for j in range(0, 30):
#         rstd = Student(random.choice(ID), name[j], random.choice(dob))
#         rstd_lst.append(rstd)
#     return rstd_lst
#
#
# c1 = Course("n1", "c1", 4)
# c1.set_marks_TEST(course_1)
#
# c2 = Course("n2", "c2", 2)
# c2.set_marks_TEST(course_2)
#
# c3 = Course("n3", "c3", 3)
# c3.set_marks_TEST(course_3)
#
# c4 = Course("n4", "c4", 4)
# c4.set_marks_TEST(course_4)

def rm_all_ws(text: str) -> str:
    return "".join(text.split())

class MarkSheet:
    def __init__(self):
        self.__student_list: list[Student] = []    # TEST: replace [] with rand_std()
        self.__course_list: list[Course] = []       # TEST: replace [] with [c1, c2, c3, c4]

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
        credit_arr = []  # get credits of course into an array for easier working

        i = 0
        for course in self.__course_list:
            credit_arr.append(course.get_credit())
            matrix[i] = course.get_marks()
            i += 1

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
