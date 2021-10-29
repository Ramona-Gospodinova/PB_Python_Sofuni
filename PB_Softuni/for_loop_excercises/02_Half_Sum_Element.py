count_numbers = int(input())

max_number = int(input())
sum_numbers = max_number

for num in range(count_numbers - 1):
    number = int(input())
    sum_numbers += number

    if number > max_number:
        max_number = number

if (sum_numbers - max_number) == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_others = sum_numbers - max_number
    print("No")
    print(f"Diff = {abs(max_number - sum_others)}")
