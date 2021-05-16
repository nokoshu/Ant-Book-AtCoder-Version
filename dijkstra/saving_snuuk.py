import heapq

n, m, s, t = map(int, input().split())
s -= 1
t -= 1

A = [[] for _ in range(n)] # 円
B = [[] for _ in range(n)] # Snuuk

for i in range(m):
    u, v, a, b = map(int, input().split())    
    u -= 1
    v -= 1
    A[u].append([v, a])
    A[v].append([u, a])
    B[u].append([v, b])
    B[v].append([u, b])

def dijkstra(start, cost_type = A):
    dist = [float('inf')] * n
    seen = [False] * n
    g = [(0, start)]
    heapq.heapify(g)

    while g:
        pre_cost, u = heapq.heappop(g)
        dist[u] = pre_cost

        if dist[u] < pre_cost:
            continue

        for v, cost in cost_type[u]:
            if cost == False: continue
            if dist[v] > pre_cost + cost:
                dist[v] = pre_cost + cost
                heapq.heappush(g, (dist[v], v))

    return dist

A_cost = dijkstra(s, A)
B_cost = dijkstra(t, B)
ans = []
min_cost = float('inf')
for i in range(n-1, -1, -1):
    cost = A_cost[i] + B_cost[i]
    min_cost = min(min_cost, cost)
    ans.append(min_cost)

ans.reverse()
for i in range(n):
    print(max(10**15 - ans[i], 0))