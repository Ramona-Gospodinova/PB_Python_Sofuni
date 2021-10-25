numbers_count = int(input())

even_positions_sum = 0
odd_positions_sum = 0

for i in range(numbers_count):
    number = int(input())

    if i % 2 == 0:
        even_positions_sum += number
    else:
        odd_positions_sum += number

if even_positions_sum == odd_positions_sum:
    print("Yes")
    print(f"Sum = {even_positions_sum}")
else:
    diff = abs(even_positions_sum - odd_positions_sum)
    print("No")
    print(f"Diff = {diff}")
