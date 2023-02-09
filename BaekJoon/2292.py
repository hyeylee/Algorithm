n = int(input())
a = 1
i = 0
while True:
    a += 6 * i
    i += 1
    if n <= a:
        break
print(i)