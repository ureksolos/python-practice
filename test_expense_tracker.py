from expense_tracker_v4 import format_expense, calculate_total

def test_calculate_total_empty():
    assert calculate_total([]) == 0
    
def test_calculate_total_single():
    assert calculate_total([{"desc" : "food", "amount" : 12.5}]) == 13
    

def test_calculate_total_multiple():
    expenses = [
        {"desc" : "food", "amount" : 5},
        {"desc" : "bills", "amount" : 12},
    ]
    assert calculate_total(expenses) == 17
    
def test_format_expense():
    assert format_expense(0, {"desc" : "food", "amount" : 21.3}) == "1. food - 21.30"