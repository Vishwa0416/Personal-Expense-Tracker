import pandas as pd
import matplotlib.pyplot as plt

def plot_expenses():
    df = pd.read_csv('data/expenses.csv')
    category_sum = df.groupby('category')['amount'].sum()

    category_sum.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Expenses by Category")
    plt.ylabel('')
    plt.show()
