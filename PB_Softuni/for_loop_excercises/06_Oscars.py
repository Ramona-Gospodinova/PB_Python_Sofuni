actor_name = input()
points = float(input())
count_rating_persons = int(input())

counter = 0
total_points = points

for i in range(count_rating_persons):
    rating_person = input()
    points_rating = float(input())

    name_length = len(rating_person)
    rating_from_person = (name_length * points_rating) / 2
    total_points += rating_from_person

    if total_points > 1250.5:
        break

#  OUTPUT
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    need_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {need_points:.1f} more!")
