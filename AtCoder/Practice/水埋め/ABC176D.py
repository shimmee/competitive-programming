# ABC176D - Wizard in Maze
# URL: https://atcoder.jp/contests/abc176/tasks/abc176_d
# Date: 2021/04/10

# ---------- Ideas ----------
# ヘンリーとの勉強会
# 前まで全然わからんかったけど今日見たらすぐ思いつけた(精進のおかげ)
# 徒歩で行ける範囲の区画をareaと名付けて，areaをグラフの頂点として見る
# 2つのarea同士は，area内のセルが5*5以内で到達可能であればワープで飛べるので，その場合グラフの頂点同士に辺を貼れる
# グラフが完成したら，あとはスタート地点のareaからゴールのareaまでの最短距離をBFSで求める
# 5*5の範囲はチェビシェフ距離らしい

# ------------------- Answer --------------------
#code:python
from collections import deque
dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
S = [input() for _ in range(H)]

area = [[-1]*W for _ in range(H)]
k = 0
# search connected (linked) area and allocate them id by BFS
for h in range(H):
    for w in range(W):
        if S[h][w] == '#' or area[h][w] != -1: continue
        area[h][w] = k
        que = deque([])
        que.append([h, w])

        while que:
            y, x = que.popleft()
            for dy, dx in dydx:
                Y = y + dy
                X = x + dx
                if 0 <= Y < H and 0 <= X < W and area[Y][X] == -1 and S[Y][X] == '.':
                    area[Y][X] = area[y][x]
                    que.append([Y, X])
        k += 1

# number of linked area
m = max(map(max, area)) + 1

# create a graph: regard id as vertex, and vertex are connected if cells in area1 is reachable from cells in area2 by warp
G = [[] for _ in range(m)]
for h in range(H):
    for w in range(W):
        if S[h][w] == '#': continue
        id_from = area[h][w] # id of linked area

        for x in range(-2, 3):
            for y in range(-2, 3):
                Y = h + y
                X = w + x
                if 0 <= Y < H and 0 <= X < W and S[Y][X] != '#':
                    id_to = area[Y][X]
                    if id_to != id_from and id_from not in G[id_to]:
                        G[id_to].append(id_from)
                        G[id_from].append(id_to)

# area id of start and goal
s_area = area[sy-1][sx-1]
g_area = area[gy-1][gx-1]

# search distance from start area to goal area by BFS
dist = [-1]*m
dist[s_area] = 0
que = deque([s_area])
while que:
    v = que.popleft()
    for u in G[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            que.append(u)

print(dist[g_area])


# ------------------ Sample Input -------------------
4 5
1 2
2 5
#.###
####.
#..##
#..##


4 4
1 1
4 4
..#.
..#.
.#..
.#..


# ----------------- Length of time ------------------
# 40分くらい？

# -------------- Editorial / my impression -------------
# こんな長いコード書いたことない
# 大変だったけど自力でACできて嬉しい
# こういう実装が重い問題はとても好き...

# ----------------- Category ------------------
#AtCoder
#最短路問題
#最短経路問題
#グリッドをグラフに見立てる
#グリッドのグラフ化
#BFS
#幅優先探索