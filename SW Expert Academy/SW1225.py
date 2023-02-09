from collections import deque
for tc in range(1,11):
    t = int(input()) # 테스트케이스 번호
    a = deque(map(int,input().split()))
    while True:
        for j in range(1,6): # 5번 반복
            s = a[0] - j
            a.append(s)
            a.popleft() # 맨왼쪽값 없애주기    
            if s <= 0:
                s = 0
                break
        if(a[-1] <= 0): # while문 해제
            break
    a[7] = 0
    result = list(a)
    result2 = ' '.join(str(s) for s in result) #문자열로 바꿔서 출력(테스트케이스 맞추기 위해서)
    print(f'#{t}',result2)


