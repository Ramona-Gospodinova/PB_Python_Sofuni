import math

record_in_seconds = float(input())
razstoqnie_v_metri = float(input())
vreme_v_seconds_za_izkachvane_na_metar = float(input())

neobhodimo_vreme_za_izkachvane_seconds = vreme_v_seconds_za_izkachvane_na_metar * razstoqnie_v_metri
broi_zabavqniq = 0

if razstoqnie_v_metri >= 50:
    broi_zabavqniq = math.floor(razstoqnie_v_metri / 50)

dopulnitelno_neobhodimo_vreme = broi_zabavqniq * 30

obshto_neobhodimo_vreme = neobhodimo_vreme_za_izkachvane_seconds + dopulnitelno_neobhodimo_vreme

if obshto_neobhodimo_vreme < record_in_seconds:
    print(f"Yes! The new record is {obshto_neobhodimo_vreme:.2f} seconds.")
else:
    print(f"No! He was {obshto_neobhodimo_vreme-record_in_seconds:.2f} seconds slower.")