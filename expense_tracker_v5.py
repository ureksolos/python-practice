import sqlite3

def create_table():
    comm = sqlite3.connect('expenses.db')
    c = comm.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS expenses
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        desc TEXT NOT NULL,
        amount REAL NOT NULL
        )
        """)

    comm.commit()
    comm.close()

def add_expense():
    comm = sqlite3.connect('expenses.db')
    c = comm.cursor()

    desc = input("Enter Description: ")
    amount = input("Enter Amount: ")

    c.execute("INSERT INTO expenses (desc, amount) VALUES (?, ?)", (desc, amount))

    comm.commit()
    comm.close()

def list_expenses():
    comm = sqlite3.connect('expenses.db')
    c = comm.cursor()

    c.execute("SELECT desc, amount FROM expenses")

    items = c.fetchall()

    if len(items) < 1:
        print("No expenses yet.")
    else:
        for item in items:
            print(format_expense(item[0], item[1]))

def calculate_total(filename='expenses.db'):
    # Pass the filename into load_expenses so it reads from the correct database
    expenses = load_expenses(filename)
    
    # Sum up the amounts (assuming amount is at index 1 of the tuple)
    return sum(amount for _, amount in expenses)


def show_total():
    comm = sqlite3.connect('expenses.db')
    c = comm.cursor()

    c.execute("SELECT amount FROM expenses")

    items = c.fetchall()

    if len(items) == 0:
        print("No expenses yet.")
    else:
        print(f"sum: {calculate_total():.2f}")

def format_expense(desc, amount):
    return f"{desc} - {amount}"

def load_expenses(filename='expenses.db'):
    comm = sqlite3.connect(filename)
    try:
        c = comm.cursor()
        c.execute("SELECT * FROM expenses")
        items = c.fetchall()
        
        if not items:
            return []
        return [(item[0], item[2]) for item in items]
    finally:
        comm.close()

def delete_expense(expense_id, filename='expenses.db'):
    with sqlite3.connect(filename) as comm:
        c = comm.cursor()
        c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        comm.commit()

def main():
    create_table()
    load_expenses()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1) Add")
        print("2) List")
        print("3) Total")
        print("4) Quit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
            print("Expense added successfully!")
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()