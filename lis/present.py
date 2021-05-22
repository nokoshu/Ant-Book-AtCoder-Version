import bisect

N = int(input())

boxes = []
for i in range(N):
    w, h = map(int, input().split())
    boxes.append((w, h))
    
boxes = sorted(boxes, key=lambda x: (x[0], -x[1]))
dp = []
for w, h in boxes:
    idx = bisect.bisect_left(dp, h)
    if idx == len(dp):
        dp += [h]
    else:
        dp[idx] = h
        
print(len(dp))