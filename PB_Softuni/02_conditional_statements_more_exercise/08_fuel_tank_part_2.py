type_gorivo = input()  # "Gas", "Gasoline" или "Diesel"
kolichestvo_gorivo = float(input())
club_card = input()  # "Yes" или "No"

discount_for_card = 0
discount_for_kolichestvo = 0

unit_price = 0

if club_card == "Yes":
    if type_gorivo == "Gas":
        unit_price = 0.93 - 0.08
    elif type_gorivo == "Gasoline":
        unit_price = 2.22 - 0.18
    else:
        unit_price = 2.33 - 0.12
else:
    if type_gorivo == "Gas":
        unit_price = 0.93
    elif type_gorivo == "Gasoline":
        unit_price = 2.22
    else:
        unit_price = 2.33

if 20 <= kolichestvo_gorivo <= 25:
    discount_for_kolichestvo = 0.08
elif kolichestvo_gorivo > 25:
    discount_for_kolichestvo = 0.10

total_price = (kolichestvo_gorivo * unit_price)
total_price_after_discount_for_kolichestvo = total_price - (total_price * discount_for_kolichestvo)

# OUTPUTS
print(f'{total_price_after_discount_for_kolichestvo:.2f} lv.')