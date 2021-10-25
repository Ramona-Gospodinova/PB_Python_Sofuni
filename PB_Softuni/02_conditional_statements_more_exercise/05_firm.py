import math

need_hours = int(input())
days_for_working = int(input())
broi_slujiteli_raboteshti_izvunredno = int(input())

# Calculations
days_for_working_after_removing = days_for_working - (days_for_working * 0.10)

hours_for_working = math.floor(days_for_working_after_removing * 8)
hours_for_working_izvunredno = math.floor(broi_slujiteli_raboteshti_izvunredno * (days_for_working * 2))

total_hours_for_working = hours_for_working + hours_for_working_izvunredno

# OUTPUT
if total_hours_for_working >= need_hours:
    ostavashti_chasove = math.floor(total_hours_for_working - need_hours)
    print(f'Yes!{ostavashti_chasove} hours left.')
else:
    nedotigashti_chasove = math.floor(need_hours - total_hours_for_working)
    print(f'Not enough time!{nedotigashti_chasove} hours needed.')
