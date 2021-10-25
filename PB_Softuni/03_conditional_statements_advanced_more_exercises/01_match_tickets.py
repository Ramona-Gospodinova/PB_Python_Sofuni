budget = float(input())
category = input()
persons = int(input())

percent = 0

if 1 <= persons <= 4:
    percent = 0.75
elif 5 <= persons <= 9:
    percent = 0.60
elif 10 <= persons <= 24:
    percent = 0.50
elif 25 <= persons <= 49:
    percent = 0.40
elif persons >= 50:
    percent = 0.25

transport_price = budget * percent
ticket_unit_price = 0

if category == 'VIP':
    ticket_unit_price = 499.99
elif category == 'Normal':
    ticket_unit_price = 249.99

budget_rest_price = budget - transport_price
total_ticket_price = persons * ticket_unit_price

if budget_rest_price >= total_ticket_price:
    rest_money = budget_rest_price - total_ticket_price
    print(f'Yes! You have {rest_money:.2f} leva left.')
else:
    need_money = total_ticket_price - budget_rest_price
    print(f'Not enough money! You need {need_money:.2f} leva.')
