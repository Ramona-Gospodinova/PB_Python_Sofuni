a = int(input())
b = int(input())
c = int(input())
percent = float(input())

# обем в куб. сантиметри
obem_paralelepiped_cm = a*b*c

# 1 литър = 1000 куб. сантиметри
obem_v_litri = obem_paralelepiped_cm / 1000

percent_not_water = percent/100
obem_voda_v_litri = obem_v_litri - (obem_v_litri * percent_not_water)

print(obem_voda_v_litri)
