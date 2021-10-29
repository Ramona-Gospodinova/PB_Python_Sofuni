# a се мени от 1 до 9
# b се мени от 9 до а
# c се мени от 0 до 9
# d се мени от 9 до c

n = int(input())
flag = 0

for a in range(1, 9):
    if not flag:
        for b in range(9, a, -1):
            if not flag:
                for c in range(0, 9):
                    if not flag:
                        for d in range(9, c, -1):
                            if not flag:
                                suma = int(a) + int(b) + int(c) + int(d)
                                product = int(a) * int(b) * int(c) * int(d)

                                n_last_digit = n % 10

                                if suma == product and n_last_digit == 5:
                                    print(f"{a}{b}{c}{d}")
                                    flag = 1
                                    break
                                elif product // suma == 3 and n % 3 == 0:
                                    print(f"{d}{c}{b}{a}")
                                    flag = 1
                                    break

if not flag:
    print("Nothing found")
