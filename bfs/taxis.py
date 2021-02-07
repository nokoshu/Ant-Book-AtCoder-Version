import heapq
from collections import deque

N, K = map(int, input().split())

R = []
C = []
for i in range(N):
    c, r = map(int, input().split())
    R.append(r)
    C.append(c)

G = [[] for _ in range(N)]
for i in range(K):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)


# bfsにより各ノードの連結を修正する
def bsf(node, limit):

    is_used = [False] * N
    is_used[node] = True
    que = deque([])
    que.append((node, 0))

    while que:
        u, cost = que.popleft()
        for v in G[u]:
            if is_used[v]:
                continue
            is_used[v] = True
            if cost + 1 <= limit:
                short_G[node].append(v)
                que.append((v, cost + 1))


short_G = [[] for _ in range(N)]
for i in range(N):
    bsf(i, R[i]) # 各タクシーでどこまでいけるかを計算


cost = [float('inf')] * N
is_used = [False] * N
cost[0] = 0
def dijkstra(start):
    hq = [(0, start)]
    heapq.heapify(hq)
    while hq:
        prev_cost, u = heapq.heappop(hq)
        is_used[u] = True # 確定処理: この時点でuは更新されなくなる
        for v in short_G[u]:
            if is_used[v]:
                continue
            if cost[v] >= prev_cost + C[u]:
                heapq.heappush(hq, (prev_cost + C[u], v))
                cost[v] = prev_cost + C[u]
dijkstra(0)
print(cost[N-1])