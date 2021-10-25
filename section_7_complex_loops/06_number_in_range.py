# num in [1...100]

num = int(input())

while num < 1 or num > 100:
    print('Invalid number!')
    num = int(input())

print('The number is %d' % num)
