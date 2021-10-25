city_name = input()
packet_type = input()
vip_discount = input()

days = int(input())
days_valid = True
pack_valid = True
valid_day_input = True
day_price = 0

if city_name == 'Bansko' or city_name == 'Borovets':
    if vip_discount == 'yes':
        if packet_type == 'withEquipment':
            day_price = 100 - (100 * 0.10)
        elif packet_type == 'noEquipment':
            day_price = 80 - (80 * 0.05)
        else:
            pack_valid = False
    else:
        if packet_type == 'withEquipment':
            day_price = 100
        elif packet_type == 'noEquipment':
            day_price = 80
        else:
            pack_valid = False
elif city_name == 'Varna' or city_name == 'Burgas':
    if vip_discount == 'yes':
        if packet_type == 'withBreakfast':
            day_price = 130 - (130 * 0.12)
        elif packet_type == 'noBreakfast':
            day_price = 100 - (100 * 0.07)
        else:
            pack_valid = False
    else:
        if packet_type == 'withEquipment':
            day_price = 130
        elif packet_type == 'noBreakfast':
            day_price = 100
        else:
            pack_valid = False
else:
    valid_day_input = False

if days > 7:
    days = days - 1

# Output
if days <= 0:
    days_valid = False
    print(f'Days must be positive number!')

if not valid_day_input or not pack_valid:
    print(f'Invalid input!')

if days_valid and valid_day_input and days_valid and pack_valid:
    total_price_for_days = day_price * days
    print(f'The price is {total_price_for_days:.2f}lv! Have a nice time!')