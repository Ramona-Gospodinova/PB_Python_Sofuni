import math

broi_dni = int(input())
ostavena_hrana_v_kg = int(input())
food_for_dog_a_day_v_kg = float(input())
food_for_cat_a_day_v_kg = float(input())
food_for_kostenurka_a_day_v_g = float(input())

need_food_for_dog_kg = broi_dni * food_for_dog_a_day_v_kg
need_food_for_cat_kg = broi_dni * food_for_cat_a_day_v_kg
need_food_for_kostenurka_kg = broi_dni * (food_for_kostenurka_a_day_v_g/1000)

total_need_food_kg = need_food_for_dog_kg + need_food_for_cat_kg + need_food_for_kostenurka_kg

if ostavena_hrana_v_kg >= total_need_food_kg:
    kg_rest = ostavena_hrana_v_kg - total_need_food_kg
    print(f'{math.floor(kg_rest)} kilos of food left.')
else:
    kg_nedostigat = total_need_food_kg - ostavena_hrana_v_kg
    print(f'{math.ceil(kg_nedostigat)} more kilos of food are needed.')