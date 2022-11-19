for tc in range(1,11):
    N = int(input()) # 원본 암호문 길이
    o_set = list(map(str,input().split())) # 원본 암호문
    T = int(input()) #  명령어의 개수
    T_set = list(map(str,input().split())) # 명령어 문자열
    for i in range(len(T_set)):
        if(T_set[i] == 'I'):
            x = int(T_set[i+1]) # x의 위치부터
            y = int(T_set[i+2]) # y 개 
            for a in range(y): # y개 개수만큼 인덱스 값에 추가
                o_set.insert(x+a,T_set[i+3+a])
            #sas = T_set[i+3:(i+3+y)]
            #saas = ' '.join(sas)
            #print(y,sas)                
            #print(x,o_set)
    print(f'#{tc}',' '.join(o_set[:10]))



