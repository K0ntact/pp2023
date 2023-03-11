# Class Info is the parent of class Student and class Course, has 2 basic attributes: ID and name
# Class Student is inherited from Info and has 1 more attribute: DOB
# Class Course is inherited from Info
# Class MarkSheet will contain instances of class Course and class Student.
#
# Each Student instance will be stored in __student_list:
#     __student_list = [std1, std2, std3]
#
# Each Course instance will be stored in __class_list:
#     __course_list = [course 1, course 2, course 3]

import re


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

    def get_dob(self) -> str: return self.__dob

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"DOB: {self.__dob}")
        print("\n")


class Course(Info):
    def __init__(self, ID: str, name: str) -> None:
        super().__init__(ID, name)
        self.__marks = []

    def get_marks(self) -> list: return self.__marks

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print("\n")

    def display_marks(self, std_list: list) -> None:
        for std in std_list:
            std_pos = std_list.index(std)
            print(f"{std.get_name()}: {self.__marks[std_pos]}")

    def set_marks(self, std_list: list) -> None:
        for std in std_list:
            mark = int(input(f"Set the score for student {std.get_name()}: "))
            self.__marks.append(mark)


class MarkSheet:
    def __init__(self):
        self.__student_list = []
        self.__course_list = []

    def get_course_list(self) -> list: return self.__course_list
    def get_student_list(self) -> list: return self.__student_list

    def add_course(self) -> None:
        name = input("Enter course name: ")
        ID = input("Enter course ID: ")
        new_course = Course(ID, name)
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
                    else:   # no marks in course
                        print(f"{COLORS.RED}You haven't put any marks in this course!{COLORS.ENDC}")
                        break


if __name__ == "__main__":
    main()