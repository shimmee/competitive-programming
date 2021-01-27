# AGC033A - Darker and Darker
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc033/tasks/agc033_a
# Date: 2021/01/25

# ---------- Ideas ----------
# フィールド作る
# 複数点をスタート地点として，全てのスタート地点のdistを0として初期化する
# 全てのスタート地点をqueの初期値としていれる
# 単純にBFSして，最大値を出力する


# ------------------- Answer --------------------
#code:python
from collections import deque
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
h, w = map(int, input().split())
G = [input() for _ in range(h)]

dist = [[-1 for _ in range(w)] for _ in range(h)]

que = deque([])
for y in range(h):
    for x in range(w):
        if G[y][x] == '#':
            que.append([y, x])
            dist[y][x] = 0

while que:
    y, x = que.popleft()
    for dy, dx in d:
        Y = y + dy
        X = x + dx

        if 0 <= Y < h and 0 <= X < w and dist[Y][X] == -1 and G[Y][X] == '.':
            dist[Y][X] = dist[y][x] + 1
            que.append([Y, X])
print(max([max(i) for i in dist]))
# ------------------ Sample Input -------------------

3 3
...
.#.
...


6 6
..#..#
......
#..#..
......
.#....
....#.


# ----------------- Length of time ------------------
# https://img.atcoder.jp/agc033/editorial.pdf
# 19分

# -------------- Editorial / my impression -------------
# BFSをコピペせずに自力で書いてみた

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#多点を1点として扱う
#グリッド
#grid
#BFS
#幅優先探索
#AGC-A
#緑diff
