# Input variables
total_money = 0
end = False

while True:
    # Inputs
    destination = input()

    if destination == 'End':
        end = True
        break

    minimal_amount = float(input())

    while True:
        money = float(input())
        total_money += money

        if total_money >= minimal_amount:
            total_money = 0
            print(f'Going to {destination}!')
            break
