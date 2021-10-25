fruit = input()
set_size = input()
count_of_sets = int(input())

price_for_set = 0
discount_percents = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        price_for_set = 2 * 56
    if set_size == 'big':
        price_for_set = 5 * 28.70

if fruit == 'Mango':
    if set_size == 'small':
        price_for_set = 2 * 36.66
    if set_size == 'big':
        price_for_set = 5 * 19.60

if fruit == 'Pineapple':
    if set_size == 'small':
        price_for_set = 2 * 42.10
    if set_size == 'big':
        price_for_set = 5 * 24.80

if fruit == 'Raspberry':
    if set_size == 'small':
        price_for_set = 2 * 20
    if set_size == 'big':
        price_for_set = 5 * 15.20

obshta_suma = count_of_sets * price_for_set

if 400 <= obshta_suma <= 1000:
    discount_percents = 15
if obshta_suma > 1000:
    discount_percents = 50

result = obshta_suma - (obshta_suma * discount_percents/100)

print(f'{result:.2f} lv.')
