import heapq
N,M,X = map(int,input().split()) # N = 학생수, 마을수 / M = 단방향 도로 / X가 도착지
INF = int(1e9)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

result = [[]]
time_list = []
for i in range(1,N+1):
    distance = [INF] * (N+1)
    result.append(dijkstra(i))
for i in range(1, N+1):
    time_list.append(result[i][X] + result[X][i])

print(max(time_list))

