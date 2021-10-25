juniors_count = int(input())
seniors_count = int(input())
road = input()  #  "trail", "cross-country", "downhill" или "road"

junior_unit_price = 0
senior_unit_price = 0
discount = 0

if road == "trail":
    junior_unit_price = 5.50
    senior_unit_price = 7
elif road == "cross-country":
    junior_unit_price = 8
    senior_unit_price = 9.50
elif road == "downhill":
    junior_unit_price = 12.25
    senior_unit_price = 13.75
elif road == "road":
    junior_unit_price = 20
    senior_unit_price = 21.50

juniors_total_price = juniors_count * junior_unit_price
senior_total_price = seniors_count * senior_unit_price

total_price = juniors_total_price + senior_total_price

total_bikers = juniors_count + seniors_count
if road == "cross-country" and total_bikers >= 50:
    discount = 0.25

total_after_discount = total_price - (total_price * discount)
total_after_outcomes = total_after_discount - (total_after_discount * 0.05)

print(f'{total_after_outcomes:.2f}')
