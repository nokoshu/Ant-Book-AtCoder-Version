import array

W = int(input())
N, K = map(int, input().split())
dp = [[[0] * 10000 for _ in range(55)] for _ in range(55)]
AB = [list(map(int, input().split())) for _ in range(N)]
# dp = [[array.array('i', [0]*(W+1)) for _ in range(K+1)] for _ in range(N+1)]
dp = [[[0] * (W+1) for _ in range(K+1)] for _ in range(N+1)]

# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)


for n in range(N):
    for k in range(K+1):
        for w in range(W+1):
            a = AB[n][0] # 幅
            b = AB[n][1] # 重要度
            if w >= a and k >= 1:
                dp[n+1][k][w] = max(dp[n][k-1][w-a] + b, dp[n][k][w])
            else:
                dp[n+1][k][w] = dp[n][k][w]
        

print(dp[N][K][W])
                
