days = int(input())
room_type = input()  # "room for one person", "apartment", "president apartment"
rating = input()  # "positive", "negative"

discount = 0
nights = days - 1

one_room_unit_price = 18
apartment_unit_price = 25
president_apartment_unit_price = 35

unit_price = 0
total_price_after_rating = 0

if nights > 15:
    if room_type == 'apartment':
        discount = 50
        unit_price = apartment_unit_price - (apartment_unit_price * 0.50)
    elif room_type == 'president apartment':
        discount = 20
        unit_price = president_apartment_unit_price - (president_apartment_unit_price * 0.20)
elif 10 <= nights <= 15:
    if room_type == 'apartment':
        discount = 35
        unit_price = apartment_unit_price - (apartment_unit_price * 0.35)
    elif room_type == 'president apartment':
        discount = 15
        unit_price = president_apartment_unit_price - (president_apartment_unit_price * 0.15)
elif nights < 10:
    if room_type == 'apartment':
        discount = 30
        unit_price = apartment_unit_price - (apartment_unit_price * 0.30)
    elif room_type == 'president apartment':
        discount = 10
        unit_price = president_apartment_unit_price - (president_apartment_unit_price * 0.10)

if room_type == 'room for one person':
    unit_price = 18

total_price_after_discount = nights * unit_price

if rating == 'positive':
    total_price_after_rating = total_price_after_discount + (total_price_after_discount * 0.25)
else:
    total_price_after_rating = total_price_after_discount - (total_price_after_discount * 0.10)

# OUTPUT
print(f'{total_price_after_rating:.2f}')