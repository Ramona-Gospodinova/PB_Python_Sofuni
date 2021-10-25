budget = float(input())
broi_noshtuvki = int(input())
cena_za_noshtuvka = float(input())
percent_dopulnitelni_razhodi = int(input())

if broi_noshtuvki > 7:
    cena_za_noshtuvka = cena_za_noshtuvka - (0.05 * cena_za_noshtuvka)

dopulnitelni_razhodi_amount = (percent_dopulnitelni_razhodi / 100) * budget
total_cena_za_noshtuvki = broi_noshtuvki * cena_za_noshtuvka

total_razhodi = total_cena_za_noshtuvki + dopulnitelni_razhodi_amount

# Outputs
if budget >= total_razhodi:
    rest_leva = budget - total_razhodi
    print(f'Ivanovi will be left with {rest_leva:.2f} leva after vacation.')
else:
    nead_money = total_razhodi - budget
    print(f'{nead_money:.2f} leva needed.')