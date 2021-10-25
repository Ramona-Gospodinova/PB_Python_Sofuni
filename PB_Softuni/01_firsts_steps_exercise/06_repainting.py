kolichestvo_nailon_kv_m = int(input())
kolichestvo_boq_litri = int(input())
kolichestvo_razreditel_za_boq_litri = int(input())
work_time_hours = int(input())

cena_nailon_za_kv_m = 1.50
cena_boq_za_litar = 14.50
cena_razreditel_za_boq_za_litar = 5
cena_torbichki = 0.4

# TOTALS:
total_kolichestvo_boq_litri = kolichestvo_boq_litri + (0.1 * kolichestvo_boq_litri)
total_kolichestvo_nailon_kv_m = kolichestvo_nailon_kv_m + 2

total_price_nailon = cena_nailon_za_kv_m * total_kolichestvo_nailon_kv_m
total_price_boq = cena_boq_za_litar * total_kolichestvo_boq_litri
total_price_razreditel = cena_razreditel_za_boq_za_litar * kolichestvo_razreditel_za_boq_litri

total_price_materiali = total_price_nailon + total_price_boq + total_price_razreditel + cena_torbichki
price_for_maistori_for_hour = 0.3 * total_price_materiali
total_price_maistori = price_for_maistori_for_hour * work_time_hours

total_razhodi = total_price_materiali + total_price_maistori

print(total_razhodi)