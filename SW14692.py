TC = int(input())
output = 0
t = 0
for i in range(1, TC+1):
    N = int(input())
 
    if(N % 2 == 0):
        print(f'#{i}','Alice')              
    else:
        print(f'#{i}','Bob')