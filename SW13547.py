T = int(input()) # 테스트케이스 수
for i in range(1,T+1):
    a = list(map(str,input()))
    if(a.count('x')>7): # 진 횟수가 8번이상인 경우 NO
        print(f'#{i}', 'NO')
    else:
        print(f'#{i}', 'YES')
