year_tax_amount = int(input())

basketbolni_kecove = year_tax_amount - (0.4 * year_tax_amount)
basketbolni_ekip = basketbolni_kecove - (0.2 * basketbolni_kecove)
basketbolni_topka = basketbolni_ekip / 4
basketbolni_aksesoari = basketbolni_topka / 5

total_razhodi = year_tax_amount + basketbolni_kecove + basketbolni_ekip + basketbolni_topka + basketbolni_aksesoari

print(total_razhodi)