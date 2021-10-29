n = int(input())
a = ""
for i in range(n):
    if i % 2 == 0:
        a = '1 ' + a
    else:
        a = '0 ' + a
    print(a)
