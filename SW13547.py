T = int(input()) # 테스트케이스 수
for i in range(1,T+1):
    a = list(map(str,input()))
    if(a.count('x')>8):
        print(f'#{i}', 'NO')
    else:
        print(f'#{i}', 'YES')
