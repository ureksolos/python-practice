bill = float(input("Enter Bill: "))
tip_percent = float(input("Enter tip %: "))
people = int (input("Enter number of persons: "))

tip = bill * (tip_percent / 100)
total = bill + tip
per_person = total / people

print (f"Tip: ${tip:.2f}")
print (f"Total: ${total:.2f}")
print (f"Per-person: ${per_person:.2f}")