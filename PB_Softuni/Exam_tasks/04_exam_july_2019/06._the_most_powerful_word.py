most_magic_power = 0
most_magic_word = ''

while True:
    word = input()

    if word == 'End of words':
        break

    first_letter = word[0].lower()
    word_length = len(word)

    sum_ascii = 0
    magic_power = 0

    for i in range(word_length):
        sum_ascii += ord(word[i])

    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u' \
            or first_letter == 'y':
        magic_power = sum_ascii * word_length
    else:
        magic_power = int(sum_ascii / word_length)

    if magic_power > most_magic_power:
        most_magic_power = magic_power
        most_magic_word = word

# Outputs
print(f'The most powerful word is {most_magic_word} - {most_magic_power}')