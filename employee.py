class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda x: x.age)
    elif key == 2:
        return sorted(employees, key=lambda x: x.name)
    elif key == 3:
        return sorted(employees, key=lambda x: x.salary)
    else:
        return employees

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table")
    print("Empid\tName\tAge\tSalary (PM)")
    for employee in employees:
        print(employee)

    try:
        sorting_option = int(input("Choose the sorting parameter (1. Age, 2. Name, 3. Salary): "))
        sorted_employees = sort_employees(employees, sorting_option)

        print("\nSorted Employee Table")
        print("Empid\tName\tAge\tSalary (PM)")
        for employee in sorted_employees:
            print(employee)
    except ValueError:
        print("Invalid input. Please enter a valid sorting option (1, 2, or 3).")

if __name__ == "__main__":
    main()
