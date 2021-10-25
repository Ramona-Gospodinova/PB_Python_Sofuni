time = int(input())
day_of_week = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 10 <= time <= 18:
    if day_of_week in working_days:
        print('open')
    else:
        print('closed')
else:
    print('closed')