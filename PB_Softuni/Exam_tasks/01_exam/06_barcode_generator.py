first_number = int(input())
second_number = int(input())

#  2345
#  6789

first_number_t = first_number // 1000  # Хилядните
second_number_t = second_number // 1000  # Хилядните

first_number_h = (first_number // 100) % 10  # Стотните
second_number_h = (second_number // 100) % 10  # Стотните

first_number_d = (first_number // 10) % 10  # Десетиците
second_number_d = (second_number // 10) % 10  # Десетиците

first_number_e = first_number % 10   # Единиците
second_number_e = second_number % 10  # Единиците


for i in range(first_number_t, second_number_t + 1):
    for j in range(first_number_h, second_number_h + 1):
        for k in range(first_number_d, second_number_d + 1):
            for m in range(first_number_e, second_number_e + 1):
                if m % 2 == 1 and k % 2 == 1 and j % 2 == 1 and i % 2 == 1:
                    if i == second_number_t:
                        print('{0}{1}{2}{3}'.format(i, j, k, m), end='')
                    else:
                        print('{0}{1}{2}{3} '.format(i, j, k, m), end='')




