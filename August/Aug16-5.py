work_hours = [int(x) for x in input("Enter weekly working hours: ").split()]
hourly_wages = int(input("Enter hourly wages: "))

weekly_working_hours = sum(work_hours)       #independent global function to find sum

salary = weekly_working_hours * hourly_wages
print("This week's salary is Rs.", salary)