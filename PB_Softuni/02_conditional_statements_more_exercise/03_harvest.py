import math

plosht_loze_kv_m = int(input())
grozde_za_kv_m = float(input())
nujni_litri_vino = int(input())
broi_rabotnici = int(input())

plosht_zadelena_za_proizvodstvo_na_vino = 0.40 * plosht_loze_kv_m
proizvedeno_kolichestvo_grozde = plosht_zadelena_za_proizvodstvo_na_vino * grozde_za_kv_m
proizvedeno_kolichestvo_vino_litri = proizvedeno_kolichestvo_grozde / 2.5

if proizvedeno_kolichestvo_vino_litri < nujni_litri_vino:
    nedostigashto_vino = nujni_litri_vino - proizvedeno_kolichestvo_vino_litri
    print(f'It will be a tough winter! More {math.floor(nedostigashto_vino)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(proizvedeno_kolichestvo_vino_litri)} liters.')

if proizvedeno_kolichestvo_vino_litri >= nujni_litri_vino:
    ostavashto_vino = proizvedeno_kolichestvo_vino_litri - nujni_litri_vino
    vino_za_edin_rabotnik = ostavashto_vino / broi_rabotnici
    print(f'{math.ceil(ostavashto_vino)} liters left -> {math.ceil(vino_za_edin_rabotnik)} liters per person.')