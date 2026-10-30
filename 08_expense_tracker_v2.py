def add_expense(expenses):
    expenses.append({"desc" : input("Enter description: "), "amount": float(input("Enter Amount: "))})

def list_expenses(expenses):
    if expenses == []:
        print("No expenses yet")
    else:
        count = 1
        for e in expenses:
            print(f"{count}. {e["desc"]} - {e["amount"]:.2f}")
            count = count + 1

def show_total(expenses):
    if expenses == []:
        print("No expenses yet.")
    else:
        total = 0
        for e in expenses:
            total = total + e["amount"]
    print(f"Total = {total:.2f}")


def main():
    expenses = []
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1) Add")
        print("2) List")
        print("3) Total")
        print("4) Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
            continue
        elif choice == '2':
            list_expenses(expenses)
            continue
        elif choice == '3':
            show_total(expenses)
            continue
        elif choice == '4':
            expenses = []
            break
        else:
            print("WRONG INPUT DETECTED: INPUT VALUES BEWTEEN 1-4!")
            continue

if __name__ == "__main__":
    main()