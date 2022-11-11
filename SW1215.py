for tc in range(1,11):
    N = int(input()) # 찾아야 하는 회문의 길이
    arr = [str(input()) for _ in range(8)]
    count = 0
    result = []
    for i in range(len(arr)):
        for j in range(9-N):
            slice_str = arr[i][j:j+N]
            reversed_arr = slice_str[::-1] # 거꾸로 뒤집기
            if(slice_str == reversed_arr): # 두개 비교해서 회문 찾기
                count += 1
        for z in range(8): # 세로 찾기 위해서 행 열 바꾸기
            slice_str2 = arr[z][i]
            result += slice_str2
    slice_str3 = list(map(''.join, zip(*[iter(result)]*8)))
    for p in range(len(slice_str3)):
        for a in range(9-N):
            slice_str4 = slice_str3[p][a:a+N]
            reversed_arr2 = slice_str4[::-1]
            if(slice_str4 == reversed_arr2):
                count += 1        
 
             
 
 
    print(f'#{tc}',count)