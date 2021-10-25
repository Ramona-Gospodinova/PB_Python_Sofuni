numbers = int(input())
sum = 0

for i in range(numbers):
    current_number = int(input())
    sum += current_number

average_number = sum / numbers
print(f'{average_number:.2f}')
