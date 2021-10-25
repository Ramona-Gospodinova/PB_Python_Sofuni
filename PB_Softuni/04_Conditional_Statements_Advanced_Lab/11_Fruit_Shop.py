fruit = input()
day_of_week = input()
quantity = float(input())

fruit_unit_price = 0

fruits = ["banana", "apple", "orange", "kiwi", "cherry", "lemon", "grapefruit", "pineapple", "grapes"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

valid = True

if fruit in fruits and day_of_week in working_days:
    if fruit == "banana":
        fruit_unit_price = 2.50
    elif fruit == "apple":
        fruit_unit_price = 1.20
    elif fruit == "orange":
        fruit_unit_price = 0.85
    elif fruit == "grapefruit":
        fruit_unit_price = 1.45
    elif fruit == "kiwi":
        fruit_unit_price = 2.70
    elif fruit == "pineapple":
        fruit_unit_price = 5.50
    elif fruit == "grapes":
        fruit_unit_price = 3.85
elif fruit in fruits and day_of_week in weekends:
    if fruit == "banana":
        fruit_unit_price = 2.70
    elif fruit == "apple":
        fruit_unit_price = 1.25
    elif fruit == "orange":
        fruit_unit_price = 0.90
    elif fruit == "grapefruit":
        fruit_unit_price = 1.60
    elif fruit == "kiwi":
        fruit_unit_price = 3.00
    elif fruit == "pineapple":
        fruit_unit_price = 5.60
    elif fruit == "grapes":
        fruit_unit_price = 4.20
else:
    valid = False
    print('error')

if valid:
    total_price = fruit_unit_price * quantity
    print(f'{total_price:.2f}')

