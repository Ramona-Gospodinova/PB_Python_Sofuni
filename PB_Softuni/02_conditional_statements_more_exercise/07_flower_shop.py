import math

broi_magnolii = int(input())
broi_zumbuli = int(input())
broi_rozi = int(input())
broi_kaktusi = int(input())

cena_na_podaruka = float(input())

total_for_magnolii = broi_magnolii * 3.25
total_for_zumbuli = broi_zumbuli * 4.00
total_for_rozi = broi_rozi * 3.50
total_for_kaktusi = broi_kaktusi * 8.00

total_for_flowers = total_for_magnolii + total_for_zumbuli + total_for_rozi + total_for_kaktusi
danuci = total_for_flowers * 0.05

total_after_danuci = total_for_flowers - danuci

if total_after_danuci >= cena_na_podaruka:
    ostanali = math.floor(total_after_danuci - cena_na_podaruka)
    print(f'She is left with {ostanali} leva.')
else:
    ostanali = math.ceil(cena_na_podaruka - total_after_danuci)
    print(f'She will have to borrow {ostanali} leva.')