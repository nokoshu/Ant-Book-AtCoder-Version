import copy
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
field = []
for i in range(10):
    field.append(list(input()))
    
def bfs(y, x):
    tmp_field = copy.deepcopy(field)

    q = deque([])
    q.append((y, x))
    while q:
        y, x = q.popleft()
        tmp_field[y][x] = 'x'
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny >= 10 or nx >= 10 or ny < 0 or nx < 0 or tmp_field[ny][nx]=='x':
                continue
            q.append((ny, nx))
    return tmp_field
        
    
    
for y in range(10):
    for x in range(10):
        # 埋め立て処理
        tmp_field = bfs(y, x)

        # 判定処理
        count = 0
        for i in range(10):
            for j in range(10):
                if tmp_field[i][j] == 'o':
                    count += 1
        if count == 0:
            print('YES')
            exit()

print('NO')


            