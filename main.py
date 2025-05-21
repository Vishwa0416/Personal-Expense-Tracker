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
