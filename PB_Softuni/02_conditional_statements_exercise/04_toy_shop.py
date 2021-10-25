trip_price = float(input())

broi_puzeli = int(input())
broi_govoreshti_kukli = int(input())
broi_plusheni_mecheta = int(input())
broi_minions = int(input())
broi_kamioncheta = int(input())

discount = 0

puzeli_total_prics = broi_puzeli * 2.60
govoreshti_kukli_total_price = broi_govoreshti_kukli * 3
plusheni_mecheta_total_price = broi_plusheni_mecheta * 4.10
minions_total_price = broi_minions * 8.20
kamioncheta_total_price = broi_kamioncheta * 2

total_toys_count = broi_puzeli + broi_govoreshti_kukli + broi_plusheni_mecheta + broi_minions + broi_kamioncheta
total_toys_price = puzeli_total_prics + govoreshti_kukli_total_price + plusheni_mecheta_total_price + \
                   minions_total_price + kamioncheta_total_price

if total_toys_count >= 50:
    total_toys_price = total_toys_price - (total_toys_price * 0.25)

# Razhodi
razhod_za_naem = total_toys_price * 0.10

ostavashti_pari_sled_razhodite = total_toys_price - razhod_za_naem

if trip_price > ostavashti_pari_sled_razhodite:
    nedostigashti_pari = trip_price - ostavashti_pari_sled_razhodite
    print(f'Not enough money! {nedostigashti_pari:.2f} lv needed.')
else:
    ostavashti_pari = ostavashti_pari_sled_razhodite - trip_price
    print(f'Yes! {ostavashti_pari:.2f} lv left.')
