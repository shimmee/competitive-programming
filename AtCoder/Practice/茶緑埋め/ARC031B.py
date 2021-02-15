# ARC031B - 埋め立て
# URL: https://atcoder.jp/contests/arc031/tasks/arc031_2
# Date: 2021/02/14

# ---------- Ideas ----------
# 最大100個の海マスxの中で，陸マスoに変換するものを全探索する
# 1マス変換してからbfsで繋がっているかどうか調べる

# ------------------- Answer --------------------
#code:python
from copy import deepcopy
from collections import deque, Counter
dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
G = [list(input()) for _ in range(10)]
inf = float('INF')

# スタート地点を探す
flag = False
for y in range(10):
    for x in range(10):
        if G[y][x] == 'o':
            sy, sx = y, x
            flag = True
            break
    if flag:
        break

def bfs(field):
    dist = [[-1 for _ in range(10)] for _ in range(10)]
    for y in range(10):
        for x in range(10):
            if field[y][x] == 'x':
                dist[y][x] = inf

    dist[sy][sx] = 0
    que = deque([])
    que.append([sy, sx])

    while que:
        y, x = que.popleft()
        for dy, dx in dydx:
            Y = y + dy
            X = x + dx
            if 0 <= Y < 10 and 0 <= X < 10 and dist[Y][X] == -1:
                dist[Y][X] = dist[y][x] + 1
                que.append([Y, X])
    return False if min(map(min, dist)) == -1 else True

# 海を陸にするマスを全探索: 陸にしてからbfsで繋がっているかどうか判別
for y in range(10):
    for x in range(10):
        if G[y][x] == 'x':
            field = deepcopy(G)
            field[y][x] = 'o'
            if bfs(field):
                print('YES')
                exit()
print('NO')


# ------------------ Sample Input -------------------
xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxoxxxxx
xxxxxxxxxx
xxxxoxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx


# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# 解答雑すぎん?: https://www.slideshare.net/chokudai/arc031
# 10*10のグリッドだからどうにでもかけた。
# dydxをいつも他のファイルからコピーしてくるのが面倒だったので，グリッドのbfs自体をスニペットに入れた。

# ----------------- Category ------------------
#AtCoder
#bfs
#幅優先探索
#全探索
#グリッド
#grid