
start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_number = 0
is_found = False

for m in range(start_number, end_number + 1):
    for n in range(start_number, end_number + 1):
        total = m + n
        combination_number += 1
        if total == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f'Combination N:{combination_number} ({m} + {n} = {magic_number})')
else:
    print(f'{combination_number} combinations - neither equals {magic_number}')
