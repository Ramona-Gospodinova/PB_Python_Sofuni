movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_unit_price = float(input())

cinema_percent = int(input())

total_tickets = days_count * tickets_count
tickets_income = total_tickets * ticket_unit_price

cinema_income = tickets_income * cinema_percent / 100

tickets_income_after = tickets_income - cinema_income

print(f'The profit from the movie {movie_name} is {tickets_income_after:.2f} lv.')
