month = input()  # May, June, July, August, September или October;
broi_noshtuvki = int(input())

studio_discount = 0
apartment_discount = 0

if month in ["May", "October"]:
    studio_unit_price = 50
    apartment_unit_price = 65

    if 7 < broi_noshtuvki < 14:
        studio_discount = 5
    elif broi_noshtuvki > 14:
        studio_discount = 30

elif month in ["June", "September"]:
    studio_unit_price = 75.20
    apartment_unit_price = 68.70

    if broi_noshtuvki > 14:
        studio_discount = 20
else:
    studio_unit_price = 76
    apartment_unit_price = 77

if broi_noshtuvki > 14:
    apartment_discount = 10

apartment_total = broi_noshtuvki * apartment_unit_price
apartment_total_after_discount = apartment_total - (apartment_total * apartment_discount / 100)

studio_total = broi_noshtuvki * studio_unit_price
studio_total_after_discount = studio_total - (studio_total * studio_discount / 100)

#  OUTPUT:
print(f"Apartment: {apartment_total_after_discount:.2f} lv.")
print(f"Studio: {studio_total_after_discount:.2f} lv.")
