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


def calculate_daily_wage(attendance, category):
    wage_per_hour = 20
    present_days = attendance.count('Present')
    total_wage = 0
    for i in range(present_days):
        if category[i] == "Permanent":
            total_daily_hours = 8
            total_wage = total_wage + (wage_per_hour * total_daily_hours)
        elif category[i] == "PartTime":
            total_daily_hours = 4
            total_wage = total_wage + (wage_per_hour * total_daily_hours)
        return total_wage, present_days


class EmployeeWages:
    def __init__(self, name):
        self.name = name

    def show_data(self):
        print("Name : ", self.name)
        attendance, category, working_days, hours_worked = employee_wage()
        total_wages, present_days = calculate_daily_wage(attendance, category)
        total_wages = hours_worked*20
        print("Salary for {} days = {}".format(present_days, total_wages))
        print("Employee {} was present for {} out of {} working days for {} hours.".format(self.name, present_days,
                                                                                           working_days,
                                                                                           hours_worked))


if __name__ == '__main__':
    employee1 = EmployeeWages('Pavan')
    employee1.show_data()
