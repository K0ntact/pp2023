from domains.marksheet import MarkSheet
from domains.colors import COLORS


def Input(ms: MarkSheet):
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

                for course in ms.get_course_list():
                    if name != course.get_name():
                        print(f"{COLORS.RED}Course not found!{COLORS.ENDC}")
                        break

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

                for course in ms.get_course_list():
                    if name != course.get_name():
                        print(f"{COLORS.RED}Course not found!{COLORS.ENDC}")
                        break

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
