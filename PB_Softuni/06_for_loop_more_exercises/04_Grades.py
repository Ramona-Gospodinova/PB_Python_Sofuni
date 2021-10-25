broi_studenti = int(input())

top_students = 0
after_top_students = 0
mid_students = 0
fail_students = 0

total_score = 0

for i in range(broi_studenti):
    tekushta_ocenka = float(input())
    total_score += tekushta_ocenka

    if tekushta_ocenka >= 5.00:
        top_students += 1
    elif 4.00 <= tekushta_ocenka <= 4.99:
        after_top_students += 1
    elif 3.00 <= tekushta_ocenka <= 3.99:
        mid_students += 1
    elif tekushta_ocenka < 3.00:
        fail_students += 1

# OUTPUT
top_students_percent = (top_students / broi_studenti) * 100
after_top_students_percent = (after_top_students / broi_studenti) * 100
mid_students_percent = (mid_students / broi_studenti) * 100
fail_students_percent = (fail_students / broi_studenti) * 100
average_score = total_score / broi_studenti

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {after_top_students_percent:.2f}%")
print(f"Between 3.00 and 3.99: {mid_students_percent:.2f}%")
print(f"Fail: {fail_students_percent:.2f}%")
print(f"Average: {average_score:.2f}")