kapacitet_na_bagajnika = float(input())

svobodno_prostranstvo = kapacitet_na_bagajnika
broi_kufari = 0

while True:
    line = input()
    if line == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break

    obem_na_kufar = float(line)

    if broi_kufari > 0 and broi_kufari % 2 == 0:
        obem_na_kufar = (0.10 * obem_na_kufar) + obem_na_kufar

    if obem_na_kufar >= svobodno_prostranstvo or svobodno_prostranstvo == 0:
        print(f'No more space!')
        break

    svobodno_prostranstvo -= obem_na_kufar
    broi_kufari += 1

# Vinagi se otpechatva:
print(f'Statistic: {broi_kufari} suitcases loaded.')