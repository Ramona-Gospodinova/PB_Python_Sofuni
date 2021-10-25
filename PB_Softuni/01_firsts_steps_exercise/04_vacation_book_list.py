book_pages = int(input())
pages_for_hour = int(input())
days_for_reading = int(input())

# Необходими часове за четене на книгата
hours_need_for_reading = book_pages // pages_for_hour

# Необходими часове на ден за четене на книгата
hours_for_day = hours_need_for_reading / days_for_reading

print(hours_for_day)
