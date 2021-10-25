fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

line = input()

if line in fruits:
    print("fruit")
elif line in vegetables:
    print("vegetable")
else:
    print("unknown")