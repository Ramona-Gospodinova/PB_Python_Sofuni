broi_himikali = int(input())
broi_markeri = int(input())
litri_preparat = int(input())
discount_percent = int(input())

cena_na_paket_himikali = 5.80
cena_na_paket_markeri = 7.20
cena_na_litur_preparat = 1.20

discount_percent_value = discount_percent / 100

total_price_without_discount = broi_himikali*cena_na_paket_himikali + broi_markeri*cena_na_paket_markeri + litri_preparat*cena_na_litur_preparat
total_price_with_discount = total_price_without_discount - (discount_percent_value * total_price_without_discount)

print(total_price_with_discount)