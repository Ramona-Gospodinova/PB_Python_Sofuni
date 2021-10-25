budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memories = int(input())

discount = 0

if video_cards > processors:
    discount = 0.15

video_card_unit_price = 250
video_cards_total_price = video_cards * video_card_unit_price


processor_unit_price = 0.35 * video_cards_total_price
processors_total_price = processors * processor_unit_price

ram_memory_unit_price = 0.10 * video_cards_total_price
ram_memories_total_price = ram_memories * ram_memory_unit_price

total_price = video_cards_total_price + processors_total_price + ram_memories_total_price

if discount:
    total_price = total_price - (total_price * discount)

# Prints outputs
if budget >= total_price:
    rest_budget = budget - total_price
    print(f'You have {rest_budget:.2f} leva left!')
else:
    need_budget = total_price - budget
    print(f'Not enough money! You need {need_budget:.2f} leva more!')
