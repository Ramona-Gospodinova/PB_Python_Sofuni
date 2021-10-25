# Inputs
# Цената на багаж над 20кг - реално число
bag_over_20 = float(input())

# Килограми на багажа – реално число
bag_weight_kg = float(input())

# Дни до пътуването – цяло число
days = int(input())

# Брой багажи – цяло число
bags_count = int(input())

# Init variables
bag_tax = 0
days_tax = 0

# Calculates taxes
if bag_weight_kg > 20:
    bag_tax = bag_over_20
elif bag_weight_kg < 10:
    bag_tax = 0.2 * bag_over_20
elif 10 <= bag_weight_kg <= 20:
    bag_tax = 0.5 * bag_over_20

# Calculate Цена на багаж
if days > 30:
    bag_tax += 0.1 * bag_tax
elif 7 <= days <= 30:
    bag_tax += 0.15 * bag_tax
elif days < 7:
    bag_tax += 0.40 * bag_tax

# Outputs
total_price_for_bags = bag_tax * bags_count
print(f'The total price of bags is: {total_price_for_bags:.2f} lv.')
