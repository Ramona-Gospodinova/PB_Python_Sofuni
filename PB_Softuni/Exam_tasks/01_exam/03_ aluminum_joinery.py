# Inputs
aluminum_count = int(input())
aluminum_type = input()
delivery = input()

discount = 0
discount_for_99 = 0
unit_price = 0
delivery_tax = 0

if delivery == 'With delivery':
    delivery_tax = 60

if aluminum_type == '90X130':
    unit_price = 110
    if 30 < aluminum_count < 60:
        discount = 0.05
    elif aluminum_count > 60:
        discount = 0.08
elif aluminum_type == '100X150':
    unit_price = 140
    if 40 < aluminum_count < 80:
        discount = 0.06
    elif aluminum_count > 80:
        discount = 0.10
elif aluminum_type == '130X180':
    unit_price = 190
    if 20 < aluminum_count < 50:
        discount = 0.07
    elif aluminum_count > 50:
        discount = 0.12
elif aluminum_type == '200X300':
    unit_price = 250
    if 25 < aluminum_count < 50:
        discount = 0.09
    elif aluminum_count > 50:
        discount = 0.14

aluminum_price = aluminum_count * unit_price
aluminum_price_with_discount = aluminum_price - (aluminum_price * discount)

aluminum_price_with_discount_and_delivery = aluminum_price_with_discount + delivery_tax

if aluminum_count > 99:
    aluminum_price_with_discount_and_delivery = aluminum_price_with_discount_and_delivery - (aluminum_price_with_discount_and_delivery * 0.04)

if aluminum_count < 10:
    print('Invalid order')
else:
    print(f'{aluminum_price_with_discount_and_delivery:.2f} BGN')
