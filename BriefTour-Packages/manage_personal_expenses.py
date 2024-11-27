import os
import zipfile
import logging
from timeit import default_timer as timer
from datetime import datetime

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

def input_salary():
    """Input the monthly salary from the user."""
    while True:
        try:
            salary = float(input("Please enter your monthly salary: "))
            if salary < 0:
                raise ValueError("Salary must be a non-negative number.")
            return salary
        except ValueError as e:
            logging.error(f"Error: {e}. Please enter a valid number!")

def input_expenses():
    """Input expenses from the user."""
    expenses = {}
    while True:
        category = input("Enter the expense category (or press Enter to finish): ")
        if category == "":
            break
        while True:
            try:
                amount = float(input(f"Enter the amount for {category}: "))
                if amount < 0:
                    raise ValueError("Expense must be a non-negative number.")
                expenses[category] = amount
                break
            except ValueError as e:
                logging.error(f"Error: {e}. Please enter a valid amount!")
    return expenses

def write_expenses_to_file(salary, expenses, total_expenses):
    """Write salary and expenses to a file."""
    with open("expenses.txt", "w") as f:
        f.write(f"Salary: {salary}\n")
        f.write("Expenses:\n")
        for category, amount in expenses.items():
            f.write(f"- {category}: {amount}\n")
        f.write(f"Total expenses: {total_expenses}\n")

def compress_expense_file():
    """Compress the expense file into a zip file."""
    with zipfile.ZipFile('expenses.zip', 'w') as zipf:
        zipf.write('expenses.txt')

def main():
    # Start timing the execution
    start_time = timer()

    # 1. Input the monthly salary
    salary = input_salary()

    # 2. Input expenses
    expenses = input_expenses()

    # Calculate total expenses
    total_expenses = sum(expenses.values())

    # 3. Write expenses to a file
    write_expenses_to_file(salary, expenses, total_expenses)

    # 4. Calculate and print the remaining money
    remaining_money = salary - total_expenses
    print(f"Remaining money after expenses: {remaining_money}")

    # 5. Compress the expense file
    compress_expense_file()

    # 6. Print execution time and current time
    end_time = timer()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(f"Current time: {datetime.now()}")

if __name__ == "__main__":
    main()
