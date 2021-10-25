animal = input()

reptile = ["crocodile", "tortoise", "snake"]

if animal == "dog":
    print("mammal")
elif animal in reptile:
    print("reptile")
elif animal == "cat":
    print("unknown")