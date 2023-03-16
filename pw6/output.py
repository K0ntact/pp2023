from domains.marksheet import MarkSheet
from domains.colors import COLORS


def Output(ms: MarkSheet):
    while True:
        print("\nPrint Info")
        print("-"*20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] List all student")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] List all course")
        print(f"[{COLORS.YELLOW}3{COLORS.ENDC}] Show student marks in a course")
        print(f"[{COLORS.YELLOW}4{COLORS.ENDC}] Sort student by GPA")
        print("-"*20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Back to main menu")
        choice = int(input("Your choice: "))
        match choice:
            # Exit
            case 0:
                break

            # List all students
            case 1:
                ms.list_student()

            # List all courses
            case 2:
                ms.list_course()

            # Show all student marks in a course
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

                    if course.get_marks():  # there are marks in course
                        course.display_marks(ms.get_student_list())
                        break
                    else:   # no marks in course
                        print(f"{COLORS.RED}You haven't put any marks in this course!{COLORS.ENDC}")
                        break

            case 4:
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