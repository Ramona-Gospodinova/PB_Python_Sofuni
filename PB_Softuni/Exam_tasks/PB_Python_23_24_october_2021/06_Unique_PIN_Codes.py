# PIN
# 0 - Even number
# 1 (2 3 5 7)
# 2 - Even number

first_number = int(input())
second_number = int(input())
third_number = int(input())

for i in range(2, first_number + 1, 2):
    for j in range(2, second_number + 1, 1):
        if j not in [2, 3, 5, 7]:
            continue
        for k in range(2, third_number + 1, 2):
            print(f"{i} {j} {k}")
