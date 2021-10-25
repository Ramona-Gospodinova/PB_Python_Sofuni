budget_za_filma = float(input())
broi_statisti = int(input())
cena_za_obleklo_na_edin_statist = float(input())

decore = 0.10 * budget_za_filma

if broi_statisti > 150:
    cena_za_obleklo_na_edin_statist = cena_za_obleklo_na_edin_statist - (0.10 * cena_za_obleklo_na_edin_statist)

cena_za_obleklo_total = broi_statisti * cena_za_obleklo_na_edin_statist

decore_obleklo_total = decore + cena_za_obleklo_total

if decore_obleklo_total > budget_za_filma:
    need_money = decore_obleklo_total - budget_za_filma
    print('Not enough money!')
    print(f'Wingard needs {need_money:.2f} leva more.')
else:
    ostanali_pari = budget_za_filma - decore_obleklo_total
    print('Action!')
    print(f'Wingard starts filming with {ostanali_pari:.2f} leva left.')
