budget = int(input())
season = input()  #  "Spring", "Summer", "Autumn" или "Winter";
count_fishers = int(input())

rent_unit_price = 0
discount = 0
discount_2 = 0

if season == "Spring":
    rent_unit_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_unit_price = 4200
elif season == "Winter":
    rent_unit_price = 2600

if count_fishers <= 6:
    discount = 10
elif 7 <= count_fishers <= 11:
    discount = 15
elif count_fishers >= 12:
    discount = 25

total_after_discount1 = rent_unit_price - (rent_unit_price * discount / 100)

if season != "Autumn" and count_fishers % 2 == 0:
    discount_2 = 5

total_after_discount2 = total_after_discount1 - (total_after_discount1 * discount_2 / 100)

if budget >= total_after_discount2:
    print(f'Yes! You have {budget - total_after_discount2:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_after_discount2 - budget:.2f} leva.')


