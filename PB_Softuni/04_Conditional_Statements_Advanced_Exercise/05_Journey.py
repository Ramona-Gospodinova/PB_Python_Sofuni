budget = float(input())
season = input()  # "summer” или "winter”

destination = ""
holiday_type = ""
percent = 0

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        holiday_type = "Camp"
        percent = 30
    elif season == "winter":
        holiday_type = "Hotel"
        percent = 70
elif 100 < budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        holiday_type = "Camp"
        percent = 40
    elif season == "winter":
        holiday_type = "Hotel"
        percent = 80
elif budget > 1000:
    destination = "Europe"
    holiday_type = "Hotel"

    percent = 90

# Outputs
money = budget * percent / 100
print(f"Somewhere in {destination}")
print(f"{holiday_type} - {money:.2f}")