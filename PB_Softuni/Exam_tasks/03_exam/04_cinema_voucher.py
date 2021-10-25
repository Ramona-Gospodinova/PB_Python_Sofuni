stoinost_na_vaucher = int(input())

broi_bileti = 0
broi_drugi_pokupki = 0

while True:
    line = input()

    if line == 'End':
        break

    count_symbols = len(line)
    if count_symbols > 8:
        stoinost_na_tekusht_product = ord(line[0]) + ord(line[1])
        if stoinost_na_tekusht_product > stoinost_na_vaucher:
            break

        stoinost_na_vaucher -= stoinost_na_tekusht_product
        broi_bileti += 1
    elif count_symbols <= 8:
        stoinost_na_tekusht_product = ord(line[0])
        if stoinost_na_tekusht_product > stoinost_na_vaucher:
            break

        stoinost_na_vaucher -= stoinost_na_tekusht_product
        broi_drugi_pokupki += 1


print(broi_bileti)
print(broi_drugi_pokupki)
