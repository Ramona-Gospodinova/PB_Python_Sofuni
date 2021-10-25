napitka = input()
zahar = input()
broi_napitki = int(input())

cena_napitka = 0
discount_napitka = 0

if napitka == 'Espresso':
    if zahar == 'Without':
        cena_napitka = 0.90
        cena_napitka -= cena_napitka * 0.35
    elif zahar == 'Normal':
        cena_napitka = 1.00
    else:
        cena_napitka = 1.20

    if broi_napitki >= 5:
        cena_napitka -= (cena_napitka * 0.25)
elif napitka == 'Cappuccino':
    if zahar == 'Without':
        cena_napitka = 1.00
        cena_napitka -= cena_napitka * 0.35
    elif zahar == 'Normal':
        cena_napitka = 1.20
    else:
        cena_napitka = 1.60
elif napitka == 'Tea':
    if zahar == 'Without':
        cena_napitka = 0.50
        cena_napitka -= cena_napitka * 0.35
    elif zahar == 'Normal':
        cena_napitka = 0.60
    else:
        cena_napitka = 0.70

total_napitka_sum = broi_napitki * cena_napitka
if total_napitka_sum > 15:
    total_napitka_sum = total_napitka_sum - (total_napitka_sum * 0.20)

print(f'You bought {broi_napitki} cups of {napitka} for {total_napitka_sum:.2f} lv.')