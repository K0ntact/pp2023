from marksheet import MarkSheet
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
        choice = input("Your choice: ")
        match choice:
            # Exit
            case "0":
                break

            # Add a student
            case "1":
                ms.add_student()
                std_file = open("students.txt", "a")

                std = ms.get_student_list()[-1]
                std_file.write(f"ID: {std.get_ID()}\n")
                std_file.write(f"\tName: {std.get_name()}\n")
                std_file.write(f"\tDOB: {std.get_dob()}\n\n")

            # Add a course
            case "2":
                ms.add_course()
                crs_file = open("courses.txt", "a")

                crs = ms.get_course_list()[-1]
                crs_file.write(f"ID: {crs.get_ID()}\n")
                crs_file.write(f"\tName: {crs.get_name()}\n")
                crs_file.write(f"\tCredits: {crs.get_credit()}\n\n")

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