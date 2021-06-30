# ARC005C - 器物損壊！高橋君
# URL: https://atcoder.jp/contests/arc005/tasks/arc005_3
# Date: 2021/05/18

# ---------- Ideas ----------
# 壁を壊す回数を持ちながら進む?
# 01−BFSらしいけど，2回BFSすればよさそう？

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
G = [input() for _ in range(h)]
for y in range(h):
    for x in range(w):
        if G[y][x] == 's':
            sy, sx = y, x
        elif G[y][x] == 'g':
            gy, gx = y, x

from collections import deque
dydx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# dist[y][x][i]: マス(y，x)にi方向から入った時の壁を壊してきた回数
inf = float('INF')
dist = [[[inf]*4 for _ in range(w)] for _ in range(h)]
dist[sy][sx] = [0]*4
que = deque([])
que.append([sy, sx])

while que:
    y, x = que.popleft()
    cost = min(dist[y][x])
    for i in range(4):
        dy, dx = dydx[i]
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w and dist[Y][X][i] == inf:
            if G[Y][X] == '.' or G[Y][X] == 'g':
                dist[Y][X][i] = cost
            elif G[Y][X] == '#':
                dist[Y][X][i] = cost + 1
            que.append([Y, X])

print('YES' if min(dist[gy][gx]) <= 2 else 'NO')

# ちょっとダメだった
##############################
##############################
##############################
# 2回BFSすれば良いんじゃない？

h, w = map(int, input().split())
G = [input() for _ in range(h)]
for y in range(h):
    for x in range(w):
        if G[y][x] == 's':
            sy, sx = y, x
        elif G[y][x] == 'g':
            gy, gx = y, x

from collections import deque
dydx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
inf = 10**14
dist = [[inf for _ in range(w)] for _ in range(h)]

dist[sy][sx] = 0
que = deque([])
que.append([sy, sx])

while que:
    y, x = que.popleft()
    for dy, dx in dydx:
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w and dist[Y][X] == inf and (G[Y][X] == '.' or G[Y][X] == 'g'):
            dist[Y][X] = dist[y][x]
            que.append([Y, X])

for y in range(h):
    for x in range(w):
        for dy, dx in dydx:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w and dist[y][x] == 0:
                dist[Y][X] = min(dist[Y][X], dist[y][x]+1)

for y in range(h):
    for x in range(w):
        if dist[y][x] == 1:
            que = deque([])
            que.append([y, x])
            while que:
                y, x = que.popleft()
                for dy, dx in dydx:
                    Y = y + dy
                    X = x + dx
                    if 0 <= Y < h and 0 <= X < w and dist[Y][X] == inf and (G[Y][X] == '.' or G[Y][X] == 'g'):
                        dist[Y][X] = dist[y][x]
                        que.append([Y, X])

for y in range(h):
    for x in range(w):
        for dy, dx in dydx:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w and dist[y][x] == 1:
                dist[Y][X] = min(dist[Y][X], dist[y][x]+1)

for y in range(h):
    for x in range(w):
        if dist[y][x] == 2:
            que = deque([])
            que.append([y, x])
            while que:
                y, x = que.popleft()
                for dy, dx in dydx:
                    Y = y + dy
                    X = x + dx
                    if 0 <= Y < h and 0 <= X < w and dist[Y][X] == inf and (G[Y][X] == '.' or G[Y][X] == 'g'):
                        dist[Y][X] = dist[y][x]
                        que.append([Y, X])

print('YES' if dist[gy][gx] <= 2 else 'NO')

# 1WAが取れません
################################################
################################################
################################################
# こちらを参考に01-BFS: https://at274.hatenablog.com/entry/2020/05/31/095858


h, w = map(int, input().split())
G = [input() for _ in range(h)]
for y in range(h):
    for x in range(w):
        if G[y][x] == 's':
            sy, sx = y, x
        elif G[y][x] == 'g':
            gy, gx = y, x

from collections import deque
dydx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
inf = 10**14
dist = [[inf for _ in range(w)] for _ in range(h)]

dist[sy][sx] = 0
que = deque([])
que.append([sy, sx])

while que:
    y, x = que.popleft()
    for dy, dx in dydx:
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w and dist[Y][X] == inf:
            if G[Y][X] == '.' or G[Y][X] == 'g': # 重み0で先頭にキュー加える
                que.appendleft([Y, X])
                dist[Y][X] = dist[y][x]
            else: # 重み1で末尾にキュー加える
                que.append([Y, X])
                dist[Y][X] = dist[y][x] + 1

print('YES' if dist[gy][gx] <= 2 else 'NO')

# ------------------ Sample Input -------------------
4 5
s####
....#
#####
#...g

# ----------------- Length of time ------------------
# 1時間で解説AC

# -------------- Editorial / my impression -------------
# 距離じゃないBFSのときはだいたい01-BFS使えそう
# 曲がった回数とか，壊した回数とか，そういうやつ
# 01-BFS = 重みが0のときはキューの先頭にappendleft，1のときはキューの末尾にappendする

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#01-BFS
#幅優先探索
#最短路問題
#最短距離
#BFS