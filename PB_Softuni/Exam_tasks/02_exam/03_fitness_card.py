razpolagaema_suma = float(input())
pol = input()
age = int(input())
sport = input()

unit_price = 0
discount_percent = 0

if sport == 'Gym':
    if pol == 'f':
        unit_price = 35
    else:
        unit_price = 42
elif sport == 'Boxing':
    if pol == 'f':
        unit_price = 37
    else:
        unit_price = 41
elif sport == 'Yoga':
    if pol == 'f':
        unit_price = 42
    else:
        unit_price = 45
elif sport == 'Zumba':
    if pol == 'f':
        unit_price = 31
    else:
        unit_price = 34
elif sport == 'Dances':
    if pol == 'f':
        unit_price = 53
    else:
        unit_price = 51
elif sport == 'Pilates':
    if pol == 'f':
        unit_price = 37
    else:
        unit_price = 39

if age <= 19:
    discount_percent = 0.2
    unit_price = unit_price - (unit_price * discount_percent)

if razpolagaema_suma >= unit_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    money = unit_price - razpolagaema_suma
    print(f"You don't have enough money! You need ${money:.2f} more.")