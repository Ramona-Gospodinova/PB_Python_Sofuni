jelana_pechalba = float(input())
subrana_suma = 0

while True:
    coctail_name = input()
    if coctail_name == 'Party!':
        break

    broi_coctails = int(input())
    coctail_price = len(coctail_name)

    cena_na_porucka = broi_coctails * coctail_price
    if cena_na_porucka % 2 == 1:
        cena_na_porucka -= cena_na_porucka * 0.25

    subrana_suma += cena_na_porucka

    if subrana_suma >= jelana_pechalba:
        break

if subrana_suma < jelana_pechalba:
    nedostigashta_suma = jelana_pechalba - subrana_suma
    print(f'We need {nedostigashta_suma:.2f} leva more.')
else:
    print(f'Target acquired.')

print(f'Club income - {subrana_suma:.2f} leva.')