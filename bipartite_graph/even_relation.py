from collections import defaultdict

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
G = defaultdict(lambda: [])

ans = [-1 for _ in range(N)]

for i in range(N-1):
    u, v, dist = map(int, input().split())
    u -= 1
    v -= 1
    G[u] += [(v, dist)]
    G[v] += [(u, dist)]

def dfs(node, pre_dist):

    for next_node, dist in G[node]:
        if ans[next_node] != -1:
            continue
        if (pre_dist + dist) % 2 == 0:
            ans[next_node] = 0
        else:
            ans[next_node] = 1
        dfs(next_node, pre_dist+dist)


ans[0] = 0
dfs(0, 0)

for value in ans:
    print(value)