town = input()
sales_amount = float(input())

percent_commission = 0

commission_valid = town in ["Sofia", "Varna", "Plovdiv"] and sales_amount >= 0


if commission_valid:
    if town == "Sofia":
        if sales_amount > 10000:
            percent_commission = 12
        elif 1000 < sales_amount <= 10000:
            percent_commission = 8
        elif 500 < sales_amount <= 1000:
            percent_commission = 7
        elif 0 <= sales_amount <= 500:
            percent_commission = 5
    elif town == "Varna":
        if sales_amount > 10000:
            percent_commission = 13
        elif 1000 < sales_amount <= 10000:
            percent_commission = 10
        elif 500 < sales_amount <= 1000:
            percent_commission = 7.5
        elif 0 <= sales_amount <= 500:
            percent_commission = 4.5
    elif town == "Plovdiv":
        if sales_amount > 10000:
            percent_commission = 14.5
        elif 1000 < sales_amount <= 10000:
            percent_commission = 12
        elif 500 < sales_amount <= 1000:
            percent_commission = 8
        elif 0 <= sales_amount <= 500:
            percent_commission = 5.5

    commission_amount = sales_amount * percent_commission / 100
    print(f'{commission_amount:.2f}')
else:
    print('error')