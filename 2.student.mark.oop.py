# courses_list will contain all instances of class Course:
#   courses_list = [ads, oop, nm]
#
# Class Course will contain everything from the info of the course
# to the students info and their marks.
#
# Each Student instance will contain the student info and stored in __std_list:
#     __std_list = [std1, std2, std3]
#
# Student score will be stored in __marks as a dictionary with 2 keys: "name" and "mark"
#     __marks = [
#         {
#             "name": "Student 1",
#             "mark": 15
#         },
#         {
#             "name": "Student 2",
#             "mark": 13
#         },
#         {
#             "name": "Student 3",
#             "mark": 18
#         }
#     ]
import re


class Student:
    def __init__(self, Id: str, name: str, dob: str):
        self.__id = Id
        self.__name = name
        self.__dob = dob

    def getID(self) -> str:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getDob(self) -> str:
        return self.__dob

    def setID(self, iD: str) -> None:
        self.__id = iD

    def setName(self, name: str) -> None:
        self.__name = name

    def setDob(self, dob: str) -> None:
        self.__dob = dob


class Course:
    def __init__(self, Id: str, name: str):
        self.__id = Id
        self.__name = name
        self.__marks = []
        self.__std_list = []

    def getID(self) -> str:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def setID(self, iD: str) -> None:
        self.__id = iD

    def setName(self, name: str) -> None:
        self.__name = name

    def addStudent(self) -> None:
        name = input("Enter student's name: ")

        Id = input("The ID should be BI/BAxx-xxx (x is from 0-9)\nEnter student id: ")
        while True:
            checker = re.search('(BI|BA)[0-9][0-9]-[0-9][0-9][0-9]', Id)
            if checker is None:
                print("You've typed in the wrong ID format.\nThe ID should be BI/BAxx-xxx (x is from 0-9)\n")
                Id = input("Enter student's id: ")
            else:
                break

        dob = input("The DOB should be dd/mm/yyyy\nEnter student DOB: ")
        while True:
            checker = re.search("[0-3][0-9]/[0-1][0-2]/[1-2][0-9[0-9][0-9]", dob)
            if checker is None:
                print("You've typed in the wrong DOB format.\nThe DOB should be dd/mm/yyyy\n")
                Id = input("Enter student's id: ")
            else:
                break

        std = Student(Id, name, dob)
        self.__std_list.append(std)

    def setScore(self) -> None:
        temp = {}
        for std in self.__std_list:
            mark = int(input(f"Enter mark for student {std.getName()}: "))
            temp["name"] = std.getName()
            temp["mark"] = mark
            self.__marks.append(temp)

    def showScore(self) -> None:
        mark_list = self.__marks
        for std in mark_list:
            name = std["name"]
            score = std["mark"]
            print(f"{name} : {score}")


def main():
    courses_list = []
    while True:
        print("\n1. Add course\n2. Add student\n3. Set score\n 4.Show score\n---------\n0. Exit\n")
        choice = int(input("Enter your choice: "))
        # Check if the choice is correct
        while True:
            try:
                if choice in range(0, 5):
                    break
            except:
                print("Invalid choice!")
            print("\n\n1. Enter course\n2. Enter student\n3. Set score\n 4. Show score\n---------\n0. Exit\n")
            choice = int(input("Enter your choice: "))

        match choice:
            # Exit the program
            case 0:
                print("Program terminated!")
                break

            # Enter course info
            case 1:
                name = input("Enter course's name: ")
                Id = input("Enter course's id: ")
                crs = Course(Id, name)
                courses_list.append(crs)

            # Enter student info for a course
            case 2:
                if len(courses_list) == 0:
                    print("No courses found! Please enter a course!\n")

                else:
                    print("Available courses: ")
                    for c in courses_list:
                        print(c.getName() + " ")
                    name = input("Choose the course: ")

                    found = False
                    while not found:
                        for c in courses_list:
                            if name == c.getName():
                                found = True
                                c.addStudent()

                        if not found:
                            print("\nCourse name not found! Check that you enter the right name!")
                            name = input("Choose the course: ")

            # Set the marks for the students
            case 3:
                print("Available courses: ")
                for c in courses_list:
                    print(c.getName() + " ")
                name = input("Choose the course: ")

                found = False
                while not found:
                    for c in courses_list:
                        if name == c.getName():
                            found = True
                            c.setScore()

                    if not found:
                        print("\nCourse name not found! Check that you enter the right name!")
                        name = input("Choose the course: ")

            # Show scores of a course
            case 4:
                name = input("Choose the course: ")
                print("Available courses: ")
                for c in courses_list:
                    print(c.getName() + " ")

                found = False
                while not found:
                    for c in courses_list:
                        if name == c.getName():
                            found = True
                            c.showScore()
                            break

                    if not found:
                        print("\nCourse name not found! Check that you enter the right name!")
                        name = input("Choose the course: ")


if __name__ == "__main__":
    main()
