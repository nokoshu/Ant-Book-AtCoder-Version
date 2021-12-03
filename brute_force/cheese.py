# 3 3 1
# S..
# ...
# ..1
from collections import deque
import copy
H, W, N = map(int, input().split())
field: list = []

gy = [0, 0, 1, -1]
gx = [1, -1, 0, 0]


def bfs(y, x, goal_number):

    step = 0
    q = deque([])
    q.append((y, x, step))
    tmp_field = copy.deepcopy(field)
    while len(q) > 0:
        y, x, step = q.popleft()

        for i in range(4):
            ny = y + gy[i]
            nx = x + gx[i]

            if (ny >= H) or (nx >= W) or (ny < 0) or (nx < 0):
                continue
            if tmp_field[ny][nx] == 'X':
                continue

            if str(tmp_field[ny][nx]) == str(goal_number):
                return step+1, ny, nx
            else:
                q.append((ny, nx, step+1))
                tmp_field[ny][nx] = 'X'


sy, sx = 0, 0
for i in range(H):
    line = input()
    if line.find('S') != -1:
        sy = i
        sx = line.find('S')
    field.append(list(line))


ans = 0
for goal_number in range(1, N+1):
    num, sy, sx = bfs(sy, sx, goal_number)
    ans += num

print(ans)
