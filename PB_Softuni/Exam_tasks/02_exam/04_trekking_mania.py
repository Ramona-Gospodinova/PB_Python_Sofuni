broi_grupi = int(input())

musala_broi_katerachi = 0
monblan_broi_katerachi = 0
kilimandjaro_broi_katerachi = 0
k2_broi_katerachi = 0
everest_broi_katerachi = 0

obsht_broi_katerachi = 0

for i in range(broi_grupi):
    broi_hora_v_grupata = int(input())
    obsht_broi_katerachi += broi_hora_v_grupata

    if broi_hora_v_grupata <= 5:
        musala_broi_katerachi += broi_hora_v_grupata
    elif 6 <= broi_hora_v_grupata <= 12:
        monblan_broi_katerachi += broi_hora_v_grupata
    elif 13 <= broi_hora_v_grupata <= 25:
        kilimandjaro_broi_katerachi += broi_hora_v_grupata
    elif 26 <= broi_hora_v_grupata <= 40:
        k2_broi_katerachi += broi_hora_v_grupata
    else:
        everest_broi_katerachi += broi_hora_v_grupata

musala_procent_hora = (musala_broi_katerachi / obsht_broi_katerachi) * 100
monblan_procent_hora = (monblan_broi_katerachi / obsht_broi_katerachi) * 100
kilimandjaro_procent_hora = (kilimandjaro_broi_katerachi / obsht_broi_katerachi) * 100
k2_procent_hora = (k2_broi_katerachi / obsht_broi_katerachi) * 100
everest_procent_hora = (everest_broi_katerachi / obsht_broi_katerachi) * 100

print(f'{musala_procent_hora:.2f}%')
print(f'{monblan_procent_hora:.2f}%')
print(f'{kilimandjaro_procent_hora:.2f}%')
print(f'{k2_procent_hora:.2f}%')
print(f'{everest_procent_hora:.2f}%')
