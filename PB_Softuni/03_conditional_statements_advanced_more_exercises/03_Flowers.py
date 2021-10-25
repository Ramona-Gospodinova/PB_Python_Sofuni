broi_hrizantemi = int(input())
broi_rozi = int(input())
broi_laleta = int(input())

season = input() #  Spring, Summer, Аutumn, Winter
is_holiday = input() #  [Y – да / N - не]

uvelichenie = 0
discount = 0
discount_laleta = 0
discount_rozi = 0
total_discount = 0
total_discount_for_count = 0
aranjirane_na_buket = 2

if season in ['Spring', 'Summer']:
    hrizantemi_unit_price = 2
    rozi_unit_price = 4.10
    laleta_unit_price = 2.50
else:
    hrizantemi_unit_price = 3.75
    rozi_unit_price = 4.50
    laleta_unit_price = 4.15

# Check for holiday
if is_holiday == "Y":
    uvelichenie = 0.15

total_hrizantemi_price = broi_hrizantemi * hrizantemi_unit_price
total_rozi_price = broi_rozi * rozi_unit_price
total_laleta_price = broi_laleta * laleta_unit_price

total_flowers_price = total_hrizantemi_price + total_rozi_price + total_laleta_price
total_flowers_price_with_uvelichenie = total_flowers_price + (total_flowers_price * uvelichenie)

if broi_laleta > 7 and season == "Spring":
    discount_laleta = 0.05
    total_discount += discount_laleta
elif broi_rozi >= 10 and season == "Winter":
    discount_rozi = 0.10
    total_discount += discount_rozi

total_flowers_price_after_discount_1 = total_flowers_price_with_uvelichenie - (total_flowers_price_with_uvelichenie * total_discount)

total_flowers_count = broi_rozi + broi_laleta + broi_hrizantemi
if total_flowers_count > 20:
    discount = 0.20
    total_discount_for_count = discount

total_flowers_price_after_discount_for_count = total_flowers_price_after_discount_1 - (total_flowers_price_after_discount_1 * total_discount_for_count)
total_flowers_price_with_uvelichenie_with_arange = total_flowers_price_after_discount_for_count + aranjirane_na_buket

# OUTPUT
print(f'{total_flowers_price_with_uvelichenie_with_arange:.2f}')
