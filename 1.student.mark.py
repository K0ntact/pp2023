def enter_student(students_list: list):
    num_student = int(input("\nEnter number of students: "))
    for i in range(num_student):
        student = {}
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_DOB = input("Enter DOB: ")
        student['id'] = student_id
        student['name'] = student_name
        student['dob'] = student_DOB
        students_list.append(student)

def enter_course(courses_list: list, students_list: list):
    num_course = int(input("\nEnter number of courses: "))
    for i in range(num_course):
        course = {
            'id': '',
            'name': '',
            'marks': {}
        }
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course['id'] = course_id
        course['name'] = course_name
        courses_list.append(course)

        print("\nEnter marks for students in {}".format(course['name']))
        for j in range(len(students_list)):
            mark = course['marks']
            std_id = students_list[j]['id']
            score = int(input("Enter mark for {}: ".format(std_id)))
            mark[std_id] = score

def show_students(student_list: list):
    for i in range(len(student_list)):
        std_id = student_list[i]['id']
        name = student_list[i]['name']
        dob = student_list[i]['dob']
        print("{} {} {}\n".format(std_id, name, dob))

def show_courses(course_list: list):
    for i in range(len(course_list)):
        course_id = course_list[i]['id']
        course_name = course_list[i]['name']
        print("{} {}\n".format(course_id, course_name))

def show_marks(course_list: list):
    choice = input("Which course do you want to see the marks: ")

    for i in range(len(course_list)):
        if choice == course_list[i]['name']:
            chosen = course_list[i]['marks']
            for key, value in chosen.items():
                print(key, ": ", value)


def main():
    student_list = []
    course_list = []

    enter_student(student_list)
    enter_course(course_list, student_list)

    choice = int(input("\n1. Show students   2. Show courses   3. Show marks   4.Exit\n"))
    while(True):
        match choice:
            case 1:
                show_students(student_list)
            case 2:
                show_courses(course_list)
            case 3:
                show_marks(course_list)
            case other:
                break
        choice = int(input("\n1. Show students   2. Show courses   3. Show marks   4.Exit\n"))

if __name__ == "__main__":
    main()