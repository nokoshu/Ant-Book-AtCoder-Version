from collections import defaultdict
N = int(input())
d = defaultdict(lambda: 0)
for i in range(N):
    key = input()
    d[key] += 1

T = int(input())
for i in range(T):
    key = input()
    d[key] -= 1

max_value = max(d.values())
print(max_value if max_value > 0 else 0)