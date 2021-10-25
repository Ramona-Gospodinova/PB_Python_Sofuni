numbers_count = int(input())

first_number = int(input())
min_number = first_number
max_number = first_number

for number in range(numbers_count - 1):
    number = int(input())
    if number < min_number:
        min_number = number

    if number > max_number:
        max_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
