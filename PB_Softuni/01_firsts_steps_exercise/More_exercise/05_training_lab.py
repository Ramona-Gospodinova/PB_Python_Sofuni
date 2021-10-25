length = float(input())
width = float(input())

length_cm = length * 100
width_cm = width * 100

rest_width = width_cm - 100
bura_na_red = rest_width // 70
redove = length_cm // 120

total_mesta = redove * bura_na_red - 3

print(int(total_mesta))
