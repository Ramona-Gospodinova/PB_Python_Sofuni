suma_koqto_trqbva = int(input())

subrana_suma = 0

subrana_suma_flag = False
transaction_valid = True

transaction_counter = 1
transaction_cash_counter = 0
transaction_card_counter = 0

total_amount_cash = 0
total_amount_card = 0

while True:
    line = input()

    if line == 'End':
        print("Failed to collect required money for charity.")
        break

    product = int(line)

    if transaction_counter % 2 == 1:
        if product > 100:
            transaction_valid = False
            print('Error in transaction!')
        else:
            transaction_cash_counter += 1
            total_amount_cash += product
    elif transaction_counter % 2 == 0:
        if product < 10:
            transaction_valid = False
            print('Error in transaction!')
        else:
            transaction_card_counter += 1
            total_amount_card += product

    if transaction_valid:
        print('Product sold!')
        subrana_suma += product

        if subrana_suma >= suma_koqto_trqbva:
            subrana_suma_flag = True
            break

    transaction_valid = True
    transaction_counter += 1

#  Output
if subrana_suma_flag:
    average_amount_cash = total_amount_cash / transaction_cash_counter
    average_amount_card = total_amount_card / transaction_card_counter

    print(f"Average CS: {average_amount_cash:.2f}")
    print(f"Average CC: {average_amount_card:.2f}")
