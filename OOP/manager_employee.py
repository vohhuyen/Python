import hashlib
from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, emp_id, name, age, position, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
        self.attendance = {} 
        self.performance = [] 

    def check_in(self):
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        
        if current_date not in self.attendance:
            self.attendance[current_date] = []
        
        self.attendance[current_date].append(current_time)
        print(f"{self.name} checked in at {current_time} on {current_date}")

    def add_performance(self, performance_score):
        self.performance.append(performance_score)
        print(f"Performance of {self.name}: {performance_score}")

    def calculate_salary(self):
        total_salary = self.salary
        total_attendance = sum(len(times) for times in self.attendance.values())
        total_salary += total_attendance * 100
        print(f"Salary of {self.name}: {total_salary}")
        return total_salary

    def view_attendance(self, date):
        if date in self.attendance:
            times = self.attendance[date]
            print(f"Check-in times for {self.name} on {date}: {', '.join(map(str, times))}")
        else:
            print(f"No check-ins for {self.name} on {date}.")

    def __str__(self):
        return f"ID: {self.emp_id}, {super().__str__()}, Position: {self.position}, Base Salary: {self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, age, position, salary):
        try:
            if emp_id in self.employees:
                raise ValueError("Employee already exists!")
            if age < 0:
                raise ValueError("Age cannot be negative.")
            if salary < 0:
                raise ValueError("Salary cannot be negative.")

            self.employees[emp_id] = Employee(emp_id, name, age, position, salary)
            print(f"Added employee {name}")

        except ValueError as e:
            print(f"Error adding employee: {e}")

    def update_employee(self, emp_id, name=None, age=None, position=None, salary=None):
        if emp_id in self.employees:
            if name:
                self.employees[emp_id].name = name
            if age:
                self.employees[emp_id].age = age
            if position:
                self.employees[emp_id].position = position
            if salary:
                self.employees[emp_id].salary = salary
            print(f"Updated information for employee {emp_id}")
        else:
            print("Employee does not exist!")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Deleted employee {emp_id}")
        else:
            print("Employee does not exist!")

    def view_all_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            for emp in self.employees.values():
                print(emp)

    def employee_check_in(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].check_in()
        else:
            print("Employee does not exist!")

    def employee_add_performance(self, emp_id, score):
        if emp_id in self.employees:
            self.employees[emp_id].add_performance(score)
        else:
            print("Employee does not exist!")

    def calculate_employee_salary(self, emp_id):
        if emp_id in self.employees:
            return self.employees[emp_id].calculate_salary()
        else:
            print("Employee does not exist!")

    def view_employee_attendance(self, emp_id, date):
        if emp_id in self.employees:
            self.employees[emp_id].view_attendance(date)
        else:
            print("Employee does not exist!")

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            print("User already exists!")
        else:
            self.users[username] = hashlib.sha256(password.encode()).hexdigest()
            print("Registration successful!")

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username] == hashed_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect username or password!")
            return False

def main():
    user_manager = UserManager()
    emp_manager = EmployeeManager()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.login(username, password):
                while True:
                    print("\n--- Employee Management ---")
                    print("1. Add Employee")
                    print("2. Update Employee")
                    print("3. Delete Employee")
                    print("4. View All Employees")
                    print("5. Check In")
                    print("6. Add Performance")
                    print("7. Calculate Salary")
                    print("8. View Attendance by Date")
                    print("9. Logout")
                    emp_choice = input("Choice: ")

                    if emp_choice == '1':
                        emp_id = input("Enter Employee ID: ")
                        name = input("Enter Employee Name: ")
                        age = int(input("Enter Age: "))
                        position = input("Enter Position: ")
                        salary = float(input("Enter Base Salary: "))
                        emp_manager.add_employee(emp_id, name, age, position, salary)

                    elif emp_choice == '2':
                        emp_id = input("Enter Employee ID to update: ")
                        name = input("Enter new name (press Enter to skip): ")
                        age = input("Enter new age (press Enter to skip): ")
                        position = input("Enter new position (press Enter to skip): ")
                        salary = input("Enter new salary (press Enter to skip): ")
                        age = int(age) if age else None
                        salary = float(salary) if salary else None
                        emp_manager.update_employee(emp_id, name, age, position, salary)

                    elif emp_choice == '3':
                        emp_id = input("Enter Employee ID to delete: ")
                        emp_manager.delete_employee(emp_id)

                    elif emp_choice == '4':
                        emp_manager.view_all_employees()

                    elif emp_choice == '5':
                        emp_id = input("Enter Employee ID to check in: ")
                        emp_manager.employee_check_in(emp_id)

                    elif emp_choice == '6':
                        emp_id = input("Enter Employee ID: ")
                        score = float(input("Enter performance score: "))
                        emp_manager.employee_add_performance(emp_id, score)

                    elif emp_choice == '7':
                        emp_id = input("Enter Employee ID: ")
                        emp_manager.calculate_employee_salary(emp_id)

                    elif emp_choice == '8':
                        emp_id = input("Enter Employee ID to view attendance: ")
                        date_str = input("Enter date (YYYY-MM-DD): ")
                        date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        emp_manager.view_employee_attendance(emp_id, date)

                    elif emp_choice == '9':
                        print("Logged out.")
                        break

        elif choice == '3':
            print("Exiting the program.")
            break

if __name__ == '__main__':
    main()

