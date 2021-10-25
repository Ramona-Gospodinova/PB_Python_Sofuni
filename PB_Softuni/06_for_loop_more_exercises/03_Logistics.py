count = int(input())

total_price = 0
total_tones = 0

microbus_count = 0
microbus_tones = 0

kamion_count = 0
kamion_tones = 0

vlak_count = 0
vlak_tones = 0

for i in range(count):
    tones = int(input())

    if tones <= 3:
        type = 'microbus'
        microbus_count += 1
        microbus_tones += tones

        total_price += tones * 200
    elif 4 <= tones <= 11:
        type = 'kamion'
        kamion_count += 1
        kamion_tones += tones

        total_price += tones * 175
    elif tones >= 12:
        type = 'vlak'
        vlak_count += 1
        vlak_tones += tones

        total_price += tones * 120

    total_tones += tones

# Calculations
average_tones = total_price / total_tones

average_microbus_percent = (microbus_tones / total_tones) * 100
average_kamion_percent = (kamion_tones / total_tones) * 100
average_vlak_percent = (vlak_tones / total_tones) * 100

print(f'{average_tones:.2f}')
print(f'{average_microbus_percent:.2f}%')
print(f'{average_kamion_percent:.2f}%')
print(f'{average_vlak_percent:.2f}%')
