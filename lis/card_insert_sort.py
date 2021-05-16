import bisect

N = int(input())

dp = [float('inf') for _ in range(N)]
for i in range(N):
    c = int(input())
    idx = bisect.bisect_left(dp, c)
    dp[idx] = c

sorted_num = bisect.bisect_left(dp, float('inf'))

ans = N - sorted_num
print(ans)
    
