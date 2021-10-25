chicken_menu_count = int(input())
fish_menu_count = int(input())
vege_menuu_count = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vege_menu_price = 8.15

delivery = 2.50

total_without_desert = chicken_menu_count*chicken_menu_price + fish_menu_count*fish_menu_price + vege_menuu_count*vege_menu_price
desert_price = total_without_desert * 0.2

total = total_without_desert + desert_price + delivery

print(f'{total:.2f}')