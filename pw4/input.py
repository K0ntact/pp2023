from domains.marksheet import MarkSheet
from domains.colors import COLORS


def Input(ms: MarkSheet):
    while True:
        print("\nAdd Info")
        print("-"*20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] Add a student")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] Add a course")
        print(f"[{COLORS.YELLOW}3{COLORS.ENDC}] Input marks for a course")
        print("-"*20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Back to main menu")
        choice = int(input("Your choice: "))
        match choice:
            # Exit
            case 0:
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
