D, G = map(int, input().split())

P = []
C = []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = 1000
for i in range(2 ** D):
    money = 0
    num = 0
    for j in range(D):
        if ((i >> j) & 1):
            money += C[j]
            money += P[j] * 100 * (j+1)
            num += P[j]
    
    if money >= G:
        ans = min(ans, num)
        continue

    for j in reversed(range(D)):
        if ((i >> j) & 1):
            continue
        
        target = G - money
        if target <= P[j] * 100 * (j+1):
            num += (target + (j+1)*100 -1) // ((j+1) *100)
            ans = min(ans, num)
        else:
            money += P[j] * 100 * (j+1)
            num += P[j]

print(ans)
        
        
           
    
    