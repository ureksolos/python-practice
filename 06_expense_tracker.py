expenses = []
total = 0

while True:
    print("\n--- Expense Tracker Menu ---")
    print("1) Add")
    print("2) List")
    print("3) Total")
    print("4) Quit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
       expenses.append({"desc": input("Enter Description: "), "Amount": float(input("Enter Amount: "))})
       continue
    elif choice == '2':
        if expenses == []:
            print("No expenses yet")
        else:
            count = 1
            for e in expenses:
                print(f"{count}.", e["desc"], "-",  e["Amount"])
                count = count + 1
                continue
        
    elif choice == '3':
        for e in expenses:
            total = total + e["Amount"]
        print (total)
        continue
    elif choice == '4':
        expenses = []
        total = 0
        break


        
