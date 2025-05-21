import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pandas as pd

from models.expense import Expense
from utils.visualizer import show_chart

CSV_FILE = "data/expenses.csv"
HEADERS = ['amount', 'category', 'date', 'description']

# Ensure CSV exists
os.makedirs("data", exist_ok=True)
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()

# Save new expense
def save_expense():
    amount = amount_var.get()
    category = category_var.get()
    if category == "Other":
     category = other_category_var.get().strip()
     if not category:
        messagebox.showerror("Input Error", "Please enter a custom category.")
        return

    date = date_var.get()
    description = description_text.get("1.0", "end-1c").strip()

    if not all([amount, category, date, description]):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    exp = Expense(amount, category, date, description)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(exp.to_dict())

    messagebox.showinfo("Saved", "Expense added successfully!")
    clear_fields()
    load_expenses()

#Load categories
def load_categories():
    try:
        with open("data/categories.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Load to table
def load_expenses():
    for row in tree.get_children():
        tree.delete(row)
    try:
        df = pd.read_csv(CSV_FILE)
        for _, row in df.iterrows():
            tree.insert('', 'end', values=list(row))
    except Exception as e:
        print(f"Error: {e}")

def clear_fields():
    amount_var.set("")
    category_var.set("")
    date_var.set("")
    description_text.delete("1.0", tk.END)

# GUI
root = tk.Tk()
root.title("💸 Expense Tracker")
root.geometry("700x600")

# Form
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(fill=tk.X)

amount_var = tk.StringVar()
category_var = tk.StringVar()
date_var = tk.StringVar()
description_var = tk.StringVar()

tk.Label(form_frame, text="Amount:").grid(row=0, column=0, sticky='e')
tk.Entry(form_frame, textvariable=amount_var).grid(row=0, column=1)

tk.Label(form_frame, text="Category:").grid(row=1, column=0, sticky='e')
categories = load_categories()
category_dropdown = ttk.Combobox(form_frame, textvariable=category_var, values=categories + ["Other"])
category_dropdown.grid(row=1, column=1)

# Custom category field for "Other"
other_category_var = tk.StringVar()
other_category_entry = tk.Entry(form_frame, textvariable=other_category_var)

tk.Label(form_frame, text="Date:").grid(row=2, column=0, sticky='e')
DateEntry(form_frame, textvariable=date_var, date_pattern='yyyy-mm-dd').grid(row=2, column=1)

tk.Label(form_frame, text="Description:").grid(row=3, column=0, sticky='ne')
description_text = tk.Text(form_frame, height=4, width=40, wrap='word')
description_text.grid(row=3, column=1, columnspan=3, sticky='w')

tk.Button(form_frame, text="Add Expense", command=save_expense).grid(row=4, columnspan=2, pady=10)

# Table
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = HEADERS
tree = ttk.Treeview(table_frame, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col.title())
    tree.column(col, width=100)
tree.pack(fill=tk.BOTH, expand=True)

# Chart Button
tk.Button(root, text="📊 Show Pie Chart", command=show_chart).pack(pady=10)

# Category handling
def handle_category_change(event):
    if category_var.get() == "Other":
        tk.Label(form_frame, text="Custom Category:").grid(row=1, column=2, padx=5)
        other_category_entry.grid(row=1, column=3)
    else:
        other_category_entry.grid_forget()

category_dropdown.bind("<<ComboboxSelected>>", handle_category_change)

load_expenses()
root.mainloop()
