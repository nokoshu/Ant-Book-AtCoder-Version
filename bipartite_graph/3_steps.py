from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
colors = [-1 for _ in range(N)]

G = defaultdict(lambda: [])
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

def dfs(u, color):

    colors[u] = color
    for v in G[u]:
        if colors[u] == colors[v]:
            return False
        if colors[v] == -1 and not dfs(v, 1^color):
            return False

    return True

ans = 0
is_bipartie = dfs(0, 1)
if is_bipartie:
    w_count = len([color for color in colors if color == 1])
    b_count = len([color for color in colors if color == 0])
    ans = w_count * b_count  - M
else:
    ans = N * (N-1) // 2 - M
print(ans)