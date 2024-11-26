import sqlite3

def create_db():
    conn = sqlite3.connect('post_office.db')
    cursor = conn.cursor()

    # Create Customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )''')

    # Create Transactions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        transaction_type TEXT,
        date TEXT,
        amount REAL,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )''')

    conn.commit()
    conn.close()

create_db()
