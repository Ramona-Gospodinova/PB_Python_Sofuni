import math

vreme_za_snimki_s_koeto_razpolagame = int(input())
scenes_count = int(input())
scene_length = int(input())

area_prepare = 0.15 * vreme_za_snimki_s_koeto_razpolagame

time_for_scenes = scenes_count * scene_length

neobhodimo_vreme_za_zasnemaneto_na_scenite = time_for_scenes + area_prepare

if vreme_za_snimki_s_koeto_razpolagame >= neobhodimo_vreme_za_zasnemaneto_na_scenite:
    time_left = math.ceil(vreme_za_snimki_s_koeto_razpolagame - neobhodimo_vreme_za_zasnemaneto_na_scenite)
    print(f"You managed to finish the movie on time! You have {time_left} minutes left!")
else:
    need_time = math.ceil(neobhodimo_vreme_za_zasnemaneto_na_scenite - vreme_za_snimki_s_koeto_razpolagame)
    print(f"Time is up! To complete the movie you need {need_time} minutes.")
