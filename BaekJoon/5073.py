while True:
    tri = []
    a,b,c = map(int,input().split())
    tri.append(a)
    tri.append(b)
    tri.append(c)
    tri.sort() # 정리해주고
    if(tri[0]==0): # 값이 0이면 break
        break
    elif(tri[0]==tri[1] and tri[1]==tri[2] and tri[0]==tri[2]):
        print('Equilateral')
    elif((tri[0]+tri[1])<=tri[2]):
        print('Invalid')
    elif(tri[0]!=tri[1] and tri[1]!= tri[2] and tri[0]!=tri[2]):
        print('Scalene')
    else:
        print('Isosceles')