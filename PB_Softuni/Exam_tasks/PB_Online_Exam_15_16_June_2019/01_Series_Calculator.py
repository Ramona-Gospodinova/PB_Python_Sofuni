import math

serial_name = input()

seasons_count = int(input())
episodes_count = int(input())
episode_length = float(input())

total_episodes = seasons_count * episodes_count

total_episodes_time = total_episodes * episode_length
total_episodes_ads = (0.20 * episode_length) * total_episodes
additional_season_time = 10 * seasons_count

total_time = total_episodes_time + total_episodes_ads + additional_season_time
total_time_int = math.floor(total_time)

#  Output
print(f"Total time needed to watch the {serial_name} series is {total_time_int} minutes.")
