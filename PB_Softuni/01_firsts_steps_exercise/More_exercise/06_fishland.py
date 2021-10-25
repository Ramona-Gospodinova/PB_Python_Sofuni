cena_skumria_za_kg = float(input())
cena_caca_za_kg = float(input())
cena_midi_za_kg = 7.50

kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

cena_palamud_za_kg = cena_skumria_za_kg * 1.6
cena_safrid_za_kg = cena_caca_za_kg * 1.8

total_cena_palamud = kg_palamud * cena_palamud_za_kg
total_cena_safrid = kg_safrid * cena_safrid_za_kg
total_cena_midi = kg_midi * cena_midi_za_kg

result = total_cena_palamud + total_cena_safrid + total_cena_midi
print(f'{result:.2f}')