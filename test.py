import random

name = ["Marshall Yoder", "Grover Miranda", "Myah Alvarado", "Luther Burgess", "Carol Davenport", "Gerald Hobbs", "Nora Bowman", "Kyan Boone", "Deacon Delacruz", "Ida Arnold", "Omer Payne", "Joshua Rogers", "Conrad Mccoy", "Tiago Skinner", "Filip Parks", "Leonie Landry", "Anton Savage", "Saskia Dennis", "Stephen Edwards", "Floyd Cross", "Eileen Mcgee", "Sophie Hess", "Millicent Whitney", "Cohen Stephenson", "Alejandro Richard", "Roman Chapman", "Lester Benton", "Angus Garner", "Greta Tucker", "Carl Martinez"]
ID = []
dob = []
course_1 = []
course_2 = []
course_3 = []
course_4 = []

for i in range(0, 30):
    iden = "BI12-0" + str(i)
    ID.append(iden)

    day = str(random.randint(0, 3)) + str(random.randint(0, 9))
    month = str(random.randint(0, 1)) + str(random.randint(0, 9))
    year = str(random.randint(1, 2)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    date_of_birth = day + "/" + month + "/" + year
    dob.append(date_of_birth)

    course_1.append(random.randint(1, 20))
    course_2.append(random.randint(1, 20))
    course_3.append(random.randint(1, 20))
    course_4.append(random.randint(1, 20))

def rand_std() -> list:
    rstd_lst = []
    for i in range(0,30):
        rstd = Student(random.choice(ID), random.choice(name), random.choice(dob))
        rstd_lst.append(rstd)
    return rstd_lst

c1 = Course("n1", "c1", 4)
c1.set_marks_TEST(course_1)

c2 = Course("n2", "c2", 2)
c2.set_marks_TEST(course_2)

c3 = Course("n3", "c3", 3)
c3.set_marks_TEST(course_3)

c4 = Course("n4", "c4", 4)
c4.set_marks_TEST(course_4)