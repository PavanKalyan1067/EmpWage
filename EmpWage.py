import random


def employee_wage():

    attendance = []

    if random.randrange(0, 2) == 0:
        attendance.append('Absent')
        print("Employee is Absent")
    else:
        attendance.append('Present')
        print("Employee is Present")


employee_wage()
