import random


def employee_wage():
    attendance = []
    category = []
    hours_worked = 0
    days = 0
    while True:
        days += 1
        if random.randrange(0, 2) == 0:
            attendance.append('Absent')
        else:
            attendance.append('Present')
            if random.randrange(0, 2) == 0:
                category.append("FullTime")
                hours_worked += 8
                print(attendance[days - 1], "FullTime", days, hours_worked)
            else:
                category.append("PartTime")
                hours_worked += 4
                print(attendance[days - 1], "PartTime", days, hours_worked)

        if days == 20 or hours_worked == 100:
            print("Month complete")
            return attendance, category, days, hours_worked


if __name__ == '__main__':
    employee_wage()
