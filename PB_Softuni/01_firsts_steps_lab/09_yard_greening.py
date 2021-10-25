# Inputs
price_meter_vat = 7.61
discount = 0.18
area = float(input())

# Calculations
total_area_price = area  * 7.61
area_discount_price = total_area_price * discount
total_area_price_with_discount = total_area_price - (total_area_price * discount)

# Outputs
print(f'The final price is: {total_area_price_with_discount} lv.')
print(f'The discount is: {area_discount_price} lv.')
