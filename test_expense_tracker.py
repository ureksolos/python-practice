from expense_tracker_v4 import calculate_total, format_expense

def test_calculate_total_empty():
    assert calculate_total([]) == 0

def test_calculate_total_single():
    assert calculate_total([{"desc" : "food", "amount" : 12.5}]) == 12.5

def test_calculate_total_multiple():
    expenses = [
        {"desc": "food", "amount" : 10.0},
        {"desc": "bus", "amount" : 5.5},
    ]
    assert calculate_total(expenses) == 15.5

def test_format_expense():
    assert format_expense(0, {"desc" : "food", "amount" : 12.5}) == "1. food - 12.50"

