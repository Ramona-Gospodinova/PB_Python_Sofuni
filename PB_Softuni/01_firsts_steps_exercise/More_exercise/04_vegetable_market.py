vegetable_price = float(input())
fruits_price = float(input())
vegetable_kg = int(input())
fruits_kg = int(input())

total_vegetable_price_bgn = vegetable_price * vegetable_kg
total_vegetable_price_eur = total_vegetable_price_bgn / 1.94

total_fruits_price_bgn = fruits_price * fruits_kg
total_fruits_price_eur = total_fruits_price_bgn / 1.94

total_price_eur = total_vegetable_price_eur + total_fruits_price_eur
print(f'{total_price_eur:.2f}')
