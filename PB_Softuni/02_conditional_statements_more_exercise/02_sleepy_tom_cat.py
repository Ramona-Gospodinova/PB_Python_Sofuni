broi_pochivni_dni = int(input())
broi_rabotni_dni = 365 - broi_pochivni_dni

vreme_za_igra = (broi_rabotni_dni * 63) + (broi_pochivni_dni * 127)

h = 0
m = 0

razlika_ot_norma = 30000 - vreme_za_igra
if razlika_ot_norma < 0:
    razlika_ot_norma = abs(razlika_ot_norma)
    if razlika_ot_norma >= 60:
        h = razlika_ot_norma // 60
        m = razlika_ot_norma % 60
    else:
        m = razlika_ot_norma
    print(f'Tom will run away')
    print(f'{h} hours and {m} minutes more for play')
else:
    razlika_ot_norma = abs(razlika_ot_norma)
    if razlika_ot_norma >= 60:
        h = razlika_ot_norma // 60
        m = razlika_ot_norma % 60
    else:
        m = razlika_ot_norma
    print(f'Tom sleeps well')
    print(f'{h} hours and {m} minutes less for play')