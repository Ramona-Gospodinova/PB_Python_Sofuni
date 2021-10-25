day_of_week = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

if day_of_week in working_days:
    print("Working day")
elif day_of_week in weekends:
    print("Weekend")
else:
    print("Error")
