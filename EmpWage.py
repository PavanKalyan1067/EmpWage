import random


def employee_wage():
    attendance = []
    wage_per_hour = 20
    hours_per_day = 8

    if random.randrange(0, 2) == 0:
        attendance.append('Absent')
        print("Employee is Absent")
    else:
        attendance.append('Present')
        print("Employee is Present and wage per day is :")
        print(wage_per_hour * hours_per_day)


if __name__ == '__main__':
    employee_wage()
