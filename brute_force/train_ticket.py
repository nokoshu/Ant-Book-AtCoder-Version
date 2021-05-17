S = input()
N = len(S)-1


for bit in range(1 << N):
    op = []
    ans = int(S[0])
    for i in range(N):
        if (1 << i) & bit:
            ans += int(S[i+1])
            op.append('+')
        else:
            ans -= int(S[i+1])
            op.append('-')

    if ans == 7:
        print(S[0]+op[0]+S[1]+op[1]+S[2]+op[2]+S[3]+'=7')
        break
