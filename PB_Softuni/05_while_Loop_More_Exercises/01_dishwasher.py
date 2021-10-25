broi_butilki = int(input())

zakupeno_kolichestvo_preparat = broi_butilki * 750
ostavashto_kolichestvo_preparat = zakupeno_kolichestvo_preparat

chuniq = 5
tendjera = 15

total_dishes_counter = 1
chunii_counter = 0
tendjera_counter = 0

dostatychno = True

while(True):
    read = input()
    if read == 'End':
        break
    dish = int(read)

    if total_dishes_counter % 3 == 0:
        count_need_washing = dish * tendjera  # Използвано количество за Х тенджери
        tendjera_counter += dish    # Увеличаваме броя на тенджерите с Х тенджери
    else:
        count_need_washing = dish * chuniq  # Използвано количество за Х чинии
        chunii_counter += dish  # Увеличаваме броя на чиниите с Х чинии

    if count_need_washing > ostavashto_kolichestvo_preparat:
        dostatychno = False
        break

    ostavashto_kolichestvo_preparat -= count_need_washing
    total_dishes_counter += 1

#   OUTPUT:
if dostatychno:
    print("Detergent was enough!")
    print(f"{chunii_counter} dishes and {tendjera_counter} pots were washed.")
    print(f"Leftover detergent {ostavashto_kolichestvo_preparat} ml.")

if not dostatychno:
    more_need = count_need_washing - ostavashto_kolichestvo_preparat
    print(f"Not enough detergent, {more_need} ml. more necessary!")