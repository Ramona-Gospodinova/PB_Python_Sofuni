day_of_week = input()

ticket_unit_price = 0

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day_of_week in ["Monday", "Tuesday", "Friday"]:
    ticket_unit_price = 12
elif day_of_week in ["Wednesday", "Thursday"]:
    ticket_unit_price = 14
else:
    ticket_unit_price = 16

print(ticket_unit_price)