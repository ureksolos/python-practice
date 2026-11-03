import sqlite3
from expense_tracker_v5 import load_expenses, calculate_total

def test_load_empty_expenses(tmp_path):
    db_file = tmp_path / "test_expenses.db"
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, desc TEXT, amount REAL)")
        conn.commit()

    assert load_expenses(str(db_file)) == []

def test_calculate_total(tmp_path):
    # 1. Create a temporary database file
    db_file = tmp_path / "test_expenses.db"
    
    # 2. Insert test data
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                desc TEXT, 
                amount REAL
            )
        """)
        c.execute("INSERT INTO expenses (desc, amount) VALUES ('Coffee', 4.50)")
        c.execute("INSERT INTO expenses (desc, amount) VALUES ('Lunch', 12.00)")
        conn.commit()

    # 3. Call calculate_total passing the temporary database path
    total = calculate_total(str(db_file))

    # 4. Assert the total is correct (4.50 + 12.00 = 16.50)
    assert total == 16.50