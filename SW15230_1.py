S = int(input()) # 테스트케이스 
for tc in range(1,S+1):
    n= list(map(str,input()))
    count=1
    for i in range(len(n)-1): #abcd 0 1 
        if(n[0] != 'a'):
            count = 0
            break            
        # elif ord(n[i])==97:
            # ount+=1
        elif ord(n[i+1])-ord(n[i])==1:
            count+=1
        else:
            break
    
    if (len(n)==0):
        count = 0        
    print(f'#{tc}',count)