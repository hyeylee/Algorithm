from collections import deque
cnt = 0
MAX = 100001

visited = [0] * MAX
N,K = map(int,input().split())
queue = deque([N])
while queue:
    v = queue.popleft()
    if v==K:
        cnt += 1
    for i in (v-1,v+1,v*2):
        if 0 <= i < MAX and not visited[i]:
            visited[i] = visited[v] + 1
            queue.append(i)


print(visited[K])
print(cnt)

