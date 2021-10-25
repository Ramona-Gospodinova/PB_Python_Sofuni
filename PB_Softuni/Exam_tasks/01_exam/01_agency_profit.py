agency_name = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
adult_tickets_price = float(input())
tax_service = float(input())

children_tickets_price = adult_tickets_price - (0.70 * adult_tickets_price)
children_tickets_with_tax = children_tickets_price + tax_service
adult_tickets_price_with_tax = adult_tickets_price + tax_service

total_tickets_price = (children_tickets_with_tax * children_tickets_count) + (adult_tickets_price_with_tax * adult_tickets_count)
profit = total_tickets_price * 0.2

print(f'The profit of your agency from {agency_name} tickets is {profit:.2f} lv.')
