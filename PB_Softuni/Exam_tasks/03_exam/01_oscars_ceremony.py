naem_na_zala = int(input())

statuetki = naem_na_zala - (0.30 * naem_na_zala)
keturing = statuetki - (0.15 * statuetki)
ozvuchavane = keturing / 2

obsho_razhodi = naem_na_zala + statuetki + keturing + ozvuchavane

print(f'{obsho_razhodi:.2f}')
