days_count = int(input())
foods = float(input())

biscuits_total = 0
dog_food_total = 0
cat_food_total = 0

for i in range(1, days_count+1):
    dog_food = int(input())
    cat_food = int(input())

    izqdena_hrana_za_denq = dog_food + cat_food

    dog_food_total += dog_food
    cat_food_total += cat_food

    if i % 3 == 0:
        biscuits_total += 0.10 * izqdena_hrana_za_denq

obshto_izqdena_hrana = dog_food_total + cat_food_total
obshto_izqdena_hrana_percent = (obshto_izqdena_hrana / foods) * 100

obshto_izqdena_hrana_dog = (dog_food_total / obshto_izqdena_hrana) * 100
obshto_izqdena_hrana_cat = (cat_food_total / obshto_izqdena_hrana) * 100

print(f'Total eaten biscuits: {int(biscuits_total)}gr.')
print(f'{obshto_izqdena_hrana_percent:.2f}% of the food has been eaten.')
print(f'{obshto_izqdena_hrana_dog:.2f}% eaten from the dog.')
print(f'{obshto_izqdena_hrana_cat:.2f}% eaten from the cat.')
