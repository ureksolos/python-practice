import json


def add_expense(expenses):
    expenses.append({"desc": input("Enter Description: "), "amount": float(input("Enter Amount: "))})

def list_expenses(expenses):
    if expenses == []:
        print("No expenses yet.")
    else:
        index = 1
        for e in expenses:
            print(f"{index}. {e["desc"]} - {e["amount"]:.2f}")
            index = index + 1

def print_total(expenses):
    if expenses == []:
        print("No expenses yet.")
    else:
        total = 0
        for e in expenses:
            total = total + e["amount"]
        print(f"sum: {total:.2f}")

def load_expenses(filename = "expenses.json"):
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"file, '{filename}' does not exist, starting with fresh list.")
        return []

def save_expenses(expenses, filename = "expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f , indent = 2)


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
            print_total(expenses)
        elif choice == '4':
            save_expenses(expenses)
            break

if __name__ == "__main__":
    main()