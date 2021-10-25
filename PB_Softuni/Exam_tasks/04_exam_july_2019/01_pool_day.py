# Inputs
import math

broi_hora = int(input())
taksa_vhod = float(input())
cena_shezlong = float(input())
cena_edin_chadur = float(input())

broi_hora_percent = math.ceil(0.75 * broi_hora)
total_shezlongi_price = broi_hora_percent * cena_shezlong

total_chadur_count = (broi_hora // 2) + (broi_hora % 2)
total_chaduri_price = total_chadur_count * cena_edin_chadur

total_taksa_vhod = broi_hora * taksa_vhod

total_razhodi = total_shezlongi_price + total_chaduri_price + total_taksa_vhod
print(f'{total_razhodi:.2f} lv.')