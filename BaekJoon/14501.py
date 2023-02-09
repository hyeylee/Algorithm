N= int(input()) # 일자

t_list = []
p_list = []
answer = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(N - 1, -1, -1):
    if t_list[i] + i > N:
        answer[i] = answer[i + 1]
        print(answer)
    else:
        answer[i] = max(p_list[i] + answer[i + t_list[i]], answer[i + 1])
        print(answer)
        
print(answer)


