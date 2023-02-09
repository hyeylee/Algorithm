for i in range(1,11):
    dump = int(input()) # 덤프횟수
    height = list(map(int,input().split())) #상자높이
     
    for _ in range(1,dump+1):
        max_height = max(height) # 최고높이
        min_height = min(height) # 최저높이
     
        height[height.index(max_height)] = max_height - 1
        height[height.index(min_height)] = min_height + 1
     
        max_height = max(height) # 최고높이
        
        min_height = min(height) # 최저높이
        if(max_height == min_height):
            max_height = max(height) # 최고높이
            min_height = min(height) # 최저높이
            break
            
    print(f'#{i}',max_height-min_height)
    
