# パ研合宿2020 I - くねくね
# URL:
# Date: 2021/01/05

# ---------- Ideas ----------
# スタート地点から左右または上下どっちで出発するかによって結果が変わりそうなので，それぞれ計算する
# 座標に加えて，どの動きで来たのか(lrかud)を保存する
# lrできたなら，次はudの動き，vise versa

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque
h, w = map(int, input().split())
sy, sx, gy, gx = map(int, input().split())
G = [input() for _ in range(h)]

inf = float('INF')


def bfs(start):
    dist = [[inf for _ in range(w)] for _ in range(h)]
    que = deque([])

    dist[sy - 1][sx - 1] = 0
    que.append([sy - 1, sx - 1, start])
    while que:
        y, x, from_ = que.popleft()

        if from_ == 'ud': # 上下移動で来た場合には，次は左右
            for dy, dx in [[0, 1], [0, -1]]:
                Y = y + dy
                X = x + dx
                if 0 <= Y < h and 0 <= X < w and G[Y][X] == '.' and dist[Y][X] == inf:
                    dist[Y][X] = dist[y][x] + 1
                    que.append([Y, X, 'lr'])
        if from_ == 'lr':  # 左右移動で来た場合には，次は上下
            for dy, dx in [[1, 0], [-1, 0]]:
                Y = y + dy
                X = x + dx
                if 0 <= Y < h and 0 <= X < w and G[Y][X] == '.' and dist[Y][X] == inf:
                    dist[Y][X] = dist[y][x] + 1
                    que.append([Y, X, 'ud'])
    return dist[gy-1][gx-1]

ans = min(bfs('lr'), bfs('ud'))
if ans == inf: print(-1)
else: print(ans)


# ------------------ Sample Input -------------------
2 3
1 1 1 3
...
..#


3 4
1 1 3 4
....
.#..
....

5 7
4 1 5 4
.#..#..
#....#.
...#..#
.#.....
..#..#.

# ----------------- Length of time ------------------
# 20分くらい

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#パ研合宿2020
#BFS
#幅優先探索