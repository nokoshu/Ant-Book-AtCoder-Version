N = int(input())

t = [0] * N
for i in range(N):
    t[i] = int(input())
    

ans = 200
max_time = sum(t)
for i in range(N**2):
    time = 0
    for j in range(N):
        if ((i >> j) & 1) == 1:
            time += t[j]
    time = max(time, max_time - time)
    ans = min(ans, time)

print(ans)
    