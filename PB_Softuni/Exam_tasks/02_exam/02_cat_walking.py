minuti_razhodka_na_den = int(input())
broi_razhodki_dnevno = int(input())
prieti_kalorii_dnevno = int(input())

izrazhodvani_halorii_za_minuti_na_den = minuti_razhodka_na_den * 5
izrazhodvani_halorii_za_minuti_za_vsichki_razhodki = broi_razhodki_dnevno * izrazhodvani_halorii_za_minuti_na_den

polovin_kalorii_dnevno = 0.5 * prieti_kalorii_dnevno

if izrazhodvani_halorii_za_minuti_za_vsichki_razhodki >= polovin_kalorii_dnevno:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {izrazhodvani_halorii_za_minuti_za_vsichki_razhodki}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {izrazhodvani_halorii_za_minuti_za_vsichki_razhodki}.")