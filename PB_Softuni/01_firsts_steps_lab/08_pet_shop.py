# --- Inputs ---
dog_pack_price = 2.50
cat_pack_price = 4

# --- Console reading ---
dog_pack = int(input())
cat_pack = int(input())

# CALCULATIONS
dog_total_pack_price = dog_pack * dog_pack_price
cat_total_pack_price = cat_pack * cat_pack_price
total_price = dog_total_pack_price + cat_total_pack_price

# --- Outputs ---
print(f'{total_price} lv.')
