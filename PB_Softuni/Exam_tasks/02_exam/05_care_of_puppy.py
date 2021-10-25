zakupeno_kolichestvo_hrana_kg = int(input())
zakupeno_kolichestvo_hrana_g = zakupeno_kolichestvo_hrana_kg * 1000

obshto_izqdena_hrana_predi_osinovqvaneto_g = 0

izqdena_hrana = input()

while izqdena_hrana != 'Adopted':
    if izqdena_hrana == 'Adopted':
        break

    obshto_izqdena_hrana_predi_osinovqvaneto_g += int(izqdena_hrana)

    izqdena_hrana = input()

if obshto_izqdena_hrana_predi_osinovqvaneto_g <= zakupeno_kolichestvo_hrana_g:
    ostanala_hrana = zakupeno_kolichestvo_hrana_g - obshto_izqdena_hrana_predi_osinovqvaneto_g
    print(f'Food is enough! Leftovers: {ostanala_hrana} grams.')
else:
    nujno_kolichestvo_hrana = obshto_izqdena_hrana_predi_osinovqvaneto_g - zakupeno_kolichestvo_hrana_g
    print(f'Food is not enough. You need {nujno_kolichestvo_hrana} grams more.')