T = int(input())
for i in range(1,T+1):
    total = 0
    for data in list(map(int, input().split())):
        total += data     
    print(f'#{i}', round(total/10))