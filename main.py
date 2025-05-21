import os
import csv
from models.expense import Expense

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    exp = Expense(amount, category, date, description)

    file_path = 'data/expenses.csv'
    file_exists = os.path.exists(file_path)
    write_header = not file_exists or os.stat(file_path).st_size == 0

    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date', 'description'])
        if write_header:
            writer.writeheader()
        writer.writerow(exp.to_dict())

    print("✅ Expense added!")


if __name__ == '__main__':
    add_expense()

def view_expenses():
    try:
        with open('data/expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Chart")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            from utils.visualizer import plot_expenses
            plot_expenses()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    menu()
