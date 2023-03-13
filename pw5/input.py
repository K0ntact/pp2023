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
                ms.add_student()    # TEST: comment this to write test data immediately
                std_file = open("students.txt", "a")
                for std in ms.get_student_list():
                    std_file.write(f"ID: {std.get_ID()}\n")
                    std_file.write(f"   Name: {std.get_name()}\n")
                    std_file.write(f"   DOB: {std.get_dob()}\n\n")

            # Add a course
            case 2:
                ms.add_course()     # TEST: comment this to write test data immediately
                crs_file = open("courses.txt", "a")
                for crs in ms.get_course_list():
                    crs_file.write(f"ID: {crs.get_ID()}\n")
                    crs_file.write(f"   Name: {crs.get_name()}\n")
                    crs_file.write(f"   Credits: {crs.get_credit()}\n\n")

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
                    course.set_marks(ms.get_student_list())     # TEST: comment this to write test data immediately
                    # write marks of course to file
                    mark_file = open("marks.txt", "a")
                    mark_file.write(f"Course: {course.get_name()}\n")
                    for mark in course.get_marks():
                        index = course.get_marks().index(mark)
                        mark_file.write(f"      {ms.get_student_list()[index]}: {mark}\n")
                    mark_file.write("\n")
