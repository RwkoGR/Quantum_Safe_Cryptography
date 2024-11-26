import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

def execute_query(query, params=()):
    conn = sqlite3.connect('post_office.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Add Customer
def add_customer():
    name = entry_name.get()
    address = entry_address.get()
    if name and address:
        execute_query('INSERT INTO customers (name, address) VALUES (?, ?)', (name, address))
        messagebox.showinfo("Success", "Customer added successfully.")
    else:
        messagebox.showwarning("Input Error", "Please fill out both fields.")

# View Customers
def view_customers():
    conn = sqlite3.connect('post_office.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    
    if customers:
        text_output.delete(1.0, tk.END)
        for customer in customers:
            text_output.insert(tk.END, f"ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}\n")
    else:
        messagebox.showinfo("No Data", "No customers found.")

# Add Transaction
def add_transaction():
    customer_id = entry_customer_id.get()
    transaction_type = entry_transaction_type.get()
    amount = entry_amount.get()
    
    if customer_id and transaction_type and amount:
        try:
            amount = float(amount)
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            execute_query('INSERT INTO transactions (customer_id, transaction_type, date, amount) VALUES (?, ?, ?, ?)',
                          (customer_id, transaction_type, date, amount))
            messagebox.showinfo("Success", "Transaction recorded successfully.")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid amount.")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# View Transactions
def view_transactions():
    conn = sqlite3.connect('post_office.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()

    if transactions:
        text_output.delete(1.0, tk.END)
        for transaction in transactions:
            text_output.insert(tk.END, f"ID: {transaction[0]}, Customer ID: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}, Amount: {transaction[4]:.2f}\n")
    else:
        messagebox.showinfo("No Data", "No transactions found.")

# Create the main window
root = tk.Tk()
root.title("Post Office Management System")

# Set window size and background color
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Add Customer Section
frame_add_customer = tk.LabelFrame(root, text="Add Customer", padx=10, pady=10, bg="#d9e1f2", font=("Helvetica", 12))
frame_add_customer.grid(row=0, column=0, padx=20, pady=10)

label_name = tk.Label(frame_add_customer, text="Name", font=("Helvetica", 10), bg="#d9e1f2")
label_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_add_customer, font=("Helvetica", 10), width=25)
entry_name.grid(row=0, column=1)

label_address = tk.Label(frame_add_customer, text="Address", font=("Helvetica", 10), bg="#d9e1f2")
label_address.grid(row=1, column=0, sticky="w")
entry_address = tk.Entry(frame_add_customer, font=("Helvetica", 10), width=25)
entry_address.grid(row=1, column=1)

button_add_customer = tk.Button(frame_add_customer, text="Add Customer", command=add_customer, bg="#4CAF50", fg="white", font=("Helvetica", 10), relief="flat", padx=10, pady=5)
button_add_customer.grid(row=2, columnspan=2, pady=10)

# View Customers Section
button_view_customers = tk.Button(root, text="View Customers", command=view_customers, bg="#007BFF", fg="white", font=("Helvetica", 10), relief="flat", padx=10, pady=5)
button_view_customers.grid(row=1, column=0, pady=10)

# View Transactions Section
button_view_transactions = tk.Button(root, text="View Transactions", command=view_transactions, bg="#007BFF", fg="white", font=("Helvetica", 10), relief="flat", padx=10, pady=5)
button_view_transactions.grid(row=1, column=1, pady=10)

# Text Output Section
text_output = tk.Text(root, width=70, height=15, font=("Helvetica", 10))
text_output.grid(row=2, column=0, columnspan=2, pady=10)

# Add Transaction Section
frame_add_transaction = tk.LabelFrame(root, text="Add Transaction", padx=10, pady=10, bg="#d9e1f2", font=("Helvetica", 12))
frame_add_transaction.grid(row=0, column=2, padx=20, pady=10)

label_customer_id = tk.Label(frame_add_transaction, text="Customer ID", font=("Helvetica", 10), bg="#d9e1f2")
label_customer_id.grid(row=0, column=0, sticky="w")
entry_customer_id = tk.Entry(frame_add_transaction, font=("Helvetica", 10), width=25)
entry_customer_id.grid(row=0, column=1)

label_transaction_type = tk.Label(frame_add_transaction, text="Transaction Type", font=("Helvetica", 10), bg="#d9e1f2")
label_transaction_type.grid(row=1, column=0, sticky="w")
entry_transaction_type = tk.Entry(frame_add_transaction, font=("Helvetica", 10), width=25)
entry_transaction_type.grid(row=1, column=1)

label_amount = tk.Label(frame_add_transaction, text="Amount", font=("Helvetica", 10), bg="#d9e1f2")
label_amount.grid(row=2, column=0, sticky="w")
entry_amount = tk.Entry(frame_add_transaction, font=("Helvetica", 10), width=25)
entry_amount.grid(row=2, column=1)

button_add_transaction = tk.Button(frame_add_transaction, text="Add Transaction", command=add_transaction, bg="#4CAF50", fg="white", font=("Helvetica", 10), relief="flat", padx=10, pady=5)
button_add_transaction.grid(row=3, columnspan=2, pady=10)

root.mainloop()
