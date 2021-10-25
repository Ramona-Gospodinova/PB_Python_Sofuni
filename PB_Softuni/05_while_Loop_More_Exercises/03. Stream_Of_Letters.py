secret_word = ''
secret_word_output = ''

all_characters_found = False

characters_found = 0
characters_c = 0
characters_o = 0
characters_n = 0

while True:
    character = input()

    if character == 'End':
        #  OUTPUT
        print(secret_word_output)
        break
    elif not character.isalpha():
        continue
    elif character in ["c", "o", "n"]:
        if character == "c":
            characters_c += 1

            if characters_c > 1:
                secret_word += character
        elif character == "o":
            characters_o += 1

            if characters_o > 1:
                secret_word += character
        elif character == "n":
            characters_n += 1

            if characters_n > 1:
                secret_word += character

        if characters_c > 0 and characters_o > 0 and characters_n > 0:
            all_characters_found = True
            secret_word += " "
            secret_word_output = secret_word

            characters_found = 0
            characters_c = 0
            characters_o = 0
            characters_n = 0
    else:
        secret_word += character
