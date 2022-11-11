import math
T = int(input())
for i in range(1,T+1):
    N, D = map(int,input().split())
    d = D * 2 + 1 # 분무기 범위
    result = math.ceil(N / d) # 올림은 math.ceil  써야함


    print(f'#{i}',result)
