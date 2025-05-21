import csv
from models.expense import Expense

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    exp = Expense(amount, category, date, description)
    
    with open('data/expenses.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date', 'description'])
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
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    menu()
