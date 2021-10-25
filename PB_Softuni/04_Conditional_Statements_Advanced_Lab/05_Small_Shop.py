product = input()
city = input()
quantity = float(input())

unit_price = 0

if city == 'Sofia':
    if product == 'coffee':
        unit_price = 0.50
    elif product == 'water':
        unit_price = 0.80
    elif product == 'beer':
        unit_price = 1.20
    elif product == 'sweets':
        unit_price = 1.45
    elif product == 'peanuts':
        unit_price = 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        unit_price = 0.40
    elif product == 'water':
        unit_price = 0.70
    elif product == 'beer':
        unit_price = 1.15
    elif product == 'sweets':
        unit_price = 1.30
    elif product == 'peanuts':
        unit_price = 1.50
else:
    if product == 'coffee':
        unit_price = 0.45
    elif product == 'water':
        unit_price = 0.70
    elif product == 'beer':
        unit_price = 1.10
    elif product == 'sweets':
        unit_price = 1.35
    elif product == 'peanuts':
        unit_price = 1.55

print(quantity * unit_price)
