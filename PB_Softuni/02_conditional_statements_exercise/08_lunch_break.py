import math

serial_name = input()
vreme_za_seriala = int(input())
vreme_za_pochivka = int(input())

vreme_za_obqd = vreme_za_pochivka / 8
vreme_za_otdih = vreme_za_pochivka / 4

ostanalo_vreme_ot_pochivkata = vreme_za_pochivka - (vreme_za_obqd + vreme_za_otdih)

if ostanalo_vreme_ot_pochivkata >= vreme_za_seriala:
    rest_time = math.ceil(ostanalo_vreme_ot_pochivkata - vreme_za_seriala)
    print(f'You have enough time to watch {serial_name} and left with {rest_time} minutes free time.')
else:
    need_time = math.ceil(vreme_za_seriala - ostanalo_vreme_ot_pochivkata)
    print(f"You don't have enough time to watch {serial_name}, you need {need_time} more minutes.")