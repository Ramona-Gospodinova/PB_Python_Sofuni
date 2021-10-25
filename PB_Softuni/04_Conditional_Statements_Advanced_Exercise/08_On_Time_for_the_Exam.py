exam_hour = int(input())  # 0 до 23
exam_minutes = int(input())  # 0 до 59

arrive_hour = int(input())   # 0 до 23
arrive_minutes = int(input())  # 0 до 59

on_time = False
late = False
early = False

minutes_before_start = 0
minutes_after_start = 0

exam_hour_to_minutes = exam_hour * 60
exam_total_minutes = exam_hour_to_minutes + exam_minutes

arrive_hour_to_minutes = arrive_hour * 60
arrive_total_minutes = arrive_hour_to_minutes + arrive_minutes

if arrive_total_minutes > exam_total_minutes:
    minutes_after_start = arrive_total_minutes - exam_total_minutes
    print('Late')

    if minutes_after_start < 60:
        print(f'{minutes_after_start} minutes after the start')
    else:
        hours = minutes_after_start // 60
        mm = minutes_after_start % 60

        if mm < 10:
            mm = '0' + str(mm)
        print(f'{hours}:{mm} hours after the start')

if arrive_total_minutes < exam_total_minutes:
    minutes_before_start = exam_total_minutes - arrive_total_minutes

    if 0 < minutes_before_start <= 30:
        print('On time')
        print(f'{minutes_before_start} minutes before the start')
    else:
        print('Early')

        hours = minutes_before_start // 60
        mm = minutes_before_start % 60

        if mm < 10:
            mm = '0' + str(mm)

        if minutes_before_start >= 60:
            print(f'{hours}:{mm} hours before the start')
        else:
            print(f'{mm} minutes before the start')

if arrive_total_minutes == exam_total_minutes:
    print('On time')
