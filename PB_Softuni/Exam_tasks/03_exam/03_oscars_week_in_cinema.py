ime_na_film = input()
vid_zala = input()

cena_na_bilet_za_filma = 0
broi_bileti_za_filma = int(input())

if vid_zala == 'normal':
    if ime_na_film == 'A Star Is Born':
        cena_na_bilet_za_filma = 7.50
    elif ime_na_film == 'Bohemian Rhapsody':
        cena_na_bilet_za_filma = 7.35
    elif ime_na_film == 'Green Book':
        cena_na_bilet_za_filma = 8.15
    elif ime_na_film == 'The Favourite':
        cena_na_bilet_za_filma = 8.75
elif vid_zala == 'luxury':
    if ime_na_film == 'A Star Is Born':
        cena_na_bilet_za_filma = 10.50
    elif ime_na_film == 'Bohemian Rhapsody':
        cena_na_bilet_za_filma = 9.45
    elif ime_na_film == 'Green Book':
        cena_na_bilet_za_filma = 10.25
    elif ime_na_film == 'The Favourite':
        cena_na_bilet_za_filma = 11.55
elif vid_zala == 'ultra luxury':
    if ime_na_film == 'A Star Is Born':
        cena_na_bilet_za_filma = 13.50
    elif ime_na_film == 'Bohemian Rhapsody':
        cena_na_bilet_za_filma = 12.75
    elif ime_na_film == 'Green Book':
        cena_na_bilet_za_filma = 13.25
    elif ime_na_film == 'The Favourite':
        cena_na_bilet_za_filma = 13.95

obshta_pechalba = cena_na_bilet_za_filma * broi_bileti_za_filma

print(f'{ime_na_film} -> {obshta_pechalba:.2f} lv.')
