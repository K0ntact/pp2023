from pw6.marksheet import MarkSheet
from domains.colors import COLORS
import pickle


def Input(ms: MarkSheet):
    while True:
        print("\nAdd Info")
        print("-"*20)
        print(f"[{COLORS.YELLOW}1{COLORS.ENDC}] Add a student")
        print(f"[{COLORS.YELLOW}2{COLORS.ENDC}] Add a course")
        print(f"[{COLORS.YELLOW}3{COLORS.ENDC}] Input marks for a course")
        print("-"*20)
        print(f"[{COLORS.YELLOW}0{COLORS.ENDC}] Back to main menu")
        choice = input("Your choice: ")
        match choice:
            # Exit
            case "0":
                break

            # Add a student
            case "1":
                ms.add_student()
                std_file = open("students.pickle", "ab")

                std = ms.get_student_list()[-1]
                pickle.dump(std, std_file)

            # Add a course
            case "2":
                ms.add_course()
                crs_file = open("courses.pickle", "ab")

                crs = ms.get_course_list()[-1]
                pickle.dump(crs, crs_file)

            # Input marks for a course
            case "3":
                if len(ms.get_course_list()) == 0:
                    print(f"{COLORS.RED}You have to add a course first!{COLORS.ENDC}")
                    continue

                if len(ms.get_student_list()) == 0:
                    print(f"{COLORS.RED}You have to add a student first!{COLORS.ENDC}")
                    continue

                ms.set_marks_course()

            # Invalid choice
            case _:
                print(f"{COLORS.RED}Invalid choice!{COLORS.ENDC}")
