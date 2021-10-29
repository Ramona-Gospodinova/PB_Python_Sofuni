movie_name = input()  # "John Wick", "Star Wars", "Jumanji"
movie_pack = input()  # "Drink", "Popcorn", "Menu"
tickets_count = int(input())

total_price = 0
ticket_unit_price = 0
discount = 0

if movie_name == "John Wick":
    if movie_pack == "Drink":
        ticket_unit_price = 12
    elif movie_pack == "Popcorn":
        ticket_unit_price = 15
    elif movie_pack == "Menu":
        ticket_unit_price = 19
elif movie_name == "Star Wars":
    if movie_pack == "Drink":
        ticket_unit_price = 18
    elif movie_pack == "Popcorn":
        ticket_unit_price = 25
    elif movie_pack == "Menu":
        ticket_unit_price = 30
elif movie_name == "Jumanji":
    if movie_pack == "Drink":
        ticket_unit_price = 9
    elif movie_pack == "Popcorn":
        ticket_unit_price = 11
    elif movie_pack == "Menu":
        ticket_unit_price = 14

if movie_name == "Star Wars" and tickets_count >= 4:
    discount = 0.30
elif movie_name == "Jumanji" and tickets_count == 2:
    discount = 0.15

total_price = tickets_count * ticket_unit_price

#  OUTPUT
if discount:
    total_price = total_price - (total_price * discount)

print(f"Your bill is {total_price:.2f} leva.")
