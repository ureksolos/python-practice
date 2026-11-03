import sqlite3
from expense_tracker_v5 import load_expenses, calculate_total

def test_load_empty_expenses(tmp_path):
    db_file = tmp_path / "test_expenses.db"
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, desc TEXT, amount REAL)")
        conn.commit()

    assert load_expenses(str(db_file)) == []

def test_calculate_total_with_db(tmp_path):
    # 1. Set up a temporary database file
    db_file = tmp_path / "test_expenses.db"
    
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                desc TEXT, 
                amount REAL
            )
        """)
        # 2. Insert some test rows
        # Note: columns are id (auto), desc (TEXT), amount (REAL)
        c.execute("INSERT INTO expenses (desc, amount) VALUES ('Coffee', 4.50)")
        c.execute("INSERT INTO expenses (desc, amount) VALUES ('Lunch', 12.00)")
        conn.commit()

    # 3. Load the expenses using your function
    loaded_items = load_expenses(str(db_file))
    # loaded_items will look like: [(1, 4.5), (2, 12.0)] based on your return tuple (item[0], item[2])

    # 4. Pass the loaded list into calculate_total
    total = calculate_total(loaded_items)

    # 5. Assert the result matches the expected sum (4.50 + 12.00 = 16.50)
    assert total == 16.50