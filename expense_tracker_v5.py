import json

def add_expense(expenses):
    expenses.append({"desc": input("Enter Description: "), "amount": float(input("Enter Amount: "))})
    print("Expense added successfully!")

def list_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        for i, e in enumerate(expenses):
            print(format_expense(i, e))

def show_total(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        print(f"sum: {calculate_total(expenses):.2f}")

def calculate_total(expenses):
    return sum(e["amount"] for e in expenses)

def format_expense(index, expense):
    return f"{index + 1}. {expense['desc']} - {expense['amount']:.2f}"


def load_expenses(filename="expenses.json"):
    try:
        # FIXED: Using the 'filename' parameter instead of hardcoding
        with open(filename, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' contains invalid JSON or is corrupted. Starting with a fresh list.")
        return []
    
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=2)

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1) Add")
        print("2) List")
        print("3) Total")
        print("4) Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            show_total(expenses)
        elif choice == '4':
            save_expenses(expenses)
            break
        else:
            print("WRONG INPUT DETECTED: INPUT VALUES BETWEEN 1-4!")

if __name__ == "__main__":
    main()