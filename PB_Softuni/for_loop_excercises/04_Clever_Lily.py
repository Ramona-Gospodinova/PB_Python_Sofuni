lily_age = int(input())
washing_mashine_price = float(input())
toy_unit_price = int(input())

toys_count = 0

money_for_birthday = 10
saved_money = 0
total_money = 0
money_for_toys = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        saved_money += money_for_birthday - 1
        money_for_birthday += 10
    else:
        toys_count += 1

money_for_toys = toys_count * toy_unit_price

total_money = money_for_toys + saved_money

if washing_mashine_price > total_money:
    n = washing_mashine_price - total_money
    print(f"No! {n:.2f}")
else:
    n = total_money - washing_mashine_price
    print(f"Yes! {n:.2f}")
