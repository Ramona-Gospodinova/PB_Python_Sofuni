broi_etaji = int(input())
broi_stai = int(input())

for e in range(broi_etaji, 0, -1):
    for r in range(0, broi_stai):
        if e == broi_etaji:
            # check space
            if r == broi_stai - 1:
                print(f'L{e}{r}')
            else:
                print(f'L{e}{r} ', end='')
        elif e % 2 == 1:  # necheten etaj
            # check space
            if r == broi_stai - 1:
                print(f'A{e}{r}')
            else:
                print(f'A{e}{r} ', end='')
        else:
            # check space
            if r == broi_stai - 1:
                print(f'O{e}{r}')
            else:
                print(f'O{e}{r} ', end='')
