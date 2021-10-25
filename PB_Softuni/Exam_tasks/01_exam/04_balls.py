# Inputs
import math

total_balls_count = int(input())

# Variables
red_balls_count = 0
orange_balls_count = 0
yellow_balls_count = 0
white_balls_count = 0
black_balls_count = 0
other_colors_count = 0
points = 0

for i in range(total_balls_count):
    current_ball_color = input()

    if current_ball_color == 'white':
        white_balls_count += 1
        points += 20
    elif current_ball_color == 'red':
        red_balls_count += 1
        points += 5
    elif current_ball_color == 'orange':
        orange_balls_count += 1
        points += 10
    elif current_ball_color == 'yellow':
        yellow_balls_count += 1
        points += 15
    elif current_ball_color == 'black':
        # Round numbers down to the nearest integer
        points = math.floor(points / 2)

        #   Правим си един брояч чрез който да броим пътите в които ни се е паднала черна топка, което автоматично
        #   означава, че това е броя на пътите в които сме делили на 2, защото само когато имаме черна топка
        #   делим на две! Броя на пътите в които сме делиди == Броя на черните топки ------------------->
        #   ----------> следователно щом са равни това е броя на пътите в които сме делиди на 2
        black_balls_count += 1
    else:
        other_colors_count += 1

# Outputs
print(f'Total points: {points}')
print(f'Points from red balls: {red_balls_count}')
print(f'Points from orange balls: {orange_balls_count}')
print(f'Points from yellow balls: {yellow_balls_count}')
print(f'Points from white balls: {white_balls_count}')
print(f'Other colors picked: {other_colors_count}')
print(f'Divides from black balls: {black_balls_count}')
