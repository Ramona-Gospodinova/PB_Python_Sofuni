student = 0
standard = 0
kids = 0

student_tickets_percent = 0
standard_tickets_percent = 0
kids_tickets_percent = 0

next_movie = False
flag = False
seats_count = 0
total_tickets = 0

while True:
    projection = input()
    # End reading movie info ....
    if projection == 'Finish':
        if total_tickets != 0:  # Check division by 0
            student_tickets_percent = (student / total_tickets) * 100
            standard_tickets_percent = (standard / total_tickets) * 100
            kids_tickets_percent = (kids / total_tickets) * 100
        print(f'Total tickets: {total_tickets}')
        print(f'{student_tickets_percent:.2f}% student tickets.')
        print(f'{standard_tickets_percent:.2f}% standard tickets.')
        print(f'{kids_tickets_percent:.2f}% kids tickets.')
        break

    kapacitet = int(input())
    while True:
        movie_type = input()
        if movie_type == 'student':
            student += 1
        elif movie_type == 'standard':
            standard += 1
        elif movie_type == 'kid':
            kids += 1

        # Checking for 'End' input...
        if movie_type == 'End':
            percent_full = (seats_count / kapacitet) * 100
            print(f'{projection} - {percent_full:.2f}% full.')
            seats_count = 0
            next_movie = True
            break

        seats_count += 1
        total_tickets += 1

        # Checking for no space...
        if seats_count == kapacitet:
            percent_full = (seats_count / kapacitet) * 100
            print(f'{projection} - {percent_full:.2f}% full.')
            seats_count = 0
            next_movie = True
            break
