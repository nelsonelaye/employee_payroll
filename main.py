# This code calculates the total amount incurred on employee salary payments and bonuses

total_due = 0

employees = [
    {'name': "John Doe", 'role': "Developer", 'salary': 250, 'bonus': 0},
    {'name': "Peter Daniel", 'role': "Executive Vice President", 'salary': 620, 'bonus': 180},
    {'name': "Owen T", 'role': "Chief Financial Officer", 'salary': 350, 'bonus': 90}
]

for employee in employees:
    total_per_employee = employee['salary'] + employee['bonus']
    total_due += int(total_per_employee)
    print("{}, the {} gets paid a total of ${}".format(employee['name'], employee['role'], total_per_employee))

print("Total expense incurred on employee's compensation is ${}".format(total_due))
