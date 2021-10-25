input_text = input()

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_sum = 0

for char in input_text:
    if char in vowels:
        index = vowels.index(char) + 1
        vowel_sum += index

print(vowel_sum)