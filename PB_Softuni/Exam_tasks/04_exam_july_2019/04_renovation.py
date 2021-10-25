visochina_na_stena = int(input())
shirina_na_stena = int(input())
not_paint_percent = int(input())

total_area = visochina_na_stena * shirina_na_stena
total_area_after_not_painted = total_area - (total_area * not_paint_percent / 100)
total_area_for_painting = int(4 * total_area_after_not_painted)

end = False

total_litri_boq = 0
while True:
    litri_boq = input()

    if litri_boq == 'Tired!':
        area_left = int(total_area_for_painting - total_litri_boq)
        end = True
        print(f'{area_left} quadratic m left.')
        break

    litri_boq = int(litri_boq)
    total_litri_boq += litri_boq
    if total_litri_boq >= total_area_for_painting:
        break

# Outputs
if not end and total_area_for_painting < total_litri_boq:
    boq_left = abs(total_area_for_painting - total_litri_boq)
    print(f'All walls are painted and you have {boq_left} l paint left!')
if total_area_for_painting == total_litri_boq:
    print(f'All walls are painted! Great job, Pesho!')