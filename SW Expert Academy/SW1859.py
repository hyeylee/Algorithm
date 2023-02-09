T = int(input())
profit = 0
for i in range(1, T+1):
    N = int(input())
    firsetList = list(map(int,input().split()))
    b = 0
    final_profitlist = []
    while b < N:
        a = firsetList
        last_day = max(a) 
        last_day_index = a.index(last_day)
        # 최대 max를 찾은 뒤 그 전 값들을 잘라내서 sum 계산
        profitlist= a[0:last_day_index]
        count2 = len(profitlist)
 
        for_profit = sum(profitlist)
 
        max_profit = (last_day * count2) - for_profit
        if(for_profit == 0):
            max_profit = 0
         
        final_profitlist.append(max_profit)
        b = last_day_index + 1
         
 
        if(sum(final_profitlist) < 0):
            final_profitlist = 0
        del a[0:last_day_index+1]
        if(a==[]):
            print(f'#{i}', sum(final_profitlist))
            break