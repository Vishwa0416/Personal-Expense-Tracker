import pandas as pd
import matplotlib.pyplot as plt

def plot_expenses():
    try:
        df = pd.read_csv('data/expenses.csv')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        category_sum = df.groupby('category')['amount'].sum()

        category_sum.plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title("Expenses by Category")
        plt.ylabel('')
        plt.show()
    except FileNotFoundError:
        print("No expense data found.")
    except Exception as e:
        print(f"Error: {e}")
