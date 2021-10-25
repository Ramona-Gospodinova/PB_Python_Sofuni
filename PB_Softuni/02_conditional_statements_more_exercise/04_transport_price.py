n_km = int(input())
type = input()

price_for_km = 0
start_price = 0

if n_km < 20:
    if type == 'day':
        price_for_km = 0.79
    elif type == 'night':
        price_for_km = 0.90
    start_price = 0.70
elif 20 <= n_km < 100:
    price_for_km = 0.09
elif n_km >= 100:
    price_for_km = 0.06

total_price = (n_km * price_for_km) + start_price

print(f'{total_price:.2f}')