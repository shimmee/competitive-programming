# AGC007A - Shik and Stone
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc007/tasks/agc007_a
# Date: 2021/01/01

# ---------- Ideas ----------
# BFS
# All # should be covered by the search
# One-stroke writing
# stones don't visit a cell multiple times as long as they move to right or down

# ------------------- Solution --------------------
# Solution1: If there are two adjacent # cell from a # cell, stone cannot move to the both cells
# Solution2: If there are # in both up and left from # cell, Impossible

# ------------------- Answer --------------------
#code:python
from collections import deque

h, w = map(int, input().split())
G = [input() for _ in range(h)]

seen = [[False]*w for _ in range(h)]
seen[0][0] = True
que = deque([])
que.append([0, 0])

while que:
    y, x = que.popleft()
    if y == h-1 and x == w-1:
        continue

    cnt = 0
    for dx, dy in [[1, 0], [0, 1]]:
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w and G[Y][X] == '#' and not seen[Y][X]:
            cnt += 1
            seen[Y][X] = True
            que.append([Y, X])
    if cnt != 1:
        print('Impossible')
        exit()
print('Possible')
# 2 cases WA out of 22 cases



# Solution2

h, w = map(int, input().split())
G = [input() for _ in range(h)]

flag = True
for y in range(h):
    for x in range(w):
        if G[y][x] == '#':

            # 左と上両方にあったらだめ
            cnt = 0
            for dx, dy in [[-1, 0], [0, -1]]:
                Y = y + dy
                X = x + dx
                if 0 <= Y < h and 0 <= X < w and G[Y][X] == '#':
                    cnt += 1
            if cnt == 2:
                flag = False
if flag:
    print('Possible')
else:
    print('Impossible')

# 2 cases WA out of 22 cases!!!!!!!




# Editorial: https://img.atcoder.jp/data/agc/007/editorial.pdf
# If number of # == H+W-1, then possible
h, w = map(int, input().split())
G = [input() for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        if G[i][j] == '#': cnt += 1
if cnt == h+w-1: print('Possible')
else: print('Impossible')


# ------------------ Input example -------------------
2 2
##
.#

4 5
##...
.##..
..##.
...##

5 3
###
..#
###
#..
###

4 5
##...
.###.
.###.
...##

# ----------------- Length of time ------------------
# 30 min Give up

# -------------- Editorial / my impression -------------
# Editorial: https://img.atcoder.jp/data/agc/007/editorial.pdf
# This is really clever solution.
# I wanna retry this later again

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #wanna_review
#