expense = {"desc": "food", "amount": 12.5}
print(expense["desc"])          # 'food'
# print(expense.get("desc"))      # None — no crash
print(expense["desc"])          # KeyError — crashes