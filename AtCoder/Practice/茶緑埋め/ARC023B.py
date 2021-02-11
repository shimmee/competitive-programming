# ARC023B - 謎の人物X
# URL: https://atcoder.jp/contests/arc023/tasks/arc023_2
# Date: 2021/02/09

# ---------- Ideas ----------
# 偶奇が大事
# Dが奇数であれば，距離がD以内の奇数のマスはどこでも行ける
# Dが偶数であれば，距離がD以内の偶数のマスはどこでも行ける

# まずは各マスへの距離をBFSで計算する: 必要ないと後に分かる


# ------------------- Answer --------------------
#code:python
r,c,d = map(int, input().split())
G = [[int(i) for i in input().split()] for _ in range(r)]
from collections import deque, Counter

dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

dist = [[-1 for _ in range(c)] for _ in range(r)]
dist[0][0] = 0
que = deque([])
que.append([0,0])

while que:
    y, x = que.popleft()

    for dy, dx in dydx:
        Y = y + dy
        X = x + dx
        if 0 <= Y < r and 0 <= X < c and dist[Y][X] == -1:
            dist[Y][X] = dist[y][x] + 1
            que.append([Y, X])

ans = 1
if d % 2 == 1:
    for y in range(r):
        for x in range(c):
            if dist[y][x] <= d and (y+x) % 2 == 1:
                ans = max(ans, G[y][x])
else:
    for y in range(r):
        for x in range(c):
            if dist[y][x] <= d and (y+x) % 2 == 0:
                ans = max(ans, G[y][x])
print(ans)

# ACしたけど，BFSのくだりは必要なかった。
# (0,0)からマス(x,y)への距離はx+yなので，このx+yがdより小さければ行ける
r,c,d = map(int, input().split())
G = [[int(i) for i in input().split()] for _ in range(r)]

ans = 1
if d % 2 == 1:
    for y in range(r):
        for x in range(c):
            if x+y <= d and (y+x) % 2 == 1:
                ans = max(ans, G[y][x])
else:
    for y in range(r):
        for x in range(c):
            if x+y <= d and (y+x) % 2 == 0:
                ans = max(ans, G[y][x])
print(ans)

# ------------------ Sample Input -------------------
3 2 1
9 5
3 1
8 9

4 4 100
999 999 999 999
999 999 999 999
999 999 999 999
999 999 999 999

# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc023
# 偶奇に着目して，市松模様の片方の色にのみ行けるという点が肝

# ----------------- Category ------------------
#AtCoder
#市松模様
#偶奇に着目
#偶奇に注目
#緑diff
#ARC-B
#グリッド内の移動