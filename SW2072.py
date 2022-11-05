T1 = int(input())
for i in range(1, T1+1):
    total = 0
    for data in list(map(int, input().split())):
        if data % 2 != 0:
            total += data       
    print(f'#{i}', total)