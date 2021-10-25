movies_count = int(input())

min_movie_rating_name = input()
min_movie_rating_score = float(input())

max_movie_rating_name = min_movie_rating_name
max_movie_rating_score = min_movie_rating_score

average_movie_rating = 0
total_rating = min_movie_rating_score

# Calculations
for i in range(movies_count-1):
    movie_name = input()
    movie_score = float(input())

    if movie_score < min_movie_rating_score:
        min_movie_rating_score = movie_score
        min_movie_rating_name = movie_name
    if movie_score > max_movie_rating_score:
        max_movie_rating_score = movie_score
        max_movie_rating_name = movie_name

    total_rating += movie_score

average_movie_rating = total_rating / movies_count

# Outputs
print(f"{max_movie_rating_name} is with highest rating: {max_movie_rating_score:.1f}")
print(f"{min_movie_rating_name} is with lowest rating: {min_movie_rating_score:.1f}")
print(f"Average rating: {average_movie_rating:.1f}")
